#!/usr/bin/env python
# encoding: utf-8

"""
@description: 组匹配

@author: baoqiang
@time: 2019/11/26 10:30 下午
"""

import re

from ch01_text.sec304_re_test_patterns import test_patterns


def run306_01():
    text = 'abbaaabbbaaaaa'
    patterns = [('a(ab)', "a followed by literal ab"),
                ('a(a*b*)', "a followed by 0-n a and 0-n b"),
                ('a(ab)*', "a followed by 0-n ab"),
                ('a(ab)+', "a followed by 1-n ab"),
                ]
    test_patterns(text, patterns)


def run306_02():
    """
    groups
    :return:
    """
    text = 'This is some text -- with punctuation.'

    print(text)
    print()

    patterns = [
        (r'^(\w+)', 'word at start of string'),
        (r'(\w+)\S*$', 'word at end, with optional punctuations'),
        (r'(\bt\w+)\W+(\w+)', 'word starting with t, another word'),
        (r'(\w+t)\b', 'word end with t'),
    ]

    for pat, desc in patterns:
        regex = re.compile(pat)
        m = regex.search(text)
        print("'{}' ({})\n".format(pat, desc))
        print(' ', m.groups())
        print()


def run306_03():
    """
    individual group
    :return:
    """
    text = 'This is some text -- with punctuation.'

    print('Input text: ', text)

    regex = re.compile(r'(\bt\w+)\W+(\w+)')
    print('Pattern: ', regex.pattern)

    m = regex.search(text)

    print('Entire match: ', m.group(0))
    print('Word starting with "t": ', m.group(1))
    print('Word after "t" word: ', m.group(2))


def run306_04():
    """
    named group: (?P<name>pat)
    :return:
    """
    text = 'This is some text -- with punctuation.'

    print(text)
    print()

    patterns = [
        r'^(?P<first_word>\w+)',
        r'(?P<last_word>\w+)\S*$',
        r'(?P<t_word>\bt\w+)\W+(?P<another_word>\w+)',
        r'(?P<ends_with_t>\w+t)\b',
    ]

    for pat in patterns:
        regex = re.compile(pat)
        m = regex.search(text)
        print("'{}'".format(pat))
        print(' ', m.groups())
        print(' ', m.groupdict())
        print()


def test_patterns2(text, patterns):
    for pat, desc in patterns:
        print("'{!r}' ({})\n".format(pat, desc))
        print(" {!r}".format(text))

        for m in re.finditer(pat, text):
            s = m.start()
            e = m.end()

            prefix = '.' * s

            print(' {}{!r}{}'.format(prefix, text[s:e], ' ' * (len(text) - e)), end=' ')

            print(m.groups())

            if m.groupdict():
                print('{}{}'.format(' ' * (len(text) - s), m.groupdict()))

        print()


def run306_05():
    """
    nested groups
    :return:
    """
    text = 'abbaabbba'
    patterns = [
        (r'a((a*)(b*))', 'a followed by 0-n a and 0-n b'),
    ]
    test_patterns2(text, patterns)


def run306_06():
    """
    alternative groups
    :return:
    """
    text = 'abbaabbba'
    patterns = [
        (r'a((a+)|(b+))', 'a then seq. of a or seq. of b'),
        (r'a((a|b)+)', 'a then seq. of a [ab]'),
    ]
    test_patterns2(text, patterns)


def run306_07():
    """
    no capturing groups: (?:pat)
    :return:
    """
    text = 'abbaabbba'
    patterns = [
        (r'a((a+)|(b+))', 'capturing form'),
        (r'a((?:a+)|(?:b+))', 'no capturing'),
    ]
    test_patterns2(text, patterns)

