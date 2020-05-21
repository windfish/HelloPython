#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('-----------错误处理--------------')
# try...except...finally... 错误数量机制
try:
    print('try...')
    r = 1/0
    print('result: ', r)
except ZeroDivisionError as e:
    print('except: ', e)
finally:
    print('finally')
print('END')

# try...except 捕获异常可以跨越多层调用，因此只有在合适的层次捕获错误就可以了
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error: ', e)
    finally:
        print('finally...')

main()

# 如果错误没有被捕获，就会一直往上抛，最终被Python 解释器捕获，打印出一个错误信息

# Python 内置的logging 模块可以记录错误信息
import logging
logging.basicConfig(level=logging.INFO)

try:
    r = 1/0
except ZeroDivisionError as e:
    logging.exception(e)

# 同样是报错，但程序会继续执行，并正常退出
print('logging end')

# 使用raise 语句可以跑出一个错误的实例，可以自定义错误类型，但尽量使用Python 内置的错误类型
# raise 语句不带参数，会被当前错误原样抛出


# assert 断言可以来调试程序，断言失败，assert 语句会抛出 AssertionError
# assert n!=0, 'n is zero'
# python 解释器可以用 -O 参数来关闭assert，参数是大写字母O，不是数字0


# logging 不会抛出错误，可以将信息输出到文件中
s = '0'
n = int(s)
logging.info('n = %d' % n)
# print(10 / n)

# logging 的好处，允许你指定记录信息的级别，有debug、info、warning、error 等几个级别，通过配置控制输出信息的级别
# 还可以通过简单的配置，一条语句可以同时输出到不同的地方，比如console 和文件


# pdb python 的调试器，可以以单步方式运行，并查看运行状态
# python -m pdb xxx.py  以参数 -m pdb 启动后，就会定位到下一步执行的代码，输入命令1 来查看代码
# 输入命令 n 可以单步执行代码；输入命令 p <变量名> 来查看变量；输入命令 q 结束调试


# 可以使用pdb 设置断点
import pdb

#pdb.set_trace() # 设置断点
#print('pdb trace end')


print('-----------单元测试--------------')
# mydict.py 和 mydict_test.py
# 运行测试，可以通过python mydict_test.py 运行；也可以通过命令行参数直接运行 python -m unittest mydict_test

# setUp() 在测试方法之前执行；tearDown() 在测试方法之后执行


# Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试
# doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。
# test_doc.py

