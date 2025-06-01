from flask import g,request,jsonify
from flask.views import MethodView

from details.api_v1 import api_v1
from details.api_v1.database import DataBase
from details.api_v1.convert import Convert
from details.api_v1.tools import Decoder,Empty
from details.api_v1.checker import ValidateMessageID,ValidateScheduleIDFM,ValidateScheduleID
from details.auth import auth_required,Validate_uid
from details.errors import api_abort

import time

def sch_schema(lres,page,s):
	return {
		"ResNum":lres,
		"Page":page,
		"Schedules":s
	}

class ScheduleAPI(MethodView):
	decorators = [auth_required]
	def get(self): # 从各种条件中获取消息
		db = DataBase()
		uid = g.current_user
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		sql_where = list()
		schID = set()
		Maxnum = 50
		Page = 1
		DeadLine = Maxnum = Type = QueryMes = Tags = Stars = ScheduleID = MessageID = StartTime = SortByTime = None
		HasTag = False
		params = (('DeadLine','TIME'),('StartTime','TIME'),('SortByTime','BOOL'),('Maxnum','INT',50),('Page','INT',1),('Type','INT'),('QueryMes','STRING'),
		('Tags','INTLIST','ARL'),('Stars','INT'),('ScheduleID','INT'),('MessageID','INT'),('HasTag','BOOL'))

		DeadLine,StartTime,SortByTime,Maxnum,Page,Type,QueryMes,Tags,Stars,ScheduleID,MessageID,HasTag = Decoder(request.args,params)

		if DeadLine != None: sql_where.append('''TIMESTAMPDIFF(second,schedule.StartTime,"%s") > 0'''%time.strftime("%Y-%m-%d %H:%M:%S",DeadLine))
		if StartTime != None: sql_where.append('''TIMESTAMPDIFF(second,schedule.StartTime,"%s") <= 0'''%time.strftime("%Y-%m-%d %H:%M:%S",StartTime))

		if Type != None: 
			if not Type in [3,4]: return api_abort(400,"Confused Type")
			sql_where.append('''schedule.type = %s'''%Type)

		if Stars != None:
			if not Stars in [0,1,2,3]: return api_abort(400,"Confused Stars")
			sql_where.append('''schedule.stars = %s'''%Stars)

		sql_limit = 'LIMIT %d,%d'%(Maxnum*(Page-1),Maxnum)

		if QueryMes != None:
			QueryMes = "'%" + QueryMes + "%'"
			sql_where.append('''(schedule.Body LIKE %s OR schedule.Title LIKE %s)'''%(QueryMes,QueryMes))
		# 条件二选一,否则返回所有的日程
		if ScheduleID != None:
			if ValidateScheduleID(db,ScheduleID,uid): # 这个会发返回指定的日程
				sql_final_query = '''SELECT scheduleID,title,body,origin,type,UNIX_TIMESTAMP(starttime) AS starttime
					,UNIX_TIMESTAMP(finishtime) AS finishtime,location,stars FROM schedule 
					WHERE owner = %s AND scheduleID = %s
					'''%(uid,ScheduleID)
			else: return api_abort(403,'invalid message')
		elif MessageID != None:
			# 返回某个消息的附属的日程
			if not ValidateMessageID(db,uid,MessageID):
				print('ww')
				return api_abort(403,'invalid message')
			else:
				sql_final_query = '''SELECT scheduleID,title,body,origin,type,UNIX_TIMESTAMP(starttime) AS starttime
				,UNIX_TIMESTAMP(finishtime) AS finishtime,location,stars FROM schedule 
				WHERE owner = 0 AND origin = %s
				'''%(MessageID)
		else: # 返回某人的所有日程
			sql_final_query = '''SELECT scheduleID,title,body,origin,type,UNIX_TIMESTAMP(starttime) AS starttime
				,UNIX_TIMESTAMP(finishtime) AS finishtime,location,stars,`owner` FROM schedule  
				WHERE 
				`owner` = %s
				'''%uid
			if not Empty(Tags): # 如果有使用tag这个删选条件
				gs = set()
				try:
					for i in Tags:
						db.crs.execute('''SELECT scheduleID FROM tag2schedule WHERE tagID = %s''',i)
						res = db.crs.fetchall()
						for j in res: gs.add(str(j[0]))
				except: return api_abort(500,"SQL ERROR")
				#schID.intersection_update(gs)
				sql_final_query += 'AND scheduleID IN%s'%Convert.ToString(gs)

			for i in sql_where:
				sql_final_query += '''AND %s\n'''%i
		if SortByTime: sql_final_query += "ORDER BY UNIX_TIMESTAMP(starttime)\n"
		else: sql_final_query += "ORDER BY scheduleID DESC\n"
		sql_final_query += sql_limit
		#print(sql_final_query)
		try:
			db.crs.execute(sql_final_query)
			res = db.crs.fetchall()
			if Empty(res):raise ValueError()
		except:
			return api_abort(204,'NO CONTENT!')
		# 格式化结果
		sches = []
		for i in res:
			ID = int(i[0])
			try:
				if HasTag:
					db.crs.execute('''SELECT tag.TagID,TagName FROM tag 
						INNER JOIN tag2schedule ON tag2schedule.TagID = tag.TagID
						WHERE tag2schedule.scheduleID = %s''',ID)
					Res_Tag = db.crs.fetchall()
			except:
				return api_abort(500,"SQL ERROR")
			sches.append({
				"ScheduleID":ID,
				"Title":i[1],
				"Body":i[2],
				"Origin":i[3],
				"Type":i[4],
				"Location":i[7],
				"Stars":i[8],
				"Created":False,
			})
			if i[4] == 4: sches[-1]["DeadLine"] = i[5]
			else: 
				sches[-1]["StartTime"] = i[5]
				sches[-1]["FinishTime"] = i[6]
			if HasTag:
				sches[-1]["Tags"]=Convert.ToDict(Res_Tag,["TagID","TagName"])
		db.close()
		return jsonify(sch_schema(len(res),Page,sches))
	
	def post(self): # 创建日程
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		Title = Body =Type = StartTime = FinishTime = Location = Tags = Stars = None 
		Self = True

		params = (('Title','STRING','NN'),('Body','STRING'),('Type','INT'),('StartTime','TIME'),('FinishTime','TIME'),
		('Location','STRING'),('Tags','INTLIST','ARL'),('Stars','INT'),('Self','BOOL'))
		try: Title,Body,Type,StartTime,FinishTime,Location,Tags,Stars,Self = Decoder(request.form,params)
		except: return api_abort(400,"invalid form")
		
		if not Type in [3,4]: return api_abort(400,"Confused type")
		if Type == 4: FinishTime = None

		if not Stars in [0,1,2,3]: return api_abort(400,"Confused stars")
		
		#将日程存储进sql
		try:
			if Self: owner = uid
			else: owner = 0
			db.crs.execute('''INSERT INTO `schedule` (title,body,type,starttime,finishtime,location,stars,`owner`,creator) 
				VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(Title,Body,Type,StartTime,FinishTime,Location,Stars,owner,uid))
			db.crs.execute("SELECT LAST_INSERT_ID() FROM `schedule`")
			res = db.crs.fetchall()
			ID = int(res[0][0])
			for i in Tags:
				db.crs.execute('''INSERT INTO `tag2schedule` (tagID,scheduleID) VALUES (%s,%s)''',(i,ID))
		except: return api_abort(500,"sql insert error")

		db.commit()
		db.close()
		response = jsonify({'ScheduleID':ID})
		response.status_code = 201
		return response

	def put(self): # 更新某个日程的信息
		# 暂时不支持更新tags
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		Title = Body =Type = StartTime = FinishTime = Location = Tags = Stars = SID = None 
		Self = True

		params = (('ScheduleID','INT','NN'),('Title','STRING','NN'),('Body','STRING'),('Type','INT'),('StartTime','INT'),('FinishTime','INT'),
		('Location','STRING'),('Tags','INTLIST','ARL'),('Stars','INT'))
		try: SID,Title,Body,Type,StartTime,FinishTime,Location,Tags,Stars = Decoder(request.form,params)
		except: return api_abort(400,"invalid form")
		
		if not Type in [3,4]: return api_abort(400,"Confused type")
		if Type == 4: FinishTime = None

		if not Stars in [0,1,2,3]: return api_abort(400,"Confused stars")
		
		if StartTime == None: StartTime = 0
		if FinishTime == None: FinishTime = 0

		#将日程存储进sql
		try:
			db.crs.execute('''SELECT `owner` FROM `schedule` WHERE scheduleID = %s''',SID)
			res = db.crs.fetchall()
			if len(res) == 0: return api_abort(403,'invalid scheduleID')
			if res[0][0] != uid: return api_abort(403,'invalid scheduleID')
			print(StartTime,FinishTime)
			db.crs.execute('''UPDATE `schedule` SET title = %s,body = %s,type = %s,starttime = FROM_UNIXTIME(%s),finishtime = FROM_UNIXTIME(%s),location = %s,stars = %s WHERE scheduleID = %s''',
				(Title,Body,Type,StartTime,FinishTime,Location,Stars,SID))
			# for i in Tags:
			# 	db.crs.execute('''INSERT INTO `tag2schedule` (tagID,scheduleID) VALUES (%s,%s)''',(i,SID))
		except: return api_abort(500,"sql insert error")

		db.commit()
		db.close()
		return api_abort(204)

	def patch(self): # 从某个附属日程创建某人专属的日程
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		MessageID = ScheduleID = Stars = None
		params = (('MessageID','INT',),('ScheduleID','INT'),('Stars','INT'))
		MessageID, ScheduleID, Stars = Decoder(request.form,params)
		# 验证权限
		if not ValidateMessageID(db,uid,MessageID):
			return api_abort(403,'invalid messageID')
		if not ValidateScheduleIDFM(db,ScheduleID,MessageID):
			return api_abort(403,'invalid scheduleID')
		# 本质上是从原附属日程复制过来了
		# 注意creator还是原来的值 但是origin变为0,owner变为当前的uid
		try:
			db.crs.execute('''INSERT INTO schedule(title,body,type,starttime,finishtime,location,stars,owner,creator)
				SELECT title,body,type,starttime,finishtime,location,stars,owner,creator FROM schedule WHERE scheduleID = %s''',ScheduleID)
			db.crs.execute("SELECT LAST_INSERT_ID() FROM `schedule`")
			ID = (db.crs.fetchall())[0][0]
			if(Stars != None): db.crs.execute('''UPDATE schedule SET `owner` = %s,`stars`=%s WHERE scheduleID = %s''',(uid,Stars,ID))
			else: db.crs.execute('''UPDATE schedule SET `owner` = %s WHERE scheduleID = %s''',(uid,ID))
			db.crs.execute('''REPLACE INTO `HaveCreate` (userID,scheduleID,realScheduleID) VALUES (%s,%s,%s)''',(uid,ScheduleID,ID))
		except: return api_abort(500,"sql insert error")

		db.commit()
		return api_abort(200,{"ScheduleID":ID})

	def delete(self): # 删除日程
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		ScheduleID = None
		params = (("ScheduleID",'INTLIST','ARL'),)
		(ScheduleID,) = Decoder(request.args,params)
		# 确保这些日程一定是某人日程表内的日程
		for i in ScheduleID:
			if not ValidateScheduleID(db,i,uid):
				return api_abort(403,'invalid scheduleID')
		try:
			for i in ScheduleID:
				db.crs.execute('''DELETE FROM schedule WHERE scheduleID = %s''',ScheduleID)
		except: return api_abort(500,"sql insert error")

		db.commit()
		return api_abort(204)

api_v1.add_url_rule('/schedule', view_func=ScheduleAPI.as_view('schedule_API'), methods=['GET','POST','PATCH','PUT','DELETE'])