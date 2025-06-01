from flask import Blueprint
from flask_cors import CORS
from details.DatabaseAddress import address
import redis
import pymysqlpool

RedisConfig = {'host':address,'port':3303,'password':'Details@hit_0397428','decode_responses':True}
TGboardcast_pool = redis.ConnectionPool(db= 0, **RedisConfig)
TGsingle_pool = redis.ConnectionPool(db= 1, **RedisConfig)
TUser_pool = redis.ConnectionPool(db= 2, **RedisConfig)
TGboardcast_cache_pool = redis.ConnectionPool(db= 3, **RedisConfig)
TGsingle_cache_pool = redis.ConnectionPool(db= 4, **RedisConfig)
TUser_cache_pool = redis.ConnectionPool(db= 5, **RedisConfig)
Schedules_pool = redis.ConnectionPool(db= 6, **RedisConfig)

MysqlConfig = {'host':address, 'port':3306, 'user':'details', 'password':'Details@hit_0397428', 'database':'details', 'autocommit':False}
Mysqlpool = pymysqlpool.ConnectionPool(**MysqlConfig)

api_v1 = Blueprint("api_v1",__name__)
CORS(api_v1,supports_credentials = True)

from details.api_v1 import userAPI,loginAPI,messageAPI,scheduleAPI,groupAPI,tagAPI,invitationAPI,templateAPI,backupAPI,welinkAPI