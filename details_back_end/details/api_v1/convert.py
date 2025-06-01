class Convert:
    @staticmethod
    def ToListInt(x)->list:
        """
        将可迭代对象转换为int的list返回
        """
        res = []
        for i in x: res.append(int(i))
        return res
    @staticmethod
    def ToString(x)->str:
        """
        将可迭代对象转换为一个字符串
        """
        if len(x)==0: return "()"
        res = "("
        for i in x:res += "%s,"%i
        return res[:-1]+')'
    @staticmethod
    def ToList(x)->list:
        """
        将可迭代对象转换为一般的list
        """
        res = []
        try: 
            for i in x: res.append(i[0])
        except: 
            for i in x: res.append(i)
        return res
    @staticmethod
    def ToDict(x:set,keys:list)->list:
        """
        将嵌套元组根据keys转换为字典的序列
        """
        res = []
        for i in x:
            res.append({})
            cnt = 0
            for j in i:
                res[-1][keys[cnt]] = j
                cnt += 1
        return res
    @staticmethod
    def ToAuthority(x:int = 0)->str:
        match x:
            case 0: return "Member"
            case 1: return "Assistant"
            case 2: return "Administrator"
            case 3: return "Owner"
            case _: return "UnKnown"
    @staticmethod
    def DisAuthority(x:str)->int:
        match x:
            case 'Assistant': return 1
            case 'Administrator': return 2
            case 'Owner': return 3
            case _: return 0
    
