'''
2020年10月16日11:15:08
18计科专升本
贪吃蛇游戏
1、利用pygame模块创建游戏窗体
2、画一个蛇头
3、蛇自动移动
4、按键控制走动
'''
import pygame
import sys
# pygame模块的初始化
pygame.init()
# 创建一个窗体
window = pygame.display.set_mode([500,500])
pygame.display.set_caption("我的贪吃蛇游戏")
#  游戏的背景颜色
beijing_color = (176,48,96)
# 蛇头颜色
snake_head_color = (0,255,0)
# 蛇的初始位置
x = 0
y = 0
while True:
    #  间隔100毫秒
    pygame.time.wait(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -=5
            elif event.key == pygame.K_DOWN:
                y +=5
            elif event.key == pygame.K_LEFT:
                x -=5
            elif event.key == pygame.K_RIGHT:
                x +=5
    window.fill(beijing_color)
    pygame.draw.rect(window,snake_head_color,(x,y,50,50))
    pygame.display.update()