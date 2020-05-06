#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块的文档注释
' a test module'

# 作者
__author__ = 'xuliang'

# 导入sys 模块
import sys


def test():
    # sys.argv 用list 存储量命令行的所有参数，至少有一个参数，第一个参数永远是该.py 文件的名称
    args = sys.argv
    print(args)
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 当在命令行运行hello 模块文件时，Python 解释器把一个特殊变量__name__ 置为__main__，而导入模块时，if 判断无效
# 这种方式可以通过命令行运行一些额外的代码，最常见的就是运行测试
if __name__ == '__main__':
    test()


