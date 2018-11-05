#!/usr/bin/env python 
# coding:utf-8
# @Time :10/30/18 16:01


"""
    📋 --->>> 控制台
    🤔 --->>> 解析
    📢 --->>> 说明
    🌰 --->>> 例子

    materials:
        # Python中__repr__和__str__区别
        1. https://blog.csdn.net/luckytanggu/article/details/53649156
"""

class Foo():

    def __init__(self):
        self.id = None

    def __str__(self):
        return "<Foo>, value={}".format(self.id)


if __name__ == '__main__':
    f = Foo()
    print(Foo())
    print(f)

# 📋：
# <Foo> id: 111
# <Foo> id: 111

# 📢：
# python会将__repr__中return的内容输出出来，不管是对象还是实例，都会将__repr__中的内容输出出来
# 如果不适用repr，则会输出f实例的地址信息，非人类友好型输出

# 📋：
#>>> class Foo():
#...     def __init__(self):
#...             self.id = None
#...     def __str__(self):
#...             return "<Foo>, value={}".format(self.id)
#>>> f = Foo()
#>>> f
#<__main__.Foo object at 0x106ec1f60>
#>>> print(f)
#<Foo>, value=None

# 📢：
# __repr__可以实现所有终端输出统一，可以将类或者实例的打印按照自己想要的方式打印出来
# __str__ 实际上是覆盖了__repr__以得到更好的用户显示，如上面的🌰所示，当使用f时，是打印实例的内存地址，而使用print(f)则打印的是__str__中定义的内容，面向的是用户输出


