'''
案例一：主人与狗
场景简介：
    主人养一条名叫旺财的小狗，有一天，
    他带着旺财到球场散步，陌生人对旺财靠近的时候，
    旺财疯狂“汪汪”的叫，主人靠近时，
    旺财高兴的摇摇尾巴。

案例分析：
1、人类
属性）姓名、狗
方法）散步、靠近

2、狗类
属性）名称
方法）叫、摇尾巴
'''

# 人类
class Person:
    def __init__(self,name):
        self.name = name
        self.dog = None
    # 散步
    def jog(self):
        print(self.name,"正在带着",self.dog.name,"散步。。。。")

    # 靠近
    def close(self,obj):
        # 物体开始反应
        obj.reaction(self)

# 狗类
class Dog:
    def __init__(self,name):
        self.name = name

    # 叫
    def bark(self):
        print("汪汪汪.....")

    # 摇尾巴
    def wag(self):
        print("摇摇尾巴.....")

    # 被物体靠近的时候，反应动作
    def reaction(self,person):
        if person.dog  == self:
            self.wag()
        else:
            self.bark()


# 场景
'''
两个人，一个是主人，一个是陌生人
一条狗
'''

xiaoming = Person("小明")
lihua = Person("李华")

wangcai = Dog("旺财")

# 指定主人
xiaoming.dog = wangcai

# 靠近
xiaoming.close(wangcai)
lihua.close(wangcai)
