#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 互联网协最重要的两个协议是TCP 和IP 协议，简称TCP/IP 协议
# 通信的时候必须知道对方的标识，互联网上的唯一标识就是IP 地址
# IP 协议负责把数据从一台计算机通过网络发送到另一台计算机，数据被分割成一小块一小块，通过IP 包发送出去
# 由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器负责决定如何把IP 包转发出去。
# IP 包的特点是按块发送，途径多个路由，但不能保证到达，也不保证顺序到达
# IPv4 是一个32位整数，以字符串表示如192.168.0.1实际上是把32位整数按8位分组后的数字表示，目的是便于阅读
# IPv6 是一个128位整数，是IPv4 的升级版，字符串表示类似2001:0db8:85a3:0042:1000:8a2e:0370:7334


# TCP 协议建立在IP 协议之上，负责两台计算机之间建立可靠连接，保证数据包按顺序到达
# TCP 协议会通过握手建立连接，然后对每个IP 包编号，确保对方按顺序收到，如果包丢了，就自动重发

# 许多常用的更高级的协议都是建立在TCP 协议基础上的，例如浏览器的HTTP 协议、发送邮件的SMTP 协议等
# 一个TCP 报文除了包含要传输的数据外，还包含源IP 地址、目标IP 地址、源端口、目标端口
# 一台计算机上跑着多个网络程序，一个TCP 报文发来之后，需要通过端口来确定交给哪个程序
# 每个网络程序都需要向操作系统申请唯一的端口号，这样两个进程在两台计算机之间建立网络连接就需要各自的IP 地址和各自的端口号


# 创建TCP 连接时，主动发起连接的叫客户端，被动响应连接的叫服务端
print('--------- TCP socket 客户端 ---------------')
# 客户端主动发起TCP 连接，必须知道服务器的IP 地址和端口号
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET 指定使用IPv4 协议，IPv6 为AF_INET6；SOCK_STREAM 指面向流的TCP 协议
# 建立连接
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据
buffer = []
while True:
    # 每次最多接收1024字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('15.net_program/sina.html', 'wb') as f:
    f.write(html)

print('--------- TCP socket 服务端 ---------------')
# 服务端进程首先要绑定一个端口并监听来自其他客户端的连接，每来一个客户端连接，就创建一个socket 连接
# 服务端会有大量来自客户端的连接，因此，服务端要能够区分一个Socket 连接是和哪个客户端绑定的
# 一个Socket 依赖4项：服务器地址、服务器端口、客户端地址、客户端端口，来唯一确定一个Socket
# tcp_server.py  tcp_client.py

print('--------- UDP 编程 ---------------')
# TCP 是建立可靠连接，并且通信双方都以流的形式发送数据。UDP 则是面向无连接的协议
# 使用UDP 时，不需要建立连接，只需要知道对方的IP 地址和端口号，就可以直接发数据包，能不能到达就不知道了
# 虽然UDP 传输不可靠，但是比TCP 快





