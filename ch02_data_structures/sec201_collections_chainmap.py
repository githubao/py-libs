#!/usr/bin/env python
# encoding: utf-8

"""
@description: 聚合在一起的map

@author: baoqiang
@time: 2019/11/27 10:24 下午
"""

from collections import ChainMap


def run201_01():
    a = {'a': 'A', 'c': 'C'}
    b = {'b': 'B', 'c': 'D'}

    m = ChainMap(a, b)
    print('Individual Values')
    print('a = {}'.format(m['a']))
    print('b = {}'.format(m['b']))
    print('c = {}'.format(m['c']))
    print()

    print('Keys = {}'.format(list(m.keys())))
    print('Values = {}'.format(list(m.values())))
    print()

    print('Items:')
    for k, v in m.items():
        print('{} = {}'.format(k, v))
    print()

    print('"d"in m: {}'.format(('d' in m)))


def run201_02():
    """
    re order
    :return:
    """
    a = {'a': 'A', 'c': 'C'}
    b = {'b': 'B', 'c': 'D'}

    m = ChainMap(a, b)
    print(m.maps)
    print('c = {}'.format(m['c']))

    # reverse
    m.maps = list(reversed(m.maps))

    print(m.maps)
    print('c = {}'.format(m['c']))


def run201_03():
    """
    re order
    :return:
    """
    a = {'a': 'A', 'c': 'C'}
    b = {'b': 'B', 'c': 'D'}

    m = ChainMap(a, b)

    print('Before: {}'.format(m['c']))
    a['c'] = 'E'
    print('After: {}'.format(m['c']))


def run201_04():
    """
    re order only first val changed
    :return:
    """
    a = {'a': 'A', 'c': 'C'}
    b = {'b': 'B', 'c': 'D'}

    m = ChainMap(a, b)

    print('Before: {}'.format(m))

    m['c'] = 'E'

    print('After: {}'.format(m))
    print('a: {}'.format(a))


def run201_05():
    """
    add a new child
    :return:
    """
    a = {'a': 'A', 'c': 'C'}
    b = {'b': 'B', 'c': 'D'}

    m1 = ChainMap(a, b)
    m2 = m1.new_child()

    print('m1 before: {}'.format(m1))
    print('m2 before: {}'.format(m2))

    m2['c'] = 'E'

    print('m1 after: {}'.format(m1))
    print('m2 after: {}'.format(m2))


def run201_06():
    """
    add a new child
    :return:
    """
    a = {'a': 'A', 'c': 'C'}
    b = {'b': 'B', 'c': 'D'}
    c = {'c': 'E'}

    m1 = ChainMap(a, b)
    # m2 = m1.new_child(c)
    m2 = ChainMap(c, m1.maps)

    print('m1["c"]: {}'.format(m1['c']))
    print('m2["c"]: {}'.format(m2['c']))
