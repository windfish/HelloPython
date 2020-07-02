#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
JSON 格式错误信息定义
'''

import json, logging, inspect, functools


class APIError(Exception):
    """
    基本的API 错误信息，包含错误、数据、消息
    """
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    """
    输入值错误
    """
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFoundError(APIError):
    """
    资源未找到错误
    """
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:not found', field, message)


class APIPermissionError(APIError):
    """
    无权限错误
    """
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)

