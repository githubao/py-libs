#!/usr/bin/env python
# encoding: utf-8

"""
@description: 正则匹配

@author: baoqiang
@time: 2019/11/26 6:31 下午
"""

import re


def run301_01():
    pat = 'this'
    text = 'Does this text match the pattern?'

    m = re.search(pat, text)

    s = m.start()
    e = m.end()

    print('Found "{}"\nin "{}"\n from {} to {} ("{}")'.format(
        m.re.pattern, m.string, s, e, text[s:e]
    ))
