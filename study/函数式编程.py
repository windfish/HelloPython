#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数式编程的一个特点是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数
print('---------------高阶函数----------------')
# 变量可以指向函数
# abs(-10) 是函数调用，而abs 是函数本身
# 要获得函数调用结果，可以把结果赋值给变量；若一个变量指向函数本身，则可通过该变量调用函数
f = abs
print(f(-10))
# 函数名也是变量

# 编写高阶函数，就是让函数的参数能够接收别的函数
def add(x, y, f):
    return f(x) + f(y)

print(add(5, -6, abs))

print('---------------map()----------------')
# map()函数接收两个参数，一个是函数，一个是Iterable，map 将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator 返回
# 例如：f(x) = x^2，把函数作用在list上
def f(x):
    return x * x


r = map(f, range(1, 10))
print(list(r))

# 将列表元素转为字符串
print(list(map(str, range(1, 10))))

print('---------------reduce()----------------')
# reduce 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce 把结果和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))

# 字符串转数字
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int('123456'))

# 字符串转浮点数
def str2float(s):
    index = s.find('.')
    s1 = reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], s[:index]))
    s2 = reduce(lambda x, y: x * 0.1 + y, map(lambda x: DIGITS[x], s[:index:-1]))
    return s1 + s2 * 0.1

print(str2float('123.456'))

print('---------------filter()----------------')
# filter() 用于过滤序列，接收一个函数和一个序列。把传入的函数依次作用于每个元素，然后根据结果是True、False 决定保留元素还是丢弃
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, range(20))))

# 用filter 求素数，埃氏筛法
# 构造一个奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 定义一个生成器，不断返回素数
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 20:
        print(n)
    else:
        break

# 删选出回数，回数是指从左向右读和从右向左读都是一样的数
def is_palindrome(n):
    tmp = str(n)
    tmp_r = tmp[::-1]
    return tmp == tmp_r

print('1~200:', list(filter(is_palindrome, range(200))))

print('---------------sorted()----------------')
print(sorted([33, 5, -10, 9, -21]))
# sorted() 可以接收一个key 函数来实现自定义的排序
print(sorted([33, 5, -10, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 忽略大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

print('---------------返回函数----------------')
# 高阶函数还可以把函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 4, 6, 9)
print(f)
print(f())

# 函数lazy_sum 中又定义了函数sum，内部函数sum 可以引用外部函数lazy_sum 的参数和局部变量
# 当返回函数sum 时，相关参数和变量就保存在返回的函数中，这种称为“闭包”
# 即使传入相同的函数，每次都返回一个新的函数
f1 = lazy_sum(1, 2, 3)
f2 = lazy_sum(1, 2, 3)
print(f1 == f2)

# 当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    print(fs)
    return fs

c1, c2, c3 = count()
print(c1(), c2(), c3())  # 9  9  9
# 三个函数都返回9，因为他们引用的变量i，在执行时都已经变为了3，所以结果都是9
# 如果一定要引用循环变量，可以再创建一个函数，用函数的参数绑定循环变量当前的值
def _count():
    def f(j):
        return lambda: j * j
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

c_1, c_2, c_3 = _count()
print(c_1(), c_2(), c_3())






