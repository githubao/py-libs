#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/12/3 5:28 下午
"""


def run401_01():
    """
    with statement
    :return:
    """
    with open('/tmp/pymotw.txt', 'wt') as fw:
        fw.write('contents go here')


def run401_02():
    """
    custom with statement
    init before enter
    :return:
    """

    class Context:
        def __init__(self):
            print('__init__()')

        def __enter__(self):
            print('__enter__()')
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            # print(exc_type, exc_val, exc_tb)
            print('__exit__()')

    with Context():
        print('do something')


def run401_03():
    """
    multi with
    :return:
    """

    class WithContext:
        def __init__(self, context):
            print('WithContext.__init__({})'.format(context))

        def do_something(self):
            print('WithContext.do_something()')
            return self

        def __del__(self):
            print('WithContext.__del__()')

    class Context:
        def __init__(self):
            print('Context.__init__()')

        def __enter__(self):
            print('Context.__enter__()')
            return WithContext(self)

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('Context.__exit__()')

    with Context() as c:
        c.do_something()


def run401_04():
    """
    __exit__ args
    :return:
    """

    class Context:
        def __init__(self, handle_err):
            print('__init__({})'.format(handle_err))
            self.handle_err = handle_err

        def __enter__(self):
            print('__enter__()')
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('__exit__()')
            print('exc_type:', exc_type)
            print('exc_val:', exc_val)
            print('exc_tb:', exc_tb)

            return self.handle_err

    with Context(True):
        raise RuntimeError('err message handled')

    print()

    with Context(False):
        raise RuntimeError('err message propagated')
