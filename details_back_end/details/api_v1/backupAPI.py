import os,subprocess,datetime

from flask import jsonify, request,g
from flask.views import MethodView

from details.errors import api_abort
from details.auth import Validate_uid,auth_required
from details.api_v1 import api_v1
from details.api_v1.database import DataBase
from details.api_v1.checker import ValidateAccount
from details.api_v1.tools import Decoder

class BackupMySQL(MethodView):
	def get(self):
		current_time =  datetime.datetime.now()
		# 格式化时间为 "年月日_小时分钟" 的样式
		formatted_time = current_time.strftime("%Y%m%d_%H%M")
		try:
			# 执行备份命令
			subprocess.run("mysqldump -u root -p'Details@hit_0397428' detail > /home/MySQLBackup/%s.sql"%formatted_time, check=True,shell=True)
			return jsonify(promt = "MySQL数据库备份成功！")
		except subprocess.CalledProcessError as e:
			return jsonify(promt = "MySQL数据库备份失败!")

class BackupRedis(MethodView):
	def get(self):
		db = DataBase()
		db.sche.save()
		current_time =  datetime.datetime.now()
		# 格式化时间为 "年月日_小时分钟" 的样式
		formatted_time = current_time.strftime("%Y%m%d_%H%M")
		print(formatted_time)
		try:
			# 执行备份命令
			subprocess.run("cp /var/lib/redis/dump.rdb /home/RedisBackup/%s.rdb "%formatted_time, check=True,shell=True)
			return jsonify(promt = "Redis数据库备份成功！")
		except subprocess.CalledProcessError as e:
			return jsonify(promt = "Redis数据库备份失败!")

api_v1.add_url_rule('/backup/mysql', view_func=BackupMySQL.as_view('BackupMySQL'), methods=['GET'])
api_v1.add_url_rule('/backup/redis', view_func=BackupRedis.as_view('BackupRedis'), methods=['GET'])
