from flask.views import MethodView
from flask import g,jsonify,request

from details.auth import auth_required,Validate_uid
from details.errors import api_abort
from details.api_v1 import api_v1
from details.api_v1.tools import Decoder
from details.api_v1.database import DataBase
from details.api_v1.checker import CheckAuth,Empty


def invitation_schema(f):
    return {"Invitations":f}

class InvitationAPI(MethodView):
    decorators = [auth_required]
    def get(self):
        uid = g.current_user
        db = DataBase()
        if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

        try:
            db.crs.execute('''SELECT ivtID,inviter,groupID FROM invitations WHERE userID = %s''',uid)
            res = db.crs.fetchall()
        except:
            return api_abort(401,"Invalid")
        grna = []
        for i in range(len(res)):
            db.crs.execute('''SELECT `name` FROM `group` WHERE `groupID` = %s''',res[i][2])
            grname = db.crs.fetchall()
            grna.append(grname[0][0])
        inna = []
        for i in range(len(res)):
            db.crs.execute('''SELECT `name` FROM `user` WHERE `userID` = %s''',res[i][1])
            inname = db.crs.fetchall()
            inna.append(inname[0][0])
        ivt = []
        for i in range(len(res)):
            ivt.append({"IvtID":res[i][0],"InviterID":res[i][1],"InverterName":inna[i],"GroupID":res[i][2],"GroupName":grna[i]})
        return jsonify(invitation_schema(ivt))

class Accept_Invitaiton_API(MethodView):
    decorators = [auth_required]
    def get(self):
        uid = g.current_user
        db = DataBase()
        if not Validate_uid(db,uid):return api_abort(400,"Invalid user")
        ID = None
        param = (('IvtID','INT'),)
        try:
            (ID,) = Decoder(request.form,param)
        except:
            return api_abort(400,"bad request")

        db.crs.execute('''SELECT inviter,groupID,userID FROM invitations WHERE ivtID = %s''',ID)
        res = db.crs.fetchall()
        if Empty(res) or res[0][2] != uid:
            return api_abort(400,'Invalid ID')
        if not CheckAuth(db,res[0][0],res[0][1],0,True):
            return api_abort(403,'Not Authorized')

        db.crs.execute('''INSERT INTO `user2group`(groupID,userID) VALUES (%s,%s)''',(res[0][1],uid))
        db.crs.execute('''DELETE FROM `invitations` WHERE `ivtID` = %s''',ID)
        db.commit()
        db.close()
        return api_abort(204)

class Delete_Invitation_API(MethodView):
    decorators = [auth_required]
    def delete(self):
        uid = g.current_user
        db = DataBase()
        if not Validate_uid(db,uid):return api_abort(400,"Invalid user")
        ID = None
        param = (('IvtID','INT'),)
        try:
            (ID,) = Decoder(request.args,param)
        except:
            return api_abort(400,"bad request")
        
        db.crs.execute('''SELECT userID FROM invitations WHERE ivtID = %s''',ID)
        res = db.crs.fetchall()
        if Empty(res) or res[0][0] != uid:
            return api_abort(400,'Invalid ID')
        
        db.crs.execute('''DELETE FROM `invitations` WHERE `ivtID` = %s''',ID)
        db.commit()
        db.close()
        return api_abort(204)


api_v1.add_url_rule('/invitation/all_invitations', view_func=InvitationAPI.as_view('InvitationAPI'), methods=['GET'])
api_v1.add_url_rule('/invitation/accept_invitaiton', view_func=Accept_Invitaiton_API.as_view('Accept_Invitaiton_API'), methods=['GET'])
api_v1.add_url_rule('/invitation/delete_invitation', view_func=Delete_Invitation_API.as_view('Delete_Invitation_API'), methods=['DELETE'])