'''
2020年11月13日08:40:19
内容：继承、重写、多态
一、继承
语法格式(单继承)：
class 类名（父类）:
    属性集合
    方法集合

语法格式(多继承)：
class 类名（父类1,父类2，。。。。）:
    属性集合
    方法集合
'''

# 动物类
class Animal:
    # 属性的集合
    def __init__(self,age=1):
        self.age = age
    # 方法的集合
    def run(self):
        print("Animal 在跑。。。。。")
    def eat(self,food):
        print("Animal 在吃",food.name)

# 人类
class Person(Animal):
    # 属性的集合
    def __init__(self, age=1,name=""):
        self.age = age
        self.name = name
    def speak(self,talk):
        print(self.name,"在说",talk)
    # 方法的重写
    def eat(self,food):
        print(self.name,"在吃",food.name)

# 狗类
class Dog(Animal):
    # 属性的集合
    def __init__(self, age=1,name=""):
        self.age = age
        self.name = name
    def jiao(self):
        print(self.name,"在旺旺的叫.....")
    # 方法的重写
    def eat(self,food):
        print(self.name,"在吃",food.name)


# 食物类
class Food:
    def __init__(self,name):
        self.name = name
'''
构造一个场景
1、一个人，一条狗,一个苹果
动物在吃东西
'''
zhangshan = Person(19,"张三")
wangcai = Dog(1,"旺财")
apple = Food("苹果")
# zhangshan.speak("我要吃饭")
# wangcai.jiao()

# 动物在吃东西
def eat(animal,food):
    animal.eat(food)

# 实现
eat(wangcai,apple)