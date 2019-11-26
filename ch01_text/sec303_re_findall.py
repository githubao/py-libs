#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/11/26 6:38 下午
"""

import re


def run303_01():
    text = 'abbaaabbbbaaaaa'
    pat = 'ab'

    for s in re.findall(pat, text):
        print('Found {!r}'.format(s))


def run303_02():
    """
    [start,end), 左闭右开
    :return:
    """
    text = 'abbaaabbbbaaaaa'
    pat = 'ab'

    for m in re.finditer(pat, text):
        s = m.start()
        e = m.end()

        print('Found {!r} at {:d}:{:d}'.format(
            text[s:e], s, e
        ))
