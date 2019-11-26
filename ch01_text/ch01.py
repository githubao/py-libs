#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/11/25 10:04 下午
"""

from ch01_text.sec101_string_capwords import run101_01
from ch01_text.sec102_string_template import run102_01, run102_02
from ch01_text.sec103_string_template_advanced import run103_01, run103_02, run103_03
from ch01_text.sec105_string_constants import run105_01
from ch01_text.sec202_textwrap_fill import run202_01
from ch01_text.sec203_textwrap_dedent import run203_01
from ch01_text.sec204_textwrap_fill_width import run204_01
from ch01_text.sec205_textwrap_indent import run205_01, run205_02
from ch01_text.sec206_textwrap_hanging_indent import run206_01
from ch01_text.sec207_textwrap_shorten import run207_01


def run2():
    run202_01()
    run203_01()
    run204_01()
    run205_01()
    run205_02()
    run206_01()
    run207_01()


def run1():
    run101_01()
    run102_01()
    run102_02()
    run103_01()
    run103_02()
    run103_03()
    run105_01()


def run():
    # run1()
    run2()


if __name__ == '__main__':
    run()
