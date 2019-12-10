#!/usr/bin/env python
# encoding: utf-8

"""
@description: 自定义的random

@author: baoqiang
@time: 2019/12/6 7:54 下午
"""

import random
import time


def run307_01():
    print('Default initialization:\n')

    r1 = random.Random()
    r2 = random.Random()

    for i in range(3):
        print('{:04.3f} {:04.3f}'.format(r1.random(), r2.random()))

    print('\nSample seed:\n')

    ts = time.time()
    r1 = random.Random(ts)
    r2 = random.Random(ts)

    for i in range(3):
        print('{:04.3f} {:04.3f}'.format(r1.random(), r2.random()))


def run307_02():
    """
    system random
    """
    print('Default initialization:\n')

    r1 = random.SystemRandom()
    r2 = random.SystemRandom()

    for i in range(3):
        print('{:04.3f} {:04.3f}'.format(r1.random(), r2.random()))

    print('\nSample seed:\n')

    ts = time.time()
    r1 = random.SystemRandom(ts)
    r2 = random.SystemRandom(ts)

    for i in range(3):
        print('{:04.3f} {:04.3f}'.format(r1.random(), r2.random()))
