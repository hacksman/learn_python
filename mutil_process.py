#!/usr/bin/env python 
# coding:utf-8
# @Time :9/29/18 18:00

# ----------分割线----------

# fork()系统调用非常特殊，调用一次，返回两次，操作系统将当前进程（称为父进程）复制一份（称为子进程），分别在父进程和子进程返回

# ----------分割线----------

# 举个 🌰：

import os

print("当前进程 ({})， 即父进程 start...".format(os.getpid()))

pid = os.fork()

# 注意这里 🤔
if pid == 0:
    print("当前是子进程({}), 我的父进程是({})".format(os.getpid(), os.getppid()))
else:
    print("父进程({}) 创造了 子进程（{}）".format(os.getpid(), pid))

