#!/usr/bin/env python
# encoding: utf-8

"""
@description: compare

@author: baoqiang
@time: 2019/12/1 4:39 下午
"""

import functools
import inspect
from pprint import pprint


@functools.total_ordering
class MyObject:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print('testing __eq__({}, {})'.format(
            self.val, other.val
        ))
        return self.val == other.val

    def __gt__(self, other):
        print('testing __gt__({}, {})'.format(
            self.val, other.val
        ))
        return self.val > other.val


def run102_01():
    print('Methods:\n')
    pprint(inspect.getmembers(MyObject, inspect.isfunction))

    a = MyObject(1)
    b = MyObject(2)

    print('\nComparisons:')
    for expr in ['a<b', 'a<=b', 'a==b', 'a>=b', 'a>b']:
        print('\n{:<6}'.format(expr))
        result = eval(expr)
        print('result of {}: {}'.format(expr, result))


class MyObject2:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return 'MyObject2({})'.format(self.val)


def compare_obj(a, b):
    print('comparing {} and {}'.format(a, b))
    if a.val < b.val:
        return -1
    elif a.val > b.val:
        return 1
    return 0


def run102_02():
    get_key = functools.cmp_to_key(compare_obj)

    def get_key_wrapper(o):
        new_key = get_key(o)
        print('key wrapper({}) -> {}'.format(o, new_key))
        return new_key

    objs = [MyObject2(x) for x in range(5, 0, -1)]
    for o in sorted(objs, key=get_key_wrapper):
        print(o)
