#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/12/5 7:41 下午
"""

import decimal


def run101_01():
    fmt = '{0:<25} {1:25}'
    print(fmt.format('Input', 'Output'))
    print(fmt.format('-' * 25, '-' * 25))

    print(fmt.format(5, decimal.Decimal(5)))

    print(fmt.format('3.14', decimal.Decimal('3.14')))

    f = 0.1
    print(fmt.format(repr(f), decimal.Decimal(str(f))))
    print('{:<0.23f} {:25}'.format(f, str(decimal.Decimal.from_float(f))[:25]))


def run101_02():
    t = (1, (1, 2, 3), -1)  # 第一位的1表示负数， -1表示小数点后面有一位
    print('Input:', t)
    print('Decimal:', decimal.Decimal(t))


def run101_03():
    """
    formatting
    {:g}的意思是只出现几个数字
    """
    d = decimal.Decimal(1.1)
    print('Precision:')
    print('{:.1}'.format(d))
    print('{:.2}'.format(d))
    print('{:.3}'.format(d))
    print('{:.18}'.format(d))

    print('\nWidth and precision combined.')
    print('{:5.1f} {:5.1g}'.format(d, d))
    print('{:5.2f} {:5.2g}'.format(d, d))
    print('{:5.3f} {:5.3g}'.format(d, d))

    print('\nZero padding:')
    print('{:05.1}'.format(d))
    print('{:05.2}'.format(d))
    print('{:05.3}'.format(d))


def run101_04():
    a = decimal.Decimal('5.1')
    b = decimal.Decimal('3.14')
    c = 4
    d = 3.14

    print('a=', repr(a))
    print('b=', repr(b))
    print('c=', repr(c))
    print('d=', repr(d))
    print()

    print('a+b=', a + b)
    print('a-b=', a - b)
    print('a*b=', a * b)
    print('a/b=', a / b)
    print()

    print('a+c=', a + c)
    print('a-c=', a - c)
    print('a*c=', a * c)
    print('a/c=', a / c)
    print()

    print('a+d=', end=' ')
    try:
        print(a + d)
    except TypeError as e:
        # unsupported operand type(s) for +: 'decimal.Decimal' and 'float'
        print(e)


def run101_05():
    for value in ['Infinity', 'NaN', '0']:
        print(decimal.Decimal(value), decimal.Decimal('-' + value))
    print()

    print('Infinity + 1:', (decimal.Decimal('Infinity') + 1))
    print('-Infinity + 1:', (decimal.Decimal('-Infinity') + 1))

    print(decimal.Decimal('NaN') == decimal.Decimal('Infinity'))
    print(decimal.Decimal('NaN') != decimal.Decimal(1))
