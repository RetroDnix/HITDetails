from flask import g,request,jsonify
from flask.views import MethodView

from details.api_v1 import api_v1
from details.api_v1.database import DataBase
from details.api_v1.convert import Convert
from details.api_v1.tools import Decoder
from details.api_v1.checker import Empty
from details.auth import auth_required,Validate_uid
from details.errors import api_abort

class TemplateAPI(MethodView):
	decorators = [auth_required]
	def get(self):
		db = DataBase()
		uid = g.current_user
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		try:
			db.crs.execute('''SELECT ID,title,body,origin,type,UNIX_TIMESTAMP(starttime) AS starttime
				,UNIX_TIMESTAMP(finishtime) AS finishtime,location,stars FROM ScheduleTemplates
				WHERE `owner` = %s''',uid)
			res = db.crs.fetchall()
		except:
			return api_abort(204,'sql query error!')
		# 格式化结果
		sches = []
		Appendix = dict()
		for i in res:
			sches.append({
				"ScheduleID":i[0],
				"Title":i[1],
				"Body":i[2],
				"Origin":i[3],
				"Type":i[4],
				"Location":i[7],
				"Stars":i[8],
			})
			if i[4] == 4: sches[-1]["DeadLine"] = i[5]
			else: 
				sches[-1]["StartTime"] = i[5]
				sches[-1]["FinishTime"] = i[6]
			if i[3] != None:
				if i[3] not in Appendix:
					Appendix[i[3]]=set(i[0])
				else: Appendix[i[3]].add(i[0])

		mesgs = []
		try:
			db.crs.execute('''SELECT ID,title,body,type,sender,stars FROM MessageTemplates 
					WHERE owner = %s''',uid)
		except: return api_abort(500,'sql query error')
		res = db.crs.fetchall()
		for i in res:
			ID = int(i[0])
			mesgs.append({
				"MessageID":ID,
				"Title":i[1],
				"Body":i[2],
				"Type":i[3],
				"Sender":i[4],
				"Stars":i[5],
			})
			if Appendix.get(ID)!=None:
				mesgs[-1]["Schedules"] = Convert.ToList(Appendix[ID])
		db.close()
		return jsonify({'ScheduleTemplates':sches,'MessageTemplates':mesgs})

	def post(self):
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		Title = Body = Sender = Location = 'Null'
		StartTime = FinishiTime = DeadLine = 'Null'
		Stars = 'Null'
		Attached = False
		
		Schedules = None

		params = (('Title','STRING'),('Body','STRING'),('Type','INT'),('StartTime','TIME'),('FinishiTime','TIME'),('DeadLine','TIME'),
		('Location','STRING'),('Stars','INT'),('Attached','BOOL'),('Sender','STRING'),('Schedules','INTLIST','ARL'))

		try: Title,Body,Type,StartTime,FinishiTime,DeadLine,Location,Stars,Attached,Sender,Schedules = Decoder(request.form,params)
		except: return api_abort(400,"invalid form")
		
		if not Type in [1,2,3,4]: return api_abort(400,"Confused Type")
		if Type == 4: StartTime = DeadLine

		#if not Stars in [0,1,2,3]: return api_abort(400,"Confused Stars")
		
		#将日程存储进sql
		try:
			if Type == 1 or Type == 2:
				db.crs.execute('''INSERT INTO `MessageTemplates`(title,body,type,sender,stars,`owner`) VALUES(%s,%s,%s,%s,%s,%s)''',(Title,Body,Type,Sender,Stars,uid))
				db.crs.execute("SELECT LAST_INSERT_ID() FROM `MessageTemplates`")
				res = db.crs.fetchall()
				ID = int(res[0][0])
				# 将附属日程的origin更新
				for i in Schedules:
					db.crs.execute('''UPDATE ScheduleTemplates SET origin = %s WHERE ID = %s AND owner = %s''',(ID,i,uid))
				response = jsonify({'MessageTemplateID':ID})
			else:
				db.crs.execute('''INSERT INTO `ScheduleTemplates`(title,body,type,starttime,finishtime,location,stars,`owner`,attached) 
					VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(Title,Body,Type,StartTime,FinishiTime,Location,Stars,uid,Attached))
				db.crs.execute("SELECT LAST_INSERT_ID() FROM `ScheduleTemplates`")
				res = db.crs.fetchall()
				ID = int(res[0][0])
				response = jsonify({'ScheduleTemplateID':ID})
		
		except: return api_abort(500,"sql insert error")
		
		db.commit()
		db.close()

		response.status_code = 201
		return response

	def delete(self): 
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		SID = MID = None
		params = (("ScheduleTemplateID",'INT'),('MessageTemplateID','INT'))
		(SID,MID) = Decoder(request.args,params)
		
		try:
			if SID != None:
				db.crs.execute('''SELECT owner FROM ScheduleTemplates WHERE ID = %s''',SID)
				res = db.crs.fetchall()
				if Empty(res): return api_abort(400,"Invalid ID")
				if res[0][0] != uid: return api_abort(403,"No right")
				db.crs.execute('''DELETE FROM ScheduleTemplates WHERE ID = %s''',SID)
			elif MID != None:
				db.crs.execute('''SELECT owner FROM MessageTemplates WHERE ID = %s''',MID)
				res = db.crs.fetchall()
				if Empty(res): return api_abort(400,"Invalid ID")
				if res[0][0] != uid: return api_abort(403,"No right")
				db.crs.execute('''DELETE FROM MessageTemplates WHERE ID = %s''',MID)
			else: return api_abort(400,'invalid args')
		except: return api_abort(500,'sql insert error')

		db.commit()
		return api_abort(204)

api_v1.add_url_rule('/template', view_func=TemplateAPI.as_view('template_API'), methods=['GET','POST','DELETE'])