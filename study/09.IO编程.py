#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print('----------------文件读写----------------')
# 读文件 open() 函数，传入文件名和标识符，标识符 r 表示读
# 文件读写时可能产生IOError，可以使用try...finally 来确保正确的该关闭文件
try:
    f = open('d:\\11231.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# with 语句可以自动调用close() 方法
with open('d:\\11231.txt', 'r') as f:
    # print(f.read())
    for line in f.readlines():
        print(line.strip())

# read(size) 每次最多读取size 个字节的内容
# readline() 每次读取一行内容；readlines() 一次读取所有内容并按行返回list

# 像open() 函数返回的有read() 方法的对象，在python 中称为file-like Object
# 除了文件外，还可以是内存的字节流、网络流、自定义流等
# file-like Object 不需要从特定类继承，只需要有read() 方法；StringIO 就是，常用作临时缓冲

# 二进制文件，比如图片、视频等，要用'rb' 模式打开
pic = open('d:\\ovh.jpg', 'rb')
print(pic.read())

# 要读取非UTF-8 编码的文本文件，需要给open() 函数传入encoding 参数
# open('gbk.txt', 'r', encoding='gbk')

# 若文件中有一些非法编码的字符，会遇到UnicodeDecodeError，需要给open() 接收一个errors 参数，表示遇到错误后如何处理
# open('gbk.txt', 'r', encoding='gbk', errors='ignore')


# 写文件，传入标识符'w' 或'wb'；'a' 已追加的方式写入
with open('d:\\11231.txt', 'w') as fw:
    fw.write('Hello, world. write file')

print('---------------StringIO----------------')
# StringIO 在内存中读写str
from io import StringIO

f = StringIO()
f.write('hello')
f.write(' world!')
print(f.getvalue())  # getvalue() 获取写入后的str

# 还可以用str 初始化StringIO，然后像读文件一样读取
f = StringIO('Hello!\nHi\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

print('---------------BytesIO----------------')
# BytesIO 操作二进制数据，实现内存中读写bytes
from io import BytesIO
f = BytesIO()
f.write('二进制'.encode('utf-8'))
print(f.getvalue())

# 也可以用一个bytes 初始化，并像文件一样读取
f = BytesIO(b'\xe4\xba\x8c\xe8\xbf\x9b\xe5\x88\xb6')
print(f.read())

print('-------------操作文件和目录------------------')
# 要操作文件、目录，那么需要使用os 模块
import os

print(os.name)

# 环境变量，可以用get('key') 获取
print(os.environ)
print(os.environ.get('PATH'))

# 操作文件和目录的函数一部分放在os 模块中，一部分放在os.path 模块中
# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 创建新目录，首先把新目录的完整路径表示出来
print(os.path.join('D:\\work\\git\\', 'testdir'))
# 创建目录
os.mkdir('D:\\work\\git\\testdir')
# 删除目录
os.rmdir('D:\\work\\git\\testdir')

# 拼接两个路径时，通过os.path.join() 函数，这样可以正确处理不同操作系统的路径分隔符
# 拆分路径时，要通过os.path.split() 函数，后一部分总是最后级别的目录或文件名
print(os.path.split('D:\\work\\git\\testdir'))

# os.path.splitext() 可以直接得到文件扩展名
print(os.path.splitext('D:\\work\\git\\file.txt'))

# 对文件重命名
# os.rename('test.txt', 'test.py')
# 删除文件
# os.remove('test.py')

# shutil 模块下还有很多实用的函数，可以看做是os 模块的补充


# 列出当前目录下的目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 列出所有的py 文件
print([x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py'])


# ls -l
from datetime import datetime

print('-------------模拟 ls -l-------------')
print('     Size     Last Modified    Name')
print('----------------------------------------')
for f in os.listdir('.'):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))


print('-------------查找当前目录及子目录下文件名包含关键字的文件--------------')
def find_file(path, name):
    if not os.path.exists(path):
        print('%s is not real path.' % path)
        return

    abs_path = os.path.abspath(path)
    # print(abs_path)

    for f in os.listdir(abs_path):
        all_path = os.path.join(abs_path, f)
        # print(all_path, os.path.isfile(all_path), name in f, name, f)

        if os.path.isfile(all_path) and name in f:
            print(all_path)
        elif os.path.isdir(all_path):
            find_file(all_path, name)


find_file('.', 'py')

# os.path.isfile() 判断子目录的文件时，需要传入文件的相对路径或绝对路径，否则函数返回有问题
# 因为isfile() 会默认从当前目录下查找是否有指定的文件，而不会从子目录中查找

print('-------------序列化----------------')
# Python 序列化称为pickling，序列化后可以把序列化的内容存储在磁盘或传输到别的机器上
# 把内容从序列化对象重新读入内存里称为反序列化，unpickling
import pickle

d = dict(name='Bob', age=20, score=88)
# 序列化一个对象
print(pickle.dumps(d))
# 序列化一个对象，并写入一个file-like Object
pickle.dump(d, open('dump.txt', 'wb'))
# 反序列化
print(pickle.load(open('dump.txt', 'rb')))


print('-------------json 序列化-----------')
# 在不同编程语言直接传递对象，就必须把对象序列化为标准格式，比如xml、json
import json

print(json.dumps(d))
json.dump(d, open('json.txt', 'w'))
# json.load() 从file-like Object 中反序列化；json.loads() 从字符串中反序列化
print(json.load(open('json.txt', 'r')))

# 序列化class
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Ted', 22, 96)
# 直接序列化json 报错，因为不知道如何将class 序列化，需指定转换方法
json_str = json.dumps(s, default=lambda obj: obj.__dict__)
print(json_str)
# class 通常有一个__dict__ 属性，存储实例变量，是一个dict 类型

# 反序列化时，先转换出一个dict 对象，再传入object_hooks 函数负责把dict 转换为obj
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

print(json.loads(json_str, object_hook=dict2student))







