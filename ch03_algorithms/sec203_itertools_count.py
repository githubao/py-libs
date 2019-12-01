#!/usr/bin/env python
# encoding: utf-8

"""
@description: iter tools

@author: baoqiang
@time: 2019/12/1 7:49 下午
"""

from itertools import count, cycle, repeat
import fractions


def run203_01():
    for i in zip(count(), ['a', 'b', 'c']):
        print(i)


def run203_02():
    """
    count start,step
    :return:
    """
    start = fractions.Fraction(1, 3)  # 分数
    step = fractions.Fraction(1, 3)

    for i in zip(count(start, step), ['a', 'b', 'c']):
        print('{}: {}'.format(*i))


def run203_03():
    """
    cycle()
    :return:
    """
    for i in zip(range(7), cycle(['a', 'b', 'c'])):
        print(i)


def run203_04():
    """
    repeat
    :return:
    """
    for i in repeat('over-and-over', 5):
        print(i)


def run203_05():
    """
    combin tools
    :return:
    """
    for i, s in zip(count(), repeat("over-and-over", 5)):
        print(i, s)

    for i in map(lambda x, y: (x, y, x * y), repeat(2), range(5)):
        print('{:d} * {:d} = {:d}'.format(*i))


def run203_06():
    pass


def run203_07():
    pass


def run203_08():
    pass


def run203_09():
    pass
