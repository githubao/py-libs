#!/usr/bin/env python
# encoding: utf-8

"""
@description: # TODO
@author: xiaobao
Date: 2019-12-04 11:07:23
"""

import datetime
import time


def run201_01():
    t = datetime.time(1, 2, 3)
    print(t)
    print('hour:', t.hour)
    print('minute:', t.minute)
    print('second:', t.second)
    print('microsecond:', t.microsecond)
    print('tzinfo:', t.tzinfo)

    print('Earliest:', datetime.time.min)
    print('Latest:', datetime.time.max)
    print('Resolution:', datetime.time.resolution)


def run201_02():
    """
    datetime resolution
    :return:
    """
    for m in [1, 0, 0.1, 0.6]:
        try:
            print('{:02.1f}'.format(m),
                  datetime.time(0, 0, 0, microsecond=m))
        except TypeError as e:
            print('ERROR:', e)


def run201_03():
    """
    datetime today
    :return:
    """
    today = datetime.date.today()
    print(today)
    print('ctime:', today.ctime())

    tt = today.timetuple()
    print('tuple:')
    print('\ttm_year:', tt.tm_year)
    print('\ttm_mon:', tt.tm_mon)
    print('\ttm_mday:', tt.tm_mday)
    print('\ttm_hour:', tt.tm_hour)
    print('\ttm_min:', tt.tm_min)
    print('\ttm_sec:', tt.tm_sec)
    print('\ttm_wday:', tt.tm_wday)
    print('\ttm_yday:', tt.tm_yday)
    print('\ttm_isdst:', tt.tm_isdst)

    print('ordinal:', today.toordinal())
    print('Year:', today.year)
    print('Mon:', today.month)
    print('Day:', today.day)


def run201_04():
    """
    构造日期
    :return:
    """
    # o = 733114
    o = 1  # 0001-01-01
    print('o:', o)
    print('fromordinal(o):', datetime.date.fromordinal(o))

    t = time.time()
    print('t:', t)
    print('fromtimestamp(t):', datetime.date.fromtimestamp(t))

    print('Earliest:', datetime.date.min)
    print('Latest:', datetime.date.max)
    print('Resolution:', datetime.date.resolution)


def run201_05():
    """
    构造日期，from_literal
    :return:
    """
    d1 = datetime.date(2008, 3, 29)
    print('d1:', d1.ctime())

    d2 = d1.replace(year=2009)
    print('d2:', d2.ctime())
