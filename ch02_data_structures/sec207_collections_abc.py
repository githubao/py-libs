#!/usr/bin/env python
# encoding: utf-8

"""
@description:  abstract base classes

@author: baoqiang
@time: 2019/11/28 1:44 下午
"""

from collections import abc


def run207_01():
    abc_classes = [
        abc.Container,  # 基础容器类型
        abc.Hashable,
        abc.Iterable,
        abc.Iterator,  # 迭代器的实现
        abc.Generator,
        abc.Sized,  # 可以知道大小的
        abc.Callable,
        abc.Sequence,  # Container,Sized,Iterable
        abc.MutableSequence,  # 可变的序列
        abc.ByteString,  # 支持bytes和bytearray
        abc.Set,  # 支持集合操作，Container,Sized,Iterable
        abc.MutableSet,
        abc.Mapping,  # 支持键值操作，Container,Sized,Iterable
        abc.MutableMapping,
        abc.MappingView,  # 可以映射类型的，Sized
        abc.ItemsView,  # item的视图
        abc.KeysView,
        abc.ValuesView,
        abc.Awaitable,  # 可以协程的
        abc.Coroutine,  # 协程的实现
        abc.AsyncIterable,  # 协程可迭代的
        abc.AsyncIterator,  # 异步迭代器
    ]

    for c in abc_classes:
        print(c)
