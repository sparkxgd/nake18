'''
2020年11月4日07:31:03
肖光鼎
贪吃蛇游戏
改编（采用面向对象编程实现）
设计：
1、蛇身类
1）属性：坐标（x，y），颜色，方向
2）方法：添加蛇身
2、蛇身类
1）属性：蛇身，运动速度，大小
2）方法：添加到蛇身上，画蛇，移动，吃食物
3、食物类
1）属性：坐标（x，y），颜色，
2）方法：画食物，被吃
4、界面控制类
'''
import random
import sys

import pygame


# 蛇身类
class SnakeBody:
    def __init__(self, x=0, y=0, color=(255, 255, 0), direction="right"):
        self.x = x
        self.y = y
        self.color = color
        self.direction = direction

    # 添加到蛇身上
    def add_to_snake(self, snake):
        snake.add(self)


# 蛇类
class Snake:
    def __init__(self, v=20, game=None):
        head = SnakeBody()
        self.body_list = [head]
        self.v = v
        self.size = game.size
        self.direction = head.direction

    # 添加到蛇身上
    def add(self, body):
        self.body_list.append(body)

    # 画蛇
    def draw(self, window):
        for s in self.body_list:
            color = s.color
            snx = s.x
            sny = s.y
            pygame.draw.rect(window, color, (snx, sny, self.size, self.size))

    # 移动
    def run(self, direction):
        if direction != None:
            self.direction = direction

        # 采用坐标交互算法进行移动
        t_x_0 = self.body_list[0].x
        t_y_0 = self.body_list[0].y
        for i in range(1, len(self.body_list)):
            t_x = self.body_list[i].x
            t_y = self.body_list[i].y
            self.body_list[i].x = t_x_0
            self.body_list[i].y = t_y_0

            t_x_0 = t_x
            t_y_0 = t_y

        # 移动
        if self.direction == "up":
            self.body_list[0].y -= self.size
        elif self.direction == "down":
            self.body_list[0].y += self.size
        elif self.direction == "right":
            self.body_list[0].x += self.size
        elif self.direction == "left":
            self.body_list[0].x -= self.size

    # 吃食物
    def eat(self, food):
        snake_wei = self.body_list[len(self.body_list) - 1]
        wei_x = snake_wei.x
        wei_y = snake_wei.y
        wei_derect = snake_wei.direction
        wei_size = self.size
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
        #  生成新的蛇身
        s_body = SnakeBody(x=x, y=y, color=food.color)
        # 加入到蛇身上
        self.add(s_body)


# 食物类
class Food:
    def __init__(self, game):
        self.x = random.randrange(0, game.width - game.size)
        self.y = random.randrange(0, game.width - game.size)
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        self.color = (r, g, b)
        self.size = game.size

    # 食物被吃
    def eated(self, snake):
        # 判断是否可以被蛇吃
        if self.x - snake.size < snake.body_list[0].x and snake.body_list[
            0].x < self.x + snake.size and self.y - snake.size < snake.body_list[0].y and snake.body_list[
            0].y < self.y + snake.size:
            # 吃到蛇的肚子里
            snake.eat(self)
            # 生成新的食物坐标及颜色
            self.x = random.randrange(0, game.width - game.size)
            self.y = random.randrange(0, game.width - game.size)
            r = random.randrange(0, 256)
            g = random.randrange(0, 256)
            b = random.randrange(0, 256)
            self.color = (r, g, b)

    # 画食物
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))


# 游戏类
class SnakeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("我的贪吃蛇游戏")
        self.width = 600
        self.heigth = 600
        self.window = pygame.display.set_mode((self.width, self.heigth))
        self.size = 30  # 20*20个格格
        self.grid = self.width / self.size
        # 背景色
        self.b_color = (0, 134, 139)

    # 事件监听
    def eventListener(self):
        # 添加键盘事件的监听
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                sys.exit()
            elif even.type == pygame.KEYDOWN:
                if even.key == pygame.K_UP:
                    direction = "up"
                    return direction
                elif even.key == pygame.K_DOWN:
                    direction = "down"
                    return direction
                elif even.key == pygame.K_RIGHT:
                    direction = "right"
                    return direction
                elif even.key == pygame.K_LEFT:
                    direction = "left"
                    return direction

    # 启动游戏
    def start(self):
        snake = Snake(game=self)
        food = Food(self)
        while True:
            pygame.time.wait(200)
            # 事件监听
            direction = self.eventListener()
            self.window.fill(self.b_color)
            # 开始移动
            snake.run(direction)
            # 画蛇
            snake.draw(self.window)
            # 画食物
            food.draw(self.window)
            # 食物是否被吃
            food.eated(snake)
            # 更新
            pygame.display.update()


if __name__ == "__main__":
    game = SnakeGame()
    game.start()
