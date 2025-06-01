from werkzeug.datastructures import MultiDict
from details.api_v1.convert import Convert

import time

def Empty(ary)->bool:
	return len(ary)==0


def GetGroupName(crs,gid:int)->str:
	"""获取某个组的组名"""
	crs.execute('''SELECT `name` FROM `group` WHERE groupID=%s''',gid)
	res = crs.fetchall()
	if len(res)==0: return None
	else: return res[0][0]

def GetUserName(crs,uid:int)->str:
	"""获取某个用户的姓名"""
	crs.execute('''SELECT `name` FROM `user` WHERE userID=%s''',uid)
	res = crs.fetchall()
	if len(res)==0: return None
	else: return res[0][0]

def dfs(x,ls,gs,crs,single):
	crs.execute('''SELECT groupID FROM groupextend WHERE fathergroupID = %s''',x)
	res = crs.fetchall()
	f = False
	gs.add(x)
	for i in res:
		if dfs(i[0],ls,gs,crs,single) == True:
			f = True
	if f:
		single.add(x)
		return True
	elif x in ls:
		single.add(x)
		ls.remove(x)
		return True
	else: return False



def Decoder(data:MultiDict,param:tuple)->tuple:
	"""
	通过param给出的键值对请求进行解析,返回解析完成的数据的元组
	允许的VALUE:
	"LIST":解析为一般的表格(String)
	"INTLIST":解析为整数的表格(Int)
	"INT":解析为数字
	"TIME":将时间戳解析为时间对象
	"STRING":解析为字符串
	"BOOL":解析为布尔值
	"""
	res = list()
	for x in param:
		#print(x)
		match x[1]:
			case "LIST":
				if x[0] in data:
					res.append(data.getlist(x[0]))
				else: res.append(None)
			case "INTLIST":
				if x[0] in data:
					if(data.getlist(x[0]) == ['']):res.append([])
					else: res.append(Convert.ToListInt(data.getlist(x[0])))
				elif x[-1] == 'ARL': # "always return list"
					res.append(list())
				else: res.append(None)
			case "INT":
				if x[0] in data:
					if data.get(x[0]) == 'NaN': res.append(0)
					else: res.append(int(data.get(x[0])))
				elif x[-1] == 'NN': raise ValueError()
				elif x[-1] != 'INT': res.append(int(x[-1]))
				else: res.append(None)
			case "TIME":
				if x[0] in data:
					res.append(time.localtime(eval(data.get(x[0]))))
				else: res.append(None)
			case "STRING":
				if x[0] in data:
					s = str(data.get(x[0]))
					if x[-1] == 'NN' and Empty(s): raise ValueError()
					res.append(s)
				elif x[-1] == 'NN': raise ValueError()
				else: res.append(None)
			case "BOOL":
				if x[0] in data and (data.get(x[0]) == 'True' or data.get(x[0]) == 'true'):res.append(True)
				else: res.append(False)
			case _:
				raise ValueError()
	return tuple(res)