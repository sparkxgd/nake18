'''
2020年12月1日10:46:14
多线程
一、多线程的创建
1、使用高级模块threading
1）函数调用的方式创建线程

//函数定义
def 函数名：
    函数体

//线程创建
xca=threadind.Thead(启动函数，函数需要传的参数（元组类型）)

//线程的启动
xca.start()

//监听线程结束
xca.join()


//定义类的方式创建线程
class 类名称（threadind.Thread）:
    def __init__(self,name):


'''