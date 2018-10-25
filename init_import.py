#!/usr/bin/env python 
# coding:utf-8
# @Time :10/25/18 17:39


"""
    📋 --->>> 控制台输出
    🤔 --->>> 解析
    📢 --->>> 说明
    🌰 --->>> 例子


    materials:
        # What is __init__.py for?
        1. https://stackoverflow.com/questions/448271/what-is-init-py-for
"""

# 📢：
# 可以将包目录下的文件import进来，不用深层次的引用

# 🌰：
# from init import add_deep_2
# print(add_deep_2(3, 2))

# 📢：
# 可以将包下__init__.py文件下__all__里面的包引用进来
# 如果没有写__all__文件，会默认将包下__init__.py所有支持的函数引用进来

# 🌰：
# from init import *
# print(convert_int_str(2))
# print(add_deep_2(2, 3))
