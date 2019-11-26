#!/usr/bin/env python
# encoding: utf-8

"""
@description: 首字母大写

@author: baoqiang
@time: 2019/11/25 10:03 下午
"""
import string


def run_01():
    s = 'The quick brown fox jumped over the lazy dog.'
    print(s)
    print(s.capitalize())
    print(string.capwords(s))

