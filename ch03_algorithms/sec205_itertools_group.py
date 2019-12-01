#!/usr/bin/env python
# encoding: utf-8

"""
@description: group impl

@author: baoqiang
@time: 2019/12/1 8:25 下午
"""
import operator
from itertools import cycle, islice, count, groupby
import functools
from pprint import pprint


@functools.total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)


def run205_01():
    data = list(map(Point, cycle(islice(count(), 3)), islice(count(), 7)))
    print('Data:')
    pprint(data, width=35)
    print()

    print('Grouped, unsorted:')
    for k, g in groupby(data, operator.attrgetter('x')):
        print(k, list(g))
    print()

    data.sort()
    print('Sorted:')
    pprint(data, width=35)
    print()

    print('Grouped, sorted:')
    for k, g in groupby(data, operator.attrgetter('x')):
        print(k, list(g))
    print()
