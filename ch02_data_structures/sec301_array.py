#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/11/28 2:18 下午
"""
import binascii
from array import array
import pprint
import tempfile


def run301_01():
    """
    array支持的类型
    :return:
    """

    class Code:
        def __init__(self, code, type_, size):
            self.code = code
            self.type = type_
            self.size = size

        def __repr__(self):
            return str(self.__dict__)

    codes = [
        Code('b', 'int', 1),
        Code('B', 'int', 1),
        Code('h', 'signed short', 2),
        Code('H', 'unsigned short', 2),
        Code('i', 'signed int', 2),
        Code('I', 'unsigned int', 2),
        Code('l', 'signed long', 4),
        Code('L', 'unsigned long', 4),
        Code('q', 'signed long long', 8),
        Code('Q', 'unsigned long long', 8),
        Code('f', 'float', 4),
        Code('d', 'double float', 8),
    ]

    for c in codes:
        print('{!r}'.format(c))


def run301_02():
    """
    array 初始化
    :return:
    """
    s = b'This is the array.'
    a = array('b', s)

    print('As byte string: ', s)
    print('As Array: ', a)
    print('As hex: ', binascii.hexlify(a))


def run301_03():
    """
    array op
    :return:
    """
    a = array('i', range(3))

    print('Initial: ', a)

    a.extend(range(3))
    print('Extend: ', a)

    print('Slice: ', a[2:5])

    print('Iterator:')
    print(list(enumerate(a)))


def run301_04():
    """
    array file io
    NOTICE: 需要临时文件测试的时候可以使用tempfile
    :return:
    """
    a = array('i', range(5))
    print('A1:', a)

    fw = tempfile.NamedTemporaryFile()
    a.tofile(fw.file)
    fw.flush()

    with open(fw.name, 'rb') as f:
        raw_data = f.read()
        print('Raw contents:', binascii.hexlify(raw_data))

        # read data to array
        f.seek(0)
        a2 = array('i')
        a2.fromfile(f, len(a))
        print('A2:', a2)


def run301_05():
    """
    array, !!! as bytes not unicode !!!
    :return:
    """
    a = array('i', range(5))
    print('A1:', a)

    as_bytes = a.tobytes()
    print('Bytes:', binascii.hexlify(as_bytes))

    a2 = array('i')
    a2.frombytes(as_bytes)
    print('A2:', a2)


def to_hex(a):
    """
    两个十六进制为一组
    :param a:
    :return:
    """
    char_per_item = a.itemsize * 2
    hex_version = binascii.hexlify(a)
    num_chunks = len(hex_version)

    # split a items
    for i in range(num_chunks):
        start = i * char_per_item
        end = start + char_per_item
        res = hex_version[start:end]
        # print(res)
        yield res


def run301_06():
    """
    array bytes format
    :return:
    """

    start = int('0x12345678', base=16)
    end = start + 5
    a1 = array('i', range(start, end))
    a2 = array('i', range(start, end))

    # 大端序还是小端序的问题
    a2.byteswap()

    s = '*' * 12
    fmt = '{:>12} {:>12} {:>12} {:>12}'
    print(fmt.format('A1 hex', 'A1', 'A2 hex', 'A2'))
    print(fmt.format(s, s, s, s))

    fmt = '{!r:>12} {:>12} {!r:>12} {:>12}'
    for values in zip(to_hex(a1), a1, to_hex(a2), a2):
        print(fmt.format(*values))
