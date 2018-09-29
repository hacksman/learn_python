
# process_demo pytho多进程模块，通过multiprocessing模块调用

import os

from multiprocessing import Process


def child_process_task(name):
    print("{} 子进程({})执行任务...".format(name, os.getpid()))


if __name__ == '__main__':
    # 父进程在此处执行，创建子进程模块通过Process构建
    print("当前创建父进程({})...".format(os.getpid()))
    print("开始创建子进程...")
    process_demo = Process(target=child_process_task, args=('child-1', ))
    print("子进程创建成功...")
    print("子进程开始执行...")
    process_demo.start()
    print("父进程继续跑，根本不管子进程执行的如何，除非遇到join才等待...")
    process_demo.join()
    print("主进程退出所有任务完成...")