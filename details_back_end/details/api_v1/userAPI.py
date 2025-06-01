from flask import g,jsonify,request
from flask.views import MethodView

from details.api_v1 import api_v1
from details.api_v1.database import DataBase
from details.api_v1.checker import GetHighestAuth
from details.auth import auth_required,Validate_uid
from details.errors import api_abort

def user_schema(uid=0,Name='Null',UserNM="UnKnown"):
	return {
		"UID":uid,
		'Name':Name,
	}

class Username_API(MethodView):
	decorators = [auth_required]
	def get(self):
		uid = g.current_user
		db = DataBase()
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")

		# 查询用户姓名
		db.crs.execute("SELECT `name` FROM `user` WHERE userID = %s",uid)
		res = db.crs.fetchall()
		return jsonify(user_schema(uid,res[0][0]))

class Joined_Group_API(MethodView):
	decorators = [auth_required]
	def get(self): # 获取组织详情
		db = DataBase()
		uid = g.current_user
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")
				
		db.crs.execute('''SELECT user2group.groupID,`group`.`name`,`group`.type FROM user2group 
 					INNER JOIN `group` ON `group`.groupID = user2group.groupID
 					WHERE user2group.userID = %s''',uid)
		data = db.crs.fetchall()
		res = []
		for group in data:
			res.append({
				'GroupID':group[0],
				'Name':group[1],
				'Type':group[2],
			})
		return jsonify(Groups = res)

class Managed_Group_API(MethodView):
	decorators = [auth_required]
	def get(self): # 获取组织详情
		db = DataBase()
		uid = g.current_user
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")
				
		db.crs.execute('''SELECT admin2group.groupID,`group`.`name`,`group`.type FROM admin2group 
 					INNER JOIN `group` ON `group`.groupID = admin2group.groupID
 					WHERE admin2group.userID = %s''',uid)
		data = db.crs.fetchall()
		res = []
		for group in data:
			res.append({
				'GroupID':group[0],
				'Name':group[1],
				'Type':group[2],
			})
		return jsonify(Groups = res)

class Get_Group_API(MethodView):
	decorators = [auth_required]
	def get(self): # 获取组织详情
		db = DataBase()
		uid = g.current_user
		if not Validate_uid(db,uid):return api_abort(400,"Invalid user")
		
		db.crs.execute('''SELECT user2group.groupID,`group`.`name`,`group`.type FROM user2group 
 					INNER JOIN `group` ON `group`.groupID = user2group.groupID
 					WHERE user2group.userID = %s''',uid)
		data = db.crs.fetchall()
		res = []
		vised = {}
		for group in data:
			res.append({
				'GroupID':group[0],
				'Name':group[1],
				'Type':group[2],
				'Authority': GetHighestAuth(db,uid,group[0]),
				'IsMember':True,
			})
			vised[group[0]] = True
		
		db.crs.execute('''SELECT admin2group.groupID,`group`.`name`,`group`.type FROM admin2group 
 					INNER JOIN `group` ON `group`.groupID = admin2group.groupID
 					WHERE admin2group.userID = %s''',uid)
		data = db.crs.fetchall()
		for group in data:
			if(not group[0] in vised):
				res.append({
					'GroupID':group[0],
					'Name':group[1],
					'Type':group[2],
					'Authority': GetHighestAuth(db,uid,group[0]),
					'IsMember':False,
				})

		return jsonify(Groups = res)
	
api_v1.add_url_rule('/user/username', view_func=Username_API.as_view('Username_API'), methods=['GET'])
api_v1.add_url_rule('/user/joined_group', view_func=Joined_Group_API.as_view('Joined_Group_API'), methods=['GET'])
api_v1.add_url_rule('/user/managed_group', view_func=Managed_Group_API.as_view('Managed_Group_API'), methods=['GET'])
api_v1.add_url_rule('/user/get_group', view_func=Get_Group_API.as_view('Get_Group_API'), methods=['GET'])