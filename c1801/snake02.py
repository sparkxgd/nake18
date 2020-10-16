'''
2020年10月16日09:07:26
凯里学院-1801
贪吃蛇游戏
功能实现：
1、键盘控蛇
2、
'''

import pygame
import sys

# 初始化pygame
pygame.init()
window = pygame.display.set_mode((500,500))

x= 0
y= 0
# 蛇的方向
direction = "right"
#  背景色
b_color = (153,50,204)
# 蛇头的颜色
snake_head_color = (0,255,0)
while True:
    # 监听键盘
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            # 退出
            sys.exit()
        elif even.type == pygame.KEYDOWN or even.type==pygame.KEYUP:
            if even.key == pygame.K_UP:
                direction = "up"
            elif even.key == pygame.K_DOWN:
                direction = "down"
            elif even.key == pygame.K_LEFT:
                direction = "left"
            elif even.key == pygame.K_RIGHT:
                direction = "right"

    if direction == "right":
        x += 5
    elif direction == "left":
        x -= 5
    elif direction == "up":
        y -= 5
    elif direction == "down":
        y += 5

    window.fill(b_color)
    # 边缘控制
    if 0<x and x <500:
        pass
    else:
        text = pygame.font.SysFont("宋体", 48)
        text_fm = text.render("eating food", 1, (255, 123, 22))
        window.blit(text_fm, (100, 100))

    pygame.time.wait(100)

    # 画蛇
    pygame.draw.rect(window,snake_head_color,(x,y,50,50))
    pygame.display.update()