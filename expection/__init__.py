#!/usr/bin/env python 
# coding:utf-8
# @Time :11/21/18 08:23


"""
    📋 --->>> 控制台输出（ter）
    🤔 --->>> 解析（thi）
    📢 --->>> 说明（exp）
    🌰 --->>> 例子（exa)
    ------>>> 分割线(sep)

    materials:
        # http://docs.python-requests.org/zh_CN/latest/user/advanced.html
        1. requests doc高级用法(官网文档)

"""

# 1. 当仅存在 __str__ 方法时

# class PersonException(Exception):
#
#     def __str__(self):
#         return "str method"
#
#
# p_exp = PersonException()
# print(p_exp)
# # 📋：str method
# # 🤔：直接打印 __str__ 中的内容
#
# print(PersonException)
# # 📋：<class '__main__.PersonException'>
# # 打印对象 PersonException
#
# raise PersonException
# # 📋：
# #   Traceback (most recent call last):
# #   File "/Users/zhangfei/myself/learn_python/repr_str/__init__.py", line 50, in <module>
# #     raise PersonException
# # __main__.PersonException: str method
# # 🤔：抛出异常，并打印类对象中定义的__str__方法


# 2. 当仅存在 __repr__ 方法时

class PersonException(Exception):
    pass

p_exp = PersonException()
print(p_exp)
# 📋：
# 🤔：直接打印时由

# print(PersonException)
# # 📋：<class '__main__.PersonException'>
# # 打印对象 PersonException

# raise PersonException
# raise p_exp
# 📋：
#   Traceback (most recent call last):
#   File "/Users/zhangfei/myself/learn_python/repr_str/__init__.py", line 50, in <module>
#     raise PersonException
# __main__.PersonException: str method
# 🤔：抛出异常，并打印类对象中定义的__str__方法



