'''
2020年12月4日09:00:19
多线程
1、多线程的创建
1）使用高级模块Threading
2）Thread类
    （1)、启动：start()
    (2)、等待线程结束：join（等待时间）
2、多线程的使用
    1)、函数
    2)、类的继承
'''

import datetime
import time
import threading

# 函数方式

def count(name,num,wait):

    c = num
    while c > 0:
        c -=1
        time.sleep(1)
        print(name,"的计数：",c)

def count2(name,num,wait):

    c = num
    while c > 0:
        c -=1
        time.sleep(1)
        print(name,"的计数：",c)

if __name__ == '__main__':
    num = 5
    start_time = time.clock()
    count("计算器A",num,1)
    count("计算器B", num, 1)
    end_time = time.clock()

    run_time = end_time-start_time
    print("总耗时：%0.7f秒" %(run_time))
    #总耗时：0.0011839秒

# 线程的方式
if __name__ == '__main__':
        num = 5

        # 创建一个线程( 函数)
        xianc_a = threading.Thread(count,("计算器A", num, 1))
        xianc_b = threading.Thread(count2, ("计算器B", num, 1))

        start_time = time.clock()
        xianc_a.start()
        xianc_b.start()

        xianc_a.join()
        xianc_b.join()
        end_time = time.clock()

        run_time = end_time - start_time
        print("总耗时：%0.7f秒" % (run_time))
        #总耗时：0.0010752秒