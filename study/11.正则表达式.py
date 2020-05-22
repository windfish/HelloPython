#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 正则表达式规则：
# \d 匹配一个数字，例如：'00\d'匹配'007'，'\d\d\d'匹配'110'
# \w 匹配一个字母或数字，例如：'\w\w\d'匹配'py3'
# . 可以匹配任意一个字符，例如：'py.'匹配'pyc'、'pyo'、'py!'
# * 匹配任意个字符（包括0个）
# + 表示至少一个字符
# ? 表示0或1个字符
# {n} 表示n个字符，{n,m}表示n-m个字符
# 例如：\d{3}\s+\d{3,8} \d{3}匹配上数字，\s+匹配至少一个空格或tab，\d{3,8}匹配3-8个数字

# 要做到更精确的匹配，可以用[]表示范围
# [0-9a-zA-Z\_] 可以匹配一个数字、字母或下划线
# [0-9a-zA-Z\_]+ 可以匹配至少由一个数字、字母或下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]{0,19} 可以匹配由一个字母或下划线开头，后接最多19个字符
# A|B 可以匹配A 或B
# ^ 表示行的开头，^\d 表示必须以数字开头
# $ 表示行的结束，\d$ 表示必须以数字结束

# python 提供了re 模块，包含所有正则表达式的功能
# 由于python 字符串也使用 \ 做转义字符，因此建议使用 r 前缀，这样不需要考虑转义字符的问题
import re

print('---------匹配----------')
# match() 方法匹配成功，返回一个Match 对象，否则返回None
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

print('---------切分字符串----------')
# 正则表达式切分字符串
print('a b   c'.split(' '))  # 无法识别连续的空格
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b  c  d,  e'))

print('---------分组，提取子串----------')
# 正则表达式还有提取子串的功能，用()表示的就是要提取的分组Group
m = re.match(r'(\d{3})\-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0), m.group(1), m.group(2))

mm = re.match(r'(0[0-9]|1[0-9]|2[0-3])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])', '15:12:39')
print(mm)
print(mm.groups())

print('---------贪婪匹配----------')
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
# 由于\d+ 采用贪婪匹配，直接把后面的0 全都匹配了，结果0* 只能匹配空字符串了
print(re.match(r'(\d+)(0*)$', '1023000').groups())
# \d+? 就可以让\d+ 采用非贪婪匹配
print(re.match(r'(\d+?)(0*)$', '1023000').groups())

# 可以先编译正则表达式，在接下来就可以重复使用
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-7894512').groups())


# 验证email
def is_valid_email(addr):
    s = r'[\w\.]+\@[\w]+\.[\w]+'
    if re.match(s, addr):
        return True
    else:
        return False


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')


# 提取email 名字
def name_of_email(addr):
    m = re.match(r'^\<?([\w\s]*)\>?[\w\s]*\@[\w]+\.[\w]+', addr)
    return m.group(1)


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
