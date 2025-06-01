from flask import g,jsonify,request
from flask.views import MethodView

from details.api_v1 import api_v1
from details.api_v1.database import DataBase
from details.api_v1.convert import Convert
from details.api_v1.tools import Decoder,Empty,GetGroupName,dfs,GetUserName
from details.api_v1.checker import CheckAuth,CheckDeleteAuth,ValidateInput,SerachAttendGroup,ValidateScheduleCR
from details.auth import Validate_uid,auth_required
from details.errors import api_abort
from details.aisummary import get_summary

import time,redis,json

# 将set v中的数据全部插入值为key的条目中
def AddSetToRedis(conn,key,v):
	for i in v: conn.sadd(key,i)
# 将消息对应的日程保存
def SaveSchedule(db:DataBase, ID:int, schedules:list)->None:
	AddSetToRedis(db.sche,ID,schedules)
# 将消息对应的收件人保存
def SaveCache(db:DataBase, ID:int, Boardcast:set, Single:set, ftu:set)->None:
	AddSetToRedis(db.tgbc,ID,Boardcast)
	AddSetToRedis(db.tgsc,ID,Single)
	AddSetToRedis(db.tuc,ID,ftu)
# 将组织收到消息的记录保存
def SaveLog(db:DataBase, ID:int, Boardcast:set, Single:set, ftu:set)->None:
	for i in Boardcast:
		db.tgb.sadd(i,ID)
	for i in Single:
		db.tgs.sadd(i,ID)
	for i in ftu:
		db.tu.sadd(i,ID)
# 返回的json的格式
def mes_schema(lres,page,mesgs):
	return {
		"ResNum":lres,
		"Page":page,
		"Messages":mesgs
	}

class MessageAPI(MethodView):
	decorators = [auth_required]
	def get(self): # 按照筛选条件获取消息
		db = DataBase()
		uid = g.current_user
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		sql_where = ["NOT EXISTS ( SELECT 1 FROM HaveDelete WHERE HaveDelete.messageID = message.ID AND HaveDelete.userID = %s)"%uid]

		FinishTime = time.time()
		Maxnum = 50
		Page = 1
		StartTime = Type = QueryMes = Group = Sender = Tags = Stars = MessageID = None
		HasTag = HasReceiver = False

		params =(('StartTime','TIME'),('FinishTime','TIME'),('Maxnum','INT',50),('Page','INT',1),('Type','INT'),
		('Group','INT'),('Sender','INTLIST'),('Tags','INTLIST'),('Stars','INT'),('QueryMes','STRING'),
		('MessageID','INT'),('HasReceiver','BOOL'),('HasTag','BOOL'))

		try: (StartTime,FinishTime,Maxnum,Page,Type,Group,Sender,Tags,Stars,QueryMes,MessageID,HasReceiver,HasTag) = Decoder(request.args,params)
		except: return api_abort(400,"Invalid request") 

		if StartTime != None: sql_where.append('''TIMESTAMPDIFF(second,"%s",message.time) >= 0'''%time.strftime("%Y-%m-%d %H:%M:%S",StartTime))
		if FinishTime != None: sql_where.append('''TIMESTAMPDIFF(second,message.time,"%s") >= 0'''%time.strftime("%Y-%m-%d %H:%M:%S",FinishTime))

		if Maxnum == None: Maxnum = 50 
		if Page == None: Page = 1
		sql_limit = 'LIMIT %d,%d'%(Maxnum*(Page-1),Maxnum)

		if Type != None: 
			if not Type in [1,2]: return api_abort(400,"Confused Type")
			sql_where.append('''message.type = %s'''%Type)

		if Sender != None: sql_where.append('''message.senderID in %s'''%Convert.ToString(Sender))

		if Stars != None:
			if not Stars in [0,1,2,3]: return api_abort(400,"Confused Stars")
			sql_where.append('''message.stars = %s'''%Stars)

		if QueryMes != None:
			QueryMes = "'%" + QueryMes + "%'"
			sql_where.append('''(message.body LIKE %s OR message.title LIKE %s OR message.sender LIKE %s)'''%(QueryMes,QueryMes,QueryMes))
		
		gsb = set()
		gss = set()
		mesID = set()
		SerachAttendGroup(db,uid,gsb,gss) # 获取用户所在的所有组织
		# 从这些组织的消息列表/用户自身的消息列表中得出用户的所有message列表
		for i in gsb:
			try: mesID.update(db.tgb.smembers(i))
			except: pass
		
		for i in gss:
			try: mesID.update(db.tgs.smembers(i))
			except: pass

		try: mesID.update(db.tu.smembers(uid))
		except: pass
		# 拼出sql查询语句
		sql_final_query = ''
		if MessageID != None: # 优先处理MessageID请求
			if str(MessageID) in mesID: # 确认权限
				sql_final_query = '''SELECT ID,UNIX_TIMESTAMP(time) AS time,title,body,type,sender,stars,senderID,OriGroup,tag,images,summary FROM message 
					WHERE message.ID = %s
					'''%MessageID
		else:
			# if Group != None: # 如果需要通过组织筛选
			# 	gs = set()
			# 	for i in Group:
			# 		print(i)
			# 		gs.update(db.tgb.smembers(i))
			# 		gs.update(db.tgs.smembers(i))
			# 	mesID.intersection_update(gs)
			if Tags != None: # 如果需要通过tag筛选
				gs = set()
				try:
					for i in Tags:
						db.crs.execute('''SELECT messageID FROM tag2message WHERE tagID = %s''',i)
						res = db.crs.fetchall()
						for j in res: gs.add(str(j[0]))
				except: return api_abort(500,"SQL ERROR")
				mesID.intersection_update(gs)
			
			sql_final_query = '''SELECT ID,UNIX_TIMESTAMP(time) AS time,title,body,type,sender,stars,senderID,OriGroup,tag,images,summary FROM message 
				WHERE 
				message.ID IN%s
				'''%Convert.ToString(mesID)
			for i in sql_where:
				sql_final_query += '''AND %s\n'''%i
		sql_final_query += "ORDER BY time DESC\n"
		sql_final_query += sql_limit
		#print(sql_final_query)
		try:
			db.crs.execute(sql_final_query)
			res = db.crs.fetchall()
			if Empty(res):raise ValueError()
		except:
			return api_abort(204,'NO CONTENT!')
		# 获取到结果后进行格式化处理
		mesgs = []
		for i in res:
			if Group != None and i[8] != Group: continue
			ID = int(i[0])
			Flag = False
			try:
				db.crs.execute('''SELECT CASE WHEN COUNT(*) > 0 THEN 'True' ELSE 'False' END AS Result
					FROM HaveRead WHERE userID = %s AND MessageID = %s;''',(uid,ID))
				Res_haveRead = db.crs.fetchall()
				if Res_haveRead[0][0] == 'True': Flag = True
			except:
				return api_abort(500,"SQL ERROR")
			try:
				if HasReceiver: # 在结果中加入收信人信息
					Recivers = []
					ReceiverBoardcast = set.intersection(gsb,db.tgbc.smembers(ID))
					ReceiverSingle = set.intersection(gss,db.tgsc.smembers(ID))
					ReceiverUser = db.tuc.smembers(ID)
					for j in ReceiverBoardcast:Recivers.append({'GroupName':GetGroupName(db.crs,int(j)),'GroupID':ID})
					for j in ReceiverSingle:Recivers.append({'GroupName':GetGroupName(db.crs,int(j)),'GroupID':ID})
					if str(uid) in ReceiverUser:Recivers.append({'Self':True})
			except:
				return api_abort(500,"DATABASE ERROR")
			try: 
				db.crs.execute('''SELECT scheduleID,title,body,origin,type,UNIX_TIMESTAMP(starttime) AS starttime
				,UNIX_TIMESTAMP(finishtime) AS finishtime,location,stars FROM `schedule` WHERE origin = %s''',ID)
				res = db.crs.fetchall()
				ssdes = []
				for sche in res:
					db.crs.execute('''SELECT * FROM `HaveCreate` WHERE userID = %s AND scheduleID = %s''',(uid,sche[0]))
					HaveCreate = db.crs.fetchall()
					if(len(HaveCreate) == 0): hc = False
					else: hc = True
					ssdes.append({
						"ScheduleID":sche[0],
						"Title":sche[1],
						"Body":sche[2],
						"Origin":sche[3],
						"Type":sche[4],
						"StartTime":sche[5],
						"FinishTime":sche[6],
						"Location":sche[7],
						"Stars":sche[8],
						"Created":hc})
			except: return api_abort(500,"sql query ERROR")
			sd = i[5]
			if sd == None: sd = GetUserName(db.crs,i[7])
			mesgs.append({
				"MessageID":ID,
				"Time":i[1],
				"Title":i[2],
				"Body":i[3],
				"Type":i[4],
				"Sender":sd,
				"Schedules":ssdes,
				"Stars":i[6],
				"OriGroupID":i[8],
				"OriGroupName":GetGroupName(db.crs,i[8]),
				"Tags":i[9],
				"Images":i[10],
				"Summary":i[11],
				"HaveRead":Flag,
			})
			if HasReceiver: 
				mesgs[-1]["Receiver"]=Recivers
		db.close()
		return jsonify(mes_schema(len(mesgs),Page,mesgs))

	def post(self): # 发送消息
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		Schedules = None
		Sender = "null"
		Images = ""
		print(request.form)
		params = (('OriginGroup','INT'),('ToUser','INTLIST','ARL'),('ToGroupBoardCast','INTLIST','ARL'),('ToGroupThrough','INTLIST','ARL'),
		('ToGroupSingle','INTLIST','ARL'),('Title','STRING','NN'),('Sender','STRING'),('Body','STRING'),('Images','STRING'),
		('Schedules','INTLIST','ARL'),('Type','INT'),('Tags','STRING'),('Stars','INT'))

		try: org,ftu,ftgb,ftgt,ftgs,Title,Sender,Body,Images,Schedules,Type,Tags,Stars = Decoder(request.form,params)
		except: return api_abort(400,"invalid form")
		
		if not Type in [1,2]: return api_abort(400,"invalid form")
		if not Stars in [0,1,2,3]: return api_abort(400,"invalid form")
		if org == None: return api_abort(400,"invalid form")
		if Images == "": Images = None
		if Tags == '''[""]''': Tags = None
		# 排除收件人为空的情况
		if len(ftu) == 0 and len(ftgb) == 0 and len(ftgt) == 0 and len(ftgs) == 0:
			return api_abort(400,"the reciver of this message is empty")
		# 验证附件列表里的所有日程
		for i in Schedules:
			if not ValidateScheduleCR(db,i,uid):
				return api_abort(403,'invalid scheduleID')
		# 利用这个dfs在验证权限的同时记录要接受消息的组织
		Boardcast = set(ftgb)
		Single = set(ftgs)
		gs = set()
		dfs(org,ftgt,gs,db.crs,Single)

		if not Empty(ftgt): return api_abort(403,"invalid reciver")
		if not CheckAuth(db,uid,org): return api_abort(403,"unauthorized")
		if not ValidateInput(gs,Boardcast,ftu,db.crs): return api_abort(403,"invalid reciver")
		
		# 如果一个消息既要被广播,又要被单独传达,就取消单独传达
		for i in Boardcast:
			if i in Single:
				Single.remove(i)
		
		#将消息存储进sql
		
		try: summary = get_summary(Body)
		except: summary = None
		print(summary)

		db.crs.execute('''INSERT INTO `message` (title,body,type,sender,senderID,stars,OriGroup,tag,images,summary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(Title,Body,Type,Sender,uid,Stars,org,Tags,Images,summary))
		db.crs.execute("SELECT LAST_INSERT_ID() FROM `message`")
		res = db.crs.fetchall()
		ID = int(res[0][0])
		# 将附属日程的origin更新
		for i in Schedules:
			db.crs.execute('''UPDATE schedule SET origin = %s WHERE scheduleID = %s AND creator = %s''',(ID,i,uid))
			# 给消息打上tag
			# for i in Tags:
			# 	db.crs.execute('''INSERT INTO `tag2message` (tagID,messageID) VALUES (%s,%s)''',(i,ID))
		#except: return api_abort(500,"sql insert error")

		# 将收件人和附带的日程存储进redis
		try:
			SaveCache(db,ID,Boardcast,Single,ftu)
			SaveLog(db,ID,Boardcast,Single,ftu)
			#SaveSchedule(db,ID,Schedules)
		except: return(api_abort(500,"something wrong when saving log"))

		db.commit()
		db.close()
		response = jsonify({'MessageID':ID})
		response.status_code = 201
		return response

	def delete(self): # 删除消息
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")
		
		params = (('MessageID','INTLIST','ARL'),)  # 元组只有一个元素的时候要加逗号显示强调这是一个元组
		try: (mesID,) = Decoder(request.args,params)
		except: api_abort(400,"invalid request")

		for i in mesID:
			if not CheckDeleteAuth(db.crs,uid,i):    # 确认是否拥有删除消息的权限
				return api_abort(403,"unauthorized") # 实际上是搜索用户是否是有权管理origroup
		# 删除消息的记录
		try:
			for i in mesID:
				tmp = db.tgbc.smembers(i)
				for j in tmp:
					db.tgb.srem(j,i)
				db.tgbc.delete(i) # 从缓存数据库中删除消息
				tmp = db.tgsc.smembers(i)
				for j in tmp:
					db.tgs.srem(j,i)
				db.tgsc.delete(i)
				tmp = db.tuc.smembers(i)
				for j in tmp:
					db.tu.srem(j,i)
				db.tuc.delete(i)
				db.crs.execute('''DELETE FROM message WHERE ID = %s''',i)
				db.crs.execute('''DELETE FROM `schedule` WHERE origin = %s''',i)
		except: return api_abort(500,'database error')
		db.commit()
		db.close()
		return api_abort(204)

api_v1.add_url_rule('/message', view_func=MessageAPI.as_view('Message_API'), methods=['GET','POST','DELETE'])

class ReadAPI(MethodView):
	decorators = [auth_required]
	def get(self):
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		messageID = None

		params = (('MessageID','INT','NN'),)

		try: messageID = Decoder(request.args,params)
		except: return api_abort(400,"invalid form")
		
		try:
			db.crs.execute('''SELECT * FROM `HaveRead` WHERE userID = %s AND messageID = %s''',(uid,messageID))
			res = db.crs.fetchall()
			if Empty(res):
				response = jsonify({'HaveRead':False})
			else:
				response = jsonify({'HaveRead':True})
			response.status_code = 200
			return response 
		except: return api_abort(500,"sql query error")
	
	def post(self):
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		messageID = None

		params = (('MessageID','INT','NN'),)

		try: messageID = Decoder(request.form,params)
		except: return api_abort(400,"invalid form")
		
		try:
			db.crs.execute('''REPLACE INTO `HaveRead` (userID,messageID) VALUES (%s,%s)''',(uid,messageID))
			db.commit()
			return api_abort(204)
		except: return api_abort(500,"sql insert error")
	
	def delete(self):
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		messageID = None

		params = (('MessageID','INT','NN'),)

		try: messageID = Decoder(request.args,params)
		except: return api_abort(400,"invalid form")
		
		try:
			db.crs.execute('''REPLACE INTO `HaveDelete` (userID,messageID) VALUES (%s,%s)''',(uid,messageID))
			db.commit()
			return api_abort(204)
		except: return api_abort(500,"sql insert error")

api_v1.add_url_rule('/messageConfirm', view_func=ReadAPI.as_view('Read_API'), methods=['GET','POST','DELETE'])