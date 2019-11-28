#!/usr/bin/env python
# encoding: utf-8

"""
@description: deque

@author: baoqiang
@time: 2019/11/28 11:33 上午
"""

from collections import deque
import threading
import time
import random


def run204_01():
    d = deque('abcdefg')
    print('Deque: ', d)
    print('Length: ', len(d))
    print('Left end: ', d[0])
    print('Right end: ', d[-1])

    d.remove('c')
    print('remove(c):', d)


def run204_02():
    """
    populating
    :return:
    """
    d1 = deque()
    d1.extend('abcdefg')
    print('extend: ', d1)
    d1.append('h')
    print('append: ', d1)

    d2 = deque()
    d2.extendleft(range(6))
    print('extendleft: ', d2)
    d2.appendleft(6)
    print('appendleft: ', d2)


def run204_03():
    """
    pop
    :return:
    """
    print('From the right:')
    d = deque('abcdefg')

    while True:
        try:
            print(d.pop(), end='')
        except IndexError:
            break
    print()

    print('\nFrom the left:')
    d = deque(range(6))
    while True:
        try:
            print(d.popleft(), end='')
        except IndexError:
            break
    print()


def run204_04():
    """
    deque is thread safe
    :return:
    """
    candle = deque(range(5))

    def burn(direction, next_source):
        while True:
            try:
                next_ = next_source()
            except IndexError:
                break
            else:
                print('{:>8}: {}'.format(direction, next_))
                time.sleep(0.1)

        print('{:>8} done'.format(direction))

    left = threading.Thread(target=burn, args=('Left', candle.popleft))
    right = threading.Thread(target=burn, args=('Right', candle.pop))

    left.start()
    right.start()

    left.join()
    right.join()


def run204_05():
    """
    队列旋转
    :return:
    """
    d = deque(range(10))
    print('Normal: ', d)

    d = deque(range(10))
    d.rotate(2)
    print('Right rotation: ', d)

    d = deque(range(10))
    d.rotate(-2)
    print('Left rotation: ', d)


def run204_06():
    """
    限制队列长度
    :return:
    """

    random.seed(1)

    d1 = deque(maxlen=3)
    d2 = deque(maxlen=3)

    for i in range(5):
        n = random.randint(0, 100)
        d1.append(n)
        d2.appendleft(n)

        print('D1: ', d1)
        print('D2: ', d2)
