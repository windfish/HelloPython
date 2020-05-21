#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process
import os


def run_child_process(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 创建子进程时，传入一个执行函数和函数的参数，创建一个Porcess 实例，用start() 启动
    p = Process(target=run_child_process, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
