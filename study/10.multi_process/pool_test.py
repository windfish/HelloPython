#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 默认进程数是CPU 的核数
    p = Pool()
    for i in range(10):
        p.apply_async(long_time_task, args=('task-'+str(i), ))
    print('Waiting for all subprocesses done.')
    # 调用close() 之后就不能继续添加新的Process 了
    p.close()
    # join() 会等待所以子进程执行完毕
    p.join()
    print('All subprocesses done.')

