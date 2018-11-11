#!/usr/bin/env python 
# coding:utf-8
# @Time :11/8/18 15:12

"""
    📋 --->>> 控制台输出
    🤔 --->>> 解析
    📢 --->>> 说明
    🌰 --->>> 例子

    materials:
        # 1. How to control padding of Unicode string containing east Asia characters
        https://stackoverflow.com/questions/4622357/how-to-control-padding-of-unicode-string-containing-east-asia-characters

"""

# #from kitchen.text.display import *

# full width versions (SPACE is non-contiguous with ! through ~)
SPACE = '\N{IDEOGRAPHIC SPACE}'
EXCLA = '\N{FULLWIDTH EXCLAMATION MARK}'
TILDE = '\N{FULLWIDTH TILDE}'

# strings of ASCII and full-width characters (same order)
west = ''.join(chr(i) for i in range(ord(' '),ord('~')))
east = SPACE + ''.join(chr(i) for i in range(ord(EXCLA),ord(TILDE)))

# build the translation table
full = str.maketrans(west, east)

# data = data.translate(full).rstrip().split('\n')


foo_1 = ["下一季度业绩指引不佳 高通股价盘后跌超4%", "2018-11-08 10:27", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890417.html"]
# foo_1 = ["desingnfrijifrj", "2018-11-08 10:27", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890417.html"]
foo_2 = ["中捷资源：公司部分不动产被法院查封", "2018-11-08 10:17", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890416.html"]
# foo_2 = ["frfjifjrifjr", "2018-11-08 10:17", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890416.html"]
# foo_3 = ["长油5回A”催热老三板 退市股“复活”没那么简单", "2018-11-08 09:45", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890391.html"]
foo_3 = ["长油5回A催热老三板 退市股复活没那么简单", "2018-11-08 09:45", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890391.html"]
foo_4 = ["携程发布第三季度财报 首次披露用户年龄结构29岁以下占50%", "2018-11-08 09:37", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890387.html"]
foo_5 = ["珠海中富获举牌 背后浮现前实控人身影", "2018-11-08 09:27", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890383.html"]
foo_6 = ["250亿天价收购案持续 闻泰科技能否吃下安世？", "2018-11-08 09:26", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890381.html"]
foo_7 = ["亿天价收购案持续闻泰科技能否吃下安世", "2018-11-08 09:26", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890381.html"]
foo_8 = ["珠海中富获举牌背后浮现前实控人身界", "2018-11-08 09:26", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890381.html"]

for i in range(1, 9):
    title = eval('foo_{}'.format(i))[0]
    date = eval('foo_{}'.format(i))[1]
    url = eval('foo_{}'.format(i))[2]



    # print(title, date, url)

    # title_raw = title.translate(full).rstrip().split('\n')
    title_raw = title.translate(full).rstrip()
    # date_raw = date.translate(full).rstrip().split('\n')
    date_raw = date.translate(full).rstrip()
    # url_raw = url.translate(full).rstrip().split('\n')
    url_raw = url.translate(full).rstrip()

    # 全角中文字符替换
    print("{:　>40} | {:18} | {:50}".format(title_raw, date_raw, url_raw))
    # print("{:>40} | {:18} | {:50}".format(title, date, url))
    # print("%18s|%20s|%50s" % (title, date, url))
    # print("{:　>40}|{:>20}|{:>40}".format(title, date, url))

    # print(len("珠海中富获举牌背后浮现前实控人身影界"))
    # print("%100s" % title.translate(full).rstrip().split('\n'))

    # for index, value in enumerate(title):
    #     print("{:4} {20:20.20}".format(index + 1, value))
    #
    # print('{:^80}    {:>15}  {:^20}'.format(title, date, url))
    #
    # print "%s" % textual_width_fill(title, 100), '11'


# # coding: utf8
#
# # full width versions (SPACE is non-contiguous with ! through ~)
# SPACE = '\N{IDEOGRAPHIC SPACE}'
# EXCLA = '\N{FULLWIDTH EXCLAMATION MARK}'
# TILDE = '\N{FULLWIDTH TILDE}'
#
# # strings of ASCII and full-width characters (same order)
# west = ''.join(chr(i) for i in range(ord(' '),ord('~')))
# east = SPACE + ''.join(chr(i) for i in range(ord(EXCLA),ord(TILDE)))
#
# # build the translation table
# full = str.maketrans(west, east)
#
# data = '''\
# 蝴蝶(A song)
# 心之城(Another song)
# 支持你的爱人(Yet another song)
# 根生的种子
# 鸽子歌(Cucurrucucu palo whatever)
# 林地之间
# 蓝光
# 在你眼里
# 肖邦离别曲
# 西行（魔戒王者再临主题曲）(Into something)
# 深陷爱河
# 钟爱大地
# 时光流逝
# 卡农
# 舒伯特小夜曲(SERENADE)
# 甜蜜的摇篮曲(Sweet Lullaby)
# '''
#
# # Replace the ASCII characters with full width, and create a song list.
# data = data.translate(full).rstrip().split('\n')
#
# # print(full)
# # print(data)
# # translate each printable line.
# print(' ----------Songs-----------'.translate(full))
# for i,song in enumerate(data):
#     # print(i, song)
#     line = '|{:4}: {:20.20}|'.format(i+1,song)
#     print(line.translate(full))
# print(' --------------------------'.translate(full))