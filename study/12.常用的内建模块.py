#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print('>>> datetime  -----------------')
from datetime import  datetime

now = datetime.now()
print(now, type(now))

# 指定日期和时间
dt = datetime(2020, 5, 22, 16, 00)
print(dt)

print('---------datetime 转换为 timestamp----------')
# 1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0，当前时间就是相对于epoch time的秒数，称为timestamp
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00 北京时间
# 可见timestamp 与时区无关
print(dt.timestamp())  # 将时间转为timestamp，浮点数，小数位表示毫秒数

print('---------timestamp 转换为 datetime----------')
print(datetime.fromtimestamp(1590134402.0))  # 转换为本地时间
print(datetime.utcfromtimestamp(1590134402.0))  # 转换为UTC 时间

print('---------str 转换为datetime----------')
print(datetime.strptime('2020-5-22 16:16:44', '%Y-%m-%d %H:%M:%S'))

print('---------datetime 转换为str----------')
print(now.strftime('%a, %Y-%m-%d %H:%M:%S'))

print('---------datetime 加减----------')
from datetime import timedelta

print(now)
print(now + timedelta(hours=5))
print(now + timedelta(minutes=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=1))

print('---------时区转换----------')
# datetime 类型有一个时区属性tzinfo，默认是None
from datetime import timezone

tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区
# 强制设置为UTC+8:00，如果系统时区不是UTC+8:00，不能强制设置
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

# utcnow() 获得当前的UTC 时间，再转换为任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# 转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# 转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# 北京时间转换为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


print('>>> collections 集合模块 -----------------')
print('---------namedtuple----------')
# namedtuple 用来创建自定义的tuple 对象，并规定tuple 元素的个数，并可以用属性而不是索引来引用tuple 的某个元素
from collections import namedtuple

# 表示点的坐标
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y, p)
print(isinstance(p, tuple))

# 表示圆
Circle = namedtuple('Circle', ['x', 'y', 'z'])

print('---------deque----------')
# deque 为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

print('---------defaultdict----------')
# dict 如果引用的key 不存在，会抛出KeyError，使用defaultdict 会返回一个默认值
from collections import defaultdict

# 返回的默认值是调用函数返回的，函数在创建defaultdict 对象时传入
dd = defaultdict(lambda: 'N/A')
print(dd['key'])

print('---------OrderedDict----------')
# dict 的key 是无序的，迭代时，无法确定key 的顺序，要保持key 的顺序，可以用OrderedDict
from collections import OrderedDict

# OrderedDict 的key 会按照插入的顺序排列
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od.keys())


# OrderedDict 实现一个FIFO 的dict，容量超出限制时删除最早的key
class LastUpdateOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]  # 参考 od.__delitem__(y) <==> del od[y]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


luod = LastUpdateOrderedDict(2)
luod['x'] = 1
luod['x'] = 1
luod['y'] = 1
luod['z'] = 1
print(luod)

print('---------ChainMap----------')
# ChainMap 可以把一组dict 串起来，组成一个逻辑上的dict，其本身也是dict，但查找的时候，会按照顺序在内部的dict 依次查找
# python3 use_chainmap.py  # 输出默认的参数
# python3 use_chainmap.py -u ted  # user参数输出ted
# color=green python3 use_chainmap.py  # color参数输出grenn
# user=admin python3 use_chainmap.py -u ted  # 命令行参数优先级高，user参数输出ted

print('---------Counter----------')
# Counter 是一个简单的计数器
from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)

c.update('update')
print(c)

print('>>> base64 -----------------')
# Base64 是常见的二进制到文本字符串的编码方法，常用于URL、Cookie、网页中传输少量二进制数据
# Base64 会把三字节的二进制数据编码为四字节的文本数据，长度增加33%，可以直接展示
# 如果二进制数据不是3的倍数，最后会剩下一个或两个字节，Base64 会用\x00 在末尾补足，再在编码的末尾加上1或2个=号，表示补了多少个字节，解码时会去掉
import base64

b64e = base64.b64encode(b'binary\x00string')
print(b64e)
print(base64.b64decode(b64e))

# 由于标准的base64 编码后可能出现字符+和/，不能在URL 中作为参数，所以有一种url safe 的base64编码，其实就是把字符+和/替换为-和_
b64e = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b64e)
ub64e = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(ub64e)
print(base64.urlsafe_b64decode(ub64e))


# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉
# 因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了
def safe_base64_decode(s):
    if len(s) % 4 == 0:
        return base64.b64decode(s)
    else:
        if isinstance(s, str):
            s = s + '='
        elif isinstance(s, bytes):
            s = s + b'='
        else:
            raise TypeError('输入的格式有误！')
        return safe_base64_decode(s)


print(safe_base64_decode('YWJjZA=='))
print(safe_base64_decode('YWJjZA'))

print('>>> struct -----------------')
# struct 模块来解决bytes 和其他二进制数据类型的转换
import struct

# struct 的pack 函数把任意数据类型编程bytes
print(struct.pack('>I', 10240099))
# pack 的第一个参数是处理指令，> 表示字节顺序是big-endian，也就是网络序，I 表示4字节无符号整数
# big-endian 大端模式，网络序，指数据的低位保存在内存的高地址中，而数据的高位保存在内存的低地址中
# little-endian 小端模式，主机序，指数据的低位保存在内存的低地址中，而数据的高位保存在内存的高地址中

# unpack 把bytes 变成相应的数据类型
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
# I 4字节无符号整数   H 2字节无符号数

print('---------bmp 文件分析-------------')
bmp = open('12.built-in_module/111.bmp', 'rb')
b = bmp.read(30)  # 前30个字节文件头
print(b)

# bmp 格式采用小端方式存储数据，文件头的结构按顺序如下：
# 两个字节：'BM' 表示windows 位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0
# 一个4字节整数：实际图像的偏移量
# 一个4字节整数：Header 的字节数
# 一个4字节整数：图像宽度
# 一个4字节整数：图像高度
# 一个2字节整数：始终为1
# 一个2字节整数：颜色数
print(struct.unpack('<ccIIIIIIHH', b))

print('>>> hashlib 摘要算法 -----------------')
import hashlib

print('--------------MD5---------------')
md5 = hashlib.md5()
md5.update('use md5 in python hashlib'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分块多次调用update，结果是一样的
md5 = hashlib.md5()
md5.update('use md5 '.encode('utf-8'))
md5.update('in python hashlib'.encode('utf-8'))
print(md5.hexdigest())

print('--------------SHA1---------------')
sha1 = hashlib.sha1()
sha1.update('use sha1 '.encode('utf-8'))
sha1.update('in python hashlib'.encode('utf-8'))
print(sha1.hexdigest())


# 摘要算法经常用于存储用户密码，但是过于简单的口令的md5值很容易被计算出来，所以，通过对原始口令加一个复杂字符串来加强保护，俗称'加盐'
import hashlib, random

db = {}


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + username + self.salt)


def register(username, password):
    user = User(username, password)
    db[username] = user


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def login(username, password):
    if username not in db.keys():
        return "username not exists."
    user = db[username]
    return user.password == get_md5(password + user.username + user.salt)


register('xxx', 'test1234')
print(login('xxx', 'test1234'))
print(login('xxx', 'test123224'))
print(login('sss', 'sdasada'))

print('>>> hmac 算法 -----------------')
# hmac 算法：通过一个标准算法，在计算哈希的过程中，把key 混入计算过程中
import hmac

# hmac 模块，需准备待计算的原始消息message，随机key，哈希算法
message = b'Hello, hmac!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())


# 将带盐的MD5 改为hmac 算法
db_hmac = {}


class UserHmac(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_hmac(password, self.key)


def hmac_register(username, password):
    user = UserHmac(username, password)
    db_hmac[username] = user


def get_hmac(s, key):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), digestmod='MD5').hexdigest()


def hmac_login(username, password):
    if username not in db_hmac.keys():
        return "username not exists."
    user = db_hmac[username]
    return user.password == get_hmac(password, user.key)


hmac_register('xxx', 'test1234')
print(hmac_login('xxx', 'test1234'))
print(hmac_login('xxx', 'test123224'))
print(hmac_login('sss', 'sdasada'))

print('>>> itertools -----------------')
import itertools

print('----------无限迭代器--------------')
# count() 会创建一个无限的迭代器，默认创建一个从0开始的数字序列，有两个参数：start 起始值，step 步长
c = itertools.count(1, 2)
print(c.__next__(), c.__next__())

# cycle() 会把传入的一个序列无限重复下去
cyc = itertools.cycle('abc')
print(cyc.__next__(), cyc.__next__(), cyc.__next__(), cyc.__next__())

# repeat() 负责把一个元素无限重复下去，第二个参数可以限定重复次数
r = itertools.repeat('ab', 2)
print(r.__next__(), r.__next__())

# 通过takewhile() 根据条件判断来截取一个有限的序列
tw = itertools.takewhile(lambda x: x <= 10, c)
print(list(tw))

print('----------迭代器操作函数--------------')
# chain() 把一组迭代对象串联起来，形成更大的迭代器
for i in itertools.chain('ab', 'c'):
    print(i)

# groupby() 把迭代器中相邻的重复元素挑出来放一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

# 挑选规则是通过函数完成的，只要作用于函数的两个元素返回值相等，这两个元素就是一组的，key 为函数的返回值
for key, group in itertools.groupby('AaaBbBcCAaa', lambda x: x.upper()):
    print(key, list(group))


# 计算圆周率
def pi(N):
    ''' 计算pi的值 '''
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和:
    seq = itertools.count(1, 2)
    i = 1
    sum = 0
    for x in seq:
        if i > N:
            break
        if i % 2 == 1:
            sum = sum + 4 / x
        else:
            sum = sum + -4 / x
        i = i + 1

    return sum


print(pi(999999))

print('>>> contextlib -----------------')
# 读写文件这样的资源要特别注意，在使用完毕后要正确关闭它们
# try...finally 来关闭，或者使用with 语句
with open('json.txt', 'r') as f:
    f.read()

# 并不是只有open() 函数返回的fp 对象才能使用with 语句，只要实现了上下文管理，就可以用于with 语句
# 上下文管理是通过__enter__和__exit__ 这两个方法实现
class Query(object):

    def __init__(self, name):
        self.mame = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.mame)


with Query('Bob') as q:
    q.query()


# Python 标准库contextlib 提供了更简单的写法
from contextlib import contextmanager

class QueryContext(object):

    def __init__(self, name):
        self.mame = name

    def query(self):
        print('Query @contextmanager info about %s...' % self.mame)


# @contextmanager 这个装饰器接收一个generator，用yield 语句把with...as var 变量输出出去
@contextmanager
def create_query(name):
    print('Begin')
    q = QueryContext(name)
    yield q
    print('End')


with create_query('Bob') as q:
    q.query()


# 也可以用@contextmanager 实现在某段代码执行前后自动执行特定代码
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)


# 代码执行顺序：
# 1. with 语句执行yield 之前的语句，打印<h1>
# 2. yield 调用会执行with 语句内部的所有语句，打印两句信息
# 3. 最后执行yield 之后的语句，打印</h1>
with tag('h1'):
    print('hello, world')
    print('@contextmanager')


# @closing 如果一个对象没有实现上下文，那么就不能用于with 语句，可以使用@closing 把对象变为上下文对象
from contextlib import closing
from urllib.request import urlopen


with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)


print('>>> urllib 操作URL -----------------')
print('-----------GET 请求--------------')
# request 模块可以抓取url 内容
from urllib import request

req = request.Request('http://www.douban.com/')
# 还可以通过Request 对象，添加HTTP 头
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

print('-----------POST 请求--------------')
from urllib import request, parse

login_date = parse.urlencode([
    ('username', 'test'),
    ('password', 'test1234'),
    ('entity', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_date.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


print('------------handler----------------')
# 如果要通过一个Proxy 去访问网址，需要利用ProxyHandler 来处理
proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
#     pass

print('>>> XML -----------------')
# 操作XML 有两种方法：DOM 和SAX
# DOM 会把整个XML 读入内存，解析为树，因此占用内存大，解析慢，优点是可以整体遍历树的节点
# SAX 是流模式，边读边解析，占用内存小，解析快，缺点是需要自己处理事件

# Python 中使用SAX，需要关心的事件是：
# 读到一个节点 <a href="/">python</a>
# 1. start_element 事件，在读取<a href="/"> 时
# 2. char_data 事件，在读取python 时
# 3. end_element 事件，在读取</a> 时
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

print('>>> HTMLParser -----------------')
# 解析HTML 页面，使用HTMLParser
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('<%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s:' % name)

    def handle_charref(self, name):
        print('&#%s:' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>
''')
# feed() 可以多次调用，不需要一次性把整个HTML 都塞进去


