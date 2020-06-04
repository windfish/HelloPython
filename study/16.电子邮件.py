#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 现在我们用Outlook 或Foxmail 等软件写好邮件后，填写对方的邮件地址，发送就好了。这些电子邮件软件称为MUA：Mail User Agent 邮件用户代理
# Email 从MUA 发出后，不是直接到对方电脑，而是发到MTA：Mail Transfer Agent 邮件传输代理，就是Email 服务提供商
# 比如，@163.com 发送到@sina.com，会先达到网易的MTA，再由网易的MTA 发送到新浪的MTA
# 邮件到达对方的MTA 后，会把Email 投递到邮件的最终目的地MDA：Mail Delivery Agent 邮件投递代理
# 邮件到达MDA 后，就存放在某个文件或数据库里，这个长期保存邮件的地方称为电子邮箱
# 对方收取邮件，必须通过MUA 从MDA 上把邮件取到自己的电脑上
# 一封电子邮件的旅程是：发件人 -> MUA -> 自己的MTA -> 若干MTA -> 对方的MTA -> MDA <- MUA <- 收件人

# 发送邮件，本质上是编写MUA 把邮件发到MTA
# 接收邮件，本质上是编写MUA 从MDA 上收邮件

# 发送邮件时，MUA 和MTA 使用的协议是SMTP：Simple Mail Transfer Protocol
# 接收邮件时，MUA 和MDA 使用的协议有两种：
# POP：Post Office Protocol，目前版本3，俗称POP3
# IMAP：Internet Message Access Protocol，目前版本4，优点是不但能取邮件，还可以操作NDA 上存储的邮件，例如从收件箱移到垃圾箱等


# Python 对SMTP 支持有smtplib 和email 两个模块，email 负责构造邮件，smtplib 负责发送邮件

# 加密SMTP
# 使用标准的25端口连接SMTP 服务器时，使用明文传输；加密SMTP，先创建SSL 安全连接，在使用SMTP 协议发送邮件
import smtplib


# smtp_server = 'smtp.qq.com'
# smtp_port = 587
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()  # 建立SSL 连接
# # 剩下的就跟明文发送邮件一样
# server.set_debuglevel(1)
# server.login(from_addr, password)  # 登录SMTP 服务器
# server.sendmail(from_addr, [to_addr], msg.as_string())  # 发送邮件，由于可以发给多个人，传入list
# server.quit()


# 构造一个邮件对象就是一个Message 对象
# 构造一个MIMEText 对象，就表示一个文本邮件对象
# 构造一个MIMEImage 对象，就表示一个作为附件的对象
# 要把多个对象组合起来，就用MIMEMultipart 对象
# MIMEBase 对象可以表示任意对象
# 继承关系
# Message
#   -- MIMEBase
#      -- MIMEMultipart
#      -- MIMENonMultipart
#         -- MIMEMessage
#         -- MIMEText
#         -- MIMEImage


# POP3 收取邮件
# Python 内置了一个poplib 模块，实现了POP3 协议
# POP3 协议收取的是邮件的原始文本，还需要用email 模块解析原始文本，变成可阅读的邮件对象

