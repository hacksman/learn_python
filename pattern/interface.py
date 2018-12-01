#!/usr/bin/env python 
# coding:utf-8
# @Time :11/30/18 14:36

"""
    📋 --->>> 控制台输出（ter）
    🤔 --->>> 解析（thi）
    📢 --->>> 说明（exp）
    🌰 --->>> 例子（exa)
    ------>>> 分割线(sep)

    materials:
        # 如何在Python里应用SOLID原则
        1. http://aju.space/2016/06/17/use-S-O-L-I-D-in-python.html

        # python--接口类与抽象类
        2. https://www.cnblogs.com/zzy-9318/p/8324127.html

"""

# 📢：
# 1. 单继承：所定义的类只继承了一个父类
# 2. 多继承：所定义的类继承了两个或两个以上的父类
# 3. 接口的例子：
#       抽象接口不应该依赖于具体实现，而具体实现应该依赖于抽象接口。三针插头可以被台灯用，也可以被冰箱用，
#       所以抽象接口（插头）并不依赖于背后的具体实现（台灯/冰箱）。而冰箱因为功率较大，一定要有能接地线的
#       三针插头，所以具体实现依赖于抽象接口。
#

# 1.接口类
# 🤔：
#   接口类应该只负责定义类的功能，但具体的实现需要在下面的每一个具体的继承类中实现

# class SpeakAction:
#
#     def speak(self):
#         raise NotImplementedError
#
# class Person(SpeakAction):
#
#     pass
#
# if __name__ == '__main__':
#     p = Person()
#     print(p)

# import abc
# class Bird(object):
#     __metaclass__ = abc.ABCMeta
#
#     @abc.abstractmethod
#     def fly(self):
#         pass
#         return "1"
#
# # @Bird.register
# # class Robin:
# #     pass
#
#
# class A(object):
#     def fly(self):
#         pass
#         return '1'
#
# Bird.register(A)


# r = Robin()

# print(issubclass(Robin, Bird))
# print(isinstance(r, Robin))
#

from collections.abc import Mapping

@Mapping.register
class ListBasedSet:
    pass

    # def __getitem__(self, item):
    #     pass

    # def __iter__(self):
    #     pass

    def __len__(self):
        return 1

print(issubclass(ListBasedSet, Mapping))

# print(len(ListBasedSet()))

class A(set):
    pass

print(A)