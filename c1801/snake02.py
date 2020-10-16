'''
2020年10月16日09:07:26
凯里学院-1801
贪吃蛇游戏
功能实现：
1、利用pygame打开游戏窗体
2、画出蛇，并移动
3、键盘控蛇
'''

import pygame
import sys

# 初始化pygame
pygame.init()
window = pygame.display.set_mode((500,500))

x= 0
y= 0
#  背景色
b_color = (153,50,204)
# 蛇头的颜色
snake_head_color = (0,255,0)
while True:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            # 退出
            sys.exit()
    pygame.time.wait(100)
    x += 5
    y += 5
    window.fill(b_color)
    # 画蛇
    pygame.draw.rect(window,snake_head_color,(x,y,50,50))
    pygame.display.update()