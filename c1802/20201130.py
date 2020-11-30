'''
2020年11月30日08:51:13
一、多线程
1、线程的创建及使用
threading---线程模块
Thread----线程类
线程对象.start()---启动线程
线程对象.join()---监听线程结束

'''

import threading
import time
# 创建地鼠线程类
class Gopher(threading.Thread):
    def __init__(self,name,v):
        super(Gopher,self).__init__()
        self.task = 20
        self.name=name
        self.v = v

    def run(self):
        while self.task>0:
            time.sleep(self.v)
            self.task -=1
            print("%s正在搬砖...(剩余任务：%d)\n" %(self.name,self.task))

# 场景3个地鼠，在搬砖

dsa= Gopher("地鼠A",1)
dsb= Gopher("地鼠B",3)
dsc= Gopher("地鼠C",2)

# 地鼠开始活动
dsa.start()
dsb.start()
dsc.start()

# 监听地鼠活动是否结束
dsa.join()
dsb.join()
dsc.join()


