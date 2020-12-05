'''
面向对象
1、创建类
语法格式
1)无继承
class 类的名称：
    属性的集合
    方法的集合
2)继承
class 类的名称（父类1，父类2，...）：
    属性的集合
    方法的集合
'''
# 人类
class Person:
    # 构造方法（初始化）
    def __init__(self,sex,age,name):
        # 属性的集合
        self.sex = sex
        self.age = age
        self.name = name
    # 方法的集合

    # 跑步
    def run(self):
        print(self.name,"在跑步。。。。。")

    # 说话
    def speak(self,content):
        print(self.name,"在说：",content)

    # 吃东西
    def eat(self,food):
        print(self.name,"在吃",food.name)

# 食物类
class Food:
    def __init__(self,name):
        self.name = name


# 场景
# 一个叫小明的人，在一边说话一边吃苹果
xiaoming = Person("男",18,"小明")
apple = Food("苹果")

xiaoming.speak("下课了，吃饭。。。")
xiaoming.eat(apple)