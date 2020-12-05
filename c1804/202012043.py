'''
题目：设计一个统计班级人数的系统

要求：面向对象程序设计思想

功能需求：
统计班级人数

分析：
一、学生类
1）属性：学号、姓名
2）方法：加入班级、退出班级
二、班级类
1）属性：学生列表，班级名称
2）方法：添加学生、删除学生、统计人数
'''
# 学生类
class Student:
    def __init__(self,no,name):
        self.no = no
        self.name = name
    def add_class(self,cls):
        cls.add_stu()
