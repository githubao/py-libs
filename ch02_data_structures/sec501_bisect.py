#!/usr/bin/env python
# encoding: utf-8

"""
@description: 实现插入排序算法的有序列表

@author: baoqiang
@time: 2019/11/28 7:56 下午
"""

import bisect


def run501_01():
    values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

    print('New Pos Contents')
    print('--- --- --------')

    lst = []
    for i in values:
        pos = bisect.bisect(lst, i)
        bisect.insort(lst, i)  # equal insort_right
        print('{:3} {:3}'.format(i, pos), lst)


def run501_02():
    """
    insort_left
    :return:
    """
    values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

    print('New Pos Contents')
    print('--- --- --------')

    lst = []
    for i in values:
        pos = bisect.bisect_left(lst, i)
        bisect.insort_left(lst, i)
        print('{:3} {:3}'.format(i, pos), lst)
