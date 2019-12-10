#!/usr/bin/env python
# encoding: utf-8

"""
@description: 分数

@author: baoqiang
@time: 2019/12/5 9:14 下午
"""
import decimal
import fractions
import math


def run201_01():
    for n, d in [(1, 2), (2, 4), (3, 6)]:
        f = fractions.Fraction(n, d)
        print('{}/{} = {}'.format(n, d, f))

    for s in ['1/2', '2/4', '3/6']:
        f = fractions.Fraction(s)
        print('{} = {}'.format(s, f))

    for s in ['0.5', '1.5', '2.0', '5e-1']:
        f = fractions.Fraction(s)
        print('{0:>4} = {1}'.format(s, f))


def run201_02():
    for v in [0.1, 0.5, 1.5, 2.0]:
        print('{} = {}'.format(v, fractions.Fraction(v)))

    values = [
        decimal.Decimal('0.1'),
        decimal.Decimal('0.5'),
        decimal.Decimal('1.5'),
        decimal.Decimal('2.0'),
    ]

    for v in values:
        print('{} = {}'.format(v, fractions.Fraction(v)))


def run201_03():
    f1 = fractions.Fraction(1, 2)
    f2 = fractions.Fraction(3, 4)

    print('{} + {} = {}'.format(f1, f2, f1 + f2))
    print('{} - {} = {}'.format(f1, f2, f1 - f2))
    print('{} * {} = {}'.format(f1, f2, f1 * f2))
    print('{} / {} = {}'.format(f1, f2, f1 / f2))


def run201_04():
    """
    浮点数的精度，限制分母的大小
    """
    print('PI:', math.pi)

    f_pi = fractions.Fraction(str(math.pi))
    print('no limit = ', f_pi)

    for i in [1, 6, 11, 60, 70, 90, 100]:
        limited = f_pi.limit_denominator(i)
        print('{0:8} = {1}'.format(i, limited))
