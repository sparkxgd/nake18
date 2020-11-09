'''
2020年11月9日08:35:23
继承、重写、多态


继承的语法格式：
class 类的名称（父类1，父类2,...）：
    属性的集合
    方法的集合

'''
# 动物类（父类）
class Animal:
    def run(self):
        print("Animal在跑。。。。")
    def speak(self):
        print("Animal在叫。。。。")

# 人类
class Person(Animal):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    # def speak(self):
    #     print(self.name,"在说")

# 狗类
class Dog(Animal):
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(self.name,"在汪汪汪的叫。。。")

'''
一个人，一条狗
'''

def speak(animal):
    animal.speak()


p1 = Person("张三","男")
dog = Dog("旺财")

speak(p1)