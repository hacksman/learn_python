#!/usr/bin/env python 
# coding:utf-8
# @Time :10/27/18 10:38

import asyncio
import datetime
import time
import concurrent.futures

"""
    📋 --->>> 控制台输出
    🤔 --->>> 解析
    📢 --->>> 说明
    🌰 --->>> 例子

    materials:
        # Coroutines and Tasks
        1. https://docs.python.org/3.7/library/asyncio-task.html#id2
"""

# Coroutines 的三种main启动方式

# 1. 通过asyncio.run(main())启动
# async def main():
#     print("hello")
#     await asyncio.sleep(1)
#     print("world")
# if __name__ == '__main__':
#     asyncio.run(main())

# 2. 通过await阻塞方式启动
# await会阻塞住，直到任务完成
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print("say {}".format(what))
#
# async def main():
#     print(f"Started at {time.strftime('%X')}")
#     await say_after(1, "hello")
#     await say_after(2, "world")
#     print(f"Finished at {time.strftime('%X')}")
#
# if __name__ == '__main__':
#     asyncio.run(main())

# 3. 通过创建task方式启动，非阻塞
# task方式会以非阻塞方式执行
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print("say {}".format(what))
#
# async def main():
#     print(f"Started at {time.strftime('%X')}")
#     task1 = asyncio.create_task(say_after(1, "hello"))
#     task2 = asyncio.create_task(say_after(2, "world"))
#     await task1
#     await task2
#     print(f"Finished at {time.strftime('%X')}")
#
# if __name__ == '__main__':
#     asyncio.run(main())


# -------------------------------------------- 分割线 --------------------------------------------

# 三种可以Awaitables的对象 Coroutines、Tasks、Futures
# 1. Coroutines
# async def nested():
#     return 42
#
# async def main():
#     nested()
#     print(await nested())
#
# asyncio.run(main())

# 2. Tasks —— 通常被用于做并发任务
# async def nested():
#     return 42
#
# async def main():
#     task = asyncio.create_task(nested())
#     val = await task
#     print(val)
#
# asyncio.run(main())

# 3. Futures —— 顾名思义，被用来指代未来返回的结果，支持异步的执行结果
# def blocking_io():
#     with open('./convertcsv.csv', 'rb') as f:
#         # print(f.read(100))
#         return f.read(100)
#
# def cpu_bound():
#     return sum(i * i for i in range(10**7))
#
# async def main():
#     loop = asyncio.get_running_loop()
#
#     # 1. run in the default loop's executor
#     result = await loop.run_in_executor(None, blocking_io)
#     print("default thread pool", result)
#
#     # 2. run in custom thread pool
#     with concurrent.futures.ThreadPoolExecutor() as pool:
#         result = await loop.run_in_executor(pool, blocking_io)
#         print("custom thread pool", result)
#
#     # 3. run in custom process pool
#     with concurrent.futures.ProcessPoolExecutor() as pool:
#         result = await loop.run_in_executor(pool, cpu_bound)
#         print("custom process pool", result)
#
# if __name__ == '__main__':
#     asyncio.run(main(), debug=True)


# -------------------------------------------- 分割线 --------------------------------------------


# Sleeping，以下是个每2秒休息一次的demo
# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 10.0
#     print(end_time)
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) > end_time:
#             break
#         await asyncio.sleep(2)
#
# asyncio.run(display_date())


# -------------------------------------------- 分割线 --------------------------------------------


# Running Tasks Concurrently
# awaitable asyncio.gather(*aws, loop=None, return_exceptions=False)
# 📢：
#   1. gather类似于多线程和进程中的pool，只要异步程序放入了gather中，就自动被当做调度程序对待
#   2. return_exceptions默认是False，如果开启，则遇到任意任务发生错误，程序将忽略继续执行


# async def factorial(name, number):
#     f = 1
#     if number == 3:
#         try:
#             print(str(number) + 2)
#         except Exception as e:
#             print('some error happened.')
#             return "error"
#     for i in range(2, number + 1):
#         print(f"Task {name}: Compute factorial({i})...")
#         await asyncio.sleep(1)
#         f *= 1
#     print(f"Task {name}: factorail({number} = {f})")
#     return "{} is Ture".format(name)
#
# async def main():
#     result = await asyncio.gather(
#         factorial("A", 2),
#         factorial("B", 3),
#         factorial("C", 4),
#         return_exceptions=True
#     )
#     print(result)
#     print(result.__class__)
#
# asyncio.run(main())


# -------------------------------------------- 分割线 --------------------------------------------

# Timeouts
# coroutine asyncio.wait_for(aw, timeout, *, loop=None)

# async def eternity():
#     await asyncio.sleep(3600)
#     print("yay!")
#
# async def main():
#     try:
#         await asyncio.wait_for(eternity(), timeout=0.1)
#     except asyncio.TimeoutError:
#         print('Time out')
#
# asyncio.run(main())

# -------------------------------------------- 分割线 --------------------------------------------


