from details.api_v1.tools import Empty
from details.api_v1.database import DataBase
from details.api_v1.convert import Convert

def SerachAttendGroup(db:DataBase,uid:int,gsb:set,gss:set)->None:
	"""搜索uid所在的所有组织"""
	db.crs.execute('''SELECT user2group.groupID FROM user2group WHERE user2group.userID = %s''',uid)
	d = list(db.crs.fetchall())
	for i in d:
		j = i[0]
		gss.add(str(j))
		while(1):
			gsb.add(str(j))
			db.crs.execute('''SELECT fathergroupID FROM groupextend
				INNER JOIN `group` ON `group`.groupID = groupextend.fathergroupID
				WHERE groupextend.groupID = %s;''',j)
			res = db.crs.fetchall()
			if Empty(res): break
			else: j = res[0][0]

def SearchGroup(x:int,db:DataBase,gs,detailed:bool=False)->None:
	"""深搜,返回所有经过的组织"""
	if detailed:
		db.crs.execute('''SELECT groupextend.groupID,`group`.`name`,`group`.type FROM groupextend
			INNER JOIN `group` ON `group`.groupID = groupextend.groupID
			WHERE fathergroupID = %s''',x)
		res = db.crs.fetchall()
		for i in res:
			gs.append({'GroupID':i[0],'Name':i[1],'Type':i[2],'FatherGroupID':x})
			SearchGroup(i[0],db,gs,detailed)
	else:
		db.crs.execute('''SELECT groupID FROM groupextend WHERE fathergroupID = %s''',x)
		res = db.crs.fetchall()
		gs.add(x)
		for i in res:
			SearchGroup(i[0],db,gs,detailed)

def SearchAdmin(x:int,db:DataBase,gs:set)->set:
	"""返回x子树上组织的所有管理员,gs是子树上组织的集合"""
	query = '('+str(x)+','
	for i in gs: query += (str(i['GroupID'])+',')
	query = query[:-1] + ')'

	db.crs.execute('''SELECT admin2group.userID,`user`.`name`,admin2group.groupID,admin2group.type 
		FROM admin2group
		INNER JOIN `user` ON `user`.userID = admin2group.userID
		WHERE groupID IN%s'''%query)
	return db.crs.fetchall()

def SerachAdminGroup(db:DataBase,uid:int,gs:set)->None:
	"""搜索uid所管理的所有组织"""
	db.crs.execute('''SELECT admin2group.groupID FROM admin2group WHERE admin2group.userID = %s''',uid)
	d = db.crs.fetchall()
	for i in d:
		SearchGroup(i[0],db,gs)
		
def CheckAuth(db:DataBase,uid:int,gid:int,auth:int = 0,upsearch:bool = False)->bool:
	"""
	判断序号为uid的用户是否有管理序号为gid的组织的权限
	若upsearch = True会在组织关系树中向上搜索
	auth = 1 需求assistant以上权限
	auth = 2 需求admin以上权限
	auth = 3 需求owner以上权限
	"""
	while True:
		db.crs.execute('''SELECT `type` FROM admin2group WHERE userID=%s and groupID=%s''',(uid,gid))
		res = db.crs.fetchall()
		if not upsearch:
			if Empty(res): return False
			else: return auth <= res[0][0]
		else:
			if not Empty(res) and auth <= res[0][0]:return True
			# print(gid)
			db.crs.execute('''SELECT fathergroupID FROM groupextend WHERE groupID=%s''',gid)
			res = db.crs.fetchall()
			if Empty(res):return False
			else: gid = res[0][0]

def GetHighestAuth(db:DataBase,uid:int,gid:int)->bool:
	"""
	判断序号为uid的用户是否有管理序号为gid的组织的权限
	若upsearch = True会在组织关系树中向上搜索
	auth = 1 需求assistant以上权限
	auth = 2 需求admin以上权限
	auth = 3 需求owner以上权限
	"""
	Auth = 0
	while True:
		db.crs.execute('''SELECT `type` FROM admin2group WHERE userID=%s and groupID=%s''',(uid,gid))
		res = db.crs.fetchall()
		
		if not Empty(res):
			Auth = max(Auth,res[0][0])
		db.crs.execute('''SELECT fathergroupID FROM groupextend WHERE groupID=%s''',gid)
		res = db.crs.fetchall()
		if Empty(res):break
		else: gid = res[0][0]
	return Auth

def CheckDeleteAuth(crs,uid,mesID):
	crs.execute('''SELECT OriGroup FROM message WHERE ID = %s''',mesID)
	res = crs.fetchall()
	if Empty(res): return False
	else: gid = res[0][0]
	while(1):
		crs.execute('''SELECT userID FROM admin2group WHERE userID=%s and groupID=%s''',(uid,gid))
		res = crs.fetchall()
		if not Empty(res): return True
		print(gid)
		crs.execute('''SELECT fathergroupID FROM groupextend WHERE groupID=%s''',gid)
		res = crs.fetchall()
		if Empty(res):return False
		else: gid = res[0][0]

# 对于用户输入进行验证
# gs: 拥有管理权限的组  tglo: 用户输入的组织集合  tul: 用户输入的用户集合
# 判断输入的组织\用户是否都在gs内
def ValidateInput(gs,tglo,tulo,crs):
	if len(tulo)!=0:
		for i in tulo:
			crs.execute('''SELECT groupID FROM user2group WHERE userID=%s''',i)
			res = crs.fetchall()
			flag = False
			for j in res:
				if j[0] in gs:
					flag = True
					break
			if not flag:
				return False
	# print(tglo)
	return tglo.issubset(gs)


def ValidateUserInGs(gs:set,uid:int,db:DataBase)->bool:
	"""
	gs: 组集合  us: 用户集合
	判断输入的用户是否在gs内
	"""
	db.crs.execute('''SELECT groupID FROM user2group WHERE userID=%s''',uid)
	res = db.crs.fetchall()
	flag = False
	for j in res:
		if j[0] in gs:
			flag = True
			break
	return flag

def ValidateMessageID(db:DataBase,uid:int,mesID:int)->bool:
	"""这个函数确认某个消息能否被某个用户访问到"""
	gsb = set()
	gss = set()
	SerachAttendGroup(db,uid,gsb,gss)
	if Empty(set.intersection(db.tgbc.smembers(str(mesID)),gsb)) and Empty(set.intersection(db.tgsc.smembers(str(mesID)),gss)) and Empty(set.intersection(db.tuc.smembers(str(mesID)),set(str(uid)))):
		return False
	else: return True

def ValidateScheduleIDFM(db:DataBase,sID:int,mID:int)->bool:
	"""这个函数确认某个日程是不是某个消息的附属日程"""
	db.crs.execute('''SELECT `owner` FROM `schedule` WHERE scheduleID = %s AND origin  = %s AND `owner` = 0''',(sID,mID))
	res = db.crs.fetchall()
	if Empty(res): return False
	else: return res[0][0] == 0

def ValidateScheduleID(db:DataBase,sID:int,uid:int)->bool:
	"""这个函数确认某个日程是不是某用户的一个普通日程"""
	db.crs.execute('''SELECT * FROM `schedule` WHERE `owner` = %s AND scheduleID = %s''',(uid,sID))
	return not Empty(db.crs.fetchall())

def ValidateScheduleCR(db:DataBase,sID:int,uid:int)->bool:
	"""这个函数确认某个附属日程是不是某个人创建的,且是否为无主的"""
	db.crs.execute('''SELECT * FROM `schedule` WHERE creator = %s AND scheduleID = %s AND `owner` = 0 AND origin IS NULL''',(uid,sID))
	return not Empty(db.crs.fetchall())

def IsFather(db:DataBase,gid:int,fgid:int)->bool:
	"""这个函数确认fgid是否为gid的父组织"""
	while gid != fgid:
		db.crs.execute('''SELECT fathergroupID FROM groupextend WHERE groupID = %s''',gid)
		res = db.crs.fetchall()
		if Empty(res): return False
		else: gid = res[0][0]
	return True

def CheckGroupType(db:DataBase,gid:int,type:int = 0)->bool:
	"""确认某个组织是不是type类型的组织"""
	db.crs.execute('''SELECT type FROM `group` WHERE groupID = %s''',gid)
	res = db.crs.fetchall()
	if Empty(res): return False
	else: return res[0][0] == type

def ValidateAccount(db:DataBase,usernm:str,pwd:str)->bool:
	"""验证用户名与密码"""
	db.crs.execute('''SELECT userID FROM `user` WHERE binary username = %s and binary password = %s;''',(usernm,pwd))
	res = db.crs.fetchall()
	if len(res)==0: return None
	else: return res[0][0]