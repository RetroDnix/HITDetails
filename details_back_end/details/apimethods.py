import pymysql
from collections import deque

def ValidateAccount(crs,usernm,pwd):
    # sql = '''SELECT userID FROM `user` WHERE username = "%s" and password = "%s";'''%(usernm,pwd)
    crs.execute('''SELECT userID FROM `user` WHERE username = %s and password = %s;''',(usernm,pwd))
    res = crs.fetchall()
    # print(sql,res)
    if len(res)==0: return None
    else: return res[0][0]

def Empty(ary):
    return len(ary)==0

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
def bfs(q,gs,crs):
    while len(q)!=0:
        x = q[0]
        q.popleft()
        crs.execute('''SELECT groupextend.groupID FROM groupextend WHERE fathergroupID=%s''',x)
        res = crs.fetchall()
        for i in res:
            q.append(i[0])
            gs.add(i[0])

# 确认权限
# 根据填入auth判断序号为uid的用户是否有管理序号为gid的组织的权限
def CheckAuth(crs,uid,gid,auth = 0):
    crs.execute('''SELECT userID FROM admin2group WHERE userID=%s and groupID=%s''',(uid,gid))
    res = crs.fetchall()
    if Empty(res):return False
    if auth != 0:
        return auth == res[0][0]
    else: return True

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

# 返回的对象
class Pass:
    def __init__(self,deny=False,auth=None,name=None,type=0):
        self.deny = deny
        self.auth = auth
        self.name = name
        self.type = type

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
        ls.remove(x)
        return True
    else: return False