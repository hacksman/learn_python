#!/usr/bin/env python 
# coding:utf-8
# @Time :11/18/18 17:16

"""
    📋 --->>> 控制台输出（ter）
    🤔 --->>> 解析（thi）
    📢 --->>> 说明（exp）
    🌰 --->>> 例子（exa)
    ------>>> 分割线(sep)

    materials:
        # 如何理解Python装饰器？ - python教程的回答 - 知乎 - (孙悟空案例)
        1. https://www.zhihu.com/question/26930016/answer/360300235

        # 廖雪峰课程 python进阶 - python中完善decorator
        2. http://www.imooc.com/code/6067

"""

# 一. 基本理解

# def me():
#     print("me")
#
#
# def primary(func):
#     def wrapper(*args, **kwargs):
#         print("学会了算术运算")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# primary_me = primary(me)
# print(primary_me.__name__)
# print(primary_me())

# 🤔：
#   1. 装饰器相当于给函数，拓展了另外的新功能，使得其更为强大
#   2. 装饰器函数的参数是需要被装饰的函数
#   3. 函数被打包成装饰器函数后，执行函数时，其实是在运行装饰器函数，真正的函数逻辑被包裹在装饰器内部(由第二段可以得出)


# -------------------------------------------- 分割线 --------------------------------------------


# 二. 语法糖

# def primary(func):
#     def wrapper(*args, **kwargs):
#         print("学会了算术运算")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @primary
# def me():
#     print("me")
# me()
#
#
# # 🌰：
# def me():
#     print("me")
# new_me = primary(me)
# new_me()


# 🤔：
#   1. 语法糖可以让装饰器变得更优雅，@primary 等价于 me = primary(me)
#   2. 语义非常贴切，装饰它，核心的那么me，并没有变化，你还是越来那个你，但是你增加了一些功能


# -------------------------------------------- 分割线 --------------------------------------------


# 三. 带参数的装饰器
def super_primary(select="normal"):
    def primary(func):
        def wrapper(*args, **kwargs):
            if select == "normal":
                print("学会了算术运算")
            else:
                print("学会了艺术")
            return func(*args, **kwargs)
        return wrapper
    return primary

# @super_primary()
# def me():
#     print('me')
#
# me()

def me():
    print('me')

# 🌰：
me = super_primary()(me)
me()


# 🤔：
#   1. 带参数的装饰器，就相当于在装饰器的外层做了一层封装，返回的是上一层的装饰器函数
#   2. 写带参数的装饰器函数时，可以先将内层的装饰器写好，再外面封装一层即可
#   3. 写带参数的装饰器函数时可以指定默认的参数。但是调用定义的时候一定记得有用调用的方式启用
#      即 使用@super_primary()的方式，而不可以用@super_primary的方式


# -------------------------------------------- 分割线 --------------------------------------------


import time, functools

def super_primary():
    def primary(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return primary


#
#
# def performance(unit):
#     def perf_decorator(f):
#         @functools.wraps(f)
#         def wrapper(*args, **kw):
#             t1 = time.time()
#             r = f(*args, **kw)
#             t2 = time.time()
#             t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
#             print('call %s() in %f %s' % (f.__name__, t, unit))
#             return r
#
#         return wrapper
#
#     return perf_decorator
#
#
# @performance('ms')
# def factorial(n):
#     return reduce(lambda x, y: x * y, range(1, n + 1))
#
#
# print(factorial.__name__)
