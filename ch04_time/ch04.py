#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/12/3 9:04 下午
"""
from ch04_time.sec101_time_clock import run101_01, run101_02, run101_06, run101_05, run101_04, run101_03, run101_09, \
    run101_08, run101_07
from ch04_time.sec201_datetime_date import run201_01, run201_02, run201_03, run201_04, run201_05
from ch04_time.sec203_datetime_timedelta import run203_01, run203_02, run203_03, run203_04
from ch04_time.sec206_datetime_combine import run206_01, run206_02
from ch04_time.sec207_datetime_format import run207_01, run207_02, run207_04
from ch04_time.sec301_calendar import run301_01, run301_02, run301_03, run301_04


def run03():
    run301_01()
    run301_02()
    run301_03()
    run301_04()


def run02():
    run201_01()
    run201_02()
    run201_03()
    run201_04()
    run201_05()
    run203_01()
    run203_02()
    run203_03()
    run203_04()
    run206_01()
    run206_02()
    run207_01()
    run207_02()
    run207_04()


def run01():
    run101_01()
    run101_02()
    run101_03()
    run101_04()
    run101_05()
    run101_06()
    run101_07()
    run101_08()
    run101_09()


def run():
    run01()
    run02()
    run03()


if __name__ == '__main__':
    run()

