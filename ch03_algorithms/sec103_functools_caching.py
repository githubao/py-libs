#!/usr/bin/env python
# encoding: utf-8

"""
@description: lru_cache

@author: baoqiang
@time: 2019/12/1 5:01 下午
"""

import functools


@functools.lru_cache()
def expensive(a, b):
    print('expensive({}, {})'.format(a, b))
    return a * b


@functools.lru_cache(maxsize=2)
def expensive2(a, b):
    print('called expensive({}, {})'.format(a, b))
    return a * b


def run103_01():
    """
    misses: 调用次数
    CacheInfo(hits=4, misses=9, maxsize=128, currsize=9)
    :return:
    """
    max_size = 2

    print('First set of calls:')
    for i in range(max_size):
        for j in range(max_size):
            expensive(i, j)
    print(expensive.cache_info())

    print('Second set of calls:')
    for i in range(max_size + 1):
        for j in range(max_size + 1):
            expensive(i, j)
    print(expensive.cache_info())

    print('\nClearing cache:')
    expensive.cache_clear()
    print(expensive.cache_info())

    print('Third set of calls:')
    for i in range(max_size):
        for j in range(max_size):
            expensive(i, j)
    print(expensive.cache_info())


def make_call(a, b):
    print('({}, {})'.format(a, b), end=' ')
    pre_hits = expensive2.cache_info().hits
    expensive2(a, b)
    post_hits = expensive2.cache_info().hits
    if post_hits > pre_hits:
        print('cache hit')


def run103_02():
    """
    lru_cache maxsize
    :return:
    """
    print('Establish the cache')
    make_call(1, 2)
    make_call(2, 3)

    print('\nUse cached items')
    make_call(1, 2)
    make_call(2, 3)

    print('\nCompute a new value, triggering cache expiration')
    make_call(3, 4)

    print('\nCache still contains one old item')
    make_call(2, 3)

    print('\nOldest item needs to be recomputed')
    make_call(1, 2)


def run103_03():
    """
    lru_cache all key should be hashable
    :return:
    """
    make_call(1, 2)

    try:
        make_call([1], 3)
    except TypeError as e:
        print('ERROR: {}'.format(e))

    try:
        make_call(1, {'2': 'two'})
    except TypeError as e:
        print('ERROR: {}'.format(e))
