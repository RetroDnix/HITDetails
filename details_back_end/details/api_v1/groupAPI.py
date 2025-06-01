from flask import g,request,jsonify
from flask.views import MethodView

from details.api_v1 import api_v1
from details.api_v1.database import DataBase
from details.api_v1.convert import Convert
from details.api_v1.tools import Decoder,Empty
from details.api_v1.checker import SerachAdminGroup,GetHighestAuth,ValidateUserInGs,SearchGroup,CheckAuth,IsFather,CheckGroupType
from details.auth import auth_required,Validate_uid
from details.errors import api_abort

class Group_Superior_API(MethodView):
	# 查询一个组织的上级组织
	decorators = [auth_required]
	def get(self): 
		db = DataBase()
		uid = g.current_user
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		gID = None
		params = (('GroupID','INT','NN'),)
		try: (gID,) = Decoder(request.args,params)
		except: return api_abort(400,'invalid groupID')

		if ValidateUserInGs({gID},{uid},db) == False and CheckAuth(db,uid,gID,upsearch=True) == False:
			return api_abort(403,'You are not in this group,and you are not a admin in this group.')

		db.crs.execute('''SELECT groupextend.fathergroupID FROM groupextend WHERE groupID=%s''',gID)
		fgroup = db.crs.fetchall()
		db.crs.execute('''SELECT `name`,type FROM `group` WHERE groupID=%s''',gID)
		info = db.crs.fetchall()
		
		#if Empty(fgroup) or Empty(info): return api_abort(400,'no data!')
		return jsonify({'GroupID':fgroup[0][0],'Name':info[0][0],'Type':info[0][1]})

class Group_Members_API(MethodView):
	# 查询一个组织的成员
	decorators = [auth_required]
	def get(self): 
		db = DataBase()
		uid = g.current_user
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		gID = None
		params = (('GroupID','INT','NN'),)
		try: (gID,) = Decoder(request.args,params)
		except: return api_abort(400,'invalid groupID')

		if ValidateUserInGs({gID},{uid},db) == False and CheckAuth(db,uid,gID,upsearch=True) == False:
			return api_abort(403,'You are not in this group,and you are not a admin in this group.')

		db.crs.execute('''SELECT user2group.userID,`user`.`name` FROM user2group 
			INNER JOIN `user` ON `user`.userID = user2group.userID
			WHERE groupID=%s''',gID)
		members = db.crs.fetchall()
		res = []
		for member in members:
			res.append({'UserID':member[0],'Name':member[1]})
		return jsonify(members = res)

class Group_Admins_API(MethodView):
	# 查询一个组织的管理员
	decorators = [auth_required]
	def get(self): 
		db = DataBase()
		uid = g.current_user
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		gID = None
		params = (('GroupID','INT','NN'),)
		try: (gID,) = Decoder(request.args,params)
		except: return api_abort(400,'invalid groupID')

		if ValidateUserInGs({gID},{uid},db) == False and CheckAuth(db,uid,gID,upsearch=True) == False:
			return api_abort(403,'You are not in this group,and you are not a admin in this group.')

		db.crs.execute('''SELECT admin2group.userID,`user`.`name`,admin2group.type FROM admin2group 
			INNER JOIN `user` ON `user`.userID = admin2group.userID
			WHERE groupID=%s''',gID)
		members = db.crs.fetchall()
		res = []
		for member in members:
			res.append({'UserID':member[0],'Name':member[1],'type':member[2]})
		return jsonify(admins = res)
	
class Group_Exit_API(MethodView):
	# 退出一个组织
	decorators = [auth_required]
	def delete(self):
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		gID = None
		params = (('GroupID','INT','NN'),)
		try: (gID,) = Decoder(request.args,params)
		except: return api_abort(400,'invalid groupID')

		if ValidateUserInGs({gID},{uid},db) == False:
			return api_abort(403,'You are not in this group')

		db.crs.execute('''SELECT type FROM `group` WHERE groupID = %s''',gID)
		res = db.crs.fetchall()
		if res[0][0] == 0:return api_abort(400,"can't exit a basic group")

		db.crs.execute('''DELETE FROM user2group WHERE userID = %s AND groupID = %s''',(uid,gID))
		db.commit()
		db.close()
		return api_abort(204)

class Group_Sub_API(MethodView):
	# 查询一个组织的下级组织
	decorators = [auth_required]
	def get(self):
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		gID = None
		params = (('GroupID','INT','NN'),)
		try: (gID,) = Decoder(request.args,params)
		except: return api_abort(400,'invalid groupID')

		if CheckAuth(db,uid,gID,upsearch=True) == False:
			return api_abort(403,'You are a admin of this group')

		db.crs.execute('''SELECT groupextend.groupID,`group`.`name`,`group`.`type` FROM groupextend
			INNER JOIN `group` ON `group`.groupID = groupextend.groupID
			WHERE groupextend.fathergroupID = %s''',gID)
		subgroups = db.crs.fetchall()
		res = []
		for subgroup in subgroups:
			res.append({'GroupID':subgroup[0],'Name':subgroup[1],'Type':subgroup[2]})
		return jsonify(subgroups = res)

class Group_Modify_Permissions_API(MethodView):
	# 修改管理员权限
	decorators = [auth_required]
	def post(self): 
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		org = UserID = GroupID = Role = None
		params = (('OriginGroup','INT'),('UserID','INT','NN'),('GroupID','INT','NN'),('Role','STRING','NN'))
		try: org,UserID,GroupID,Role = Decoder(request.form,params)
		except: return api_abort(400,"bad request")

		# if org == GroupID: au = 2
		# else: au = 1
		# print(org)
		
		if(GetHighestAuth(db,uid,GroupID) < 3): return api_abort(403)
		# if not CheckAuth(db,uid,org,2,False): return api_abort(403,'Invalid OriginGroup')
		# if not IsFather(db,GroupID,org): return api_abort(403,'Target group is not a subgroup of the origin group.')

		if Role == 'Member':
			db.crs.execute('''DELETE FROM admin2group WHERE userID = %s AND groupID = %s''',(UserID,GroupID))
		else:
			db.crs.execute('''REPLACE INTO admin2group(userID,groupID,type) VALUES(%s,%s,%s)''',(UserID,GroupID,Convert.DisAuthority(Role)))
		
		db.commit()
		return api_abort(204)

class Group_Create_Group_API(MethodView): 
	# 创建组织
	decorators = [auth_required]
	def post(self): 
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		GroupName = Users = None
		params = (('GroupName','STRING','NN'),('Users','INTLIST','ARL'))
		try: GroupName, Users = Decoder(request.form,params)
		except: return api_abort(400,"bad request")

		try:
			db.crs.execute('''INSERT INTO `group`(name,type) VALUES(%s,%s) ''',(GroupName,2))
			db.crs.execute("SELECT LAST_INSERT_ID() FROM `group`")
			ID = (db.crs.fetchall())[0][0]
			db.crs.execute('''INSERT INTO admin2group(userID,groupID,type) VALUES(%s,%s,3)''',(uid,ID))
			db.crs.execute('''INSERT INTO user2group(groupID,userID) VALUES(%s,%s)''',(ID,uid))

			gs = set()
			SerachAdminGroup(db,uid,gs) 
			res = {}
			res['GroupID'] = ID
			ures = list()
			for i in Users:
				ures.append({'UserID':i})
				if ValidateUserInGs(gs,i,db):
					ures[-1]['Type'] = 0
					db.crs.execute('''INSERT INTO user2group(groupID,userID) VALUES(%s,%s)''',(ID,i))
				else:
					ures[-1]['Type'] = 1
					db.crs.execute('''INSERT INTO `invitations` (inviter,groupID,userID) VALUES (%s,%s,%s)''',(uid,ID,i))
		except: return api_abort(500,'sql insert error')
		db.commit()
		res['Users'] = ures
		response = jsonify(res)
		response.status_code = 202
		return response
	
class Group_Modify_Superior_Group_API(MethodView): 
	# 修改上级组织
	decorators = [auth_required]
	def post(self):
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		gid = fgid = None
		params = (('GroupID','INT','NN'),('FatherGroupID','INT',0))
		try: gid,fgid = Decoder(request.form,params)
		except: return api_abort(400,"bad request")

		if not CheckAuth(db,uid,gid,3,True):
			return api_abort(403,'invalid groupID')
		
		if gid == fgid: api_abort(400,"can't set a group as its own father group")
		
		try:
			if fgid == 0: db.crs.execute('''DELETE FROM groupextend WHERE groupID = %s''',gid)
			else: db.crs.execute('''REPLACE INTO groupextend(groupID,fathergroupID) VALUES(%s,%s)''',(gid,fgid))
		except: return api_abort(500,'sql insert error')

		db.commit()
		return api_abort(204)

class Group_Modify_Member_API(MethodView): 
	# 增加/删除成员
	decorators = [auth_required]
	def post(self):
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		UID = GroupID = Type = None
		params = (('UserID','INT','NN'),('GroupID','INT','NN'),('Type','INT','NN'))
		try: UID,GroupID,Type = Decoder(request.form,params)
		except: return api_abort(400,"bad request")
		if not Type in [0,1]: return api_abort(400,"confused type")

		# if not CheckAuth(db,uid,org,1,False): return api_abort(403,'Invalid OriginGroup')
		# if not IsFather(db,GroupID,org): return api_abort(403,'Target group is not a subgroup of the origin group.')
		if not CheckAuth(db,uid,GroupID,1,True): return api_abort(403,'没有权限操作此群组!')
		# if CheckGroupType(db,GroupID,0): return api_abort(403,"不能修改基本群组!")
		#for i in UIDs:
		#	if not Validate_uid(db,i):
		#		return api_abort(400,"invalid userID")
		if not Validate_uid(db,UID):
			return api_abort(400,"invalid userID")
		if Type == 0:
			try:
				db.crs.execute('''INSERT INTO user2group(groupID,userID) VALUES(%s,%s)''',(GroupID,UID))
				# gs = set()
				# SerachAdminGroup(db,uid,gs) 
				# ures = list()
				# for i in UIDs:
				# 	ures.append({'UserID':i})
					# if ValidateUserInGs(gs,i,db):
					# 	ures[-1]['type'] = 0
					# 	db.crs.execute('''INSERT INTO user2group(groupID,userID) VALUES(%s,%s)''',(GroupID,i))
					# else:
					# 	ures[-1]['type'] = 1
					# 	db.crs.execute('''INSERT INTO `invitations` (inviter,groupID,userID) VALUES (%s,%s,%s)''',(uid,GroupID,i))
			except: return api_abort(500,'sql insert error')
			db.commit()
			#response = jsonify({"Users":ures})
			#response.status_code = 202
			return api_abort(202)
		else:
			try:
				# print(UIDs)
				# for i in UIDs:
				db.crs.execute('''DELETE FROM user2group WHERE groupID = %s AND userID = %s''',(GroupID,UID))
			except: return api_abort(500,'sql insert error')
			db.commit()
			return api_abort(204)

class Group_Delete_Group_API(MethodView): 
	# 增加/删除成员
	decorators = [auth_required]
	def delete(self): 
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		gid = None
		params = (('GroupID','INT','NN'),)
		try: (gid,) = Decoder(request.args,params)
		except: return api_abort(400,'bad request')

		if gid == None: return api_abort(400,'bad request')
		
		if not CheckAuth(db,uid,gid,3,True):
			return api_abort(403,'invalid groupID')
		gs = set()
		SearchGroup(gid,db,gs)
		try:
			for i in gs:
				tmp = db.tgb.smembers(i)
				for j in tmp:
					db.tgbc.srem(j,i)
				db.tgb.delete(i)

				tmp = db.tgs.smembers(i)
				for j in tmp:
					db.tgsc.srem(j,i)
				db.tgs.delete(i)

				tmp = db.tu.smembers(i)
				for j in tmp:
					db.tuc.srem(j,i)
				db.tu.delete(i)

				db.crs.execute('''DELETE FROM `group` WHERE groupID = %s''',i)
		except: return api_abort(500,'sql_error')
		
		db.commit()
		return api_abort(204)
	
api_v1.add_url_rule('/group/superior', view_func=Group_Superior_API.as_view('Group_Superior_API'), methods=['GET'])
api_v1.add_url_rule('/group/members', view_func=Group_Members_API.as_view('Group_Members_API'), methods=['GET'])
api_v1.add_url_rule('/group/admins', view_func=Group_Admins_API.as_view('Group_Admins_API'), methods=['GET'])
api_v1.add_url_rule('/group/exit', view_func=Group_Exit_API.as_view('Group_Exit_API'), methods=['DELETE'])
api_v1.add_url_rule('/group/sub', view_func=Group_Sub_API.as_view('Group_Sub_API'), methods=['GET'])
api_v1.add_url_rule('/group/modify_permissions', view_func=Group_Modify_Permissions_API.as_view('Group_Modify_Permissions_API'), methods=['POST'])
api_v1.add_url_rule('/group/create_group', view_func=Group_Create_Group_API.as_view('Group_Create_Group_API'), methods=['POST'])
api_v1.add_url_rule('/group/modify_superior_group', view_func=Group_Modify_Superior_Group_API.as_view('Group_Modify_Superior_Group_API'), methods=['POST'])
api_v1.add_url_rule('/group/modify_member', view_func=Group_Modify_Member_API.as_view('Group_Modify_Member_API'), methods=['POST'])
api_v1.add_url_rule('/group/delete_group', view_func=Group_Delete_Group_API.as_view('Group_Delete_Group_API'), methods=['DELETE'])

class GroupClassicAPI(MethodView):
	decorators = [auth_required]
	def get(self): # 获取组织详情
		db = DataBase()
		uid = g.current_user
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		gID = None

		params = (('GroupID','INT','NN'),)

		try: (gID,) = Decoder(request.args,params)
		except: return api_abort(400,"bad request")
		
		isMember = False
		db.crs.execute('''SELECT * FROM `user2group` WHERE userID = %s AND groupID = %s''',(uid,gID))
		res = db.crs.fetchall()
		if(not Empty(res)): isMember = True
		Authority = GetHighestAuth(db,uid,gID)
	
		db.crs.execute('''SELECT `name`,type  FROM `group` WHERE groupID = %s;''',gID)
		res = db.crs.fetchall()
		if Empty(res): return api_abort(400,'no data!')
		GroupName = res[0][0]
		GroupType = res[0][1]

		fatherGroup = [{'GroupID':gID,'GroupName':GroupName,'Type':GroupType}]

		j = gID
		while(1):
			db.crs.execute('''SELECT fathergroupID,`group`.`name`,type  FROM groupextend
				INNER JOIN `group` ON `group`.groupID = groupextend.fathergroupID
				WHERE groupextend.groupID = %s;''',j)
			res = db.crs.fetchall()
			if Empty(res): break
			else: fatherGroup.append({'GroupID':res[0][0],'GroupName':res[0][1],'Type':res[0][2]})
			j = res[0][0]
		fatherGroup.reverse()
		return {'GroupID':gID,'GroupName':GroupName,'Type':GroupType,'FatherGroup':fatherGroup,'Authority':Authority,'IsMember':isMember}
api_v1.add_url_rule('/groupClassic', view_func=GroupClassicAPI.as_view('group_cls_API'), methods=['GET'])

class GetSubGroupClassicAPI(MethodView):
	decorators = [auth_required]
	def get(self): # 获取组织详情
		db = DataBase()
		uid = g.current_user
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		gID = None

		params = (('GroupID','INT','NN'),)

		try: (gID,) = Decoder(request.args,params)
		except: return api_abort(400,"bad request")

		gs = list()
		SearchGroup(gID,db,gs,detailed=True)

		return jsonify({'Groups':gs})
		
api_v1.add_url_rule('/getSubGroupClassic', view_func=GetSubGroupClassicAPI.as_view('getsubgroup_cls_API'), methods=['GET'])

