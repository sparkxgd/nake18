'''
内容：面向对象程序设计

场景描述:
小明家养两种宠物，一条名叫“旺财”的狗和一只名叫“米克”的猫。
有一天小明一边吃饼干一边给宠物喂食物，当他喂饼干时，旺财摇摇头；
当他喂骨头时，旺财对着小明高兴的摇摇尾巴；
当他给米克喂骨头时，米克闭着眼睛摇摇头；
当他给米克一条鱼的时候，米克高兴的发出呼噜呼噜的声音。


设计：
一、人类
属性：姓名、宠物
方法：给宠物喂食物、吃

二、宠物类
属性：名称、食物
方法：吃、反应、高兴、难过

三、食物类
属性：名称、类型（1：饼干类，2：骨头类，3：鱼类）
方法：

'''

# 人类
class Person:
    def __init__(self,name):
        self.name = name
        self.pet = []
    def eat(self,food):
        print(self.name,"在吃",food.name)
    def add_pet(self,pet):
        self.pet.append(pet)
    def feeding(self,food):
        print(self.name,"给宠物们喂",food.name)
        for pet in self.pet:
            pet.feeding(food,self)
# 宠物类
class Pet:
    def __init__(self,name):
        self.name = name
        self.like_food = []
    # 吃食物
    def eat(self,food):
        print(self.name,"高兴的在吃",food.name)
    # 高兴
    def happy(self,p):
        print(self.name, "高兴的对着",p.name)
    # 伤心
    def sad(self,p):
        print(self.name, "难过的对着",p.name)
    # 被喂食物
    def feeding(self,food,person):
        if self.is_like_food(food):
            self.happy(person)
            self.eat(food)
        else:
            self.sad(person)
    # 设置喜欢的食物
    def set_like_food(self,food):
        self.like_food.append(food)
    # 判断是否是喜欢的食物
    def is_like_food(self,food):
        if food in self.like_food:
            return True
        else:
            return False
# 食物类
class Food:
    def __init__(self,name):
        self.name = name

# 狗类
class Dog(Pet):
    # 高兴
    def happy(self, p):
        print(self.name, "高兴的对着", p.name,"摇摇尾巴！！")
    # 伤心
    def sad(self, p):
        print(self.name, "难过的对着", p.name,"摇摇头！！")
# 猫类
class Cat(Pet):
    # 高兴
    def happy(self, p):
        print(self.name, "高兴的对着", p.name,"发出呼噜呼噜的声音！！")
    # 伤心
    def sad(self, p):
        print(self.name, "难过的对着", p.name,"闭着眼睛摇摇头！！")


if __name__ == '__main__':
    # 场景
    xiaoming = Person("小明")
    wangcai = Dog("旺财")
    mike = Cat("米克")

    bingan = Food("饼干")
    gutou = Food("骨头")
    yu = Food("鱼")

    xiaoming.add_pet(wangcai)
    xiaoming.add_pet(mike)

    wangcai.set_like_food(gutou)
    mike.set_like_food(yu)

    xiaoming.feeding(gutou)
    xiaoming.feeding(yu)
