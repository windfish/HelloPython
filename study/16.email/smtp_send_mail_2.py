'文本邮件和HTML 邮件发送'

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
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

msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python 学习者 <%s>' % from_addr)
# msg['To'] 接收的不是list，是字符串，多个邮件地址，用 , 分隔即可
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP 的问候', 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 发送HTML 邮件，构造MIMEText 把html 字符串传入，第二个参数传入html 即可
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#                '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#                '</body></html>', 'html', 'utf-8')


