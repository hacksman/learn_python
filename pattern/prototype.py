#!/usr/bin/env python 
# coding:utf-8
# @Time :12/5/18 10:54

"""
    📋 --->>> 控制台输出（ter）
    🤔 --->>> 解析（thi）
    📢 --->>> 说明（exp）
    🌰 --->>> 例子（exa)
    ------>>> 分割线(sep)

    materials:
        # python prototype模块使用示例
        1. https://github.com/faif/python-patterns/blob/master/creational/prototype.py

        # Prototype Design Pattern
        2. https://sourcemaking.com/design_patterns/prototype

"""


class Prototype(object):

    value = 'default'

    def clone(self, **attrs):
        """Clone a prototype and update inner attributes dictionary"""
        # Python in Practice, Mark Summerfield
        obj = self.__class__()
        obj.__dict__.update(attrs)
        print(obj.__dict__)
        return obj

    @classmethod
    def fin(cls):
        print(cls.__dict__)


class PrototypeDispatcher(object):
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """Get all objects"""
        return self._objects

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])


if __name__ == '__main__':
    main()

# 🤔：
#   提取通用的模板部分，尤其当需要提取的通用模板每次初始化时成本很高，那就更应该用此种方式
#   通常这种设计模式是基于需要更进一步提高程序的灵活性
#   通常需要结合其他设计模式一起使用，另外一个优势，他不需要基于类实现，只需要对象即可实现


