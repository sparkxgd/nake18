'''
2020年11月24日11:11:11
士兵突击
场景简介：
    托雷斯是一名美国大兵，
    在一次突击中捡到一把AK47的枪，
    于是他就利用这把枪，一边开着枪，
    一边高喊着“冲啊，冲啊”的操作的敌人方向冲过去。
分析：
一、士兵类
1）属性：姓名、国籍、枪
2）方法：捡枪、喊、冲锋、射击
二、枪类
1）属性：名称、子弹个数
2）方法：被开枪

'''

# 士兵类
class Shibing:
    def __init__(self,name,country):
        self.name = name
        self.country = country
        self.gun = None
    # 喊
    def han(self):
        print(self.name,"朝着敌人方向高喊着：冲啊，冲啊。。。。")

    # 捡枪
    def jian(self,gun):
        self.gun = gun

    # 射击
    def fire(self):
        print(self.name,"扛个一把",self.gun.name,"朝着敌人方向开了一枪。。。。")
        self.gun.shoted()

    # 冲锋
    def chongfen(self):
        self.han()
        self.fire()

# 枪类
class Gun:
    def __init__(self,name):
        self.name = name
        self.dan = 10

    # 被开
    def fried(self):
        self.dan -= 1
        print("======剩余子弹：%d========" % self.dan)


# 一个士兵、一把枪

tuoleis = Shibing("托雷斯","美国")
ak47 = Gun("ak47")

# 托雷斯捡到一把枪
tuoleis.jian(ak47)

while ak47.dan>0:
    # 托雷斯开始冲锋
    tuoleis.chongfen()
