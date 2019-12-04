#!/usr/bin/env python
# encoding: utf-8

"""
@description: calendar

@author: baoqiang
@time: 2019/12/4 3:00 下午
"""

import calendar
from pprint import pprint


def run301_01():
    c = calendar.TextCalendar(calendar.SUNDAY)
    c.prmonth(2019, 12)


def run301_02():
    cal = calendar.Calendar(calendar.SUNDAY)

    # 3个月一行，组织数据
    cal_data = cal.yeardays2calendar(2019, 3)
    print('len(cal_data):', len(cal_data))

    top_months = cal_data[0]
    print('len(top_months):', len(top_months))

    first_month = top_months[0]
    print('len(first_month):', len(first_month))

    print('first month:')
    pprint(first_month, width=65)

    # another format impl
    # 可选参数 w,l和c 分别表示日期列数，周的行数，和月之间的间隔
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print(cal.formatyear(2019, 2, 1, 1, 3))
    print(cal.formatyear(2019))


def run301_03():
    """
    locales
    :return:
    """
    cal = calendar.LocaleTextCalendar(locale='en_US')
    cal.prmonth(2019, 12)
    print()

    cal = calendar.LocaleTextCalendar(locale='zh_CN')
    cal.prmonth(2019, 12)


def run301_04():
    """
    calender cal
    :return:
    """
    c = calendar.monthcalendar(2019, 12)
    pprint(c)

    year = 2019

    for month in range(1, 13):
        c = calendar.monthcalendar(year, month)
        one = c[0]
        two = c[1]
        three = c[2]

        if one[calendar.THURSDAY]:
            meeting_date = two[calendar.THURSDAY]
        else:
            meeting_date = three[calendar.THURSDAY]

        print('{:>3}: {:>2}'.format(calendar.month_abbr[month], meeting_date))
