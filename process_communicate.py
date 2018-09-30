#!/usr/bin/env python 
# coding:utf-8
# @Time :9/30/18 15:30

# ----------分割线----------

# 学习资料：
#   https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000
#   https://www.jianshu.com/p/a4de38b8c68d
#   https://segmentfault.com/a/1190000008122273

# ----------分割线----------

import multiprocessing


def child_task_input(name, pipe):
    pipe.send("我是输入管道，我的名字是{}".format(name))
    print("输入管道已经输入完毕...")


def child_task_output(name, pipe):
    result = pipe.recv()
    print("输出管道 {} 吐出的内容是：{}".format(name, result))


# # ----------分割线----------
#
# # 主进程放入内容，由p1子进程来输出内容
# out_pipe, in_pipe = multiprocessing.Pipe()
#
# in_pipe.send("我是主进程，我放入的内容为😝")
#
# p1 = multiprocessing.Process(target=child_task_output, args=('p1', out_pipe))
#
# p1.start()
# p1.join()
#
# # >>> 输出管道 p1 吐出的内容是：我是主进程，我放入的内容为😝
#
# # 和segmentfault中说的一致，主进程push内容，然后子进程可以提取到其中的内容
#
# # ----------分割线----------

# # ----------分割线----------
#
# # 主进程不开启，由多条子进程实现自产自消
#
# out_pipe, in_pipe = multiprocessing.Pipe()
# p1 = multiprocessing.Process(target=child_task_input, args=('p1', in_pipe))
# p2 = multiprocessing.Process(target=child_task_output, args=('p2', out_pipe))
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()
#
# # >>> 输出管道 p2 吐出的内容是：我是输入管道，我的名字是p1
# # 管道多个连接时，可以不依靠主进程，子进程自己实现管道内的生产和消费
#
# # ----------分割线----------

# # ----------分割线----------
#
# # 主线程和子线程同时发送数据至管道时
# out_pipe, in_pipe = multiprocessing.Pipe()
# p1 = multiprocessing.Process(target=child_task_input, args=('p1', in_pipe))
# p2 = multiprocessing.Process(target=child_task_output, args=('p2', out_pipe))
# p3 = multiprocessing.Process(target=child_task_output, args=('p3', out_pipe))
# import time
#
# p1.start()
# p2.start()
# p3.start()
#
# time.sleep(2)
# in_pipe.send("我是主进程，我发送数据进来啦😝")
# p1.join()
# p2.join()
# p3.join()
#
# # >>> 输入管道已经输入完毕...
# # 输出管道 p2 吐出的内容是：我是输入管道，我的名字是p1
# # 输出管道 p3 吐出的内容是：我是主进程，我发送数据进来啦😝
#
# # 连接的时候是看发送数据的时间，主进程或者子进程得看谁先发出来，谁先发进来，管道对面拿数据时，就拿到谁的数据，其实就还是队列的模式
#
# # ----------分割线----------

# # ----------分割线----------
#
# # 启动双工管道模式，看下他的效果
# out_pipe, in_pipe = multiprocessing.Pipe(duplex=True)
# in_pipe.send("我是主进程，我发送东西进来啦!😁")
# result = out_pipe.recv()
# print("主进程提取出来的东西是: {}".format(result))
#
# # >>> 主进程提取出来的东西是: 我是主进程，我发送东西进来啦!😁
# # 开启双工模式，则可以一个进程中，同时收发信息
#
# # ----------分割线----------


# ----------分割线----------

# 启动双工管道模式，看下他的效果
out_pipe, in_pipe = multiprocessing.Pipe(duplex=True)
in_pipe.send("我是主管道，我输入的内容是：😝")
p1 = multiprocessing.Process(target=child_task_input, args=('p1', in_pipe))
p2 = multiprocessing.Process(target=child_task_output, args=('p2', out_pipe))
p3 = multiprocessing.Process(target=child_task_output, args=('p3', out_pipe))

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

# >>> 输入管道已经输入完毕...
# 输出管道 p2 吐出的内容是：我是主管道，我输入的内容是：😝
# 输出管道 p3 吐出的内容是：我是输入管道，我的名字是p1

# 因为所有的连接全部开启，所有是谁输入进来和输出出去的并没有什么关系，可以随意调用

# # ----------分割线----------





