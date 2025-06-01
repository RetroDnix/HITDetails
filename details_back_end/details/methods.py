from collections import deque
import pymysql
from flask import session

from details import app

# 将用户输入转换为数字列表
def splitnum(s):
    l = s.split(',')
    res = set()
    for i in l:
        if i.isdigit():
            res.add(int(i))
    return res

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
    print(tglo)
    return tglo.issubset(gs)

# 获取某个用户的所有有邀请成员权限的组
def GetAdminGroups(crs,uid): 
    q = deque()
    qs = []
    gs = set()
    crs.execute('''SELECT admin2group.groupID,`group`.`name` 
        FROM admin2group 
        INNER JOIN `group` ON `group`.groupID = admin2group.groupID
        WHERE userID = %s and admin2group.au5 = 1''',uid)
    res = crs.fetchall() 
    for i in res:
        q.append(i[0])
        qs.append((i[0],i[1]))
        gs.add(i[0])
    return  q,qs,gs

# 广度优先搜索
# q:双端队列
# qs:以(序号,名字)储存搜索过的组织
# gs:以序号储存搜索过的组织
# q中应当已放入要开始搜索的树根,本函数会按照广度优先规则遍历所有子组织
def bfs(q,qs,gs,crs):
    while len(q)!=0:
        x = q[0]
        q.popleft()
        crs.execute('''SELECT groupextend.groupID,`group`.`name` FROM groupextend
        INNER JOIN `group` ON `group`.groupID = groupextend.groupID
        WHERE fathergroupID=%s''',x)
        res = crs.fetchall()
        for i in res:
            qs.append((i[0],i[1]))
            q.append(i[0])
            gs.add(i[0])

# 确认权限
# 根据填入auth判断序号为uid的用户是否有管理序号为gid的组织的权限
def CheckAuth(crs,uid,gid,auth=[]):
    sql = '''SELECT userID'''
    for i in auth:
        sql += (','+i)
    sql += ''' FROM admin2group WHERE userID=%s and groupID=%s'''
    print(sql)
    while(1):
        crs.execute(sql,(uid,gid))
        res = crs.fetchall()
        print(res)
        if len(res)!=0 and res[0][1:1+len(auth)]==tuple([1]*len(auth)):return True
        crs.execute('''SELECT fathergroupID FROM groupextend WHERE groupID=%s''',gid)
        res = crs.fetchall()
        if len(res)==0:return False
        else: gid = res[0][0]

# 返回的对象
class Pass:
    def __init__(self,deny=False,auth=None,name=None,type=0):
        self.deny = deny
        self.auth = auth
        self.name = name
        self.type = type

# 确认用户对某个组的管理权限(不向上搜索)
def ConfirmAdmin(crs,uid,gid):
    if not 'id' in session: return Pass(deny=True)
    sql = '''SELECT au1,au2,au3,au4,au5,`group`.`name`,`group`.`type`
        FROM admin2group 
        INNER JOIN `group` ON `group`.groupID=admin2group.groupID 
        WHERE admin2group.userID=%s AND admin2group.groupID=%s'''
    crs.execute(sql,(uid,gid))
    res=crs.fetchall()
    if len(res) == 0: return Pass(deny=True)
    else: return Pass(auth=[None]+list(res[0][0:5]),name=res[0][5],type=res[0][6])

# 获取某个组的组名
def GetGroupName(crs,gid):
    crs.execute('''SELECT `name` FROM `group` WHERE groupID=%s''',gid)
    res = crs.fetchall()
    if len(res)==0: return None
    else: return res[0][0]

# 获取某个组的类型
def CheckType(crs,gid):
    crs.execute('''SELECT `type` FROM `group` WHERE groupID=%s''',gid)
    res = crs.fetchall()
    if len(res)==0: return None
    else: return res[0][0]