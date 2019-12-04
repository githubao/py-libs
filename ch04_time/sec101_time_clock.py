#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/12/3 9:05 下午
"""
import hashlib
import os
import textwrap
import time


def run101_01():
    """
    different time implements
    :return:
    """
    available_clocks = [
        ('monotonic', time.monotonic),
        ('perf_counter', time.perf_counter),
        ('process_time', time.process_time),
        ('time', time.time),
    ]

    for clock_name, func in available_clocks:
        print(textwrap.dedent("""\
        {name}:
            adjustable: {info.adjustable}
            implementation: {info.implementation}
            monotonic: {info.monotonic} 
            resolution: {info.resolution}
            current: {current}
        """).format(
            name=clock_name,
            info=time.get_clock_info(clock_name),
            current=func(),
        ))


def run101_02():
    """
    time funcs
    :return:
    """
    print('The time is:', time.time())
    print('The ctime is:', time.ctime())
    later = time.time() + 15
    print('15 seconds later:', time.ctime(later))


def run101_03():
    """
    monotonic clock
    :return:
    """
    start = time.monotonic()
    time.sleep(0.1)
    end = time.monotonic()

    print('start: {:>9.2f}'.format(start))
    print('end: {:>9.2f}'.format(end))
    print('span: {:>9.2f}'.format(end - start))


def run101_04():
    """
    processor clock
    :return:
    """
    data = open(__file__, 'rb').read()

    for i in range(5):
        h = hashlib.sha1()
        print(time.ctime(), ': {:0.3f} {:0.3f}'.format(
            time.time(), time.process_time()
        ))

        for _ in range(300000):
            h.update(data)
        cksum = h.digest()
        print(cksum)


def run101_05():
    """
    processor clock does not add when sleeping
    :return:
    """
    template = '{} - {:0.2f} - {:0.2f}'
    print(template.format(
        time.ctime(), time.time(), time.process_time()
    ))

    for i in range(3, 0, -1):
        print('sleeping:', i)
        time.sleep(i)

        print(template.format(
            time.ctime(), time.time(), time.process_time()
        ))


def run101_06():
    """
    monotonic clock
    :return:
    """
    data = open(__file__, 'rb').read()

    loop_start = time.perf_counter()

    for i in range(5):
        iter_start = time.perf_counter()

        h = hashlib.sha1()
        print(time.ctime(), ': {:0.3f} {:0.3f}'.format(
            time.time(), time.process_time()
        ))

        for _ in range(300000):
            h.update(data)
        cksum = h.digest()

        now = time.perf_counter()
        loop_elapsed = now - loop_start
        iter_elapsed = now - iter_start

        print(time.ctime(), ': {:0.3f} {:0.3f}'.format(
            iter_elapsed, loop_elapsed
        ))


def show_struct(s):
    print('tm_year:', s.tm_year)
    print('tm_mon:', s.tm_mon)
    print('tm_mday:', s.tm_mday)
    print('tm_hour:', s.tm_hour)
    print('tm_min:', s.tm_min)
    print('tm_sec:', s.tm_sec)
    print('tm_wday:', s.tm_wday)  # !!! 星期二，值是1 !!!
    print('tm_yday:', s.tm_yday)
    print('tm_isdst:', s.tm_isdst) # Daylight Saving Time flag


def run101_07():
    """
    struct_time
    :return:
    """
    print('gmtime:')
    show_struct(time.gmtime())  # 格林尼治时间
    print(time.time())

    print('\nlocaltime:')
    show_struct(time.localtime())
    print('\nmktime:', time.mktime(time.localtime()))


def show_zone_info():
    print('TZ:', os.environ.get('TZ', '(not set)'))
    print('tzname', time.tzname)
    print('Zone: {} ({})'.format(time.timezone, (time.timezone / 3600)))
    print('DST:', time.daylight)
    print('Time:', time.ctime())
    print()


def run101_08():
    """
    monotonic clock
    :return:
    """
    print('Default:')
    show_zone_info()

    ZONES = ['GMT', 'Europe/Amsterdam']

    for zone in ZONES:
        os.environ['TZ'] = zone
        time.tzset()

        print(zone, ":")
        show_zone_info()


def run101_09():
    """
    ctime(ts) return str
    strptime(str, fmt) return time
    mktime(time) return ts

    time() return ts
    localtime() return time
    strftime(fmt, time) return str

    :return:
    """
    now = time.ctime(time.time())
    print('Now:', now)

    parsed = time.strptime(now)
    print('\nParsed:')
    show_struct(parsed)

    print('\nFormatted:', time.strftime('%a %b %d %H:%M:%S %Y', parsed))
