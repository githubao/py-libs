#!/usr/bin/env python
# encoding: utf-8

"""
@description: 截断长文本，提供一个摘要

@author: baoqiang
@time: 2019/11/26 1:29 下午
"""
import textwrap

from ch01_text.sec201_textwrap_sample import sample_text


def run207_01():
    dedented_text = textwrap.dedent(sample_text)
    original = textwrap.fill(dedented_text, 50)
    print('Original: \n')
    print(original)

    shortened = textwrap.shorten(original, 100)
    shortened_wrapper = textwrap.fill(shortened, 50)

    print('\nshortened:\n')
    print(shortened_wrapper)
