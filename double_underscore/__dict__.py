#!/usr/bin/env python 
# coding:utf-8
# @Time :10/30/18 18:12

"""
    📋 --->>> 控制台
    🤔 --->>> 解析
    📢 --->>> 说明
    🌰 --->>> 例子

    materials:
        # python 类 __dict__ 在赋值时的使用
        1. https://blog.csdn.net/AlanGuoo/article/details/78006942
"""


class Foo():

    def __init__(self):
        self.a = "a"
        self.b = "b"


if __name__ == '__main__':
    f = Foo()
    print(f.__dict__)
    # 将整个__dict__更新
    f.__dict__ = {"a": 10, "b": 11, "c": 100}
    print(f.__dict__)
    print(f.a)
    print(f.b)
    # 更新完后，f中就有了c属性，即使原始类中没有这个元素也可以打印，不过不推荐这么做，可以看到编译器已经有警示的提示了
    print(f.c)
    # 更新其中的一部分属性，并增加新的属性
    f.__dict__.update({"a": 11, "d": "foo"})
    print(f.__dict__)

# 📋：
# {'a': 'a', 'b': 'b'}
# {'a': 10, 'b': 11, 'c': 100}
# 10
# 11
# 100
# {'a': 11, 'b': 11, 'c': 100, 'd': 'foo'}

