from flask import jsonify, request
from flask.views import MethodView

from details.errors import api_abort
from details.auth import generate_token
from details.api_v1 import api_v1
from details.api_v1.database import DataBase
from details.api_v1.checker import ValidateAccount

class LoginAPI(MethodView):

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        #print(username,password)
        db = DataBase()
        uid = ValidateAccount(db,username,password)
        
        if uid == None:
            return api_abort(400,"Invalid username or password")

        token = generate_token(uid)

        db.crs.execute('''SELECT `name` FROM `user` WHERE userID = %s''',uid)
        res = db.crs.fetchall()

        response = jsonify({
            'access_token': token,
            'Name':res[0][0],
            'UserID':uid
        })
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        return response

    
api_v1.add_url_rule('/login', view_func=LoginAPI.as_view('Login_API'), methods=['POST'])
