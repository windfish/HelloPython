#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Python 支持多种图形界面的第三方库，TK、wxWidgets、Qt、GTK等，自带的是支持TK 的Tkinter，无需安装任何包
# use_tkinter.py

# Python 内置了turtle 库，基本复制了原始的海龟绘图（Turtle Graphics）的所有功能
# use_turtle.py

from turtle import *

def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)


for x in range(0, 250, 50):
    drawStar(x, 0)

done()
