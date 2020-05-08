#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print('-------------------使用__slots__-----------------------')
# 动态语言可以给实例绑定属性和方法，但是不影响其他的实例，若要其他实例也起作用，需要给class 绑定
# 但要限制实例可绑定的属性时，需要用到__slots__ 这个特殊的变量，来限制class 可以添加的属性
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple 定义允许绑定的属性名称


s = Student()
s.name = 'Ted'
#s.score = 99  # score 不能绑定，抛出AttributeError

# __slots__ 仅对当前类起作用，对子类不起作用
class GraduateStudent(Student):
    __slots__ = 'score'

# 若子类也定义了_slots__，那么子类实例允许的属性就是自身的__slots__ 加上父类的__slots__

gs = GraduateStudent()
gs.score = 999
gs.name = 'gs'
# gs.nickname = 'nick'
print(dir(gs))

print('-------------------使用@property-----------------------')
# Python内置的@property 装饰器就是负责把一个方法变成属性调用的
class Student1(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer.')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = score

    # 只读属性
    @property
    def age(self):
        return 20


s1 = Student1()
s1.score = 60
print(s1.score, s1._score)
print(dir(s1))
# s1.score = 999

print('-------------------多重继承-----------------------')
# Python 支持多重继承，在设计类的继承关系时，通常主线都是单一继承的，如果要混入额外的功能，就通过多重继承来实现，这种设计称为Mixln
class Animal(object):
    pass

# 大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 额外的功能
class RunnableMixln(object):
    def run(self):
        print('Running...')

class FlyableMixln(object):
    def fly(self):
        print('Flying...')

# 各种动物
class Dog(Mammal, RunnableMixln):
    pass

class Bat(Mammal, FlyableMixln):
    pass

class Parrot(Bird, FlyableMixln):
    pass

class Ostrich(Bird, RunnableMixln):
    pass

# Mixln 的目的就是给一个类增加多个功能，这样在设计类时，优先考虑通过多重继承来组合多个Mixln 的功能，而不是设计多层次的复杂的继承关系


print('-------------------类中的特殊函数-----------------------')
# __len__() 方法作用于len() 函数
# __str__() 方法作用于print() 函数，返回用户看到的字符串
# __repr__() 方法返回程序开发者看到的字符串
class Student2(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name


print(Student2('Ted'))


# __iter__() 方法返回一个迭代对象，这样一个类就可以作用于for...in 循环，for 循环就会不断调用该迭代对象的__next__() 方法
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            # 未对slice 负数做处理
            start = n.start
            stop = n.stop
            step = n.step
            if start is None:
                start = 0
            if step is None:
                step = 1
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start and x % step == 0:
                    L.append(a)
                a, b = b, a + b
            return L


i = 0
for n in Fib():
    print(n)
    i = i + 1
    if i > 20:
        break

# Fib 实例如果要像list 一样按下标取元素，那么需要实现 __getitem__() 方法
fib = Fib()
print(fib[5], fib[100])

# list 的切片方法，需要特殊处理，因为__getitem__ 方法的参数n 有可能是int，也有可能是slice
print(fib[:5], fib[2:10], fib[2:10:2])


# __getattr__() 方法，可以在没有找到某个属性的情况下，返回默认的信息或者自定义的提示
class Student3(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == 'score':
            return 98
        raise AttributeError('\'Student \' object has no attribute \'%s\'' % item)


s3 = Student3('s3')
print(s3.name, s3.score)

# 还可以利用__getattr__，写一个链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().user.list)


