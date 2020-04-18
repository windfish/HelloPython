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


print('---------------list----------------')
# list 内置的数据结构，是有序的集合，可以随时添加和删除其中的元素
dota_list = ['820', '430', 'zsmj', 'Mu']
print(dota_list)

# len() 函数可以获得list 元素的个数
print(len(dota_list))

# 可以索引每个位置的元素，索引从0 开始
print(dota_list[0])
print(dota_list[3])

# 也可以从后面取元素，-1 表示最后一个元素
print(dota_list[-1])
print(dota_list[-2])

# list 是可变的有序表，append 可以往list 中追加元素到末尾
dota_list.append('longdd')
print(dota_list)

# 也可以将元素插入到指定位置 insert
dota_list.insert(1, 'zhou')
print(dota_list)

# pop() 删除末尾的元素，pop(i) 删除指定位置的元素
dota_list.pop()
dota_list.pop(1)
print(dota_list)

# 要替换某个元素，直接赋值给对应的位置即可
dota_list[3] = '剑来'
print(dota_list)

# list 里的元素类型也可以不同
L = ['aaa', 123, True]
print(L)

# list 元素也可以是另一个list
L1 = ['python', 'java', ['asp', 'php'], 'js']
print(L1)
print(len(L1))
print(L1[2])


print('---------------tuple----------------')
# tuple 也是有序列表，但其一初始化就不能修改，因此，定义一个tuple 时，其元素就必须被确定下来
dota_tuple = ('ame', 'Maybe', 'emo')
print(dota_tuple)

# 定义只有一个元素的tuple 时，需要加一个逗号，否则会按括号运算符计算，定义的就不是tuple 了
t1 = (1, )
print(t1)
t0 = ()
print(t0)

# “可变的”tuple ，元素是list 时，list 可变，而tuple 指向list 不能变为其他的数据类型
t = ('123', 'abc', ['111', '222'])
print(t)
t[2][0] = 'aaa'
print(t)


print('---------------条件判断----------------')
# if else elif 实现条件判断，根据缩进规则，缩进的语句会跟在 if 或else 后执行
age = 13
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('your age is', age)
    print('kid')

# 条件也可以简写 if x:  只要x 是非零数值、非空字符串、非空list等，就判断为True，否则为False

# input() 读取控制台输入，返回的是str 类型，使用int() 函数转换为数字才能与数字比较
#str = input('birth: ')
#birth = int(str)
#if birth < 2000:
#    print('00前')
#else:
#    print('00后')


print('---------------循环----------------')
# for...in 循环，依次把list或tuple中的每个元素迭代出来
names = ['Micheal', 'Bob', 'Tracy']
for name in names:
    print(name)

# range(n) 会生成一个从0开始，小于n 的整数序列
sum = 0
for x in range(10):
    sum = sum + x
print(sum)

# while 循环，只要条件满足，就不断循环
sum = 0
n = 9
while(n>0):
    sum = sum + n
    n = n - 2
print(sum)

# break 提前退出循环  continue 跳过当前的这次循环，直接开始下一次循环


print('---------------dict 字典----------------')
# dict 全程dictionary，相当于map，使用key-value 存储，key 必须用不可变对象
d = {'Micheal':95, 'Bob':75, 'Tracy':85}
print(d['Bob'])

# key 不存在时会报错，可以通过in 判断是否存在，也可以通过dict 的get() 方法
print('Jack' in d)
print(d.get('Jack'))
print(d.get('Jack', -1))

# pop(key) 删除一个key-value
d.pop('Bob')
print(d)

# set 和dict 类似，是一组key 的集合，但不存储value，并且在set 中，没有重复的key
# 创建set 需要一个list 作为输入集合，重复的元素会自动过滤
s = set([1, 2, 3, 2, 4, 1, 1])
print(s)

# add(key) 添加元素到set 中，remove(key) 删除元素
s.add(5)
print(s)
s.remove(5)
print(s)

# set 可以看成数学意义上的无序和无重复元素的集合，可以做并集、交集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  # 交集
print(s1 | s2)  # 并集

