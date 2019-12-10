#!/usr/bin/env python
# encoding: utf-8

"""
@description: random

@author: baoqiang
@time: 2019/12/6 7:27 下午
"""
import os
import random
import pickle


def run301_01():
    for i in range(5):
        print('{:04.3f}'.format(random.random()), end=' ')

    print()
    for i in range(5):
        print('{:04.3f}'.format(random.uniform(1, 100)), end=' ')


def run301_02():
    """
    seeding
    """
    random.seed(1)

    for i in range(5):
        print('{:04.3f}'.format(random.random()), end=' ')


def run301_03():
    """
    set stats
    """
    filename = '/tmp/stats.dat'

    if os.path.exists(filename):
        print('Found state.dat, initializing random module')
        with open(filename, 'rb') as f:
            state = pickle.load(f)
        random.setstate(state)
    else:
        print('no state.dat, seeding')
        random.seed(1)

    for i in range(3):
        print('{:04.3f}'.format(random.random()), end=' ')
    print()

    with open(filename, 'wb') as f:
        pickle.dump(random.getstate(), f)

    print('\nAfter saving state:')
    for i in range(3):
        print('{:04.3f}'.format(random.random()), end=' ')
    print()


def run301_04():
    print('[1, 100]:', end=' ')
    for i in range(3):
        print('{}'.format(random.randint(1, 100)), end=' ')
    print()

    print('\n[-5, 5]:', end=' ')
    for i in range(3):
        print('{}'.format(random.randint(-5, 5)), end=' ')
    print()

    for i in range(3):
        print('{}'.format(random.randrange(0, 101, 5)), end=' ')
    print()
