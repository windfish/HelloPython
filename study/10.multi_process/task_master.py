#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


def get_task_queue():
    return task_queue


def get_result_queue():
    return result_queue


# 从BaseManager 继承的QueueManager
class QueueManager(BaseManager):
    pass


def do_test_master():
    # 把两个Queue 都注册到网络上，callable 参数关联了Queue 对象
    QueueManager.register('get_task_queue', callable=get_task_queue)  # windows 不支持lambda 表达式，需要使用函数代替
    QueueManager.register('get_result_queue', callable=get_result_queue)
    # QueueManager.register('get_task_queue', callable=lambda: task_queue)

    # 绑定端口5000，设置验证码'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动Queue
    manager.start()
    # 获得通过网络访问的Queue 对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    print('Try get results...')
    for i in range(10):
        r = result.get(True)
        print('Result: %s' % r)

    # 关闭
    manager.shutdown()
    print('master exit.')


if __name__ == '__main__':
    do_test_master()

