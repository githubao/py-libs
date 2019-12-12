#!/usr/bin/env python
# encoding: utf-8

"""
@description: 角度相关的计算

@author: baoqiang
@time: 2019/12/11 9:48 下午
"""

import math


def run409_01():
    print('{:^7} {:^7} {:^7}'.format('Degrees', 'Radians', 'Expected'))
    print('{:-^7} {:-^7} {:-^7}'.format('', '', ''))

    INPUTS = [
        (0, 0),
        (30, math.pi / 6),
        (45, math.pi / 4),
        (60, math.pi / 3),
        (90, math.pi / 2),
        (180, math.pi),
        (270, math.pi * 3.0 / 2),
        (360, math.pi * 2),
    ]

    for deg, expected in INPUTS:
        print('{:7} {:7.2f} {:7.2f}'.format(
            deg, math.radians(deg), expected
        ))

    print('\n\n')
    for expected, rad in INPUTS:
        print('{:7.2f} {:7.2f} {:7.2f}'.format(
            rad, math.degrees(rad), expected
        ))


def run409_02():
    print('{:^7} {:^7} {:^7}  {:^7}  {:^7}'.format(
        'Degrees', 'Radians', 'Sine', 'Cosine', 'Tangent'))
    print('{:-^7} {:-^7} {:-^7}  {:-^7} {:-^7}'.format('', '', '', '', ''))

    fmt = ' '.join('{:7.2f}' for _ in range(5))

    for deg in range(0, 361, 30):
        rad = math.radians(deg)
        if deg in (90, 270):
            t = float('inf')
        else:
            t = math.tan(rad)
        print(fmt.format(deg, rad, math.sin(rad), math.cos(rad), t))


def run409_03():
    fmt1 = ' '.join('{:^8}' for _ in range(5))
    fmt2 = ' '.join('{:-^8}' for _ in range(5))
    fmt3 = ' '.join('{:8.2f}' for _ in range(5))
    fmt4 = ' '.join('{:8.2f}' for _ in range(3))

    print(fmt1.format('X1', 'Y1', 'X2', 'Y2', 'Distance'))
    print(fmt2.format(*['' for _ in range(5)]))

    POINTS = [
        [(5, 5), (6, 6)],
        [(-6, -6), (-5, -5)],
        [(0, 0), (3, 4)],
        [(-1, -1), (2, 3)]
    ]

    for (x1, y1), (x2, y2) in POINTS:
        h = math.hypot((x1 - x2), (y1 - y2))
        print(fmt3.format(x1, y1, x2, y2, h))

    POINTS = [
        (1, 1),
        (math.sqrt(2), math.sqrt(2)),
        (math.sqrt(2) / 2, math.sqrt(2) / 2),
        (0.5, math.sqrt(3) / 2)
    ]

    for x, y in POINTS:
        h = math.hypot(x, y)
        print(fmt4.format(x, y, h))


def run409_04():
    for r in [0, 0.5, 1]:
        print('arcsine({:.1f}) = {:5.2f}'.format(r, math.asin(r)))
        print('arccosine({:.1f}) = {:5.2f}'.format(r, math.acos(r)))
        print('arctangent({:.1f}) = {:5.2f}'.format(r, math.atan(r)))


def run409_05():
    fmt1 = ' '.join('{:^6}' for _ in range(4))
    fmt2 = ' '.join('{:-^6}' for _ in range(4))
    fmt3 = ' '.join('{:6.4f}' for _ in range(4))

    print(fmt1.format('X', 'sinh', 'cosh', 'tanh'))
    print(fmt2.format(*['' for _ in range(4)]))

    for i in range(0, 11, 2):
        x = i / 10.0
        print(fmt3.format(x, math.sinh(x), math.cosh(x), math.tanh(x)))


def run409_06():
    """
    erfc(x) = 1-erf(x)
    """
    print('{:^5} {:7} {:7}'.format('x', 'erf(x)', 'erfc(x)'))
    print('{:-^5} {:-^7} {:-^7}'.format('', '', ''))

    for x in [-3, -2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, 3]:
        print('{:5.2f} {:7.4f} {:7.4f}'.format(x, math.erf(x), math.erfc(x)))
