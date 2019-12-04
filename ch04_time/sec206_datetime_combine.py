#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/12/4 2:36 下午
"""

import datetime


def run206_01():
    """
    now datetime
    :return:
    """
    print('now:', datetime.datetime.now())
    print('today:', datetime.datetime.today())
    print('utc now:', datetime.datetime.utcnow())

    FIELDS = [
        'year', 'month', 'day', 'hour',
        'minute', 'second', 'microsecond'
    ]

    d = datetime.datetime.now()
    for attr in FIELDS:
        print('{:15}: {}'.format(attr, getattr(d, attr)))


def run206_02():
    """
    combine datetime
    :return:
    """
    t = datetime.time(1, 2, 3)
    print('t:', t)

    d = datetime.date.today()
    print('d', d)

    dt = datetime.datetime.combine(d, t)
    print('dt:', dt)
