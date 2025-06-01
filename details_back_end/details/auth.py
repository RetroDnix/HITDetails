from flask import request, current_app, g
from functools import wraps
from itsdangerous import URLSafeSerializer as Serializer, BadSignature

from details import app,logger
from details.errors import invalid_token, token_missing
from details.api_v1.database import DataBase
from details.api_v1.tools import Empty
def generate_token(uid):
    s = Serializer(current_app.config['SECRET_KEY'])
    token = s.dumps({'id': uid})
    return token


def validate_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        return False
    g.current_user = data['id']
    return True


def get_token():
    # Flask/Werkzeug do not recognize any authentication types
    # other than Basic or Digest, so here we parse the header by hand.
    if 'Authorization' in request.headers:
        try:
            token = request.headers['Authorization']
        except ValueError:
            # The Authorization header is either empty or has no token
            token = None
    else:
        token = None

    return token


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token()

        # 写入日志文件
        db = DataBase()
        db.crs.execute('''INSERT INTO `Log` (`User_Agent`,`Method`,`Args`,`Form`,`Authorization`) 
            VALUES (%s,%s,%s,%s,%s)''',(request.headers.get('User-Agent'),str(request.method),str(request.args),str(request.form),str(request.headers.get('Authorization'))))
        db.crs.execute("SELECT LAST_INSERT_ID() FROM `group`")
        ID = (db.crs.fetchall())[0][0]
        logger.info("Quest:"+str(ID))
        db.commit()
        db.close()

        # Flask normally handles OPTIONS requests on its own, but in the
        # case it is configured to forward those to the application, we
        # need to ignore authentication headers and let the request through
        # to avoid unwanted interactions with CORS.
        if request.method != 'OPTIONS':
            if token is None:
                return token_missing()
            if not validate_token(token):
                return invalid_token()
        return f(*args, **kwargs)

    return decorated

def Validate_uid(db:DataBase,uid:int)->bool:
    db.crs.execute("USE details")
    db.crs.execute("SELECT `name` FROM `user` WHERE userID = %s",uid)
    return not Empty(db.crs.fetchall())

