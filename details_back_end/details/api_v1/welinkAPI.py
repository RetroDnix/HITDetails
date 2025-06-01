from flask import g,jsonify,request
from flask.views import MethodView

from details.api_v1 import api_v1
from details.api_v1.database import DataBase
from details.api_v1.checker import GetHighestAuth
from details.api_v1.tools import Decoder, Empty
from details.auth import auth_required,Validate_uid,generate_token
from details.api_v1.checker import ValidateAccount
from details.errors import api_abort

from welink.api import (
    AuthV2TicketsRequest
)

import requests

class LoginProxyAPI(MethodView):
    def post(self): # 获取组织详情
        req = AuthV2TicketsRequest("https://open.welink.huaweicloud.com/api/auth/v2/tickets")
        req.client_id = "20230910123550346238753"
        req.client_secret = "a6934f6c-eb27-457c-bf34-07b7fdb68078"
        
        auth_code = None
        try: (auth_code,) = Decoder(request.form, (('AuthCode','STRING'),))
        except: return api_abort(400,"Invalid request")
        access_token = ""

        try:
            access_token = req.get_response()['access_token']
        except Exception as e:
            return api_abort(500,str(e))
        
        url = 'https://open.welink.huaweicloud.com/api/auth/v2/userid'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Access-Control-Allow-Origin': '*',
            'x-wlk-Authorization': access_token
        }
        params = {'code': auth_code}
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=5)
            response.raise_for_status()  # 检查请求是否成功
            return response.json()['userId']
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'An error occurred: {err}')
        return "err"

class WeLinkLoginAPI(MethodView):
    def post(self): # 获取组织详情
        db = DataBase()
        WLuid = None
        try: (WLuid,) = Decoder(request.form, (('WeLinkUID','STRING'),))
        except: return api_abort(400,"Invalid request")

        db.crs.execute('''SELECT uid FROM user2welink WHERE welinkID = %s''',WLuid)
        data = db.crs.fetchall()
        print(data)
        if(Empty(data)): return api_abort(204,"Unkonwn User")
        else: return jsonify(access_token = generate_token(data[0][0]))

class WeLinkBindAPI(MethodView):
    def post(self): # 获取组织详情
        db = DataBase()
        WLuid = None
        UserName = None
        PassWord = None
        params = (('WeLinkUID','STRING'),('username','STRING'),('password','STRING'),)
        try: WLuid, UserName, PassWord = Decoder(request.form, params)
        except: return api_abort(400,"Invalid request")
        print(UserName,PassWord)
        uid = ValidateAccount(db,UserName,PassWord)

        if uid == None:
            return api_abort(400,"Invalid username or password")
        try:
            db.crs.execute('''SELECT * FROM user2welink WHERE welinkID = %s''',WLuid)
            data = db.crs.fetchall()
            if(not Empty(data)): return api_abort(204,"Can't Bind an account twice!")

            db.crs.execute('''REPLACE INTO user2welink (uid,welinkID) VALUES (%s,%s)''',(uid,WLuid))
            db.commit()
        except:
            return api_abort(500,"SQL Error")
        return {'access_token': generate_token(uid)}


api_v1.add_url_rule('/Welinklogin', view_func=WeLinkLoginAPI.as_view('WeLink_Login_API'), methods=['POST'])
api_v1.add_url_rule('/WeLinkBind', view_func=WeLinkBindAPI.as_view('WeLink_Bind_API'), methods=['POST'])
api_v1.add_url_rule('/LoginProxy', view_func=LoginProxyAPI.as_view('Login_Proxy_API'), methods=['POST'])