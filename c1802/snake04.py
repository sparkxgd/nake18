'''
2020年11月9日09:32:00
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
        print("")

# 食物类
class Food:
    def __init__(self, color=(255, 123, 11), x=0, y=0):
        self.color = color
        self.x = x
        self.y = y





w_with = 500
w_heigth = 500

s_with = 50
s_heigth = 50

pygame.init()
window = pygame.display.set_mode((w_with,w_heigth))

Gold = (255,215,0)
Green1 =(0,255,0)
Magenta =(255,0,255)

# 初始化
x = 0
y = 0
# 蛇头颜色
head_color = (255,0,0)

# 蛇身字典
snake_dict = {"head":1,"color":head_color,"x":x,"y":y,"dirction":"right"}
# 蛇列表
snake_list = [snake_dict]

# 随机产生颜色
def get_color():
    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)
    return r,g,b

# 画蛇
def draw_snake():
    # 蛇头的位置
    x0 = snake_list[0].get("x")
    for i in range(len(snake_list)):
        # 下一个位置
        x1 = snake_list[i+1].get("x")
        # 将上一个位置设置到下一个位置
        snake_list[i + 1]["x"] = x0
        x0 = x1
        # 食物的颜色
        c = s.get("color")
        sx = s.get("x")
        sy = s.get("y")
        # 画一个矩形代表蛇
        pygame.draw.rect(window, c, (sx, sy, s_with, s_heigth))


# 获取位置
def getXY():
    x = random.randrange(0, w_with - s_with)
    y = random.randrange(0, w_heigth - s_heigth)
    return x,y

# 移动步数
stup = 1

# 运动方向
direction = "right"

is_stop = False

# 初始化食物的位置
f_x,f_y =getXY()
# 初始化食物颜色
f_color = get_color()

while True:
    pygame.time.wait(10)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()
        elif ev.type == pygame.KEYDOWN or ev.type == pygame.KEYUP:
            if ev.key == pygame.K_UP:
                direction = "up"
            elif ev.key == pygame.K_DOWN:
                direction = "down"
            elif ev.key == pygame.K_LEFT:
                direction = "left"
            elif ev.key == pygame.K_RIGHT:
                direction = "right"
    window.fill(Gold)

    if not is_stop:
        # 方向是向上运动
        if direction == "up":
            snake_list[0]["y"] -= stup
        elif direction == "down":
            snake_list[0]["y"] += stup
        elif direction == "left":
            snake_list[0]["x"] -= stup
        elif direction == "right":
            snake_list[0]["x"] += stup

    # 判断是否到达边缘
    if snake_list[0]["x"] < 0 or snake_list[0]["y"] > w_with-s_with:
        is_stop = True
    elif snake_list[0]["y"] < 0 or snake_list[0]["y"] > w_heigth-s_heigth:
        is_stop = True

    # 判定食物是否被吃
    if f_y - s_with < snake_list[0]["y"] and snake_list[0]["y"]< f_y+ s_with and f_x - s_with < snake_list[0]["x"] and snake_list[0]["x"] < f_x +s_with:
        text = pygame.font.SysFont("宋体", 48)
        text_fm = text.render("eating", 1, (255, 0, 0))
        window.blit(text_fm, (150, 200))
        # 重新生成食物（重新产生x，y）
        f_x, f_y = getXY()
        f_color = get_color()
        s_wei = snake_list[len(snake_list)-1]
        s_wei_x = s_wei["x"]
        s_wei_y = s_wei["y"]
        s_direction = s_wei["dirction"]
        if s_direction == "up":
            x = s_wei_x
            y = s_wei_y+s_with
        elif s_direction == "down":
            x = s_wei_x
            y = s_wei_y-s_with
        elif s_direction == "right":
            x = s_wei_x+s_with
            y = s_wei_y
        elif s_direction == "left":
            x = s_wei_x-s_with
            y = s_wei_y

        # 添加蛇身
        snake_s = {"head": 0, "color": f_color, "x": x, "y": y, "dirction": s_direction}
        snake_list.append(snake_s)
    # 画食物
    pygame.draw.rect(window, f_color, (f_x, f_y, s_with, s_heigth))
    # 画蛇
    draw_snake()
    pygame.display.update()