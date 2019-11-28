#!/usr/bin/env python
# encoding: utf-8

"""
@description: 命名元组

@author: baoqiang
@time: 2019/11/28 1:05 下午
"""

from collections import namedtuple


def run205_01():
    bob = ('Bob', '30', 'male')
    print('Representation: ', bob)

    jane = ('Jane', '29', 'female')
    print('\nField by index: ', jane[0])

    print('\nFields by index:')
    for p in [bob, jane]:
        print('{} is a {} year old {}'.format(*p))


def run205_02():
    Person = namedtuple('Person', 'name age')

    bob = Person(name='Bob', age='30')
    print('\nRepresentation: ', bob)

    jane = Person(name='Jane', age='29')
    print('\nField by name: ', jane.name)

    print('\nFields by index:')
    for p in [bob, jane]:
        print('{} is a {} year old'.format(*p))


def run205_03():
    """
    immutable
    :return:
    """
    Person = namedtuple('Person', 'name age')

    pat = Person(name='Pat', age='12')
    print('\nRepresentation: ', pat)

    # Attribute Error
    # pat.age = 21


def run205_04():
    """
    dup or keywords
    :return:
    """
    try:
        Person = namedtuple('Person', 'name class age')
    except ValueError as e:
        print(e)

    try:
        Person = namedtuple('Person', 'name age age')
    except ValueError as e:
        print(e)


def run205_05():
    """
    can be renamed
    :return:
    """
    with_class = namedtuple('Person', 'name class age', rename=True)
    print(with_class._fields)

    two_ages = namedtuple('Person', 'name age age', rename=True)
    print(two_ages._fields)


def run205_06():
    """
    field & method
    :return:
    """
    Person = namedtuple('Person', 'name age')

    bob = Person(name='Bob', age='30')
    print('\nRepresentation: ', bob)

    print('Fields:', bob._fields)
    print('As Dictionary:', bob._asdict())

    bob2 = bob._replace(name='Robert')
    print('Bob2:', bob2)
    print('Same?:', bob is bob2)
