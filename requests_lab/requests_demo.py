#!/usr/bin/env python 
# coding:utf-8
# @Time :11/19/18 08:37

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

import requests

# # 1. auth用法
#
# res = requests.get("http://www.baidu.com", auth={})
# print("before_nothing(response):", res.headers)
# print("before_nothing(request):", res.request.headers)
#
# from requests.auth import AuthBase
# _session = requests.session()
#
# class Auth(AuthBase):
#     def __call__(self, r):
#         print(r)
#         r.headers['xxxx'] = "yyyy"
#         r.headers['User-Agent'] = "baidu"
#         return r
#
# res = _session.post("http://www.baidu.com", auth=Auth())
#
# print("\n")
# print("Auth_add(response):", res.headers)
# print("Auth_add(request):", res.request.headers)
#
#
# # 🤔：
# #   auth中需要传递的是PreparedRequest对象，在请求发起之前，进行请求的前置操作，比如修改其中的请求头等

# -------------------------------------------- 分割线 --------------------------------------------


# 2. requests.adapters 用法

import requests.adapters

_session = requests.session()

ADAPTER_WITH_RETRY = requests.adapters.HTTPAdapter(
    max_retries=requests.adapters.Retry(
        total=10,
        status_forcelist=[404],
    )
)


_session.mount("http://", ADAPTER_WITH_RETRY)

_session.get("http://www.2dianban.com/frkfkofr")

# 🤔：
#   可以指定的url进行特定的处理适配，比如以上实例，对http://请求，出现404状态码的进行最多10次的重试操作
