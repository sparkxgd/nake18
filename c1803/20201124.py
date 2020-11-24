'''
2020年11月24日10:29:11
主人与狗
分析：
一、人类
1）属性：姓名、狗
2）方法：散步、靠近
二、狗类
1）属性：名称
2）方法：叫、、摇尾巴、被靠近

'''

# 人类
class Person:
    def __init__(self,name):
        self.name = name
        self.dog = None
    # 散步
    def walk(self):
        if self.dog:
            print(self.name,"带着",self.dog.name,"在操场上散步。。。。")
        else:
            print(self.name,"在操场上散步。。。。")
    # 靠近
    def kaojin(self,obj):
        # 物体开始反应
        obj.action(self)

# 狗类
class Dog:
    def __init__(self,name):
        self.name = name

    # 叫
    def jiao(self):
        print(self.name,"疯狂汪汪汪汪的叫。。。。")

    # 摇尾巴
    def yaowei(self):
        print(self.name,"高兴的摇摇尾巴。。。")

    # 被靠近（被物体靠近的是反应）
    def action(self,obj):
        print(obj.name,"在靠近",self.name)
        if obj.dog == self:  # 是主人
            self.yaowei()
        else:               # 陌生人
            self.jiao()



# 场景实现,2人和一条狗

xiaoming = Person("小明")
xiaohu = Person("小华")

wangcai = Dog("旺财")

xiaoming.dog = wangcai

xiaoming.walk()
xiaohu.walk()

xiaohu.kaojin(wangcai)

