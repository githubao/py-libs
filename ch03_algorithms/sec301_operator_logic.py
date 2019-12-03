#!/usr/bin/env python
# encoding: utf-8

"""
@description: 逻辑运算符

@author: baoqiang
@time: 2019/12/3 4:46 下午
"""

from operator import abs, neg, pos
from operator import add, floordiv, mod, mul, pow, sub, truediv
from operator import and_, invert, lshift, or_, rshift, xor
from operator import lt, le, eq, ne, ge, gt
from operator import concat, contains, countOf, indexOf
from operator import getitem, setitem, delitem
from operator import iadd, iconcat
from operator import attrgetter, itemgetter


def run301_01():
    """
    logic ops
    :return:
    """
    a = -1
    b = 5.0

    for expr in ['not_(a)', 'truth(a)', 'is_(a,b)', 'is_not(a,b)']:
        print('{}: {}'.format(expr, eval(expr)))


def run301_02():
    """
    comparison ops
    :return:
    """
    a = -1
    b = 5

    for func in (lt, le, eq, ne, ge, gt):
        print('{}(a,b): {}'.format(func.__name__, func(a, b)))


def run301_03():
    """
    arithmetic ops
    :return:
    """
    a = -1
    b = 5.0
    c = 2
    d = 6

    print('a =', a)
    print('b =', b)
    print('c =', c)
    print('d =', d)

    print('\nPositive/Negative:')
    print('abs(a):', abs(a))
    print('neg(a):', neg(a))
    print('neg(b):', neg(b))
    print('pos(a):', pos(a))
    print('pos(b):', pos(b))

    print('\nArithmetic:')
    print('add(a, b)     :', add(a, b))
    print('floordiv(a, b):', floordiv(a, b))  # for py2
    print('floordiv(d, c):', floordiv(d, c))  # for py2
    print('mod(a, b)     :', mod(a, b))
    print('mul(a, b)     :', mul(a, b))
    print('pow(c, d)     :', pow(c, d))
    print('sub(b, a)     :', sub(b, a))
    print('truediv(a, b) :', truediv(a, b))
    print('truediv(d, c) :', truediv(d, c))

    print('\nBitwise:')
    print('and_(c, d)  :', and_(c, d))
    print('invert(c)   :', invert(c))  # ~c
    print('lshift(c, d):', lshift(c, d))  # c << d
    print('or_(c, d)   :', or_(c, d))
    print('rshift(d, c):', rshift(d, c))  # d >> c
    print('xor(c, d)   :', xor(c, d))  # 不同得1 ^


def run301_04():
    """
    sequence ops
    :return:
    """
    a = [1, 2, 3]
    b = ['a', 'b', 'c']

    print('a=', a)
    print('b=', b)

    print('Constructive:')
    print('concat(a,b): ', concat(a, b))

    print('\nSearching:')
    print('contains(a,1):', contains(a, 1))
    print('contains(b,"d"):', contains(b, 'd'))
    print('countOf(a,1):', countOf(a, 1))
    print('countOf(b,"d"):', countOf(b, 'd'))
    print('indexOf(a,1):', indexOf(a, 1))
    # print('indexOf(a,5):', indexOf(a, 5)) # ValueError

    print('\nAccess Items:')
    print('getitem(b,1):', getitem(b, 1))
    print('getitem(b,slice(1,3)):', getitem(b, slice(1, 3)))
    print('setitem(b,1,"d"):', setitem(b, 1, 'd'))
    print(b)
    print('setitem(a,slice(1,3),[4,5]):', setitem(a, slice(1, 3), [4, 5]))
    print(a)

    print('\nDestructive:')
    print('delitem(b,1)', delitem(b, 1))
    print(b)
    print('delitem(a,slice(1,3))', delitem(b, slice(1, 3)))
    print(a)


def run301_05():
    """
    inplace ops
    :return:
    """
    a = -1
    b = 5.0
    c = [1, 2, 3]
    d = ['a', 'b', 'c']

    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)
    print()

    a = iadd(a, b)
    print('iadd(a,b):', a)
    print()

    c = iconcat(c, d)
    print('iconcat(c,d)', c)


class MyObj:
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)

    def __str__(self):
        return repr(self)

    def __lt__(self, other):
        print('Testing: {} < {}'.format(self, other))
        return self.arg < other.arg

    def __add__(self, other):
        print('Adding: {} + {}'.format(self, other))
        return MyObj(self.arg + other.arg)


def run301_06():
    """
    attr getter ops
    :return:
    """
    l = [MyObj(i) for i in range(5)]
    print('objs:', l)

    g = attrgetter('arg')
    vals = [g(i) for i in l]
    print('arg values:', vals)

    l.reverse()
    print('reversed:', l)
    print('sorted:', sorted(l, key=g))


def run301_07():
    """
    item get ops
    :return:
    """
    l = [dict(val=-1 * i) for i in range(5)]
    print('Dictionaries:')

    print('original:', l)
    g = itemgetter('val')
    vals = [g(i) for i in l]
    print('values:', vals)
    print('sorted:', sorted(l, key=g))
    print()

    l = [(i, -2 * i) for i in range(5)]
    print('\nTuples:')

    print('original:', l)
    g = itemgetter(1)
    vals = [g(i) for i in l]
    print('values:', vals)
    print('sorted:', sorted(l, key=g))


def run301_08():
    """
    custom objs
    :return:
    """
    a = MyObj(1)
    b = MyObj(2)

    print('Comparison:')
    print(lt(a, b))

    print('Arithmetic:')
    print(add(a, b))
