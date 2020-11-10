'''
2020年11月10日10:28:08
内容：继承、重写、多态
一、继承
概念：
继承是面向对象编程中一个重要功能，它指的是新设计的类（子类）可以使用现有类（父类）所有的功能，并可以对这些功能进行扩展。继承是面向对象编程中一个重要功能，它指的是新设计的类（子类）可以使用现有类（父类）所有的功能，并可以对这些功能进行扩展。
语法格式：
1)单继承
class 类名（父类）:
    属性集合
    方法集合

2)多继承
class 类名（父类1，父类2）:
    属性集合
    方法集合

二、重写
父类方法的重写

三、多态

'''
# 人类
class Person:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def speak(self,talk):
        print(self.name,"在说",talk)
    def run(self):
        print(self.name,"在跑步")

class Person2:
    def __init__(self,age):
        self.age = age
    def eat(self,food):
        print("在吃",food)

# 学生类
class Student(Person,Person2):
    def __init__(self,no,name,sex,age):
        self.no = no
        self.name = name
        self.sex = sex
        self.age = age
    def speak(self,talk):
        print(self.name, "用普通话在说", talk)

# 普通的人类
class Putongren(Person,Person2):
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age


# 构造场景
stu1 = Student("20180301","张三","男",19)
putong = Putongren("李四","女",18)

def speak(ren):
    ren.speak("我要吃饭")

speak(putong)

