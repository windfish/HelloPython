#! /usr/bin/enc python3
# -*- coding: utf-8 -*-


print('-------------------类与实例-----------------------')


# 定义类，关键字class，后面是类名，(object)表示类是从哪个类继承下来的
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 通过定义一个特殊方法__init__，在创建实例时将name、score 绑定到实例上。__init__ 第一个参数用于是self，表示创建的实例本身
# 在类中定义函数，第一个参数永远都是self，并且调用时，不用传递该参数
# 每个实例拥有各自不同的数据，这些数据可以通过类的方法来访问，这样就把数据封装起来了


# 创建类的实例
bart = Student('Bart', 59)
print(bart, Student)
print(bart.name, bart.score)
bart.print_score()

print('-------------------访问限制-----------------------')
# Class 内部，如果要让内部属性不被外部访问，可以把属性名称前加两个下划线__
# 如果要获取，则增加get 方法；如果要修改，则增加set 方法
class Student2(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart2 = Student2('Bart', 59)
print(Student2)
#print(bart2.__name, bart2.__score) # 不能访问__name 和 __score

# Python 解释器对外会将__name 变量改为_Student2__name，但不同的解释器，会改为不同的变量名
print(bart2._Student2__name)

print('-------------------继承和多态-----------------------')
class Animal(object):
    def run(self):
        print('Animal is running.')

class Dog(Animal):
    def run(self):
        print('Dog is running.')

class Cat(Animal):
    def run(self):
        print('Cat is running.')

dog = Dog()
dog.run()

cat = Cat()
cat.run()
# 子类的run() 覆盖父类的run()，运行时，总会调用子类的run()
# 继承的另一个好处，多态。例如：dog 既是Dog，也是Animal
# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。
print(isinstance(dog, Dog), isinstance(dog, Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running.')

run_twice(Tortoise())


# 多态的好处：只需要知道它的父类型，而具体的调用，是在运行时该对象的确切类型决定
# 这就是著名的开闭原则：对扩展开放，允许新增Animal 子类；对修改封闭，不需要修改依赖Animal 类型的run_twice() 函数


class Timer(object):
    def run(self):
        print('Timer start.')


run_twice(Timer())
# Python 中并不一定要传入Animal 类型，只需要确保传入的对象有run 方法就行，这就是动态语言的“鸭子类型”

print('-------------------获取对象信息-----------------------')
# type() 函数，判断对象类型
# 可以判断基本类型，变量指向函数或类，也可以判断
print(type(123), type('str'), type(None), type(abs))

# type() 返回对应的Class 类型，判断基本类型可以直接写int、str，对象或函数需要使用types 模块中定义的常量
import types

print(type(run_twice) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


# 对于class 继承关系，使用isinstance() 函数，判断对象是否是该类型本身或者位于该类型的父继承链上
print(isinstance('a', str))

# 还可以判断是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))


# dir() 函数可以获得一个对象的所有属性和方法，返回一个包含字符串的list
print(dir('abc'))
print(dir(dog))
print(dir(bart2))

# 配合getattr()、setattr()、hasattr()，可以操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))  # 有属性 x 吗
print(hasattr(obj, 'y'))  # 有属性 y 吗
setattr(obj, 'y', 111)  # 设置属性 y
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))  # 获取属性 y

# 如果获取不存在的属性，会抛出AttributeError；可传入一个default 参数，若属性不存在，就返回默认值
# print(getattr(obj, 'z'))
print(getattr(obj, 'z', 123))

fn = getattr(obj, 'power')  # 获取对象的方法
print(fn, fn())


print('-------------------实例属性和类属性-----------------------')
# Python 是动态语言，根据类创建的实例可以任意绑定属性
# 给实例绑定属性的方法是通过实例变量，或者self 变量
# 给类绑定属性可以再class中定义属性，就是类属性，所有的实例都可以访问
class Student3(object):
    name = 'Student'


s = Student3()
print(s.name, Student3.name)


# 统计学生人数，每创建一个学生实例，人数加1
class Student4(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student4.count = Student4.count + 1


print(Student4.count)
s1 = Student4('s1')
s2 = Student4('s2')
print(Student4.count)





