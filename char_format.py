#!/usr/bin/env python 
# coding:utf-8
# @Time :11/8/18 15:12


from kitchen.text.display import *


foo_1 = ["下一季度业绩指引不佳 高通股价盘后跌超4%", "2018-11-08 10:27", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890417.html"]
# foo_1 = ["desingnfrijifrj", "2018-11-08 10:27", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890417.html"]
foo_2 = ["中捷资源：公司部分不动产被法院查封", "2018-11-08 10:17", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890416.html"]
# foo_2 = ["frfjifjrifjr", "2018-11-08 10:17", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890416.html"]
foo_3 = ["长油5“回A”催热老三板 退市股“复活”没那么简单", "2018-11-08 09:45", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890391.html"]
foo_4 = ["携程发布第三季度财报 首次披露用户年龄结构29岁以下占50%", "2018-11-08 09:37", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890387.html"]
foo_5 = ["珠海中富获举牌 背后浮现前实控人身影", "2018-11-08 09:27", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890383.html"]
foo_6 = ["250亿天价收购案持续 闻泰科技能否吃下安世？", "2018-11-08 09:26", "http://www.cs.com.cn/ssgs/gsxw/201811/t20181108_5890381.html"]

for i in range(1, 7):
    title = eval('foo_{}'.format(i))[0]
    date = eval('foo_{}'.format(i))[1]
    url = eval('foo_{}'.format(i))[2]

    print "%s" % textual_width_fill(title, 100), '11'