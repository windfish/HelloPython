#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello, world')

# 字符串
print('---------------字符串----------------')

# 转义字符 \
print('I\'m ok.')

# 若需要转义的字符串过多，可使用不转义字符串 r''
print('\\\\t\\\\')
print(r'\\\\t\\\\')

# 若字符串有很多换行，可使用 '''...''' 表示多行内容
print('''第一行
第二行
第三行''')

# 布尔值，可以直接使用 True、False 表示布尔值，也可以通过布尔运算计算
print('---------------布尔值----------------')
print(True)
print(False)
print(3 > 1)

# 布尔值可以用 and、or、not 运算，经常用在条件判断中
age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')


# 空值，python 的空值用None 表示

print('---------------变量----------------')
# 变量，python 中等号 = 是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，并且可以是不同类型
a = 123  # a 是整数
print(a)
a = 'abc' # a 是字符串
print(a)

# 常量，在python 中使用全部大写的变量名称

print('---------------除法----------------')
# python 中有两种除法，一种是 / ，这种除法的结果是浮点数
print(10 / 3)
print(9 / 3)

# 还有一种是地板除 //  ，整数的地板除永远是整数，即使除不尽，因为// 只取结果的整数部分。可以使用 % 进行求余运算
print(9 // 3)
print(10 // 3)
print(10 % 3)

print('---------------字符编码----------------')
# 计算机只能处理数字，需将文本转换为数字才能处理。8bit 为一个字节，一个字节能表示的最大整数是255
# ASCII 编码是一个字节，包含大小写英文字母、数字和一些符号
# 要处理中文，至少需要两个字节，GB2312 编码把中文加了进去
# 最终，出现了Unicode 编码，把所有语言都统一到了这套编码里。一般情况下使用两个字节表示一个字符，非常偏僻的字符会用到四个字节
# 由于Unicode 编码是两个字节，ASCII 编码是一个字节，那么就会造成存储和传输的浪费
# UTF-8 编码，是可变长编码，它会把一个Unicode 字符编码为 1-6 个字节。英文一个字节，汉字通常三个字节
# ASCII 编码实际上被看成是UTF-8 编码的一部分，所以一些只支持ASCII 编码的历史软件在UTF-8 下可以正常工作
print('包含中文的字符串')

# ord() 函数获取字符的整数表示，chr() 函数把编码转换为对应的字符
print(ord('A'))
print(chr(65))

# 如果知道字符的整数编码，还可以直接写十六进制编码
print('\u4e2d\u6587')

# python 保存字符串或者传输时，都会将字符串变为以字节为单位的bytes
# bytes 类型的数据用带 b 前缀的单引号或双引号表示
x = b'abc'
print('abc')
print(x)
# 'abc' 是字符串，b'abc' 的每一个字符都只占用一个字节
# 字符串通过encode() 编码为指定的bytes，纯英文的字符串可以用ASCII 编码，含义中文的用UTF-8 编码
print('abc'.encode('ascii'))
print('中文'.encode('UTF-8'))
# bytes 中无法显示为ASCII 字符的字节，会用\x## 来显示

# 使用decode() 方法将bytes 转换为字符串
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 若bytes 中有部分无效的字节，则可以传入 errors='ignore' 来忽略错误的字节
print(b'\xe4\xb8\xad\xe6\x96'.decode('utf-8', errors='ignore'))

# 计算字符串有多少个字符，使用len()
print(len('abc'))
print(len('中文'))

# bytes 类型时，len()计算的是字节数；字符串时，计算的是字符数
print(len(b'abc'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))


print('---------------格式化字符串----------------')
# 使用 % 格式化字符串，%s 替换字符串，%d 替换整数，%f 浮点数，%x 十六进制整数，%? 占位符，跟参数一一对应
print('Hello, %s' % 'world')

print('格式化指定是否补0：%2d-%02d' % (3, 1))
print('格式化指定小数位数：%.2f' % 3.1415926)

print('format 方式格式化，参数一({0})，参数二({1:.1f}) '.format('abc', 18.245))
