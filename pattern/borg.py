#!/usr/bin/env python 
# coding:utf-8
# @Time :11/29/18 17:05

"""
    📋 --->>> 控制台输出（ter）
    🤔 --->>> 解析（thi）
    📢 --->>> 说明（exp）
    🌰 --->>> 例子（exa)
    ------>>> 分割线(sep)

    materials:
        # python borg模块使用教程
        1. https://github.com/faif/python-patterns/blob/master/creational/borg.py

        # Python设计模式(二) ——Borg模式
        2. https://xionchen.github.io/2017/03/01/python-patterns_02/



"""


# class Brog(object):
#     __share_status = {}
#
#     def __init__(self, x):
#         self.__dict__ = self.__share_status
#         self.x = x
#
#     def show(self):
#         return self.x

class Brog(object):
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        self = object.__new__(cls)
        self.__dict__ = cls.__shared_state
        return self

    def __init__(self, x):
        self.x = x

    def show(self):
        return self.x



if __name__ == '__main__':
    b1 = Brog('b1')
    b2 = Brog('b2')

    print(b1.show())
    print(b2.show())

    print(id(b1))
    print(id(b2))

# 📋：
# b2
# b2
# 4550899136
# 4550960800
#
# 🤔：
#   单态模式，实际b1和b2仍然是两个对象，可以通过id看出来，但他们之间实现的状态的共享
#
#