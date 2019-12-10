#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/12/10 9:00 下午
"""
import math


def run403_01():
    """
    format 冒号后面的第一个字符为"空白补位的填充字符"
    """
    INPUTS = [
        (1000, 900, 0.1),
        (100, 90, 0.1),
        (10, 9, 0.1),
        (1, 0.9, 0.1),
        (0.1, 0.09, 0.1),
    ]

    print('{:^8} {:^8} {:^8} {:^8} {:^8} {:^8}'.format(
        'a', 'b', 'rel_tol', 'abs(a-b)', 'tolerance', 'close'))

    print('{:-^8} {:-^8} {:-^8} {:-^8} {:-^8} {:-^8}'.format(
        '', '', '', '', '', ''))

    fmt = '{:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f} {!s:>8}'

    for a, b, rel_tol in INPUTS:
        close = math.isclose(a, b, rel_tol=rel_tol)
        tolerance = rel_tol * max(abs(a), abs(b))
        abs_diff = abs(a - b)
        print(fmt.format(a, b, rel_tol, abs_diff, tolerance, close))


def run403_02():
    INPUTS = [
        (1.0, 1.0 + 1e-07, 1e-08),
        (1.0, 1.0 + 1e-08, 1e-08),
        (1.0, 1.0 + 1e-09, 1e-08),
    ]

    print('{:^8} {:^11} {:^8} {:^10} {:^8}'.format(
        'a', 'b', 'abs_tol', 'abs(a-b)', 'close'))

    print('{:-^8} {:-^11} {:-^8} {:-^10} {:-^8}'.format(
        '', '', '', '', ''))

    for a, b, abs_tol in INPUTS:
        close = math.isclose(a, b, abs_tol=abs_tol)
        abs_diff = abs(a - b)
        print('{:8.2f} {:11} {:8} {:0.9f} {!s:>8}'.format(
            a, b, abs_tol, abs_diff, close))


def run403_03():
    """
    inf & inf is close
    """
    print('nan, nan:', math.isclose(math.nan, math.nan))
    print('nan, 1.0:', math.isclose(math.nan, 1.0))
    print('inf, inf:', math.isclose(math.inf, math.inf))
    print('inf, 1.0:', math.isclose(math.inf, 1.0))
