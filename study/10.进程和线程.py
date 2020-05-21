#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 多任务实现有三种方式：多进程模式、多线程模式、多进程+多线程模式
# Python 既支持多进程，又支持多线程
# 线程是最小的执行单元，而进程由至少一个线程组成

print('--------------多进程-----------------')
# Unix/Linux 操作系统提供了一个fork() 系统调用，普通的函数调用，调用一次，返回一次，但是fork() 调用一次，返回两次
# 因为操作系统自动把当前进程（父进程）复制了一份（子进程），然后分别在父进程和子进程内返回
# 子进程永远返回0，而父进程返回子进程的ID，因为一个父进程可以fork 多个子进程，需要记录每个子进程的ID，子进程通过getppid() 就可以获取父进程ID

# Python的os模块封装了常见的系统调用，其中就包括fork，只能在Unix/Linux/Mac 上执行
import os, sys


if sys.platform != 'win32':
    print('Process (%s) start...' % os.getpid())

    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s)' % (os.getpid(), pid))


# multiprocessing 是跨平台的多进程模块，其提供了一个Process 类来代表一个进程对象
# 创建子进程时，传入一个执行函数和函数的参数，创建一个Porcess 实例，用start() 启动
# multiprocess_test.py


# 如果要启动大量子进程，可以用线程池Pool 的方式批量创建子进程
# pool_test.py


# subprocess 模块可以启动一个子进程，并控制其输入和输出
import subprocess


print('$ nslookup www.baidu.com')
r = subprocess.call(['nslookup', 'www.baidu.com'])
print('Exit code:', r)

print('-------------------------------------')
# 子进程需要输入，则通过communicate() 方法输入
print('$ nklookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)


# 进程间通信，multiprocessing 模块提供了Queue、Pipes 等多种方式来交换数据
# process_queue_test.py

print('--------------多线程-----------------')
# Python 标准库提供了两个模块：_thread 和threading，threading 对_thread 进行了封装，我们只使用threading 就可以了
# 启动一个线程就是把一个函数传入并创建Thread 实例，然后调用start() 开始执行
import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 多线程和多进程最大的不同是，多进程中，同一个变量在各个进程中都有一份拷贝，互不影响；而多线程中，变量由所有的线程共享
# 可以通过加锁，来保证同一时间只有一个线程修改共享变量
balance = 0
lock = threading.Lock()


def change(n):
    # global 在函数中声明调用全局变量的值
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(99999):
        # 获取锁
        lock.acquire()
        try:
            change(n)
        finally:
            # 释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

print('--------------ThreadLocal-----------------')
# 多线程环境下，线程使用自己的局部变量比使用全局变量好，因为不需要加锁
# ThreadLocal 是局部变量，但每个线程都只读写自己线程的独立副本，互补干扰，解决了参数在一个线程中各个函数直接传递的问题
local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

print('--------------分布式进程-----------------')
# 在Thread 和Process 中，应当优选Process，因为更稳定，而且Process 可以分布到多个机器，而Thread 最多只能分布到同一台机器的多个CPU上
# multiprocessing 模块不但支持多进程，其中managers 子模块还支持把多进程分布到多台机器上
# task_master.py 服务进程  task_worker.py 工作进程
# Queue 对象存储在task_master.py 进程中，通过网络进行访问
# 通过QueueManager 实现网络访问，而QueueManager 需要给每一个queue 的网络调用接口定义名字，比如，get_task_queue




