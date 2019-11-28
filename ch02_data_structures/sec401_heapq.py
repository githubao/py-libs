#!/usr/bin/env python
# encoding: utf-8

"""
@description: min-heap sort algorithm

@author: baoqiang
@time: 2019/11/28 6:10 下午
"""

import heapq
import math
import random
from io import StringIO

data = [19, 9, 4, 10, 11]


def show_tree(tree, total_width=36, fill=' '):
    sf = StringIO()
    last_row = -1

    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0

        if row != last_row:
            sf.write('\n')

        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        sf.write(str(n).center(col_width, fill))

        last_row = row

    print(sf.getvalue())
    print('-' * total_width)
    print()


def run401_01():
    heap = []
    print('random:', data)
    print()

    for n in data:
        print('add {:>3}:'.format(n))
        heapq.heappush(heap, n)
        show_tree(heap)

    print(heap)


def run401_02():
    """
    heapify
    :return:
    """
    print('random:', data)
    heapq.heapify(data)
    print('heapified: ')
    show_tree(data)


def run401_03():
    """
    heap pop
    :return:
    """
    print('random:', data)
    heapq.heapify(data)
    # print(data)
    print('heapified: ')
    show_tree(data)

    for i in range(2):
        smallest = heapq.heappop(data)
        print('pop {:>3}'.format(smallest))
        # print(data)
        show_tree(data)


def run401_04():
    """
    heap replace: use new replace the smallest
    :return:
    """
    heapq.heapify(data)
    print('start:')
    show_tree(data)

    for n in [0, 13]:
        smallest = heapq.heapreplace(data, n)
        print('replace {:>2} with {:2}'.format(smallest, n))
        show_tree(data)


def run401_05():
    """
    heap nlargest
    :return:
    """
    print('all: ', data)
    print('3 largest: ', heapq.nlargest(3, data))
    print('from sort: ', list(reversed(sorted(data)[-3:])))
    print('3 smallest: ', heapq.nsmallest(3, data))
    print('from sort: ', sorted(data)[:3])


def run401_06():
    """
    heap merge
    :return:
    """

    random.seed(2016)
    datas = []
    for i in range(4):
        new_data = list(random.sample(range(1, 101), 5))
        new_data.sort()
        datas.append(new_data)

    for i, d in enumerate(datas):
        print('{}: {}'.format(i, d))

    print('\nMerged:')
    for i in heapq.merge(*datas):
        print(i, end=' ')
    print()
