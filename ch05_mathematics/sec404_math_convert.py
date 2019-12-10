#!/usr/bin/env python
# encoding: utf-8

"""
@description: float convert

@author: baoqiang
@time: 2019/12/10 9:23 下午
"""

import math


def run404_01():
    HEADINGS = ('i', 'int', 'trunk', 'floor', 'ceil')

    print('{:^5} {:^5} {:^5} {:^5} {:^5}'.format(*HEADINGS))
    print('{:-^5} {:-^5} {:-^5} {:-^5} {:-^5}'.format(
        '', '', '', '', '', ))

    fmt = '{:5.1f} {:5.1f} {:5.1f} {:5.1f} {:5.1f}'

    TEST_VALUES = [-1.5, -0.8, -0.5, -0.2, 0, 0.2, 0.5, 0.8, 1]

    for i in TEST_VALUES:
        print(fmt.format(i, int(i), math.trunc(i), math.floor(i), math.ceil(i)))


def run404_02():
    """
    小数和整数部分
    """
    for i in range(6):
        print('{}/2 = {}'.format(i, math.modf(i / 2.0)))


def run404_03():
    """
    x = m * 2 ** e
     0.5 <= abs(m) < 1
    """
    print('{:^7} {:^7} {:^7}'.format('x', 'm', 'e'))
    print('{:-^7} {:-^7} {:-^7}'.format('', '', ''))

    for x in [0.1, 0.5, 4.0]:
        m, e = math.frexp(x)
        print('{:7.2f} {:7.2f} {:7d}'.format(x, m, e))

    print('{:^7} {:^7} {:^7}'.format('m', 'e', 'x'))
    print('{:-^7} {:-^7} {:-^7}'.format('', '', ''))

    for m, e in [(0.8, -3), (0.5, 0), (0.5, 3)]:
        x = math.ldexp(m, e)
        print('{:7.2f} {:7d} {:7.2f}'.format(m, e, x))


def run404_04():
    print(math.fabs(-1.1))
    print(math.fabs(-0.0))
    print(math.fabs(0.0))
    print(math.fabs(1.1))


def run404_05():
    """
    copysign()
    nan can not compare
    """
    HEADINGS = ('f', 's', '< 0', '> 0', '= 0')

    print('{:^5} {:^5} {:^5} {:^5} {:^5}'.format(*HEADINGS))
    print('{:-^5} {:-^5} {:-^5} {:-^5} {:-^5}'.format(
        '', '', '', '', '', ))

    fmt = '{:5.1f} {:5d} {!s:5} {!s:5} {!s:5}'

    TEST_VALUES = [-1.0, 0.0, 1.0, float('-inf'), float('inf'), float('-nan'), float('nan')]

    for f in TEST_VALUES:
        s = int(math.copysign(1, f))
        print(fmt.format(f, s, f < 0, f > 0, f == 0))
