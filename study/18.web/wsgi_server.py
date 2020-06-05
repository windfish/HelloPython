'WSGI 服务器'


from wsgiref.simple_server import make_server
from hello_wsgi import application


# 创建一个服务器，IP 地址为空，端口是8000，处理函数为application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP 请求
httpd.serve_forever()
