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

def createCounter():
    L = [0]
    def counter():
        L[0] = L[0] + 1
        return L[0]
    return counter

counter = createCounter()
print(counter(), counter(), counter(), counter())


print('---------------匿名函数----------------')
# lambda 表示匿名函数，冒汗前面的变量，表示函数参数
f_lambda = lambda x: x * x
print(f_lambda)
print(f_lambda(5))

# 也可以把匿名函数作为函数值返回
def build(x, y):
    return lambda: x * x + y * y


print('---------------装饰器----------------')
# 在代码运行期间动态增加功能的方式，称为装饰器 Decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2020-4-30')

# @log 相当于执行了 now = log(now)，原函数仍然存在，只是同名的now 指向了包装过的函数，即log 返回的wrapper 函数
# wrapper() 函数参数定义是(*args, **kw)，因此可以接受任意参数的调用
now()

# 如果decorator 本身需要传入参数，那么需要一个返回decorator 的高阶函数
def _log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@_log('execute')
def now():
    print('2020-4-30')

# @_log('execute') 相当于执行 now = _log('execute')(now)，返回的最终还是wrapper 函数
now()

print(now.__name__)
# 但返回的函数名 __name__ 是wrapper，需要将原始的函数名复制给wrapper 函数，否则有些依赖函数签名的代码执行就会出错
# Python 内置的 functools.wraps 就是做这个事的
import functools

def __log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@__log
def now():
    print('2020-4-30')

now()
print(now.__name__)

# 打印函数执行时间的decorator
import time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        begin = time.time()
        result = fn(*args, **kw)
        end = time.time()
        duration = end - begin
        print('%s executed in %s ms' % (fn.__name__, duration))
        return result
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

print('fast result:', fast(11, 22))
print('slow result:', slow(11, 22, 33))


def log_last(params='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            # if len(params) == 0:
            #     print('call %s():' % func.__name__)
            # else:
            print('%s %s():' % (params, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log_last()
def test():
    print('no params')

test()

@log_last('execute')
def test():
    print('have a params')

test()

print('---------------偏函数----------------')
# 偏函数，就是把一个函数的某些参数给固定住（设置默认值），返回一个新的函数，调用这个新函数更简单
from functools import partial
int2 = partial(int, base=2)
print(int2('00000100'))
print(int2('10101010', base=10))






