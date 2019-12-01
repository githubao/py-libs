#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/12/1 11:50 上午
"""

import functools


def my_func(a, b=2):
    """
    docstring for my_fun()
    :param a:
    :param b:
    :return:
    """
    print('call my_func with: ', (a, b))


def show_details(name, f, is_partial=False):
    """
    show details of a callable object.
    :param name:
    :param f:
    :param is_partial:
    :return:
    """
    print('{}:'.format(name))
    print('object:', f)
    if not is_partial:
        print('__name__:', f.__name__)
    else:
        print('func:', f.func)
        print('args:', f.args)
        print('keywords:', f.keywords)


def show_details2(name, f):
    """
    show details2 of a callable object.
    :param name:
    :param f:
    :return:
    """
    print('{}:'.format(name))
    print('object:', f)
    print('__name__:')

    try:
        print(f.__name__, end='')
    except AttributeError:
        print('(no __name__)')

    print('__doc__', repr(f.__doc__))
    print()


def run101_01():
    show_details('my_func', my_func)
    my_func('a', 3)
    print()

    p1 = functools.partial(my_func, b=4)
    show_details('partial with named default', p1, True)
    p1('passing a')
    p1('override b', b=5)
    print()

    p2 = functools.partial(my_func, 'default a', b=99)
    show_details('partial with defaults', p2, True)
    p2()
    p2(b='override b')
    print()

    print('Insufficient args:')
    # p1()


def run101_02():
    """
    partial update __doc__
    :return:
    """
    show_details2('my_func', my_func)

    p1 = functools.partial(my_func, b=4)
    show_details2('raw wrapper', p1)

    print('Updating wrapper:')
    print('assign:', functools.WRAPPER_ASSIGNMENTS)
    print('update:', functools.WRAPPER_UPDATES)
    print()

    functools.update_wrapper(p1, my_func)
    show_details2('update wrapper', p1)


class MyClass:
    """
    demonstration class for functools
    """

    def __call__(self, e, f=6):
        """
        docstring for MyClass.__call__
        :return:
        """
        print('called object with:', self, e, f)


def run101_03():
    """
    partial instance
    :return:
    """
    o = MyClass()
    show_details2('instance', o)
    o('e goes here')
    print()

    p = functools.partial(o, e='default for e', f=8)
    functools.update_wrapper(p, o)
    show_details2('instance wrapper', p)
    p()


def standalone(self, a=1, b=2):
    """standalone function"""
    print('call standalone with:', (self, a, b))
    if self is not None:
        print('self.attr=', self.attr)


class MyClass2:
    """Demonstration class for functools"""

    def __init__(self):
        self.attr = 'instance attribute'

    method1 = functools.partialmethod(standalone)
    method2 = functools.partial(standalone)


def run101_04():
    """
    partial method
    :return:
    """
    o = MyClass2()
    print('standalone')
    standalone(None)
    print()

    print('method as partial_method')
    o.method1()
    print()

    print('method as partial')
    try:
        o.method2(o)  # pass
        o.method2()  # type err
    except TypeError as err:
        print('Error: {}'.format(err))


def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print('decorated:', (a, b))
        print(' ', end=' ')
        return f(a, b=b)

    return decorated


@simple_decorator
def decorated_myfunc(a, b):
    my_func(a, b)
    return


def run101_05():
    """decorator"""
    show_details2('my_func', my_func)
    my_func('unwrapped, default b')
    my_func('unwrapped, passing b', 3)
    print()

    wrapped_myfunc = simple_decorator(my_func)
    show_details2('wrapped_myfunc', wrapped_myfunc)
    wrapped_myfunc()
    wrapped_myfunc('args to wrapped', 4)

    show_details2('decorated_myfunc', decorated_myfunc)
    decorated_myfunc()
    decorated_myfunc('args to decorated', 4)


