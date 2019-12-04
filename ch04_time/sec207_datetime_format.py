#!/usr/bin/env python
# encoding: utf-8

"""
@description: time format

@author: baoqiang
@time: 2019/12/4 2:44 下午
"""

import datetime


def run207_01():
    layout = '%a %b %d %H:%M:%S %Y'

    today = datetime.datetime.today()
    print('ISO:', today)

    s = today.strftime(layout)
    print('strftime:', s)

    d = datetime.datetime.strptime(s, layout)
    print('strptime:', d.strftime(layout))


def run207_02():
    """
    fmt in format func
    :return:
    """
    today = datetime.datetime.today()
    print('ISO:', today)

    print('format():{:%a %b %d %H:%M:%S %Y}'.format(today))


def run207_03():
    """
    %a: week_day abbr str
    %A: week_day str
    %w: week_num(0-6)
    %d: day
    %b: month_day abbr str
    %B: month_day str
    %m: month
    %y: year with 2 length
    %Y: year with 4 length
    %H: hour with 24 format
    %I: hour with 12 format
    %p: AM/PM
    %M: minutes
    %S: seconds
    %f: milliseconds
    %z: utf offset
    %Z: timezone name
    %j: day of the year
    %W: week of the year
    %c: datetime default format
    %x: date default format
    %X: time default format
    """


def run207_04():
    """
    beijing tz: CST
    astimezone(): time default format with timezone
    :return:
    """
    min6 = datetime.timezone(datetime.timedelta(hours=-6))
    plus6 = datetime.timezone(datetime.timedelta(hours=6))
    d = datetime.datetime.now(min6)

    print(min6, ':', d)
    print(datetime.timezone.utc, ':', d.astimezone(datetime.timezone.utc))
    print(plus6, ':', d.astimezone(plus6))

    d_system = d.astimezone()
    print(d_system.tzinfo, ':', d_system)
