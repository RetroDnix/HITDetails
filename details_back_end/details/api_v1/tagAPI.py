from flask import g,jsonify,request
from flask.views import MethodView

from details.api_v1 import api_v1
from details.apimethods import *
from details.auth import auth_required
from details.errors import api_abort
from details.api_v1.database import DataBase
from details.api_v1.tools import Decoder,Empty
from details.api_v1.checker import ValidateMessageID,ValidateScheduleID
from details.auth import auth_required,Validate_uid

def tag_schema(TagID,TagName):
    return {"Tags":[{'TagID':TagID,'TagName':TagName}]}

class Get_Tags_API(MethodView):
    decorators = [auth_required]
    def get(self):
        # 建立连接
        uid = g.current_user
        #print(uid)
        db = DataBase()
        if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

        # 获取数据/类型转换/判断合法性
       
        TagID = MessageID = ScheduleID = None
        params = (('TagID','INT'),('ScheduleID','INT'))
        try: TagID ,ScheduleID = Decoder(request.args,params)
        except: return api_abort(400,"bad request")

        # 确认权限
        if TagID != None:
            db.crs.execute('''SELECT `owner` FROM tag WHERE TagID = %s''',TagID)
            res = db.crs.fetchall()
            if Empty(res): return api_abort(400,"have not TagID")
            elif res[0][0] != uid: return api_abort(400,"bad request")
            else:
                db.crs.execute('''SELECT TagName FROM tag WHERE TagID = %s''',TagID)
                res = db.crs.fetchall()
                TagName = res[0][0]
                return jsonify(tag_schema(TagID,TagName))

        elif ScheduleID != None:
            if not ValidateScheduleID(db,ScheduleID,uid):
                return api_abort(400,'invalid messageID')
            db.crs.execute('''SELECT `TagID` FROM tag2schedule WHERE ScheduleID = %s''',ScheduleID)
            res = db.crs.fetchall()
            if Empty(res): return api_abort(400,"have not TagID")
            else:
                # 可能返回多个tags
                a = []
                b = []
                for i in range(len(res)):
                    TagID = res[i][0]
                    a.append(TagID)
                    db.crs.execute('''SELECT TagName FROM tag WHERE TagID = %s''',TagID)
                    ab = db.crs.fetchall()
                    TagName = ab[0][0]
                    b.append(TagName)
                return jsonify(tag_schema(a,b))

        else:
            Tags = []
            db.crs.execute('''SELECT `TagID` FROM tag WHERE owner = %s''',uid)
            res = db.crs.fetchall()
            #print(len(res))
            for i in range(len(res)):
                TagID = res[i][0]
                db.crs.execute('''SELECT `TagName` FROM tag WHERE TagID = %s''',TagID)
                abc = db.crs.fetchall()
                TagName = abc[0][0]
                Tags.append({"TagID":TagID,"TagName":TagName})
            return {"Tags":Tags}

class Create_Tag_API(MethodView):
    decorators = [auth_required]
    def post(self):
        uid = g.current_user
        db = DataBase()
        if not Validate_uid(db,uid):return api_abort(400,"Invalid user")
        param = (('TagName','STRING'),)
        try: (TagName,) = Decoder(request.form,param)
        except: return api_abort(400,"bad request")
        #print(TagName)
        db.crs.execute('''INSERT INTO `tag` (TagName,Owner) VALUES (%s,%s)''',(TagName,uid))
        db.crs.execute('''SELECT LAST_INSERT_ID() FROM tag''')
        res = db.crs.fetchall()
        TagID = int(res[0][0])
        #print(TagID)
        db.commit()
        db.close()
        response = jsonify({"TagID":TagID})
        response.status_code = 201
        return response

class Add_Tag_to_Schedule_API(MethodView):
    decorators = [auth_required]
    def post(self):
        uid = g.current_user
        db = DataBase()
        if not Validate_uid(db,uid):return api_abort(400,"Invalid user")
        params = (('TagID','INT'),('ScheduleID','INT'))
        try: TagID,ScheduleID = Decoder(request.form,params)
        except: return api_abort(400,"bad request")
        
        #检验ScheduleID是否存在
        if not ValidateScheduleID(db,ScheduleID,uid):
            return api_abort(400,'invalid scheduleID')
        #检验输入的TagIDs是否存在
        db.crs.execute('''SELECT TagID FROM tag WHERE Owner = %s AND TagID = %s''',(uid,TagID))
        res = db.crs.fetchall()
        if Empty(res):
            return api_abort(400,'invalid TagID')
        try:
            db.crs.execute('''REPLACE INTO `tag2schedule`(tagID, scheduleID) VALUES (%s,%s)''',(TagID,ScheduleID))
            db.commit()
        except:
            api_abort(500,"sql insert error")

        return api_abort(204)

class Remove_Tag_from_Schedule_API(MethodView):
    decorators = [auth_required]
    def post(self):
        uid = g.current_user
        db = DataBase()
        if not Validate_uid(db,uid):return api_abort(400,"Invalid user")
        params = (('TagID','INT'),('ScheduleID','INT'))
        try: TagID,ScheduleID = Decoder(request.form,params)
        except: return api_abort(400,"bad request")
        
        #检验ScheduleID是否存在
        if not ValidateScheduleID(db,ScheduleID,uid):
            return api_abort(400,'invalid scheduleID')
        #检验输入的TagIDs是否存在
        db.crs.execute('''SELECT TagID FROM tag WHERE Owner = %s AND TagID = %s''',(uid,TagID))
        res = db.crs.fetchall()
        if Empty(res):
            return api_abort(400,'invalid TagID')
        try:
            db.crs.execute('''DELETE FROM `tag2schedule` WHERE tagID = %s AND scheduleID = %s''',(TagID,ScheduleID))
            db.commit()
        except:
            api_abort(500,"sql insert error")

        return api_abort(204)

class Delete_Tag_API(MethodView):
    decorators = [auth_required]
    def delete(self):
        uid = g.current_user
        db = DataBase()
        if not Validate_uid(db,uid):return api_abort(400,"Invalid user")
        param = (('TagID','INT'),)
        try:
            (TagID,) = Decoder(request.args,param)
        except:
            return api_abort(400,"bad request")
        db.crs.execute('''SELECT Owner FROM tag WHERE TagID = %s''',TagID)
        res = db.crs.fetchall()
        Owner = res[0][0]
        if Owner == uid:
            db.crs.execute('''DELETE FROM `tag` WHERE TagID = %s''',TagID)
        else:
            return api_abort(400,"No right")
        db.commit()
        db.close()
        return api_abort(204)
        
api_v1.add_url_rule('/tags/get_tags', view_func=Get_Tags_API.as_view('Get_Tags_API'), methods=['GET'])
api_v1.add_url_rule('/tags/create_tag', view_func=Create_Tag_API.as_view('Create_Tag_API'), methods=['POST'])
api_v1.add_url_rule('/tags/add_tag_to_schedule', view_func=Add_Tag_to_Schedule_API.as_view('Add_Tag_to_Schedule_API'), methods=['POST'])
api_v1.add_url_rule('/tags/remove_tag_from_schedule', view_func=Remove_Tag_from_Schedule_API.as_view('Remove_Tag_from_Schedule_API'), methods=['POST'])
api_v1.add_url_rule('/tags/delete_tag', view_func=Delete_Tag_API.as_view('Delete_Tag_API'), methods=['DELETE'])
