'''
面向对象
2020年11月2日08:36:42
内容：
1、类的创建
1)普通
class 类的名称：
    # 类的属性
    # 类的方法

2)继承类
class 类的名称（继承的父类）：
    # 类的属性
    # 类的方法

2、类的使用（实例化）

'''

# 人类
class Person:
    # 人类属性(类属性)
    # name = ""
    # sex = "女"
    # age = 20
    # 人类属性（实例属性,构造方法）
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    # 人类的方法（动作:跑步）
    def run(self):
        print(self.name,"在跑步")

    # 人类的方法（动作:跑步）
    def eating(self,food):
        print(self.name,"正在吃",food)


# 类的使用(实例化，构造出来)
xiaoming = Person("小明","男",1)
lilei = Person("李磊","男",20)

# 查看信息
print(lilei.name)
# 类的方法的使用
lilei.run()

'''
题目：设计一个统计班级人数的系统

'''
# 班级类
class Cla:
    def __init__(self,name,num=0):
        self.num = num  # 人数
        self.name = name    # 名称
    def add_stu(self,student):
        self.num +=1
    def del_stu(self,student):
        self.num -= 1
    def count(self):
        print(self.name,"总人数：",self.num)

# 学生类
class Student:
    def __init__(self,name,sex="男",age=19):
        self.name=name
        self.sex = sex
        self.age = age
    # 加入班级
    def add_cla(self,cla):
        cla.add_stu(self)
    # 退出班级
    def del_cla(self,cla):
        cla.del_stu(self)

# 场景设计
'''
一个班级，5个学生
学生加入班级
统计班级的学生人数

'''
cla1 = Cla(name="大数18计科本2班")
shibiao = Student("石彪")
wangquan = Student("王权")
# 学生加入班级
shibiao.add_cla(cla1)
shibiao.add_cla(cla1)
# 统计班级的人数
cla1.count()
