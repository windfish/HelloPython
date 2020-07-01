import orm
from models import User, Blog, Comment
import asyncio


'测试orm的类'


async def test():
    await orm.create_pool(user='py3', password='py3mysql', db='py3app')

    u = User(name='test001', email='test001@test.com', passwd='12345236', image='about:blank')

    await u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test())

