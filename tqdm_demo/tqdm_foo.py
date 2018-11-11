#!/usr/bin/env python 
# coding:utf-8
# @Time :11/9/18 08:40


from tqdm import tqdm
import time



# print("demo1:")
# text = ""
# for char in tqdm(["a", "b", "c", "d"]):
#     text = text + char
#
# print("\n"); time.sleep(1)
#
# print("demo2:")
# from tqdm import trange
# for i in trange(10000):
#     pass
#
# print("\n"); time.sleep(3)
#
# print("demo3:")
# pbar = tqdm(["a", "b", "c", "d"])
# for char in pbar:
#     pbar.set_description("Processing %s" % char)

# print("\n"); time.sleep(1)
# print("demo4:")
#
# # 手动更新进度条
# with tqdm(1000) as pbar:
#     for i in range(20):
#         pbar.update(10)


# from tqdm import trange
# from time import sleep
#
# for i in trange(10, desc='1st loop'):
#     for j in trange(5, desc='2nd loop', leave=False):
#         for k in trange(100, desc='3nd loop'):
#             sleep(0.01)


from time import sleep
from tqdm import trange, tqdm
from multiprocessing import Pool, freeze_support, RLock

L = list(range(9))


def progresser(n):
    interval = 0.001 / (n + 2)
    total = 5000
    text = "#{}, est. {:<04.2}s".format(n, interval * total)

    for i in trange(total, desc=text, position=n):
        sleep(interval)

if __name__ == '__main__':
    freeze_support()  # for Windows support
    p = Pool(len(L),
             # again, for Windows support
             initializer=tqdm.set_lock, initargs=(RLock(),))
    p.map(progresser, L)
    print("\n" * (len(L) - 2))



