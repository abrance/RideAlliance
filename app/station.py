
import inspect
import re
import datetime

"""
station: 驿站
我们要搭建点对点的平台，考虑到具体场景（需要快速响应，使用时段不平均，需要对使用日志进行追踪等需求），决定各个驿站都会部署服务器

"""

class Station(object):
    """
    Station需要有类属性：
    Station的实例属性：location scale(ob){has_server capacity team(ob){length guard manager agent adviser} ...}  
    id: 驿站唯一标识
    位置： 点对点服务本质
    规模： station决定了能力
    """
    
    def __init__(self):
        self.location = None
        self.scale = None

class Scale(object):
    """
    规模类属性：
    规模实例属性：team(ob){length guard manager agent adviser}
    
    """

    def __init__(self):
        pass
    
class Team(object):
    """
    队伍类属性：
    队伍实例属性：
    """
    def __init__(self):
        self.team = None
        self.length = None
        self.guard = None
        self.manager = None
        self.agent = None
        self.adviser = None


class Member(object):
    """
    组织成员类属性：
    组织成员实例属性：组织成员 id 唯一表示
    """
    def __init__(self, *args, **kwargs):
        self.id = None

        self.work_id = None
        
        self.health = None
        self.temperament = None
        self.family = None
        self.stu = None

        self.hometown = None
        self.mail = None
        self.tel = None
        self.interest = None
        self.birth = None
        self.age = None
        self.gender = None
        if len(args) == 13:
            pass
        f = [i for i in dir(Member) inspect.isfunction(getattr(Member, i))]
        for k, v in kwargs.items():
            if 'set_'+k in f:
                try:
                    ret = getattr(self, 'set_'+k)(v)
                    if not ret:
                        print('error k: {} v: {}'.format(k, v))
                except Exception as e:
                    print(e)
                    continue
                    

    def set(self, *args, **kwargs):
        pass

    def set_work(self, *args, **kwargs):
        pass

    def set_health(self, *args, **kwargs):
        pass

    def set_temperament(self, *args, **kwargs):
        pass

    def set_family(self, *args,  **kwargs):
        pass

    def set_stu(self, *args, **kwargs):
        pass

    def set_hometown(self, town):
        length = len(town)
        if 0 < length <= 255:
            self.hometown = town
            return True
        else:
            return False

    def set_mail(self, mail):
        if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',text):
            self.mail = mail
            return True
        else:
            return False

    def set_tel(self, tel):
        f = re.findall(r"1\d{10}", tel)
        if f:
            self.tel = f
            return True
        return False

    def set_interest(self, interest: list):
        for i in interest:
            if isinstance(i, str) and len(i) <= 8:
                continue
            else:
                return False
        self.interest = interest
        return True

    def set_birth(self, str_birth):
        # 接受如 1912-09-21 这种字符串
        try:
            birth = datetime.datetime.strptime(str_birth, '%Y-%m-%d').date()
            self.birth = birth
        except Exception as e:
            print('str_birth error {}'.format(e))
            return False

    def set_age(self, age):
        if isinstance(age, int) and 14 < age < 120:
            self.age = age
            return True
        return False

    def set_gender(self, gender):
        if gender in ('f',  'm'):
            self.gender = gender
            return True
        return False

        
class Work(object):
    """
    岗位
    """
    def __init__(self):
        self.id = None


class SafeGuard(Work):
    """
    保卫：
    """
    duty = ['保护...']

    def __init__(self):
        pass


class Manage(Work):
    """
    管理station：
    """
    duty = ['管理station']


class Manager(Member):
    """
    station经理
    """
    def __init__(self):
        super(Manager, self).__init__(*args, **kwargs)

    def set_work(self):
        return super(Manager, self).set_work(id=1)
    
    
def add_member():
    pass

    
def create_team():
    pass
