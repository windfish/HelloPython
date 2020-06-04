import socket

# 创建socket，SOCK_DGRAM 指定这个socket 类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')

while True:
    # 接收数据，返回数据和客户端的地址与端口
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    # sendto() UDP 方式发送给客户端
    s.sendto(b'Hello, %s' % data, addr)
