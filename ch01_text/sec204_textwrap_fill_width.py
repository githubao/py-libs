#!/usr/bin/env python
# encoding: utf-8

"""
@description: 字符装饰-去除缩进+填充

@author: baoqiang
@time: 2019/11/26 1:14 下午
"""
import textwrap

from ch01_text.sec201_textwrap_sample import sample_text


def run204_01():
    """
    去除空格，并且左对齐，并且限制每行的宽度
    :return:
    """
    dedented_text = textwrap.dedent(sample_text).strip()
    for width in [45, 60]:
        print('{} Columns:\n'.format(width))
        print(textwrap.fill(dedented_text, width))
        print()
