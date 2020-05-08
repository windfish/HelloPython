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

# 可变参数，允许传入0个或任意个参数，在函数调用时组装为一个tuple

print('---------------------关键字参数------------------------')
# 关键字参数，允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部组装为一个dict，可以扩展函数的功能
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 只传入必选参数
person('Michael', 30)
# 传入任意个数的关键字参数
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 可以先组装出一个dict，再转换为关键字参数传入，在dict 前加**，将dict 的key-value 传入函数的关键字参数中
extra = {'city':'Tianjin', 'job':'Engineer'}
person('Jack', 24, **extra)
# 传入的是extra 的一份拷贝，对kw 的改动不影响extra

print('---------------------命名关键字参数------------------------')
# 如果要限制传入的关键字名称，需要使用命名关键字参数，使用 * 作为分隔符，* 后面的参数被视为命名关键字参数
# 例如，只接受city 和job 作为关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)

person2('Jack', 24, city='Tianjin', job='Engineer')

# 如果函数已经定义了一个可变参数，那么后面的命名关键字参数就不需要* 分隔符了，命名关键字还可以有默认值
def person3(name, age, *args, city='Tianjin', job):
    print(name, age, args, city, job)

person3('Jack', 24, city='Tianjin', job='Engineer')
person3('Jack', 24, job='Engineer')

print('---------------------参数组合------------------------')
# python 函数中，可以组合使用必选参数、默认参数、可变参数、关键字参数和命名关键字参数
# 定义顺序必须是：必选参数、默认参数、可变参数、命名关键字参数、关键字参数


print('---------------------递归函数------------------------')
# 如果一个函数在内部调用自身本身，这个函数就是递归函数
# 阶乘函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(1))
print(fact(5))

# 使用递归函数要注意防止栈溢出
# 函数调用是通过栈stack 来实现的，当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就减少一层栈帧
# 由于栈的大小不是无限的，那么递归次数过多，会导致栈溢出

# 解决递归调用栈溢出的方法是通过尾递归优化，python 解释器并未针对尾递归做优化，因此也会导致栈溢出
# 尾递归是，在函数返回的时候，调用自身，且return 语句不能包含表达式，这样编译器会优化尾递归，使递归只占用一个栈帧
def fact2(n):
    return fact_tail(n, 1)

def fact_tail(num, product):
    if num==1:
        return product
    return fact_tail(num-1, num * product)

print(fact2(5))


# 汉诺塔
def move(n, a, b, c):
    # n 表示A 柱子上盘子的数量
    # print(n)
    if n==1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')


