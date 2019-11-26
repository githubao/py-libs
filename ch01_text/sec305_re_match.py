#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/11/26 9:57 下午
"""
import re


def run305_01():
    text = 'This is some text -- with punctuation.'
    pat = 'is'

    print('Text     :', text)
    print('Pattern:', pat)

    m = re.match(pat, text)
    print('Match    :', m)
    s = re.search(pat, text)
    print('Search   :', s)


def run305_02():
    """
    full match
    :return:
    """
    text = 'This is some text -- with punctuation.'
    pat = 'is'

    print('Text     :', text)
    print('Pattern:', pat)

    m = re.fullmatch(pat, text)
    print('Full Match :', m)
    s = re.search(pat, text)
    print('Search   :', s)


def run305_03():
    """
    search substring
    :return:
    """
    text = 'This is some text -- with punctuation.'
    pat = re.compile(r'\b\w*is\w*\b')

    print('Text     :', text)
    print()

    pos = 0

    while True:
        m = pat.search(text, pos)
        if not m:
            break

        s = m.start()
        e = m.end()

        print(' {:>2d} : {:>2d} = "{}"'.format(
            s, e - 1, text[s:e]
        ))

        pos = e
