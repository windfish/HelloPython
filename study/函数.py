#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数名其实是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给函数起了个别名
alias_abs = abs
print(alias_abs(-1))

# 定义函数，使用def 语句，依次写出函数名、括号、括号中的参数和冒号，缩进块中写函数体，返回值用return 语句返回
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-3))

# 空函数：使用pass 语句
def nop():
    pass

# 数据类型检查可以用内置函数 isinstance() 实现
#print(my_abs('a'))

# 函数可以返回多个值，
# import 语句导入math 包，并允许使用math 包里的sin、cos 等函数
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
print(move(100, 100, 60))
# 多个返回值只是假象，其实返回的是一个tuple，只不过多个变量可以同时接收一个tuple，按位置赋值

# 一元二次方程 ax^2+bx+c=0 的两个解，求根公式 x = (-b ± √(b^2-4ac)) / 2a
def quadratic(a, b, c):
    temp = b * b - 4 * a * c
    x1 = (-b + temp) / (2 * a)
    x2 = (-b - temp) / (2 * a)
    return x1, x2

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))

print('---------------------函数的参数------------------------')

#def power(x):
#    return x * x

def power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s

print(power(2))
print(power(2, 3))

# x 和n 都是位置参数，传入的两个值根据位置顺序依次赋值给x 和n
# n=2 就是把参数n 的默认值设置为2，以便旧的调用能够正确
# 默认参数需要注意：
# 一、必选参数在前，默认参数在后。
# 二、变化大的参数放前面，变化小的放后面，变化小的可以作为默认参数
# 三、默认参数必须指向不变对象

def enroll(name, gender, age=6, city='Beijing'):
    print('name', name)
    print('gender', gender)
    print('age', age)
    print('city', city)

enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
# 可以不按顺序传入参数，需要将参数名写上
enroll('Adam', 'M', city='Tianjin')

# 注意，默认参数的一个大坑
def add_end_error(L=[]):
    L.append('END')
    return L

print(add_end_error([1, 2, 3]))
# 使用默认参数调用时，结果就会出错
print(add_end_error())
print(add_end_error())
# 原因是：默认参数L 指向了对象[]，每次调用函数时，改变了L 的内容，那么默认参数的内容也就变了

# 可以使用None 这个不变对象来实现上面的例子
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end([1, 2, 3]))
print(add_end())
print(add_end())

print('---------------------可变参数------------------------')
# 可变参数，就是传入的参数个数是可变的
# 一组数字 a, b, c ... 计算 a^2 + b^2 + c^2 + ...

# 非可变参数的函数
def calc_sum1(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 调用时，需要先组装list 或 tuple
print(calc_sum1([1, 3, 5]))

# 可变参数的函数，函数内部，参数接收到的是一个tuple，函数代码完全不变
def calc_sum2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc_sum2(1, 3, 5))
# 也可以传入0个参数
print(calc_sum2())

# 如果已经有了一个list 或tuple 那么在list 或tuple 前加一个* 号，可以把元素变为可变参数传入函数中
nums = [1, 2, 3, 5]
print(calc_sum2(*nums))

print('---------------------关键字参数------------------------')



