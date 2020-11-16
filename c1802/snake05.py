'''
2020年11月16日08:36:35
18计科本2班
贪吃蛇（面向对象程序设计）
1、蛇身类
1)属性：颜色、方向、位置（x,y）
2)方法：
2、蛇类
1)属性：蛇身（list），
2)方法：移动、吃食物
3、食物类
1)属性：位置、颜色
2）方法：

'''

import pygame
import sys
import random

# 蛇身类
class Body:
    def __init__(self,color=(255,255,0),direction="right",x=0,y=0):
        self.color = color
        self.direction = direction
        self.x = x
        self.y = y


# 蛇类
class Snake:
    def __init__(self):
        body = Body()
        self.bodys = [body]
    def run(self):
        print("")
    def eat(self,food):
        color = food.color
        b = Body(color=color)
        self.bodys.append(b)

# 食物类
class Food:
    def __init__(self, color=(255, 123, 11), x=0, y=0):
        self.color = color
        self.x = x
        self.y = y
    # 设置位置
    def set_position(self,x=0,y=0):
        self.x = x
        self.y = y
    # 被吃
    def eated(self,snake):
        snake.eat(self)
        x = random.randrange(0, 500)
        y = random.randrange(0, 500)
        self.set_position(x,y)

    # 显示
    def display(self,window):
        x = random.randrange(0, 500)
        y = random.randrange(0, 500)
        self.set_position(x,y)
        # 画食物
        pygame.draw.rect(window, self.color, (self.x, self.y, 50, 50))


# 游戏类
class SnakeGame():
    def __init__(self,width = 500,height = 500,background_color=(134,123,22)):
        self.width = width
        self.height = height
        self.window = None
        self.background_color=background_color
    #  初始化
    def init(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))

    # 游戏开始
    def start(self):
        food = Food()
        while True:
            pygame.time.wait(10)
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit()
            self.window.fill(self.background_color)
            # 出现食物
            food.display(self.window)
            pygame.display.update()

if __name__ == "__main__":
    game = SnakeGame()
    game.init()
    game.start()
