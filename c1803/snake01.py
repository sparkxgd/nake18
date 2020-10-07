'''
2020年9月30日08:27:38
18计科本3班
贪吃蛇游戏

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

# 移动方向
direct = "right"
# 移动步伐
stup = 5
# 是否可以移动
is_stop = False

pygame.init()
window = pygame.display.set_mode((w_with,w_height))
pygame.display.set_caption("我的贪吃蛇游戏")

# 食物的位置
f_x = random.randrange(0,w_with-s_size)
f_y = random.randrange(0,w_height-s_size)
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
            y -= stup
        elif direct == "down":
            y += stup
        elif direct == "right":
            x += stup
        elif direct == "left":
            x -= stup

    # 边界的判定
    if x < 0 or x > w_with-s_size or y < 0 or y > w_height - s_size:
        is_stop = True

    window.fill(b_color)
    if is_stop:
        text = pygame.font.SysFont("宋体", 48)
        text_fm = text.render("GAME OVER!!!!", 1, (255, 0, 0))
        window.blit(text_fm, (200, 200))
    pygame.draw.rect(window,snake_color,(x, y, s_size,s_size))
    pygame.draw.rect(window, food_color, (f_x, f_y, s_size, s_size))
    pygame.display.update()

