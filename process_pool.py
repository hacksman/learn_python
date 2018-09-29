
from multiprocessing import Pool

import os
import time
import random


def long_time_task(task_name):
    print("{} 执行子进程({})...".format(task_name, os.getpid()))
    start_time = time.time()
    time.sleep(random.random() * 10)
    end_time = time.time()
    print("{} 任务执行了 {} s".format(task_name, round(end_time-start_time, 2)))


if __name__ == '__main__':
    print("当前进程({})，即父进程启动...".format(os.getpid()))
    pid_num = 10
    pool = Pool(pid_num)
    # pool = Pool()
    print("当前创建了一个数目为 {} 的进程池".format(pid_num))
    for i in range(15):
        task_name = "task_{}".format(i)
        print("即将将 {} 丢进进程池...".format(task_name))
        pool.apply_async(long_time_task, args=(task_name, ))
        print("{} 任务已丢进程池...".format(task_name))
    print("所有任务已整装待发...")
    pool.close()
    pool.join()
    print("主进程退出，所有任务执行完毕")

    # 总结 😝
    # 进程池创建后，将任务指定给它，它就会在其中自动执行
    # 进程池创建后需要进行手动关闭，并且需要先手动关闭，之后才能执行进程池阻塞等待操作
    # 实验证明，pool就像是一台冰箱，你只要关闭了冰箱门即可，里面的东西自动执行（保持冷冻），那么可以很容易理解，冰箱门自动关闭了，程序就自动在里面运行了
    # 子进程执行完毕后，会自动被杀掉回收
    # pool的默认大小是cpu的核数
