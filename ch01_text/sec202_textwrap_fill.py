#!/usr/bin/env python
# encoding: utf-8

"""
@description: 文本装饰-填充

@author: baoqiang
@time: 2019/11/26 1:03 下午
"""
import textwrap

from ch01_text.sec201_textwrap_sample import sample_text


def run202_01():
    """
    左对齐
    :return:
    """
    print(textwrap.fill(sample_text, width=50))
