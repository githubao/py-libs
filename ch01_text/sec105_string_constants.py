#!/usr/bin/env python
# encoding: utf-8

"""
@description: 字符串常量

@author: baoqiang
@time: 2019/11/26 12:38 下午
"""

import string
import inspect


def is_str(value):
    # return True
    return isinstance(value, str)


def run105_01():
    """
    ascii_letters
    ascii_lowercase
    ascii_uppercase
    digits
    hexdigits
    octdigits
    printable
    punctuation
    whitespace
    :return:
    """
    for name, value in inspect.getmembers(string, is_str):
        if name.startswith('__'):
            continue
        print('%s=%r\n' % (name, value))
        # print('%s' % name)
