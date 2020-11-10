'''
2020年10月22日09:38:54
肖光鼎
贪吃蛇游戏
实现的功能：
1、显示速度，分数
2、按空格键暂停游戏
'''
import random
import sys

import pygame

# 窗体大小
w_with = 500
w_height = 500
# 蛇身
s_size = 20
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
stup = 20
# 是否可以移动
is_stop = False
# 积分
score = 0
pygame.init()
window = pygame.display.set_mode((w_with,w_height))
pygame.display.set_caption("我的贪吃蛇游戏")

# 蛇身
snake = {"head": 1,"color":(255,255,0),"x":x,"y":y,"derect":"right","size":s_size}
# 蛇身列表
snake_list = [snake]

# 食物的位置
def get_x_y():
    f_x = random.randrange(0, w_with - s_size)
    f_y = random.randrange(0, w_height - s_size)
    return f_x, f_y

def get_color():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    return r,g,b

def draw_snake(window):
    # print(snake_list)
    for s in snake_list:
        snake_color = s.get("color")
        snx = s.get("x")
        sny = s.get("y")
        s_size = s.get("size")
        pygame.draw.rect(window, snake_color, (snx, sny, s_size, s_size))

def show_core(info):
    infos = "score:"+ str(info)
    text = pygame.font.SysFont("宋体", 30)
    text_fm = text.render(infos, 1, (255,255,0))
    text_fm2 = text.render("speed:"+str(stup), 1, (255, 255, 0))
    window.blit(text_fm, (250, 50))
    window.blit(text_fm2, (100, 50))

f_x, f_y = get_x_y()

while True:
    pygame.time.wait(200)

    # 添加键盘事件的监听
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()

        elif even.type == pygame.KEYDOWN:
            if even.key == pygame.K_UP:
                direct = "up"
            elif even.key == pygame.K_DOWN:
                direct = "down"
            elif even.key == pygame.K_RIGHT:
                direct = "right"
            elif even.key == pygame.K_LEFT:
                direct = "left"
            elif even.key == pygame.K_SPACE:
                if is_stop:
                    is_stop = False
                else:
                    is_stop = True

    if not is_stop:
        # 更新蛇位置
        # print("========更新蛇位置========")
        # print(snake_list)
        # t_x = 0
        # t_y = 0
        t_x_0 = snake_list[0].get("x")
        t_y_0 = snake_list[0].get("y")
        for i in range(1, len(snake_list)):
            # print("%d :(%s，%s)" %(i,snake_list[i-1].get("x"),snake_list[i-1].get("y")))
            t_x = snake_list[i].get("x")
            t_y = snake_list[i].get("y")
            snake_list[i]["x"] = t_x_0
            snake_list[i]["y"] = t_y_0

            t_x_0 = t_x
            t_y_0 = t_y

        # 移动
        if direct == "up":
            snake_list[0]["y"] -= stup
        elif direct == "down":
            snake_list[0]["y"] += stup
        elif direct == "right":
            snake_list[0]["x"] += stup
        elif direct == "left":
            snake_list[0]["x"] -= stup


    # 边界的判定
    if snake_list[0]["x"] < 0 or snake_list[0]["x"] > w_with-s_size or  snake_list[0]["y"] < 0 or snake_list[0]["y"] > w_height - s_size:
        is_stop = True

    window.fill(b_color)
    # 显示分数
    show_core(score)
    # 判定吃食物
    if f_x - s_size < snake_list[0]["x"] and snake_list[0]["x"] < f_x + s_size and f_y - s_size < snake_list[0]["y"] and snake_list[0]["y"] < f_y + s_size:
        text = pygame.font.SysFont("宋体", 48)
        text_fm = text.render("eating food", 1, (255, 123, 22))
        window.blit(text_fm, (100, 100))
        # 吃掉食物（改变食物位置，然后将食物添加到蛇的身上）
        old_food_color = food_color
        f_x, f_y = get_x_y()
        food_color = get_color()
        snake_wei = snake_list[len(snake_list)-1]
        wei_x = snake_wei["x"]
        wei_y = snake_wei["y"]
        wei_derect = snake_wei["derect"]
        wei_size = snake_wei["size"]
        if wei_derect == "up":
            y = wei_y + wei_size
            x = wei_x
        elif wei_derect == "down":
            y = wei_y - wei_size
            x = wei_x
        elif wei_derect == "right":
            x = wei_x - wei_size
            y = wei_y
        elif wei_derect == "left":
            x = wei_x + wei_size
            y = wei_y

        # 蛇身
        s = {"head": 0, "color": old_food_color,"x":x,"y":y, "derect": wei_derect, "size": wei_size}
        # 蛇身列表
        snake_list.append(s)
        # 加分
        score += 1
    # 化蛇
    draw_snake(window)
    pygame.draw.rect(window, food_color, (f_x, f_y, s_size, s_size))
    if is_stop:
        text = pygame.font.SysFont("宋体", 48)
        text_fm = text.render("Paused !!!!", 1, (255, 0, 0))
        window.blit(text_fm, (150, 200))
    pygame.display.update()
