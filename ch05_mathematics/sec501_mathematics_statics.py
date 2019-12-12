#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/12/12 1:18 下午
"""

import statistics
import subprocess


def run501_01():
    data = [1, 2, 2, 5, 10, 12]
    print('{:0.2f}'.format(statistics.mean(data)))
    print('{:0.2f}'.format(statistics.mode(data)))  # 众数
    print('{:0.2f}'.format(statistics.median(data)))  # average 3.5
    print('{:0.2f}'.format(statistics.median_low(data)))  # low 2
    print('{:0.2f}'.format(statistics.median_high(data)))  # high 5

    data = [10, 20, 30, 40]

    print('{:0.2f}'.format(statistics.median_grouped(data, interval=1)))
    print('{:0.2f}'.format(statistics.median_grouped(data, interval=2)))
    print('{:0.2f}'.format(statistics.median_grouped(data, interval=3)))


def get_line_lengths():
    cmd = 'wc -l ../[a-z]*/*.py'

    out = subprocess.check_output(cmd, shell=True).decode('utf-8')
    for line in out.splitlines():
        parts = line.split()
        if parts[1].strip().lower() == 'total':
            break

        nlines = int(parts[0].strip())
        if not nlines:
            continue

        yield nlines, parts[1].strip()


def run501_02():
    """
    pstdev: population variance 1/n
    stdev:  sample variance 1/(n-1), common use
    """
    data = get_line_lengths()

    lengths = [d[0] for d in data]
    sample = lengths[::2]

    print('Basic statistics:')
    print('count:{}'.format(len(lengths)))
    print('min:{}'.format(min(lengths)))
    print('max:{}'.format(max(lengths)))
    print('mean:{}'.format(statistics.mean(lengths)))

    print('Population variance:')
    print('pstdev:{}'.format(statistics.pstdev(lengths)))
    print('pvariance:{}'.format(statistics.pvariance(lengths)))

    print('Estimated variance for sample:')
    print('count:{}'.format(len(sample)))
    print('stddev:{}'.format(statistics.stdev(sample)))
    print('variance:{}'.format(statistics.variance(sample)))
