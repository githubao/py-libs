#!/usr/bin/env python
# encoding: utf-8

"""
@description: decimal context

@author: baoqiang
@time: 2019/12/5 8:37 下午
"""

import decimal
import threading
from queue import PriorityQueue


def run105_01():
    ctx = decimal.getcontext()

    print('Emax:', ctx.Emax)  # 允许结果的最大指数
    print('Emin:', ctx.Emin)
    print('capitals:', ctx.capitals)  # 为1时打印指数"E"
    print('prec:', ctx.prec)
    print('rouding:', ctx.rounding)
    print('flags:')
    for f, v in ctx.flags.items():
        print('\t{}:{}'.format(f, v))
    print('traps:')
    for t, v in ctx.traps.items():
        print('\t{}:{}'.format(t, v))


def run105_02():
    d = decimal.Decimal('0.123456')
    for i in range(1, 5):
        decimal.getcontext().prec = i
        print(i, ':', d, d * 1)


def run105_03():
    """
    rounding
    """
    ctx = decimal.getcontext()

    ROUNDING_MODES = [
        'ROUND_CEILING',  # 向正无穷大取整
        'ROUND_DOWN',  # 向零取整
        'ROUND_FLOOR',  # 向负无穷大取整
        'ROUND_HALF_DOWN',  # 最后一位大于等于5朝0反方向取整，否则朝0取整
        'ROUND_HALF_EVEN',  # 类似ROUND_HALF_DOWN，但是最后一位是5的时候前一位是偶数则向下取整，奇数则向上取整
        'ROUND_HALF_UP',  # 类似ROUND_HALF_DOWN，但是最后一位是5的话则朝0的反方向取整
        'ROUND_UP',  # 朝0的反方向取整
        'ROUND_05UP',  # 如果最后一位是0或者5则朝0的反方向取整，否则向0取整
    ]

    header_fmt = '{:10} ' + ' '.join(['{:8}'] * 6)
    print(header_fmt.format(
        ' ',
        '1/8 (1)', '-1/8 (1)',
        '1/8 (2)', '-1/8 (2)',
        '1/8 (3)', '-1/8 (3)',
    ))

    for round_mode in ROUNDING_MODES:
        print('{0:10}'.format(round_mode.partition('_')[-1]), end=' ')

        for precision in [1, 2, 3]:
            ctx.prec = precision
            ctx.rounding = getattr(decimal, round_mode)
            value = decimal.Decimal(1) / decimal.Decimal(8)
            print('{0:^8}'.format(value), end=' ')
            value = decimal.Decimal(-1) / decimal.Decimal(8)
            print('{0:^8}'.format(value), end=' ')
        print()


def run105_04():
    """
    local ctx
    """
    with decimal.localcontext() as ctx:
        ctx.prec = 2
        print('Local precision:', ctx.prec)
        print('3.14 / 3 = ', decimal.Decimal('3.14') / 3)

    print()
    print('Default precision:', decimal.getcontext().prec)
    print('3.14 / 3 = ', decimal.Decimal('3.14') / 3)


def run105_05():
    """
    different ctx prec
    """

    ctx = decimal.getcontext().copy()
    ctx.prec = 3

    # ctx local prec
    pi = ctx.create_decimal('3.1415')
    print('PI:', pi)

    # global local prec
    print('RESULT:', decimal.Decimal('2.01') * pi)


def run105_06():
    """
    thread local ctx
    """

    class Multiplier(threading.Thread):
        def __init__(self, a, b, prec, q):
            self.a = a
            self.b = b
            self.prec = prec
            self.q = q
            threading.Thread.__init__(self)

        def run(self) -> None:
            c = decimal.getcontext().copy()
            c.prec = self.prec
            decimal.setcontext(c)
            self.q.put((self.prec, a * b))

    a = decimal.Decimal('3.14')
    b = decimal.Decimal('1.234')

    q = PriorityQueue()
    threads = [Multiplier(a, b, i, q) for i in range(1, 6)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    for i in range(5):
        prec, value = q.get()
        print('{} {}'.format(prec, value))
