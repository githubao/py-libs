#!/usr/bin/env python
# encoding: utf-8

"""
@description: filter

@author: baoqiang
@time: 2019/12/1 7:59 下午
"""

from itertools import dropwhile, takewhile, filterfalse, cycle, compress


def should_drop(x):
    # print('Testing:', x)
    return x < 1


def should_take(x):
    # print('Testing:', x)
    return x < 2


def check_item(x):
    # print('Testing:', x)
    return x < 2


def run204_01():
    """
    dropwhile: 找到第一个条件为False的直到最后，之前的都丢弃，包括该条False的
    Yielding: 1 Yielding: 2 Yielding: -2
    :return:
    """
    for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
        print('Yielding:', i, end=' ')
    print()


def run204_02():
    """
    takewhile: 找到第一个条件为False的取所有前面的，不包括该条判断为False的
    Yielding: -1 Yielding: 0 Yielding: 1
    :return:
    """
    for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
        print('Yielding:', i, end=' ')
    print()


def run204_03():
    """
    filter
    :return:
    """
    for i in filter(check_item, [-1, 0, 1, 2, -2]):
        print('Yielding:', i, end=' ')
    print()

    for i in filterfalse(check_item, [-1, 0, 1, 2, -2]):
        print('Yielding:', i, end=' ')
    print()


def run204_04():
    """
    compress, filter val
    :return:
    """
    every_third = cycle([False, False, True])

    for i in compress(range(1, 10), every_third):
        print(i, end=' ')
    print()
