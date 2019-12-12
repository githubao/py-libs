#!/usr/bin/env python
# encoding: utf-8

"""
@description: funcs

@author: baoqiang
@time: 2019/12/11 9:13 下午
"""

import math


def run407_01():
    """
    fsum()
    """
    values = [0.1] * 10
    print('Input values:', values)
    print('sum(): {:0.20f}'.format(sum(values)))

    s = 0.0
    for i in values:
        s += i

    print('for loop: {:.20f}'.format(s))

    print('math.fsum(): {:.20f}'.format(math.fsum(values)))


def run407_02():
    """
    factorial() & gamma()
    """
    for i in [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.1]:
        try:
            print('{:2.0f} {:6.0f}'.format(i, math.factorial(i)))
        except ValueError as e:
            print(e)

    print()
    for i in [0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6]:
        try:
            print('{:2.1f} {:6.2f}'.format(i, math.gamma(i)))
        except ValueError as e:
            print(e)

    print()
    for i in [0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6]:
        try:
            print('{:2.1f} {:.20f} {:.20f}'.format(i, math.lgamma(i), math.log(math.gamma(i))))
        except ValueError as e:
            print(e)


def run407_03():
    """
    fmod(): 被除数的符号一致
    %: 与除数的符号一致
    """
    print('{:^4} {:^4} {:^4} {:^5}'.format('x', 'y', '%', 'fmod'))
    print('{:-^4} {:-^4} {:-^4} {:-^4}'.format('', '', '', ''))

    INPUTS = [(5, 2), (5, -2), (-5, 2), (-5, -2)]

    for x, y in INPUTS:
        print('{:4.1f} {:4.1f} {:5.2f} {:5.2f}'.format(
            x, y, x % y, math.fmod(x, y)
        ))


def run407_04():
    """
    gcd(): 最大公约数
    """
    print(math.gcd(10, 8))
    print(math.gcd(10, 0))
    print(math.gcd(50, 255))
    print(math.gcd(11, 9))
    print(math.gcd(0, 0))


def run407_05():
    """
    pow()
    """
    INPUTS = [
        (2, 3),
        (2.1, 3.2),
        (1.0, 5),
        (2.0, 0),
        (2, float('nan')),
        (9.0, 0.5),
        (27.0, 1.0 / 3),
    ]

    for x, y in INPUTS:
        print('{:5.1f} ** {:5.3f} = {:6.3f}'.format(
            x, y, math.pow(x, y)
        ))

    print(math.sqrt(9.0))
    print(math.sqrt(3))
    print(math.sqrt(-1))  # ValueError: math domain error


def run407_06():
    """
    log()
    """
    print(math.log(8))
    print(math.log(8, 2))
    print(math.log(0.5, 2))

    print('{:^2} {:^12} {:^10} {:^20} {:^8}'.format('i', 'x', 'accurate', 'inaccurate', 'mismatch'))
    print('{:-^2} {:-^12} {:-^10} {:-^20} {:-^8}'.format('', '', '', '', ''))

    for i in range(0, 10):
        x = math.pow(10, i)
        accurate = math.log10(x)
        inaccurate = math.log(x, 10)
        match = '' if int(inaccurate) == i else '*'

        print('{:2d} {:12.1f} {:10.8f} {:20.18f} {:^5}'.format(
            i, x, accurate, inaccurate, match
        ))

    print('{:^2} {:^12} {:^10}'.format('i', 'x', 'log2'))
    print('{:-^2} {:-^12} {:-^10}'.format('', '', ''))

    for i in range(0, 10):
        x = math.pow(2, i)
        accurate = math.log2(x)

        print('{:2d} {:5.1f} {:5.1f}'.format(
            i, x, accurate
        ))


def run407_07():
    """
    log1p(): 用于计算接近1的log()
    """
    x = 0.0000000000000000000000001
    print('x:', x)
    print('1+x:', x)
    print('log(1+x):', math.log(1 + x))
    print('log1p(x):', math.log1p(x))

    x = 2
    fmt = '{:.20f}'
    print(fmt.format(math.e ** 2))
    print(fmt.format(math.pow(math.e, 2)))
    print(fmt.format(math.exp(2)))

    x = 0.0000000000000000000000001
    print(x)
    print(math.exp(x) - 1)
    print(math.expm1(x))
