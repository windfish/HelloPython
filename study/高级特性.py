#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('---------------切片----------------')
# 切片操作，用来取指定索引范围的操作
L = ['Michael', 'Bob', 'Sarah', 'Tracy', 'Jack']

# 取前三个元素
print(L[0:3])

# L[0:3] 表示从索引0开始取，直到索引3为止，但不包括索引3
# 若索引从0开始，则0可以省略
print(L[:3])

print(L[1:3])

# 切片也支持倒着取元素
print(L[-3:-1])

# 由于不包含右边的索引数，所以要取到最后一个元素，需要省略-1
print(L[-2:])
print(L[-1:])

# 切片可以做很多事情
L100 = list(range(100))

# 前10个数
print(L100[:10])

# 后10个数
print(L100[-10:])

# 中间10个数
print(L100[30:40])

# 每5个取一个
print(L100[::5])

# list 做切片后的结果是list，tuple 做切片后的结果还是tuple
print((0, 1, 2, 3, 4, 5)[:3])

# 字符串也可以看做是一种list，每个元素就是一个字符，也可以做切片操作
print('abcdefg'[:4])
print('abcdefg'[::2])

# 去除字符串收尾的空格
def trim(s):
    if len(s) == 0:
        return s
    if s[:1] == ' ':
        return trim(s[1:])
    elif s[-1:] == ' ':
        return trim(s[:-1])
    else:
        return s

print(trim('hello  '))
