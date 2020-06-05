# HTTP 协议是在网络上传输HTML 的协议，用于浏览器和服务器的通信

# HTTP 协议是一种文本协议，每个HTTP 请求和响应都遵循相同的格式，一个HTTP 包含Header 和Body 两部分，其中Body 是可选的
# HTTP GET 请求的格式
# GET /path HTTP/1.1
# Header1: Value1
# Header2: Value2
# Header3: Value3
# 每个Header 一行，换行符是 \r\n

# HTTP POST 请求的格式
# POST /path HTTP/1.1
# Header1: Value1
# Header2: Value2
# Header3: Value3
#
# body data goes here...
# 当遇到连续两个 \r\n 时，Header 部分结束，后面的数据全部是Body

# HTTP 响应的格式
# 200 OK
# Header1: Value1
# Header2: Value2
# Header3: Value3
#
# body data goes here...
# HTTP 响应如果包含body，也是通过连续两个\r\n 来分隔的
# Body 的数据类型由 Content-Type 头来确定，如果是网页，Body 就是文本；如果是图片，Body 就是图片的二进制数据
# 当存在Content-Encoding 时，Body 数据是被压缩的，最常见的压缩方式是gzip


# WSGI：Web Server Gateway Interface 用来接收HTTP 请求、解析HTTP 请求、发送HTTP 响应
# WSGI 接口定义，需要实现一个函数，就可以响应HTTP 请求
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello Web!</h1>']
# 接收两个参数：
# environ：一个包含所有HTTP 请求信息的dict 对象
# start_response：一个发送HTTP 响应的函数，接收两个参数，HTTP 响应码和一组list 表示HTTP Header，每一个Header 都用包含两个str 的tuple 表示
# 调用start_response 就发送了HTTP 响应的Header，注意只能发送一次，也就是只能调用一次start_response 函数

# WSGI 接口需要由WSGI 服务器来调用，Python 内置了一个，模块叫wsgiref


# Web 框架 Flask
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Flask Home Page</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 从request 对象读取表单内容
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password</h3>'


if __name__ == '__main__':
    app.run()
# Flask 自带的server 端口为5000


# 常用的Web 框架：
# Django 全能型Web 框架
# web.py 小巧的Web 框架
# Bottle 和Flask 类似的Web 框架
# Tornado Facebook 开源的异步Web 框架


