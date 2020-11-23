'''
案例二：士兵突击

场景简介：
    托雷斯是一名美国大兵，
    在一次突击中捡到一把AK47的枪，
    于是他就利用这把枪，
    一边开着枪，
    一边高喊着“冲啊，冲啊”的朝着的敌人方向冲过去。


案例分析：
1、士兵
属性）姓名、枪
方法）开枪、冲锋、喊

2、枪
属性）名称、子弹
方法）被开枪，装弹
'''

# 士兵
class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None

    # 喊叫
    def cry(self):
        print("高喊着，冲啊，冲啊.......")

    # 开火
    def fire(self):
        self.gun.fired(self)

    # 冲锋
    def assault(self):
        self.fire()
        self.cry()

# 枪
class Gun:
    def __init__(self,name):
        self.name = name
        self.bullet = 0

    # 装弹
    def install(self,num):
        self.bullet += num

    # 被开枪
    def fired(self,soldier):
        self.bullet -= 1
        print("%s朝着敌人开一枪....（剩余子弹:%s）" %(soldier.name,self.bullet))


'''
一名美国大兵
一把AK47的枪，1发子弹
'''

tuoleisi = Soldier("托雷斯")
ak47 = Gun("ak47")
ak47.bullet = 10

tuoleisi.gun = ak47

while ak47.bullet>0:
    tuoleisi.assault()