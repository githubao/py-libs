#!/usr/bin/env python
# encoding: utf-8

"""
@description: 文本装饰-去除缩进

@author: baoqiang
@time: 2019/11/26 1:08 下午
"""
import textwrap

from ch01_text.sec201_textwrap_sample import sample_text


def run203_01():
    dedented_text = textwrap.dedent(sample_text)
    print('Dedented: ')
    print(dedented_text)
