#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 第三方模块一般都在PyPI 上注册，找到对应的模块名字，使用pip 安装；或者安装Anaconda 即可
print('>>> Pillow 图像处理标准库  -----------------')
from PIL import Image


# 打开图片
im = Image.open('13/dog.jpg')
# 获取图片尺寸
w, h = im.size
print('Original image size: %s x %s' % (w, h))
# 缩放到50%
im.thumbnail((w//2, h//2))
print('Resize image to: %s x %s' % (w//2, h//2))

# windows 下保存会报错，OSError: cannot write mode P as JPEG
# windows 下要24位色彩，因此需要将PIL 模块的P 模式转为RGB
print(im.mode)
if im.mode == 'P':
    im = im.convert('RGB')
# 保存缩放后的图像
im.save('13/thumbnail.jpg', 'jpeg')

# PIL 模块的图像模式
# 1             1位像素，黑和白，存成8位的像素
# L             8位像素，黑白
# P             8位像素，使用调色板映射到任何其他模式
# RGB           3×8位像素，真彩
# RGBA          4×8位像素，真彩+透明通道
# CMYK          4×8位像素，颜色隔离
# YCbCr         3×8位像素，彩色视频格式
# I             32位整型像素
# F             32位浮点型像素

from PIL import ImageFilter

im2 = Image.open('13/dog.jpg')
if im2.mode == 'P':
    im2 = im2.convert('RGB')
# 模糊效果
im2.filter(ImageFilter.BLUR)
im2.save('13/filter.jpg', 'jpeg')


print('------------绘制字母验证码-----------------')
# ImageDraw 绘图
from PIL import ImageDraw, ImageFont
import random


# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色
def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)

# 随机颜色2
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


# 240 * 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font 对象，若无法定位字体文件的位置，则提供绝对路径即可
font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 36)
# 创建Draw 对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('13/code.jpg', 'jpeg')

print('>>> requests  -----------------')
# 内置的urllib 模块，用于访问网络资源，但用起来比较麻烦，而且缺少很多高级功能
# requests 第三方库，处理URL 资源更方便
import requests

# HTTP header 可以传入dict 作为headers 参数
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
r = requests.get('https://www.douban.com', headers=headers)
print(r.status_code)
print(r.text[:200])

# 带参数的URL，传入dict 作为params 参数
params = {'q': 'python'}
r = requests.get('https://www.douban.com/search', headers=headers, params=params)
# r.url 实际请求的url，r.encoding 编码，r.content 获取返回的bytes 对象
print(r.url, r.encoding)

# 对应特定的响应类型，可以直接获取，例如json
# r = requests.get('http://pk.uuuwin.com/game/acc')
# print(r.text)
# print(r.json())

# 要发送POST 请求，调用post() 方法，传入data 参数作为POST 请求的数据
r = requests.post('https://www.douban.com/search', headers=headers, data=params)
print(r.url, r.text[:200])

# requests 默认使用application/x-www-form-urlencoded 对POST 数据编码
# 若要传入JSON 数据，可以直接传入json 参数
params = {'key': 'value'}
requests.post('http://pk.uuuwin.com/', json=params)  # 内部自动序列化为json

# 上传文件需要更复杂的编码格式，requests 将其简化为files 参数
upload_file = {'file': open('13/code.jpg', 'rb')}
requests.post('http://pk.uuuwin.com/', files=upload_file)

# put()、delete() 等，就可以以PUT、DELETE 方式请求资源

# requests 对获取HTTP 响应的其他信息也非常简单
# 获取响应头
print(r.headers)
print(r.headers['Content-Type'])

# 获取Cookie
print(r.cookies)

# 要在请求中传入Cookie，只需要dict 传入cookies 参数
cs = {'token': '123456', 'status': 'working'}
requests.get('http://pk.uuuwin.com/', cookies=cs)

# 指定超时，传入以秒为单位的timeout 参数
requests.get('http://pk.uuuwin.com/', timeout=2.5)

print('>>> chardet  -----------------')
import chardet

# chardet 用来检测编码格式
print(chardet.detect(b'Hello, world!'))
# 结果中，encoding 表示编码；confidence 表示检测的概率，1.0 表示100%

data = '鹅鹅鹅，曲项向天歌，白毛浮绿水，红掌拨清波'.encode('gbk')
print(chardet.detect(data))

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))

print('>>> psutil  -----------------')
# psutil 可以在python 中获取系统信息，可以跨平台使用，支持linux、unix、osx、windows
import psutil

# 获取CPU 信息
print('CPU 数量 %s，CPU 物理核心数量 %s' % (psutil.cpu_count(), psutil.cpu_count(logical=False)))

# 统计CPU 的用户、系统、空闲时间
print(psutil.cpu_times())

print('-----------top-------------')
# 实现类似top 命令的CPU 使用率，每秒刷新一次，累计10次
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))

print('--------获取内存信息-------------')
print('物理内存', psutil.virtual_memory())
print('交换内存', psutil.swap_memory())

print('--------获取磁盘信息-----------')
print('磁盘分区信息', psutil.disk_partitions())
print('磁盘使用情况', psutil.disk_usage('/'))
print('磁盘IO', psutil.disk_io_counters())

print('--------获取网络信息-----------')
print('网络读写字节/包的个数', psutil.net_io_counters())
print('网络接口信息', psutil.net_if_addrs())
print('网络接口状态', psutil.net_if_stats())
print('当前网络连接信息', psutil.net_connections())

print('--------获取进程信息-----------')
print('所有进程ID', psutil.pids())

print('指定获取PyCharm 进程：')
p = psutil.Process(1320)
print('进程名称', p.name())
print('进程exe 路径', p.exe())
print('进程工作目录', p.cwd())
print('进程启动的命令行', p.cmdline())
print('父进程ID', p.ppid())
print('父进程', p.parent())
print('子进程列表', p.children())
print('进程状态', p.status())
print('进程用户名', p.username())
print('进程创建时间', p.create_time())
# print('进程终端', p.terminal())
print('进程使用的CPU 时间', p.cpu_times())
print('进程使用的内存', p.memory_info())
print('进程打开的文件', p.open_files())
print('进程相关网络连接', p.connections())
print('进程的线程数量', p.num_threads())
print('进程的环境变量', p.environ())
# p.terminate()  # 结束进程


# psutil.test()  # 模拟ps 命令，展示当前的进程信息



