#!/usr/bin/env python
# encoding: utf-8

"""
@description: 编译的正则表达式

@author: baoqiang
@time: 2019/11/26 6:35 下午
"""

import re


def run302_01():
    regexes = [
        re.compile(p) for p in ['this', 'that']
    ]

    text = 'Does this text match the pattern?'

    print('Text: {!r}\n'.format(text))

    for regex in regexes:
        print('Seeking "{}" ->'.format(regex.pattern), end=' ')

        if regex.search(text):
            print('match!')
        else:
            print('not match')
