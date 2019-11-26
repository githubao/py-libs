#!/usr/bin/env python
# encoding: utf-8

"""
@description: 文本装饰-缩进

@author: baoqiang
@time: 2019/11/26 1:19 下午
"""
import textwrap

from ch01_text.sec201_textwrap_sample import sample_text


def run205_01():
    dedented_text = textwrap.dedent(sample_text)
    wrapped = textwrap.fill(dedented_text, 50)
    wrapped += "\n\nSecond paragraph after a blank line."
    final = textwrap.indent(wrapped, "> ")

    print('Quoted block: \n')
    print(final)


def should_indent(line):
    """
    NOTICE: "{str!s} {str!r} {str!a}".format(str="π")
    分别表示调用str的str,repr,ascii方法
    :param line:
    :return:
    """
    print('Intent {!r}?'.format(line))
    return len(line.strip()) % 2 == 0


def run205_02():
    """
    缩进，添加predict
    :return:
    """
    dedented_text = textwrap.dedent(sample_text)
    wrapped = textwrap.fill(dedented_text, 50)
    final = textwrap.indent(wrapped, "EVEN ", predicate=should_indent)

    print('Quoted block: \n')
    print(final)
