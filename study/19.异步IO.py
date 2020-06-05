# 异步IO，当代码执行一个耗时的IO 操作时，只发出IO 指令，并不等待结果，当IO 返回结果时，再通知CPU 进行处理
# 异步IO 模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息 - 处理消息”这一过程


# 协程，又称微线程，纤程，英文名Coroutine
# 子程序，或称为函数，其调用是通过栈实现的，一个线程就是执行一个子程序。子程序调用总是一个入口，一次返回，调用顺序是明确的
# 协程调用与子程序不同，在执行过程中，子程序内部可中断，转而执行别的子程序，在适当的时候再返回接着执行
# 协程执行看起来像多线程，但是其特点在于是在一个线程执行，不需要线程切换，拥有极高的执行效率，也不需要锁机制，因为同一个线程，不存在同时写变量冲突

# Python 对协程的支持是通过generator 实现的
# 在generator 中，不但可以通过for 循环来迭代，也可以通过调用next() 获取yield 语句返回的下一个值
# yield 不但可以返回一个值，还可以接受调用者发出的参数

# 生产者-消费者模型，使用协程，通过yield 跳转到消费者执行，消费者执行完毕后，切回生产者继续生产
def consumer():
    # print('consumer begin')
    r = ''
    while True:
        # print('consumer while begin')
        n = yield r
        if not n:
            print('consumer get None from producer')
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    # print('producer begin')
    c.send(None)
    n = 0
    while n < 5:
        # print('producer while begin')
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()  # 构造generator 对象
produce(c)

# 执行顺序：
# 1. 将生成器generator 传入produce
# 2. 通过 c.send(None) 启动生成器，生成器consumer 执行到yield 返回
# 3. 生产者produce 生产东西，通过c.send(n) 切换到consumer 执行
# 4. consumer 通过yield 拿到消息，处理，又通过yield 把结果传回produce
# 5. produce 拿到consumer 返回的结果，继续产生下一条消息，并再次传给consumer
# 6. produce 决定不生产了，通过c.close() 关闭consumer，整个过程结束


print('-------------asyncio------------------')
# asyncio 是Python 3.4 引入的标准库，内置了对异步IO 的支持
# asyncio 编程模型就是一个消息循环，从asyncio 模块中直接获取一个EventLoop 的引用，然后把需要执行的协程扔到EventLoop 中执行
import asyncio, threading


@asyncio.coroutine
def hello():
    print('Hello world!')
    # 异步调用 asyncio.sleep(1)
    r = yield from asyncio.sleep(2)
    print('Hello again!')


# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())


@asyncio.coroutine
def hello2():
    print('Hello world! (%s)' % threading.current_thread())
    # 异步调用 asyncio.sleep(1)
    r = yield from asyncio.sleep(2)
    print('Hello again! (%s)' % threading.current_thread())


# 封装两个coroutine，发现执行的线程都是主线程
tasks = [hello2(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))


# 通过asyncio 的异步网络连接获取sina、qq和163的网站首页
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        # 读取Header
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


tasks = [wget(host) for host in ['www.sina.com.cn', 'www.qq.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))

# asyncio 提供了完善的异步IO 支持；
# 异步操作需要在coroutine 中通过yield from 完成；
# 多个coroutine 可以封装成一组Task，并发执行

print('--------async/await---------------')


# 为了简化并更好的标识异步IO，从3.5 引入了新语法async 和await
# async 替换 @asyncio.coroutine；await 替换 yield from
async def wget2(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        # 读取Header
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


tasks = [wget2(host) for host in ['www.sina.com.cn', 'www.qq.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))

# loop.close()

print('-----------aiohttp-------------------')
# asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持
# asyncio 实现了TCP、UDP、SSL 等协议，aiohttp 是基于asyncio 实现的HTTP 框架
from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')


async def hello_web(request):
    await asyncio.sleep(0.5)
    text = '<h1>Hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')


app = web.Application()
app.router.add_route('GET', '/', index)
app.router.add_route('GET', '/hello/{name}', hello_web)
web.run_app(app, host='127.0.0.1', port=8000)

# aiohttp 官方文档：https://docs.aiohttp.org/en/stable/web_quickstart.html#run-a-simple-web-server

