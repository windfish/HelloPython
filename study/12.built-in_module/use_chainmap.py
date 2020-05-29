#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import ChainMap
import os, argparse

# 构造函数缺省参数
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
print(namespace)
command_line_args = {k: v for k, v in vars(namespace).items() if v}

print(command_line_args)
print(os.environ)

# 组合成ChainMap
combined = ChainMap(command_line_args, os.environ, defaults)
print(combined)  # 由多个dict 组成，查找顺序从前往后

# 打印参数
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])




