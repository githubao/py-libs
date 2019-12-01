#!/usr/bin/env python
# encoding: utf-8

"""
@description: single dispatch

@author: baoqiang
@time: 2019/12/1 5:31 下午
"""

import functools


@functools.singledispatch
def my_func(arg):
    print('default myfunc({!r})'.format(arg))


@my_func.register(int)
def my_func_int(arg):
    print('myfunc_int({})'.format(arg))


@my_func.register(list)
def my_func_list(arg):
    print('myfunc_list()')
    for item in arg:
        print(' {}'.format(item))


def run105_01():
    my_func('string argument')
    my_func(1)
    my_func(2.3)
    my_func(['a', 'b', 'c'])


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


class E(C, D):
    pass


@functools.singledispatch
def myfunc2(arg):
    print('default myfunc2({})'.format(arg.__class__.__name__))


@myfunc2.register(A)
def myfunc2_A(arg):
    print('default myfunc2_A({})'.format(arg.__class__.__name__))


@myfunc2.register(B)
def myfunc2_B(arg):
    print('default myfunc2_B({})'.format(arg.__class__.__name__))


@myfunc2.register(C)
def myfunc2_C(arg):
    print('default myfunc2_C({})'.format(arg.__class__.__name__))


def run105_02():
    myfunc2(A())
    myfunc2(B())
    myfunc2(C())
    myfunc2(D())
    myfunc2(E())
