#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 一个.py 文件就是一个模块Module，每一个模块都可以被其他地方引用
# 使用模块可以避免函数名和变量名冲突，相同名字的函数和变量可以存在于不同的模块中
# 为了避免模块冲突，Python 按目录来组织模块的方法，称为包Package
# 引入包以后，模块名就变成了 package.module
# 每一个包目录下都会有一个 __init__.py 的文件，标识该目录为一个包。__init__.py 可以是空文件，也可以有python 代码。__init__.py 也是一个模块，模块名就是包名本身

# 测试模块 hello.py

# 作用域
# 正常的函数和变量名是公开的public
# __xxx__ 这样的变量时特殊变量，可以被直接引用，但是有特殊用途，比如__name__、__author__，一般不要用这样的变量名
# 类似_xxx 和__xxx 的函数名和变量名就是非公开的private，不应该被引用，但不是强制性的

# 安装第三方模块
# 使用pip 安装：需要知道第三方库的名称，pip install Pillow
# 安装Anaconda：更新IDE 环境中的python 路径指向Anaconda 自带的，并且Anaconda安装的第三方模块会安装在自己的路径下

# 模块搜索路径
# 当加载一个模块时，python 会在指定的路径下搜索对应的.py 文件，模块路径在sys 模块的path 变量中
import sys
print(sys.path)

# 添加模块搜索目录有两种方法：
# sys.path.append('')
# 设置环境变量 PYTHONPATH

# __pycache__ 文件夹中存放的是编译好的字节码，再次执行时，引入的模块未发生变化，则直接跳过编译这一步




