#!/usr/bin/env python
# encoding: utf-8

"""
@description: with func decorators

@author: baoqiang
@time: 2019/12/3 7:52 下午
"""

import contextlib


def run402_01():
    class Context(contextlib.ContextDecorator):
        def __init__(self, how_used):
            self.how_used = how_used
            print('__init__({})'.format(how_used))

        def __enter__(self):
            print('__enter__({})'.format(self.how_used))
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('__exit__({})'.format(self.how_used))

    # call __init__ immediately
    @Context('as decorator')
    def func(msg):
        print(msg)

    print()
    with Context('as context manager'):
        print('Doing work in the Context')

    print()
    func('Doing work in the wrapped function')


@contextlib.contextmanager
def make_context():
    """
    context manager
    :return:
    """
    print('entering:')
    try:
        yield {}
    except RuntimeError as err:
        print('ERROR:', err)
    finally:
        print('exiting')


def run402_02():
    print('Normal:')
    with make_context() as value:
        print('inside with statement:', value)

    print('\nHandled err:')
    with make_context() as value:
        raise RuntimeError('show example of handling an err')

    print('\nUnhandled err:')
    with make_context() as value:
        raise ValueError('this exception is not handled')


def run402_03():
    """
    decorate a func
    :return:
    """

    @make_context()
    def normal():
        print('inside with statement:')

    @make_context()
    def throw_err(err):
        raise err

    print('Normal:')
    normal()

    print('\nHandled err:')
    throw_err(RuntimeError('show example of handling an err'))

    print('\nUnhandled err:')
    throw_err(ValueError('this exception is not handled'))
