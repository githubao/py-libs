#!/usr/bin/env python
# encoding: utf-8

"""
@description: 悬挂缩进

@author: baoqiang
@time: 2019/11/26 1:26 下午
"""
import textwrap

from ch01_text.sec201_textwrap_sample import sample_text


def run206_01():
    """
    首行缩进样式与其他行不同
    :return:
    """
    dedented_text = textwrap.dedent(sample_text).strip()
    print(textwrap.fill(dedented_text,
                        initial_indent='',
                        subsequent_indent=' ' * 4,
                        width=50,
                        ))
