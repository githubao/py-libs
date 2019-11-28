#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/11/28 11:04 上午
"""

from collections import defaultdict


def default_factory():
    return 'default value'


def run203_01():
    d = defaultdict(default_factory, foo='bar')

    print('d: ', d)
    print('foo =>', d['foo'])
    print('bar =>', d['bar'])
