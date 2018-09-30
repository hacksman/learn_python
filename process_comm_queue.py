#!/usr/bin/env python 
# coding:utf-8
# @Time :9/30/18 17:59

# ----------分割线----------

# 学习资料：
#   https://www.jianshu.com/p/a4de38b8c68d

# ----------分割线----------

import queue
import time

from multiprocessing import Process, Queue


def child_task_a(q):
    while True:
        val = q.get()
        time.sleep(0.0001)
        print("child_task_a 得到的内容是 {}".format(val))


def child_task_b(q):
    while True:
        val = q.get()
        print("child_task_b 得到的内容是 {}".format(val))


# # ----------分割线----------
#
# q = queue.Queue()
# for i in range(100):
#     q.put(i)
#
# p1 = Process(target=child_task_a, args=(q, ))
# p2 = Process(target=child_task_b, args=(q, ))
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()
#
# # 这里的queue，相当于一个独立的模块，里面的任务不共享，一个子线程自己去独立处理里面的所有任务
#
# # ----------分割线----------

# ----------分割线----------

q = Queue()
for i in range(10):
    q.put(i)

p1 = Process(target=child_task_a, args=(q, ))
p2 = Process(target=child_task_b, args=(q, ))

p1.start()
p2.start()

time.sleep(2)
p1.terminate()
p2.terminate()

# 这里的是multiprocessing提供的，用于多进程并发时使用，里面的数据在子进程之间共享的，一个子线程进行处理，另一个就不会处理

# queue.Queue 是进程内非阻塞队列
# mutilprocess.Queue 是跨进程通信队列
# 多进程执行时，前者各自私有，后者各个子进程共有

# ----------分割线----------

