#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/11/26 6:49 下午
"""

import re


def test_patterns(text, patterns):
    for pat, desc in patterns:
        print("'{}' ({})\n".format(pat, desc))
        print("     '{}'".format(text))

        for m in re.finditer(pat, text):
            s = m.start()
            e = m.end()

            substr = text[s:e]

            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)

            print("     {}'{}'".format(prefix, substr))

        print()


def run304_01():
    text = 'abbaaabbbaaaaa'
    patterns = [('ab', "'a' followed by 'b'"), ]
    test_patterns(text, patterns)


def run304_02():
    """
    pattern
    :return:
    """

    text = 'abbaaabbbaaaaa'
    patterns = [('ab*', 'a followed by zero or more b'),
                ('ab+', 'a followed by one or more b'),
                ('ab?', 'a followed by zero or one b'),
                ('ab{3}', 'a followed by three b'),
                ('ab{2,3}', 'a followed by two or three b'),
                ]
    test_patterns(text, patterns)


def run304_03():
    """
    no grady pattern
    :return:
    """

    text = 'abbaabbba'
    patterns = [('ab*?', 'a followed by zero or more b'),
                ('ab+?', 'a followed by one or more b'),
                ('ab??', 'a followed by zero or one b'),
                ('ab{3}?', 'a followed by three b'),
                ('ab{2,3}?', 'a followed by two or three b'),
                ]
    test_patterns(text, patterns)


def run304_04():
    """
    charset pattern
    :return:
    """

    text = 'abbaabbba'
    patterns = [('[ab]', 'either a or b'),
                ('a[ab]+', 'a followed by 1 or more a or b'),
                ('a[ab]+?', 'a followed by 1 or more a or b, not greedy'),
                ]
    test_patterns(text, patterns)


def run304_05():
    """
    exclude pattern
    :return:
    """

    text = 'This is some text -- with punctuation.'
    patterns = [('[^-. ]+', 'sequences without -,., or space'),
                ]
    test_patterns(text, patterns)


def run304_06():
    """
    charset range pattern
    :return:
    """

    text = 'This is some text -- with punctuation.'
    patterns = [('[a-z]+', 'sequences of lowercase letters'),
                ('[A-Z]+', 'sequences of uppercase letters'),
                ('[a-zA-Z]+', 'sequences of letters of either case'),
                ('[A-Z][a-z]+', 'one uppercase followed by lowercase'),
                ]
    test_patterns(text, patterns)


def run304_07():
    """
    charset dot pattern
    :return:
    """
    text = 'abbaabbba'
    patterns = [('a.', 'a followed by any one character'),
                ('b.', 'b followed by any one character'),
                ('a.*b', 'a followed by anything, ending in b'),
                ('a.*?b', 'a followed by anything, ending in b'),
                ]
    test_patterns(text, patterns)


def run304_08():
    """
    escape codes pattern
    \\d(digit) \\D(non-digit) \\s(whitespace, tab,space,newline,etc)
    \\S \\w(alphanumeric) \\W
    :return:
    """
    text = 'A prime #1 example!'
    patterns = [(r'\d+', 'sequence of digits'),
                (r'\D+', 'sequence of non-digits'),
                (r'\s+', 'sequence of whitespace'),
                (r'\S+', 'sequence of non-whitespace'),
                (r'\w+', 'alphanumeric characters'),
                (r'\W+', 'non-alphanumeric'),
                ]
    test_patterns(text, patterns)


def run304_09():
    """
    escape escapes pattern
    :return:
    """
    text = r'\d+ \D+ \s+'
    patterns = [(r'\\.\+', 'escape code'),
                ]
    test_patterns(text, patterns)


def run304_10():
    """
    anchoring pattern
    ^(line start) $(line end) \\A(str start) \\Z(str end)
    \\b(word start or end) \\B(not word start or end)
    :return:
    """
    text = r'This is some text -- with punctuation.'
    patterns = [(r'^\w+', 'word at start of string'),
                (r'\A\w+', 'word at start of string'),
                (r'\w+\S*$', 'word near end of string'),
                (r'\w+\S*\Z', 'word near end of string'),
                (r'\w*t\w*', 'word containing t'),
                (r'\bt\w+', 't at start of word'),
                (r'\w+t\b', 't at end of word'),
                (r'\Bt\B', 'not start or end of word'),
                ]
    test_patterns(text, patterns)
