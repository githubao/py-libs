#!/usr/bin/env python
# encoding: utf-8

"""
@description: struct pack

@author: baoqiang
@time: 2019/11/28 9:52 下午
"""
import ctypes
import struct
import binascii
from array import array


def run701_01():
    values = (1, 'ab'.encode(), 2.7)
    s = struct.Struct('I 2s f')
    packed_data = s.pack(*values)

    print('Original values:', values)
    print('Format string:', s.format)
    print('Uses:', s.size, 'bytes')
    print('Packed Value:', binascii.hexlify(packed_data))


def run701_02():
    """
    unpack
    :return:
    """
    hex_byte = b'0100000061620000cdcc2c40'
    packed_data = binascii.unhexlify(hex_byte)

    s = struct.Struct('I 2s f')
    unpacked_data = s.unpack(packed_data)
    print('Unpacked Value:', unpacked_data)


def run701_03():
    """
    endianness
    :return:
    """
    values = (1, 'ab'.encode(), 2.7)
    print('Original values:', values)

    endianness = [
        ('@', 'native, native'),
        ('=', 'native, standard'),
        ('<', 'little-endian'),
        ('>', 'big-endian'),
        ('!', 'network'),
    ]

    for code, name in endianness:
        s = struct.Struct(code + ' I 2s f')
        packed_data = s.pack(*values)
        print()
        print('Format string:', s.format, 'for', name)
        print('Uses:', s.size, 'bytes')
        print('Packed Value:', binascii.hexlify(packed_data))
        print('Unpacked Value:', s.unpack(packed_data))


def run701_04():
    """
    pack buffer
    c_string_buffer or array
    :return:
    """
    s = struct.Struct(' I 2s f')
    values = (1, 'ab'.encode(), 2.7)
    print('Original values:', values)

    print()
    print('ctypes string buffer')

    b = ctypes.create_string_buffer(s.size)
    print('Before:', binascii.hexlify(b.raw))
    s.pack_into(b, 0, *values)
    print('After:', binascii.hexlify(b.raw))
    print('Unpacked:', s.unpack_from(b, 0))

    print()
    print('array')

    a = array('b', b'\0' * s.size)
    print('Before:', binascii.hexlify(a))
    s.pack_into(a, 0, *values)
    print('After:', binascii.hexlify(a))
    print('Unpacked:', s.unpack_from(a, 0))
