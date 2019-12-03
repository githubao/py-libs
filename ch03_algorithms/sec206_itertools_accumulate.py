#!/usr/bin/env python
# encoding: utf-8

"""
@description: 累计

@author: baoqiang
@time: 2019/12/2 8:13 下午
"""

from itertools import accumulate, product, chain, permutations, combinations, combinations_with_replacement
from pprint import pprint


def run206_01():
    """
    accumulate, 累计前面的值到后一个值
    :return:
    """
    print(list(accumulate(range(5))))
    print(list(accumulate('abcde')))


def custom_accumulate(a, b):
    print(a, b)
    return b + a + b


def run206_02():
    """
    custom_accumulate
    :return:
    """
    print(list(accumulate('abcde', custom_accumulate)))


def run206_03():
    """
    product, 笛卡尔积
    :return:
    """
    FACE_CARDS = ['T', 'J', 'Q', 'K', 'A']
    SUITS = ['H', 'D', 'C', 'S']

    DECK = list(product(chain(range(2, 10), FACE_CARDS), SUITS))

    for card in DECK:
        print('{:>2}{}'.format(*card), end=' ')
        if card[1] == SUITS[-1]:
            print()

    DECK2 = list(product(SUITS, chain(range(2, 10), FACE_CARDS)))

    for card in DECK2:
        print('{:>2}{}'.format(card[1], card[0]), end=' ')
        if card[1] == FACE_CARDS[-1]:
            print()


def run206_04():
    """
    product with repeat
    :return:
    """

    def show(iterable):
        for i, item in enumerate(iterable, 1):
            print(item, end=' ')
            if (i % 3) == 0:
                print()
        print()

    print('Repeat 2:')
    show(list(product(range(3), repeat=2)))

    print('Repeat 3:')
    show(list(product(range(3), repeat=3)))


def run206_05():
    """
    permutations: 排列
    :return:
    """

    def show(iterable):
        first = None
        for i, item in enumerate(iterable, 1):
            if first != item[0]:
                if first is not None:
                    print()
                first = item[0]
            print(''.join(item), end=' ')
        print()

    print('All permutations:\n')
    show(permutations('abcd'))

    print('\nPairs:\n')
    show(permutations('abcd', r=2))


def run206_06():
    """
    combinations: 组合
    :return:
    """

    def show(iterable):
        first = None
        for i, item in enumerate(iterable, 1):
            if first != item[0]:
                if first is not None:
                    print()
                first = item[0]
            print(''.join(item), end=' ')
        print()

    print('Unique pairs:\n')
    show(combinations('abcd', r=2))

    # with itself
    print('Unique pairs:\n')
    show(combinations_with_replacement('abcd', r=2))

