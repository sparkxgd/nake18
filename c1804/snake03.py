'''
2020年10月27日 16:02:21
班级：18计科专升本
贪吃蛇
1、蛇能移动
2、键盘控制方向
3、边界判定

'''
# 导入pygame模块
import pygame
import sys

# 窗体的大小
win_w = 500
win_h = 500
# 初始化pygame
pygame.init()
# 打开一个游戏界面
window = pygame.display.set_mode([win_w,win_h])
# 蛇的颜色
snake_head_color = (255,106,106)

# 蛇的位置
x = 0
y = 0

# 蛇的运动方向
direc = "right"

# 背景色
background_color =(119,136,153)

# 循环显示界面
while True:
    # 画面延迟刷新
    pygame.time.wait(50)
    # 监听事件
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            # 退出游戏
            sys.exit()
        elif even.type == pygame.KEYDOWN:
            if even.key == pygame.K_UP:
                direc = "up"
            elif even.key == pygame.K_DOWN:
                direc = "down"
            elif even.key == pygame.K_LEFT:
                direc = "left"
            elif even.key == pygame.K_RIGHT:
                direc = "right"

    # 根据方向进行移动
    if direc == "up":
        y -= 5
    elif direc == "down":
        y += 5
    elif direc == "left":
        x -= 5
    elif direc == "right":
        x += 5

    # 边界的判定
    if x<0 or x>win_w or y<0 or y> win_h:
        x = 0
        y = 0

    # 填充一个背景色
    window.fill(background_color)
    # 画蛇
    pygame.draw.rect(window,snake_head_color,(x,y,50,50))
    # 更新界面
    pygame.display.update()
