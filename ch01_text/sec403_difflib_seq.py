#!/usr/bin/env python
# encoding: utf-8

"""
@description: 比较序列

@author: baoqiang
@time: 2019/11/27 5:52 下午
"""

import difflib


def run403_01():
    s1 = [1, 2, 3, 5, 6, 4]
    s2 = [2, 3, 5, 4, 6, 1]

    print('Initial data:')
    print('s1: ', s1)
    print('s2: ', s2)
    print('s1 == s2:', s1 == s2)
    print()

    m = difflib.SequenceMatcher(None, s1, s2)

    for tag, i1, i2, j1, j2 in reversed(m.get_opcodes()):
        if tag == 'delete':
            print('Remove {} from positions [{}:{}]'.format(
                s1[i1:i2], i1, i2))
            print(' before = ', s1)
            del s1[i1:i2]

        elif tag == 'equal':
            print('s1[{}:{}] and s2[{}:{}] are the same'.format(
                i1, i2, j1, j2))

        elif tag == 'insert':
            print('Insert {} from s2[{}:{}] into s1 at {}'.format(
                s2[j1:j2], j1, j2, i1))
            print(' before = ', s1)
            s1[i1:i2] = s2[j1:j2]

        elif tag == 'replace':
            print('Replace {} from s1[{}:{}] with {} from s2[{}:{}]'.format(
                s1[i1:i2], i1, i2, s2[j1:j2], j1, j2))
            print(' before = ', s1)
            s1[i1:i2] = s2[j1:j2]

        print(' after = ', s1, end='\n')
        print()

    print('s1 == s2:', s1 == s2)
