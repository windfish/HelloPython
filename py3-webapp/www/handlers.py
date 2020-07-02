#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
url handlers
"""


from coreweb import get, post


@get('/')
def index():
    return '<h1>Awesome</h1>'
