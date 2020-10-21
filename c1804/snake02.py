'''
2020年10月20日 16:22:50
班级
贪吃蛇
1、
'''
# 导入pygame模块
import pygame
import sys

# 初始化pygame
pygame.init()
# 打开一个游戏界面
window = pygame.display.set_mode([500,500])
# 蛇的颜色
snake_head_color = (255,106,106)

# 循环显示界面
while True:
    # 监听事件
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            # 退出游戏
            sys.exit()
    # 画蛇
    pygame.draw.rect(window,snake_head_color,(0,0,50,50))
    # 更新界面
    pygame.display.update()
