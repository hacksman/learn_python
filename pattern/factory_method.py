#!/usr/bin/env python 
# coding:utf-8
# @Time :11/29/18 17:54


"""
    📋 --->>> 控制台输出（ter）
    🤔 --->>> 解析（thi）
    📢 --->>> 说明（exp）
    🌰 --->>> 例子（exa)
    ------>>> 分割线(sep)

    materials:
        # python factory_method模块使用示例
        1. https://github.com/faif/python-patterns/blob/master/creational/factory_method.py

        # Python 设计模式: 工厂模式(factory pattern)
        2. https://mozillazg.com/2016/08/python-factory-pattern.html

"""


class EmojiTrans:

    def __init__(self):
        self.char_center = {
            "cat": "🐱",
            "dog": "🐶"
        }

    def trans(self, char):
        return self.char_center[char]


class ChineseTrans:

    def __init__(self):
        self.char_center = {
            "cat": "猫",
            "dog": "狗",
        }

    def trans(self, char):
        return self.char_center[char]


def init_class(language="emoji"):
    class_center = {
        "emoji": EmojiTrans,
        "Chinese": ChineseTrans
    }
    return class_center[language]()


if __name__ == '__main__':
    for per_char in ["cat", "dog"]:
        trans_class = init_class("emoji")
        print(trans_class.trans(per_char))


