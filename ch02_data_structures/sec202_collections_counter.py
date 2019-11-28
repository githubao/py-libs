#!/usr/bin/env python
# encoding: utf-8

"""
@description: counter

@author: baoqiang
@time: 2019/11/27 10:43 下午
"""

from collections import Counter


def run202_01():
    print(Counter(['a', 'b', 'c', 'a', 'b', 'b']))
    print(Counter({'a': 2, 'b': 3, 'c': 1}))
    print(Counter(a=2, b=3, c=1))


def run202_02():
    """
    counter update
    :return:
    """
    c = Counter()
    print('Initial: ', c)

    c.update('abcdaab')
    print('Sequence:', c)

    c.update({'a': 1, 'd': 5})
    print('Dict: ', c)


def run202_03():
    """
    get from dict
    :return:
    """
    c = Counter('abcdaab')

    for letter in 'abcde':
        print('{}: {}'.format(letter, c[letter]))


def run202_04():
    """
    elements()
    :return:
    """
    c = Counter('extremely')
    c['z'] = 0

    print(c)
    print(list(c.elements()))


def run202_05():
    """
    most common
    {:>7}: 右对齐，一共占用7位
    :return:
    """
    c = Counter()

    with open('/usr/share/dict/words', 'rt') as f:
        for line in f:
            c.update(line.rstrip().lower())

    print('Most common')
    for letter, count in c.most_common(3):
        print('{}: {:>7}'.format(letter, count))


def run202_06():
    """
    arithmetic
    :return:
    """
    c1 = Counter('abcabb')
    c2 = Counter('alphabet')

    print('C1: ', c1)
    print('C2: ', c2)

    print('\nCombined counts:')
    print(c1 + c2)

    print('\nSubtraction:')
    print(c1 - c2)

    print('\nInteraction (taking positive minimums):')
    print(c1 & c2)

    print('\nUnion (take maximums):')
    print(c1 | c2)
