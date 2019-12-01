#!/usr/bin/env python
# encoding: utf-8

"""
@description: do reduce

@author: baoqiang
@time: 2019/12/1 5:19 下午
"""

import functools


def do_reduce(a, b):
    print('do_reduce({}, {})'.format(a, b))
    return a + b


def run104_01():
    data = range(1, 5)
    print(data)
    result = functools.reduce(do_reduce, data)
    print('result: {}'.format(result))

    # initial provided
    result2 = functools.reduce(do_reduce, data, 99)
    print('result2: {}'.format(result2))


def run104_02():
    """
    # empty iterable without initializer leads err
    reduce() of empty sequence with no initial value
    :return:
    """

    print('Single item in sequence:', functools.reduce(do_reduce, [1]))
    print('Single item in sequence with initializer:', functools.reduce(do_reduce, [1], 99))
    print('Empty sequence with initializer:', functools.reduce(do_reduce, [], 99))

    try:
        print('Empty sequence:', functools.reduce(do_reduce, []))
    except TypeError as e:
        print('ERROR: {}'.format(e))
