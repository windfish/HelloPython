#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'async web application'

import logging
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


app = web.Application()
app.router.add_route('GET', '/', index)
logging.info('server started at http://localhost:9000...')
web.run_app(app, host='localhost', port=9000)


