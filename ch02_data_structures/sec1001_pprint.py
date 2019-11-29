#!/usr/bin/env python
# encoding: utf-8

"""
@description: pprint, 美观打印

@author: baoqiang
@time: 2019/11/29 4:11 下午
"""

from pprint import pprint, pformat
import logging

data = [
    (1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
    (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
         'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}),
    (3, ['m', 'n']),
    (4, ['o', 'p', 'q']),
    (5, ['r', 's', 't''u', 'v', 'x', 'y', 'z']),
]


def run1001_01():
    print('PRINT:')
    print(data)
    print()
    print('PPRINT:')
    pprint(data)


def run1001_02():
    """
    pprint to stream
    :return:
    """

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)-8s %(message)s'),

    formatted = pformat(data)

    for line in formatted.splitlines():
        logging.debug(line.rstrip())


def run1001_03():
    """
    pprint can use __repr__ implemented by PrettyPrinter class
    :return:
    """

    class node:
        def __init__(self, name, contents=[]):
            self.name = name
            self.contents = contents[:]

        def __repr__(self):
            return (
                    'node(' + repr(self.name) + ', ' +
                    repr(self.contents) + ')'
            )

    tree = [
        node('node-1'),
        node('node-2', [node('node-2-1')]),
        node('node-3', [node('node-3-1')]),
    ]

    print(tree)
    pprint(tree)


def run1001_04():
    """
    recursive
    ['a', 'b', 1, 2, <Recursion on list with id=4504684256>]
    :return:
    """
    local_data = ['a', 'b', 1, 2]
    local_data.append(local_data)
    print('id(local_data) =>', id(local_data))
    pprint(local_data)


def run1001_05():
    """
    depth control
    :return:
    """
    pprint(data, depth=1)
    pprint(data, depth=2)


def run1001_06():
    """
    width control
    :return:
    """
    for width in [80, 5]:
        print('WIDTH:', width)
        pprint(data, width=width)
        print()


def run1001_07():
    """
    compact control
    :return:
    """
    print('DEFAULT:')
    pprint(data, compact=False)
    print('\nCOMPACT:')
    pprint(data, compact=True)
