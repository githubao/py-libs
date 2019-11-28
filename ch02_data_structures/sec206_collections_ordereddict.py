#!/usr/bin/env python
# encoding: utf-8

"""
@description: 有序字典
(notice: python3.6 以后字典已经有序了)

@author: baoqiang
@time: 2019/11/28 1:34 下午
"""

from collections import OrderedDict


def run206_01():
    print('Regular dict:')
    # d = {'a':'A','b':'B','c':'C'}
    d = {}
    d['a'] = 'A'
    d['b'] = 'B'
    d['c'] = 'C'
    for k, v in d.items():
        print(k, v)

    print('OrderedDict:')
    d = OrderedDict()
    d['a'] = 'A'
    d['b'] = 'B'
    d['c'] = 'C'
    for k, v in d.items():
        print(k, v)


def run206_02():
    """
    相等性判断，需要考虑顺序
    :return:
    """
    print('Regular dict:')
    d1 = {'a': 'A', 'b': 'B', 'c': 'C'}
    d2 = {'c': 'C', 'b': 'B', 'a': 'A'}
    print(d1 == d2)

    for k, v in d1.items():
        print(k, v)
    for k, v in d2.items():
        print(k, v)

    print('OrderedDict:')
    d1 = OrderedDict(d1)
    d2 = OrderedDict(d2)
    print(d1 == d2)

    for k, v in d1.items():
        print(k, v)
    for k, v in d2.items():
        print(k, v)


def run206_03():
    """
    re ordering
    :return:
    """
    d = OrderedDict([('a', 'A'), ('b', 'B'), ('c', 'C')])

    print('Before:')
    for k, v in d.items():
        print(k, v)

    d.move_to_end('b')
    print('\nmove_to_end():')
    for k, v in d.items():
        print(k, v)

    d.move_to_end('b', last=False)
    print('\nmove_to_end(last=False):')
    for k, v in d.items():
        print(k, v)
