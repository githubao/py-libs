#!/usr/bin/env python
# encoding: utf-8

"""
@description: chain

@author: baoqiang
@time: 2019/12/1 6:28 下午
"""

from itertools import chain, zip_longest, islice, tee, count, starmap


def run201_01():
    for i in chain([1, 2, 3], ['a', 'b', 'c']):
        print(i, end=' ')
    print()


def make_iterable_to_chain():
    yield ['a', 'b', 'c']
    yield [1, 2, 3]


def run201_02():
    """
    chain.from_iterable
    :return:
    """
    for i in chain.from_iterable(make_iterable_to_chain()):
        print(i, end=' ')
    print()


def run201_03():
    """
    zip
    :return:
    """
    for i in zip([1, 2, 3], ['a', 'b', 'c']):
        print(i, end=' ')
    print()


def run201_04():
    """
    zip_longest
    :return:
    """
    for i in zip([1, 2, 3], ['a', 'b']):
        print(i, end=' ')
    print()

    for i in zip_longest([1, 2, 3], ['a', 'b']):
        print(i, end=' ')
    print()


def run201_05():
    """
    islice()
    :return:
    """
    print('Stop at 5:')
    for i in islice(range(100), 5):
        print(i, end=' ')
    print()

    print('Start at 5, Stop at 10:')
    for i in islice(range(100), 5, 10):
        print(i, end=' ')
    print()

    print('By tens to 100:')
    for i in islice(range(100), 0, 100, 10):
        print(i, end=' ')
    print()


def run201_06():
    """
    tee: repeat iterator
    :return:
    """
    r = islice(count(), 5)
    i1, i2 = tee(r)

    print('i1:', list(i1))
    print('i2:', list(i2))


def run201_07():
    """
    tee: value consumed
    :return:
    """
    r = islice(count(), 5)
    i1, i2 = tee(r)

    print('r: ', end=' ')
    for i in r:
        print(i, end=' ')
        if i > 1:
            break

    print()
    print('i1:', list(i1))
    print('i2:', list(i2))

