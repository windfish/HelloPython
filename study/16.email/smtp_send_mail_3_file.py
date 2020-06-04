'发送带附件的邮件'

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    # 中文需要使用Header 对象进行编码
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = input('From: ')
password = input('Password: ')
to_addr = input('to: ')
smtp_server = input('SMTP server: ')

msg = MIMEMultipart()
msg.attach(MIMEText('Hello, send with file by Python...', 'plain', 'utf-8'))

msg['From'] = _format_addr('Python 学习者 <%s>' % from_addr)
# msg['To'] 接收的不是list，是字符串，多个邮件地址，用 , 分隔即可
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP 的问候', 'utf-8').encode()

# 发送附件，添加附件就是加上一个MIMEBase
with open('../13/code.jpg', 'rb') as f:
    # 设置附件的MIME 和文件名
    mime = MIMEBase('image', 'jpeg', filename='code.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='code.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件内容读进来
    mime.set_payload(f.read())
    # 用Base64 编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 将图片嵌入邮件正文中，不能在邮件中直接链接图片地址，因为一般邮寄服务商都会屏蔽外链
# 需要先把图片作为附件添加进去，然后在HTML 中通过src="cid:0"将图片嵌入，若多个图片，则依次编号引用即可
# msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
#                     '<p><img src="cid:0"></p>' +
#                     '</body></html>', 'html', 'utf-8'))

# 同时支持HTML 和Plain 格式邮件，当收件人看不了HTML 邮件时，自动降级为文本邮件
# 指定subtype是alternative
# msg = MIMEMultipart('alternative')
# msg.attach(MIMEText('hello', 'plain', 'utf-8'))
# msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

