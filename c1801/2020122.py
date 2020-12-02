'''
场景简介：
    主人养一条名叫旺财的小狗，有一天，
    他带着旺财到球场散步，陌生人对旺财靠近的时候，
    旺财疯狂“汪汪”的叫，主人靠近时，
    旺财高兴的摇摇尾巴。

分析：
一、人类
1）属性：姓名、狗
2）方法：散步、靠近
二、狗类
1）属性：名称
2）方法：叫、摇尾巴、被靠近
'''


# 人类
class Person:
    def __init__(self, name):
        self.name = name
        self.dog = None
        self.friends = []

    # 散步
    def jog(self):
        print(self.name, "正在带着", self.dog.name, "散步。。。。")

    # 靠近
    def close(self, obj):
        # 物体开始反应
        obj.reaction(self)

    # 交朋友
    def makeFriend(self,person):
        self.friends.append(person)
        person.friends.append(self)

# 狗类
class Dog:
    def __init__(self, name):
        self.name = name

    # 叫
    def bark(self,obj):
        print(self.name,"向",obj.name,"疯狂汪汪汪的叫.....")

    # 摇尾巴
    def wag(self,obj):
        print(self.name,"向",obj.name,"高兴的摇摇尾巴.....")

    # 被物体靠近的时候，反应动作
    def reaction(self, person):
        if person.dog == self:
            self.wag(person)
        else:
            f = True
            for p in person.friends:
                if p.dog == self:
                    self.wag(person)
                    f = False
            if f:
                self.bark(person)

# 场景
'''
两个人，一个是主人，一个是陌生人
一条狗
'''

xiaoming = Person("小明")
lihua = Person("李华")
xiaolei = Person("小雷")

wangcai = Dog("旺财")

# 指定主人
xiaoming.dog = wangcai

# 指定朋友
xiaoming.makeFriend(xiaolei)
# 靠近
xiaoming.close(wangcai)
lihua.close(wangcai)
xiaolei.close(wangcai)