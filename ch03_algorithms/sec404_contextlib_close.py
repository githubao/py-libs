#!/usr/bin/env python
# encoding: utf-8

"""
@description: closing

@author: baoqiang
@time: 2019/12/3 8:01 下午
"""

import contextlib
import io
import sys


def run404_01():
    """
    closing
    :return:
    """

    class Door:
        def __init__(self):
            print('__init__()')
            self.status = 'open'

        def close(self):
            print('close()')
            self.status = 'closed'

    print('Normal Example:')
    with contextlib.closing(Door()) as door:
        print('inside with statement: ', door.status)
    print('outside with statement: ', door.status)

    print('\nError handling Example:')
    try:
        with contextlib.closing(Door()) as door:
            print('raise from inside with statement')
            raise RuntimeError('err msg')
    except Exception as err:
        print('handle err: ', err)


def run404_02():
    """
    ignore exceptions
    :return:
    """

    class NonFatalError(Exception):
        pass

    def non_idempotent_operation():
        raise NonFatalError('The operation failed because of existing state')

    try:
        print('trying non-idempotent operation')
        non_idempotent_operation()
        print('succeeded!')
    except NonFatalError:
        pass

    print('done')

    # contextlib ignore err
    with contextlib.suppress(NonFatalError):
        print('trying non-idempotent operation')
        non_idempotent_operation()
        print('succeeded!')
    print('done2')


def run404_03():
    """
    redirect stdout and stderr
    :return:
    """

    def misbehaving_function(a):
        sys.stdout.write('(stdout) A: {!r}\n'.format(a))
        sys.stderr.write('(stderr) A: {!r}\n'.format(a))

    capture = io.StringIO()
    with contextlib.redirect_stdout(capture), contextlib.redirect_stderr(capture):
        misbehaving_function(5)

    print(capture.getvalue())

