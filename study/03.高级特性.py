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

print('---------------迭代----------------')
# 迭代是通过 for...in 完成的，可以作用于list 或tuple，也可以应用于可迭代对象
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

# 判断对象是可迭代对象
from collections.abc import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

# enumerate 函数可以把一个list 变成索引-元素对
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)

print('---------------列表生成式----------------')
# 可以用range 生成list
print(list(range(1, 11)))

L1 = []
for x in range(1, 11):
    L1.append(x * x)
print(L1)
# 可以用一行语句替代上面生成的list
print([x * x for x in range(1, 11)])

# for 循环后面还可以加上if 判断
print([x * x for x in range(1, 11) if x % 2 == 0])

# 还可以使用两层循环，生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

# 列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])

# 列表生成式可以使用两个变量来生成list
d1 = {'x': 'a', 'y': 'b', 'z': 'c'}
print([k+'='+v for k, v in d1.items()])

# 把list 中的字符串变为小写
print([s.lower() for s in ['Hello', 'World', 'IBM', 'Apple']])

# 在列表生成式中，for 前面的if...else 是表达式，而for 后面的if 是过滤条件，不能带else
print([x for x in range(1, 11) if x %2 == 0])
print([x if x % 2 == 0 else -x for x in range(1, 11)])

print('---------------生成器----------------')
# 列表生成式可以直接创建一个列表，但是占用内存
# 生成器是按照某种算法，一边循环一边计算的机制
# 生成器generator 创建方法一：将列表生成式的[]改为()即可
g = (x * x for x in range(1, 11))
print(g)

# 通过next() 函数获取generator 下一个值
print(next(g), next(g), next(g))
# 通过for 循环来遍历generator
print([x for x in g])

# 算法比较复杂，可以用函数实现
def fin(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return "done"

fin(6)

# 要将函数变为generator，只需要将结果yield 出来就行了
# 执行顺序为每次执行到yield 就停下，调用next() 函数后再从yield 往下执行
def fin_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return "done"

fg = fin_g(6);
print(fg)
print(next(fg), next(fg), next(fg), next(fg))

# 使用for 循环时，generator 的返回值拿不到，需要捕获StopIteration 错误，返回值包含在StopIteration 的value 中
while True:
    try:
        x = next(fg)
        print('g:', x)
    except StopIteration as e:
        print("Generator return:", e.value)
        break

# 杨辉三角
def triangles():
    result = [1]
    while True:
        yield result
        tmp = []
        n = 0
        while n <= len(result):
            if n == 0:
                tmp.append(result[n])
            elif n == len(result):
                tmp.append(result[-1])
            else:
                tmp.append(result[n - 1] + result[n])
            n = n + 1
        result = tmp


n = 0
R = []
for x in triangles():
    R.append(x)
    n = n + 1
    if n >= 10:
        break
for r in R:
    print(r)

print('---------------迭代器----------------')
# 可以被next() 函数调用并不断返回下一个值的对象，称为迭代器 Iterator
# 可以使用isinstance() 判断一个对象是不是Iterator 对象
from collections.abc import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance('abc', Iterator))

# 生成器都是Iterator 对象，但list、tuple、str 虽然是Iterable，却不是Iterator
# 把list、tuple、str 等Iterable 变为Iterator，可以使用Iter() 函数
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))




