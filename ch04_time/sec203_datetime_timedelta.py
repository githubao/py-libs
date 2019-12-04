#!/usr/bin/env python
# encoding: utf-8

"""
@description: 时间差

@author: baoqiang
@time: 2019/12/4 2:16 下午
"""

from datetime import timedelta
import datetime


def run203_01():
    print('microseconds:', timedelta(microseconds=1))
    print('milliseconds:', timedelta(milliseconds=1))
    print('seconds:', timedelta(seconds=1))
    print('minutes:', timedelta(minutes=1))
    print('days:', timedelta(days=1))
    print('weeks:', timedelta(weeks=1))

    for delta in [
        timedelta(microseconds=1),
        timedelta(milliseconds=1),
        timedelta(seconds=1),
        timedelta(minutes=1),
        timedelta(days=1),
        timedelta(weeks=1),
    ]:
        print('{:15} = {:8} seconds'.format(
            str(delta), delta.total_seconds()
        ))


def run203_02():
    """
    date arithmetic
    :return:
    """
    today = datetime.date.today()
    print('Today:', today)

    one_day = datetime.timedelta(days=1)
    print('one day:', one_day)

    yesterday = today - one_day
    print('Yesterday:', yesterday)

    tomorrow = today + one_day
    print('Tomorrow:', tomorrow)

    print()
    print('tomorrow - yesterday', tomorrow - yesterday)
    print('yesterday - tomorrow', yesterday - tomorrow)


def run203_03():
    """
    timedelta arithmetic
    :return:
    """
    one_day = datetime.timedelta(days=1)

    print('1 day:', one_day)
    print('5 day:', one_day * 5)
    print('1.5 day:', one_day * 1.5)
    print('1/4 day:', one_day / 4)

    work_day = datetime.timedelta(hours=7)
    meeting_length = datetime.timedelta(hours=1)
    print('meeting per day:', work_day / meeting_length)


def run203_04():
    """
    time compare
    :return:
    """
    print('Times:')
    t1 = datetime.time(12, 55, 0)
    print('t1:', t1)
    t2 = datetime.time(13, 5, 0)
    print('t2:', t2)
    print('t1<t2:', t1 < t2)

    print('Dates:')
    d1 = datetime.date.today()
    print('d1:', d1)
    d2 = datetime.date.today() + datetime.timedelta(days=1)
    print('d2:', d2)
    print('d1<d2:', d1 < d2)
