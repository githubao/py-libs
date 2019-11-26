#!/usr/bin/env python
# encoding: utf-8

"""
@description: 高级字符串模板

@author: baoqiang
@time: 2019/11/26 11:42 上午
"""
import string


def run103_01():
    class MyTemplate(string.Template):
        delimiter = '%'
        idpattern = '[a-z]+_[a-z]+'

    template_text = """
    Delimiter: %%  
    Replaced: %with_underscore
    Ignored: %notunderscored
"""

    d = {
        'with_underscore': 'replaced',
        'notunderscored': 'not replaced',
    }

    t = MyTemplate(template_text)
    print("Modified ID pattern: ")
    print(t.safe_substitute(d))


def run103_02():
    """
    t.pattern: re.Pattern
    t.pattern.pattern: str
    :return:
    """
    t = string.Template('$var')
    print(t.pattern)
    print(t.pattern.pattern)
    print(type(t.pattern))
    print(type(t.pattern.pattern))


def run103_03():
    class MyTemplate(string.Template):
        delimiter = '{{'
        pattern = r"""
        \{\{(?:
        (?P<escaped>\{\{)|
        (?P<named>[_a-z][_a-z0-9]*)\}\}|
        (?P<braced>[_a-z][_a-z0-9]*)\}\}|
        (?P<invalid>)
        )
        """

    t = MyTemplate("""
{{{{
{{var}}    
""")
    print('MATCHES: ', t.pattern.findall(t.template))
    print('SUBSTITUTED: ', t.safe_substitute(var='replacement'))
