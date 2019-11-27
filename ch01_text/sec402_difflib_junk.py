#!/usr/bin/env python
# encoding: utf-8

"""
@description: diff的时候过滤一些噪音数据

@author: baoqiang
@time: 2019/11/27 5:42 下午
"""

from difflib import SequenceMatcher


def run402_01():
    A = " abcd"
    B = "abcd abcd"

    def show_results(match):
        print('a       = {}'.format(match.a))
        print('b       = {}'.format(match.b))
        print('size    = {}'.format(match.size))

        i, j, k = match
        print('A[a:a+size] = {!r}'.format(A[i: i + k]))
        print('B[b:b+size] = {!r}'.format(B[j: j + k]))

    print('A = {!r}'.format(A))
    print('B = {!r}'.format(B))

    print('\nWithout junk detection:')
    s1 = SequenceMatcher(None, A, B)
    m1 = s1.find_longest_match(0, len(A), 0, len(B))
    show_results(m1)

    print('\nTreat spaces as junk:')
    s1 = SequenceMatcher(lambda x: x == " ", A, B)
    m1 = s1.find_longest_match(0, len(A), 0, len(B))
    show_results(m1)
