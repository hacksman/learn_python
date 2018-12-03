#!/usr/bin/env python 
# coding:utf-8
# @Time :12/3/18 14:44

"""
    📋 --->>> 控制台输出（ter）
    🤔 --->>> 解析（thi）
    📢 --->>> 说明（exp）
    🌰 --->>> 例子（exa)
    ------>>> 分割线(sep)

    materials:
        # python lazy_evaluation模块使用示例
        1. https://github.com/faif/python-patterns/blob/master/creational/lazy_evaluation.py

        # 离线数据任务中的惰性求值语法设计
        2. http://mvj3.com/2017/02/28/lazy-evaluation-and-its-syntax-design-in-offline-data-job

"""


from __future__ import print_function
import functools


class lazy_property(object):
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property2(fn):
    attr = '_lazy__' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)

    return _lazy_property


class Person(object):
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        relatives = "Many relatives."
        return relatives

    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return "Father and mother"


def main():
    Jhon = Person('Jhon', 'Coder')
    print(u"Name: {0}    Occupation: {1}".format(Jhon.name, Jhon.occupation))
    print(u"Before we access `relatives`:")
    print(Jhon.__dict__)
    print(u"Jhon's relatives: {0}".format(Jhon.relatives))
    print(u"After we've accessed `relatives`:")
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.__dict__)
    print(Jhon.call_count2)
    print(Jhon.__dict__)
    print(Jhon.call_count2)


if __name__ == '__main__':
    main()

# 🤔：
#    主要是两方面的作用：
#               1. 加快程序处理，在导入惰性求值的数据后，是直接存在缓存中的，如果后面需要计算，是直接在缓存里面拿，效率较高
#               2. 一次计算，多次使用，节省了重复计算所消耗的计算机资源
