#!/usr/bin/env python
# encoding: utf-8

"""
@description: 弱引用

@author: baoqiang
@time: 2019/11/29 11:42 上午
"""
import gc
import weakref
from pprint import pprint


class ExpensiveObject:
    def __del__(self):
        print('(Deleting {})'.format(self))

    def on_finalize(self):
        print('do_finalize')


def run801_01():
    obj = ExpensiveObject()
    r = weakref.ref(obj)

    print('obj:', obj)
    print('ref:', r)
    print('r():', r())

    print('deleting obj')
    del obj
    print('r()', r())


def callback(ref):
    print('callback({!r})'.format(ref))


def run801_02():
    """
    在对象删除的时候指定一个callback函数
    :return:
    """
    obj = ExpensiveObject()
    r = weakref.ref(obj, callback)

    print('obj:', obj)
    print('ref:', r)
    print('r():', r())

    print('deleting obj')
    del obj
    print('r()', r())


def on_finalize(*args):
    print('on_finalize({!r})'.format(args))


def run801_03():
    """
    对象删除的时候调用finalize
    :return:
    """
    obj = ExpensiveObject()
    f = weakref.finalize(obj, on_finalize, 'extra argument')
    # at exit 的时候是否调用on_finalize函数
    f.atexit = True


def run801_04():
    """
    对象删除的时候调用finalize，传入一个弱引用即使被del也可以保证该对象不被回收
    :return:
    """
    obj = ExpensiveObject()
    obj_id = id(obj)

    f = weakref.finalize(obj, on_finalize, obj)
    f.atexit = False
    # f.atexit = True

    del obj

    for o in gc.get_objects():
        if id(o) == obj_id:
            print('found uncollected object in gc')


def run801_05():
    """
    传入对象的一个函数，也可以保证对象不被回收
    :return:
    """
    obj = ExpensiveObject()
    obj_id = id(obj)

    f = weakref.finalize(obj, obj.on_finalize)
    f.atexit = False

    del obj

    for o in gc.get_objects():
        if id(o) == obj_id:
            print('found uncollected object in gc')


class ExpensiveObject2:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('(Deleting {})'.format(self))

    def __repr__(self):
        return 'ExpensiveObject2({})'.format(self.name)


def run801_06():
    """
    弱引用持有的代理
    :return:
    """
    obj = ExpensiveObject2('My Object')

    r = weakref.ref(obj)
    p = weakref.proxy(obj)

    print('via obj:', obj.name)
    print('via ref:', r().name)
    print('via proxy:', p.name)

    del obj

    # ReferenceError
    # print('via proxy;', p.name)


def demo(cache_factory):
    gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

    all_refs = {}

    print('CACHE TYPE:', cache_factory)
    cache = cache_factory()

    for name in ['one', 'two', 'three']:
        o = ExpensiveObject2(name)
        cache[name] = o
        all_refs[name] = o
        del o

    print('all_refs = ', end=' ')
    pprint(all_refs)

    print('\n Before, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('{} = {}'.format(name, value))
        del value  # rm ref

    print('\n Clean up:')
    del all_refs
    gc.collect()

    print('\n After, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('{} = {}'.format(name, value))

    print('demo returning')


def run801_07():
    """
    WeakValueDictionary，对象val被删除的时候，kv也被删除
    :return:
    """
    demo(dict)
    print()
    demo(weakref.WeakValueDictionary)
