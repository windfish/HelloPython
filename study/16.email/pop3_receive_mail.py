'pop3 获取最新的一封邮件'

import poplib

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


# 输入邮件地址
email = input('Email:')
password = input('Password:')
pop3_server = input('POP3 server:')

# 连接到POP3 服务器
server = poplib.POP3(pop3_server)
# 打开调试信息
server.set_debuglevel(1)
# 可选：打印POP3 服务器的欢迎信息
print(server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(password)

# stat() 返回邮件数量和占用空间
print('Message: %s. Size: %s' % server.stat())
# list() 返回所有邮件的编号
resp, mails, octets = server.list()
# 可以查看返回的列表
print(len(mails))

# 获取最新的一封邮件，序号从1开始
index = len(mails)
resp, lines, octets = server.retr(index)

# lines 存储了邮件的原始文本的每一行
msg_content = b'\r\n'.join(lines).decode('utf-8')

# 可以根据邮件索引从服务器删除邮件
# server.dele(index)
# 关闭连接
server.quit()


# 解析邮件内容为Message 对象，本身可能是一个MIMEMultipart 对象，即包含嵌套的其他MIMEBase 对象
msg = Parser().parsestr(msg_content)
print(msg)


# 需要递归地打印出Message 对象的层次结构，indent 用于缩进显示
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('    ' * indent, header, value))
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('    ' * indent, n))
            print('%s-------------------------' % ('    ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('    ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('    ' * indent, content_type))


def decode_str(s):
    # decode_header() 返回一个list，因为像层cc、bcc 都可能包含多个邮件地址
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


print_info(msg)
