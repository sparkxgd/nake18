'''
2020年10月6日17:33:20
18计科本2班
贪吃蛇
'''

import pygame
import sys
import random

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

f_x = random.randrange(0,w_with-s_with)
f_y = random.randrange(0, w_heigth - s_heigth)
# 移动步数
stup = 1

# 运动方向
direction = "right"

is_stop = False

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
            y -= stup
        elif direction == "down":
            y += stup
        elif direction == "left":
            x -= stup
        elif direction == "right":
            x += stup
    # 画一个矩形代表蛇
    pygame.draw.rect(window,Green1,(x,y,s_with,s_heigth))

    pygame.draw.rect(window, Magenta, (f_x, f_y, s_with, s_heigth))
    # 判断是否到达边缘
    if x < 0 or x > w_with-s_with:
        is_stop = True
    elif y < 0 or y > w_heigth-s_heigth:
        is_stop = True

    # 判定食物是否被吃
    if y == f_y:
        if direction == "right":
            if x+s_with == f_x:
                # 遇到食物
                s_with +=s_with

    pygame.display.update()