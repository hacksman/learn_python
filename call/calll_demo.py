#!/usr/bin/env python 
# coding:utf-8
# @Time :11/17/18 10:30

"""
    📋 --->>> 控制台输出（ter）
    🤔 --->>> 解析（thi）
    📢 --->>> 说明（exp）
    🌰 --->>> 例子（exa)
    ------>>> 分割线(sep)

    materials:
        # Python __call__ special method practical example
        1. https://stackoverflow.com/questions/5824881/python-call-special-method-practical-example

        # 理解 Python 装饰器看这一篇就够了
        2. https://foofish.net/python-decorator.html

        # 简述 __init__、__new__、__call__ 方法
        3. https://foofish.net/magic-method.html

"""


# 1. python中对象可调用和不可调用的概念

# def foo(x):
#     return x
#
#
# a = foo(3)
#
# print(callable(a))
# print(callable(foo))
# print(callable(foo(1)))
#
# # 📋：
# #   False
# #   True
# #   False
#
# # 📢：
# #   python中一切皆对象，而对象又分为可调用和不可调用，如上结果所示，其中a是实例对象，不可以再被调用，
# #   因此为False，而foo是函数对象，可以被继续调用，因此为True


# -------------------------------------------- 分割线 --------------------------------------------


# 2. __call__ 方法打破实例不可被调用的魔法
# 🤔：
#   谁说不可被调用我们就一定不可被调用？只要是方便我们的，就拿来玩。call方法就是用来实现实例可以再被调用的黑魔法

# class Foo:
#     pass
#
# a = Foo()
# a()

# 📋：
#   TypeError: 'Foo' object is not callable
# 📢：
#   提示Foo对象是不可被调用对象，其实这里更准确的说法是a实例，是不可以被调用的对象。而Foo是可以的，我们试下__call__
#   方法的神奇之处，黑喂狗~

# 🌰：

class Foo:

    def __call__(self, *args, **kwargs):
        print("I am __call__ magic...")
        return 1

a = Foo()
print(a())

# 📋：
#   I am __call__ magic...
#   1

# 📢：
#   神奇吧？将a的实例化对象再次变成了可调用对象。



# class EnterExitParam(object):
#
#     def __init__(self, p1):
#         self.p1 = p1
#
#     def __call__(self, f):
#         def new_f():
#             print("Entering", f.__name__)
#             print("p1=", self.p1)
#             f()
#             print("Leaving", f.__name__)
#         return new_f
#
#
# @EnterExitParam("foo bar")
# def hello():
#     print("Hello")
#
#
# if __name__ == "__main__":
#     hello()