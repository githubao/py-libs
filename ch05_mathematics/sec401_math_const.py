#!/usr/bin/env python
# encoding: utf-8

# TODO description
"""
@description: 

@author: baoqiang
@time: 2019/12/6 8:00 下午
"""

import math


def run401_01():
    print('pi: {:.30f}'.format(math.pi))
    print('e: {:.30f}'.format(math.e))
    print('nan: {:.30f}'.format(math.nan))
    print('inf: {:.30f}'.format(math.inf))


def run401_02():
    print('{:^3} {:6} {:6} {:6}'.format(
        'e', 'x', 'x**2', 'isinf'))
    print('{:-^3} {:-^6} {:-^6} {:-^6}'.format(
        '', '', '', ''))

    for e in range(0, 201, 20):
        x = 10.0 ** e
        y = x * x
        print('{:3d} {:<6g} {:<6g} {!s:6}'.format(
            e, x, y, math.isinf(y)
        ))


def run401_03():
    x = 10.0 ** 200
    print('x=', x)
    print('x*x=', x * x)
    print('x**2=', end=' ')
    try:
        print(x ** 2)
    except OverflowError as e:
        print(e)


def run401_04():
    """
    isnan()
    """
    x = 10.0 ** 200
    x = x * x
    y = x / x

    print('x=', x)
    print('isnan(x)=', math.isnan(x))
    print('y=x/x = ', x / x)
    print('y==nan =', y == math.nan)
    print('isnan(y) =', math.isnan(y))


def run401_05():
    """
    isfinite()
    """
    for f in [0.0, 1.0, math.pi, math.e, math.inf, math.nan]:
        print('{:5.2f} {!s}'.format(f, math.isfinite(f)))
