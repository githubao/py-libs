#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/11/27 4:31 下午
"""

import re


def run307_01():
    """
    case insensitive
    :return:
    """
    text = 'This is some text -- with punctuation.'

    pat = r'\bT\w+'
    with_case = re.compile(pat)
    without_case = re.compile(pat, re.IGNORECASE)

    print('Text:\n {!r}'.format(text))
    print('Pattern:\n {}'.format(pat))

    print('Case-sensitive')
    for s in with_case.findall(text):
        print(' {!r}'.format(s))

    print('Case-insensitive')
    for s in without_case.findall(text):
        print(' {!r}'.format(s))


def run307_02():
    """
    multi line: 可以换行匹配
    :return:
    """
    text = 'This is some text -- with punctuation.\nA second line.'

    pat = r'(^\w+)|(\w+\S*$)'
    single_line = re.compile(pat)
    multiline = re.compile(pat, re.MULTILINE)

    print('Text:\n {!r}'.format(text))
    print('Pattern:\n {}'.format(pat))

    print('Single Line: ')
    for s in single_line.findall(text):
        print(' {!r}'.format(s))

    print('Multiline: ')
    for s in multiline.findall(text):
        print(' {!r}'.format(s))


def run307_03():
    """
    dotall: 点号默认不匹配换行，dotall包含匹配换行
    :return:
    """
    text = 'This is some text -- with punctuation.\nA second line.'

    pat = r'.+'
    no_newlines = re.compile(pat)
    dotall = re.compile(pat, re.DOTALL)

    print('Text:\n {!r}'.format(text))
    print('Pattern:\n {}'.format(pat))

    print('No newlines: ')
    for s in no_newlines.findall(text):
        print(' {!r}'.format(s))

    print('Dotall: ')
    for s in dotall.findall(text):
        print(' {!r}'.format(s))


def run307_04():
    """
    ascii: 非unicode模式
    :return:
    """
    text = 'Français złoty Österreich'

    pat = r'\w+'
    ascii_pat = re.compile(pat, re.ASCII)
    unicode_pat = re.compile(pat)

    print('Text:\n {!r}'.format(text))
    print('Pattern:\n {}'.format(pat))
    print('ASCII:\n {}'.format(list(ascii_pat.findall(text))))
    print('Unicode:\n {}'.format(list(unicode_pat.findall(text))))


def run307_05():
    """
    verbose模式，可以写注释
    :return:
    """
    address = re.compile(r'[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)')

    candidates = [
        'first.last@example.com',
        'first.last+category@gmail.com',
        'valid-address@mail.example.com',
        'not-valid@example.foo',
    ]

    for candidate in candidates:
        m = address.search(candidate)
        print('{:<30}   {}'.format(
            candidate, 'Matches' if m else 'No match'
        ))


def run307_06():
    """
    verbose模式，可以写注释
    :return:
    """
    address = re.compile(r"""
    [\w\d.+-]+          # username
    @
    ([\w\d.]+\.)+       # domain name prefix
    (com|org|edu)       # fTODO: support more top-level domains
    """, re.VERBOSE)

    candidates = [
        'first.last@example.com',
        'first.last+category@gmail.com',
        'valid-address@mail.example.com',
        'not-valid@example.foo',
    ]

    for candidate in candidates:
        m = address.search(candidate)
        print('{:<30}   {}'.format(
            candidate, 'Matches' if m else 'No match'
        ))


def run307_07():
    """
    verbose模式，可以写注释
    :return:
    """
    address = re.compile(r"""
    
    # A name is made up of letters, and may include "."
    # for title abbreviations and middle initials.
    ((?P<name>
        ([\w.,]+\s+)*[\w.,]+)
        \s*
        # Email addresses are wrapped in angle brackets < >, 
        # but only if a name is found, so keep the start 
        # bracket in this group.
        <
    )? # the entire name is optional

    # The address itself: username@domain.tld
    (?P<email>
    [\w\d.+-]+          # username
    @
    ([\w\d.]+\.)+       # domain name prefix
    (com|org|edu)       # limit the allowed top-level domains
    )
    
    >? #optional closing angle bracket
    """, re.VERBOSE)

    candidates = [
        'first.last@example.com',
        'first.last+category@gmail.com',
        'valid-address@mail.example.com',
        'not-valid@example.foo',
        'First Last <first.last@example.com>',
        'No Brackets first.last@example.com',
        'First Last',
        'First Middle Last <first.last@example.com>',
        'First M. Last <first.last@example.com>',
        '<first.last@example.com>',
    ]

    for candidate in candidates:
        print('Candidate: ', candidate)

        m = address.search(candidate)

        if m:
            print('Name: ', m.groupdict()['name'])
            print('Email: ', m.groupdict()['email'])
        else:
            print('No match')

        print()


def run307_08():
    """
    embedded flags
    ASCII: a
    IGNORECASE: i
    MULTILINE: m
    DOTALL: s
    VERBOSE: x
    :return:
    """
    text = 'This is some text -- with punctuation.'

    pat = r'(?i)\bT\w+'
    regex = re.compile(pat)

    print('Text:\n {!r}'.format(text))
    print('Pattern:\n {}'.format(pat))
    print('Matches:\n {}'.format(regex.findall(text)))
