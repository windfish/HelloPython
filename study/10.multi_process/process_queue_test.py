#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process, Queue
import os, time, random


def offer(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue.' % value)
        q.put(value)
        time.sleep(random.random())


def poll(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给子进程
    q = Queue()
    pw = Process(target=offer, args=(q,))
    pr = Process(target=poll, args=(q,))
    # 启动生产者进程
    pw.start()
    # 启动消费者进程
    pr.start()
    # 等待生产者进程结束
    pw.join()
    # 强行终止消费者进程
    pr.terminate()


