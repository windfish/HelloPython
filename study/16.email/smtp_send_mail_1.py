'文本邮件发送'

from email.mime.text import MIMEText
import smtplib

# MIMEText 对象，第一个参数是邮件正文，
# 第二个是MIME 的subtype，plain 表示纯文本，最终MIME 是“text/plain”
# 第三个 utf-8 编码保证多语言支持
msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')

# 输入Email 地址和口令
from_addr = input('From: ')
password = input('Password: ')

# 输入收件人地址
to_addr = input('to: ')
# 输入SMTP 服务器地址
smtp_server = input('SMTP server: ')

server = smtplib.SMTP(smtp_server, 25)  # 25 是SMTP 协议默认端口
server.set_debuglevel(1)  # 可以打印出和SMTP 服务器交互的所有信息
server.login(from_addr, password)  # 登录SMTP 服务器
server.sendmail(from_addr, [to_addr], msg.as_string())  # 发送邮件，由于可以发给多个人，传入list
server.quit()

# 邮件有以下问题
# 1. 发送的邮件没有主题
# 2. 收件人没有显示
# 3. 收了邮件，却提示不在收件人中

# 因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP 协议发给MTA 的，而是包含在MTA 的文本中
# 所以需要把From、To、Subject 添加到MIMEText 中
# smtp_send_mail_2.py
