import pymysqlpool,redis
from details.api_v1 import TGboardcast_pool,TGboardcast_cache_pool,TGsingle_cache_pool,TGsingle_pool,TUser_cache_pool,TUser_pool,Schedules_pool,Mysqlpool

class DataBase:
	def __init__(self):
		self.tgb = redis.Redis(connection_pool = TGboardcast_pool)
		self.tgs = redis.Redis(connection_pool = TGsingle_pool)
		self.tu = redis.Redis(connection_pool = TUser_pool)
		self.tgbc = redis.Redis(connection_pool = TGboardcast_cache_pool)
		self.tgsc = redis.Redis(connection_pool = TGsingle_cache_pool)
		self.tuc = redis.Redis(connection_pool = TUser_cache_pool)
		self.sche = redis.Redis(connection_pool = Schedules_pool)
		self.db = Mysqlpool.get_connection()
		self.crs = self.db.cursor()
		self.crs.execute("USE details")
	def close(self):
		self.tgb.close()
		self.tgs.close()
		self.tu.close()
		self.tgbc.close()
		self.tgsc.close()
		self.tuc.close()
		self.sche.close()
		self.crs.close()
		self.db.close()
	def commit(self):
		self.db.commit()