#!/usr/bin/env python
# encoding: utf-8

"""
@description: copy

@author: baoqiang
@time: 2019/11/29 3:20 下午
"""

import copy
import functools


@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name

    def __copy__(self):
        print('__copy__()')
        return MyClass(self.name)

    def __deepcopy__(self, memodict={}):
        print('__deepcopy__({})'.format(memodict))
        return MyClass(copy.deepcopy(self.name, memodict))


def run901_01():
    a = MyClass('a')
    my_list = [a]
    dup = copy.copy(my_list)

    print('my_list:', my_list)
    print('dup:', dup)
    print('dup is my_list:', dup is my_list)
    print('dup == my_list:', dup == my_list)
    print('dup[0] is my_list[0]:', dup[0] is my_list[0])
    print('dup[0] == my_list[0]:', dup[0] == my_list[0])


def run901_02():
    """
    deepcopy: MyClass is copied
    :return:
    """
    a = MyClass('a')
    my_list = [a]
    dup = copy.deepcopy(my_list)

    print('my_list:', my_list)
    print('dup:', dup)
    print('dup is my_list:', dup is my_list)
    print('dup == my_list:', dup == my_list)
    print('dup[0] is my_list[0]:', dup[0] is my_list[0])
    print('dup[0] == my_list[0]:', dup[0] == my_list[0])


def run901_03():
    """
    :return:
    """
    a = MyClass('a')
    sc = copy.copy(a)
    dc = copy.deepcopy(a)


class Graph:
    def __init__(self, name, connections):
        self.name = name
        self.collections = connections

    def add_connection(self, other):
        self.collections.append(other)

    def __repr__(self):
        return 'Graph(name={}, id={})'.format(
            self.name, id(self)
        )

    def __deepcopy__(self, memodict={}):
        print('\nCalling __deepcopy__ for {!r}'.format(self))
        if self in memodict:
            existing = memodict.get(self)
            print('Already copied to {!r}'.format(existing))
            return existing

        print('Memo dictionary:')
        if memodict:
            for k, v in memodict.items():
                print('{}: {}'.format(k, v))
        else:
            print('empty()')

        dup = Graph(copy.deepcopy(self.name, memodict), [])
        print('Copying to new object {}'.format(dup))

        memodict[self] = dup

        for c in self.collections:
            dup.add_connection(copy.deepcopy(c, memodict))

        return dup


def run901_04():
    """
    resolve deepcopy recursion
    :return:
    """
    root = Graph('root', [])
    a = Graph('a', [root])
    b = Graph('b', [a, root])

    root.add_connection(a)
    root.add_connection(b)

    dup = copy.deepcopy(root)
