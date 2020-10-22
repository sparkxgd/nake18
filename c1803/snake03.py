'''
2020年10月20日11:28:13
18计科本3班
贪吃蛇游戏
1、遇到食物，并且吃掉
2、将食物吃到蛇的身上（身体加长）
'''

import pygame
import sys
import random

# 窗体大小
w_with = 500
w_height = 500
# 蛇身
s_size = 50
# 背景色
b_color = (0,134,139)
# 蛇的颜色
snake_color = (255,0,255)
# 食物的颜色
food_color = (0,0,255)
# 蛇的位置
x = 0
y = 0
# 蛇身
food_dict = {"head":1,"x":x,"y":y,"color":snake_color}
# 蛇列表
snake_list = [food_dict]

# 移动方向
direct = "right"
# 移动步伐
stup = 5
# 是否可以移动
is_stop = False

# 画蛇
def draw_snake(window):
    for s in snake_list:
        s_x = s.get("x")
        s_y = s.get("y")
        pygame.draw.rect(window, snake_color, (s_x, s_y, s_size, s_size))

# 随机产生一个位置
def getXY():
    x = random.randrange(0, w_with - s_size)
    y = random.randrange(0, w_height - s_size)
    return x,y

pygame.init()
window = pygame.display.set_mode((w_with,w_height))
pygame.display.set_caption("我的贪吃蛇游戏")

# 初始化食物的位置
f_x,f_y =getXY()

while True:

    pygame.time.wait(100)
    # 添加键盘事件的监听
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()
        elif even.type == pygame.KEYDOWN or even.type == pygame.KEYUP:
            if even.key == pygame.K_UP:
                direct = "up"
            elif even.key == pygame.K_DOWN:
                direct = "down"
            elif even.key == pygame.K_RIGHT:
                direct = "right"
            elif even.key == pygame.K_LEFT:
                direct = "left"
    if not is_stop:
        if direct == "up":
            snake_list[0]["y"] -= stup
        elif direct == "down":
            snake_list[0]["y"] += stup
        elif direct == "right":
            snake_list[0]["x"] += stup
        elif direct == "left":
            snake_list[0]["x"] -= stup

    # 边界的判定
    if snake_list[0]["x"] < 0 or snake_list[0]["x"] > w_with-s_size or snake_list[0]["y"] < 0 or snake_list[0]["y"] > w_height - s_size:
        is_stop = True

    window.fill(b_color)
    # 吃食物
    if f_x - s_size < snake_list[0]["x"] and snake_list[0]["x"] < f_x +s_size and f_y - s_size < snake_list[0]["y"] and snake_list[0]["y"] < f_y + s_size:
        text = pygame.font.SysFont("宋体", 48)
        text_fm = text.render("eating food", 1, (255, 0, 0))
        window.blit(text_fm, (100, 100))
        # 改变食物的位置（x,y）
        f_x, f_y = getXY()
        # 蛇身
        f = {"head": 0, "x": x, "y": y, "color": snake_color}
        snake_list.append(f)

    if is_stop:
        text = pygame.font.SysFont("宋体", 48)
        text_fm = text.render("GAME OVER!!!!", 1, (255, 0, 0))
        window.blit(text_fm, (200, 200))
    draw_snake(window)
    pygame.draw.rect(window, food_color, (f_x, f_y, s_size, s_size))
    pygame.display.update()

