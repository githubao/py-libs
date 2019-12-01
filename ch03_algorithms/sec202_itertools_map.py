#!/usr/bin/env python
# encoding: utf-8

"""
@description: map

@author: baoqiang
@time: 2019/12/1 7:48 下午
"""
from itertools import starmap


def times_two(x):
    return 2 * x


def multiply(x, y):
    return x, y, x * y


def run202_01():
    """
    map func
    :return:
    """
    print('Doubles:')
    for i in map(times_two, range(5)):
        print(i)

    print('\nMultiples:')
    r1 = range(5)
    r2 = range(5, 10)
    for i in map(multiply, r1, r2):
        print('{:d} * {:d} = {:d}'.format(*i))

    print('\nStopping:')
    r1 = range(5)
    r2 = range(2)
    for i in map(multiply, r1, r2):
        print(i)


def run202_02():
    """
    starmap
    :return:
    """
    values = [(0, 5), (1, 6), (2, 7)]
    for i in starmap(lambda x, y: (x, y, x * y), values):
        print('{:d} * {:d} = {:d}'.format(*i))


