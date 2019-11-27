#!/usr/bin/env python
# encoding: utf-8

"""
@description: 创建enum

@author: baoqiang
@time: 2019/11/27 6:07 下午
"""

import enum


class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


class IntBugStatus(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


class DupBugStatus(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    by_design = 4
    closed = 1


@enum.unique
class UniqueBugStatus(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    # ValueError: duplicate values found in < enum 'UniqueBugStatus' >:
    #  by_design -> wont_fix, closed -> fix_released

    # by_design = 4
    # closed = 1


def run101_01():
    """
    name & value
    :return:
    """
    print('\nMember name: {}'.format(BugStatus.wont_fix.name))
    print('Member value: {}'.format(BugStatus.wont_fix.value))


def run101_02():
    """
    iter
    :return:
    """
    for status in BugStatus:
        print('{:15} = {}'.format(status.name, status.value))


def run101_03():
    actual_state = BugStatus.wont_fix
    desired_state = BugStatus.fix_released

    print('Equality:', actual_state == desired_state,
          actual_state == BugStatus.wont_fix)

    print('Identity:', actual_state is desired_state,
          actual_state is BugStatus.wont_fix)

    print('Order by value: ')

    try:
        print('\n'.join('   ' + s.name for s in sorted(BugStatus)))
    except TypeError as e:
        print('Cannot sort: {}'.format(e))


def run101_04():
    """
    intEnum can sort
    :return:
    """
    print('Order by value: ')
    print('\n'.join('   ' + s.name for s in sorted(IntBugStatus)))


def run101_05():
    """
    dup
    :return:
    """
    for status in DupBugStatus:
        print('{:15} = {}'.format(status.name, status.value))

    print('\nSame: by_design is wont_fix:', DupBugStatus.by_design == DupBugStatus.wont_fix)
    print('Same: closed is fix_released:', DupBugStatus.closed == DupBugStatus.fix_released)


def run101_06():
    """
    enum.unique
    :return:
    """
    pass


def run101_07():
    """
    dynamic create enum
    :return:
    """
    DynamicBugStatus = enum.Enum(
        value='DynamicBugStatus',
        names=('fix_released fix_committed in_progress '
               'wont_fix invalid incomplete new')
    )

    print('Member: {}'.format(DynamicBugStatus.new))
    print('\nAll members: ')

    for status in DynamicBugStatus:
        print('{:15} = {}'.format(status.name, status.value))


def run101_08():
    """
    dynamic create enum with val
    :return:
    """
    DynamicBugStatus2 = enum.Enum(
        value='DynamicBugStatus2',
        names=[
            ('new', 7),
            ('incomplete', 6),
            ('invalid', 5),
            ('wont_fix', 4),
            ('in_progress', 3),
            ('fix_committed', 2),
            ('fix_released', 1),
        ]
    )

    print('All members: ')

    for status in DynamicBugStatus2:
        print('{:15} = {}'.format(status.name, status.value))


def run101_09():
    """
    dynamic create enum with init
    :return:
    """

    class DynamicBugStatus3(enum.Enum):
        new = (7, ['incomplete', 'invalid', 'wont_fix', 'in_progress'])
        incomplete = (6, ['new', 'wont_fix'])
        invalid = (5, ['new'])
        wont_fix = (4, ['new'])
        in_progress = (3, ['new', 'fix_committed'])
        fix_committed = (2, ['in_progress', 'fix_released'])
        fix_released = (1, ['new'])

        def __init__(self, num, transitions):
            self.num = num
            self.transitions = transitions

        def can_transition(self, new_status):
            return new_status.name in self.transitions

    print('Name: ', DynamicBugStatus3.in_progress)
    print('Value: ', DynamicBugStatus3.in_progress.value)
    print('Custom attribute: ', DynamicBugStatus3.in_progress.transitions)
    print('Using attribute: ', DynamicBugStatus3.in_progress.can_transition(DynamicBugStatus3.new))


def run101_10():
    """
    dynamic create enum with dict
    :return:
    """

    class DynamicBugStatus4(enum.Enum):
        new = {'num': 7, 'transitions': ['incomplete', 'invalid', 'wont_fix', 'in_progress']}
        incomplete = {'num': 6, 'transitions': ['new', 'wont_fix']}
        invalid = {'num': 5, 'transitions': ['new']}
        wont_fix = {'num': 4, 'transitions': ['new']}
        in_progress = {'num': 3, 'transitions': ['new', 'fix_committed']}
        fix_committed = {'num': 2, 'transitions': ['in_progress', 'fix_released']}
        fix_released = {'num': 1, 'transitions': ['new']}

        def __init__(self, vals):
            self.num = vals['num']
            self.transitions = vals['transitions']

        def can_transition(self, new_status):
            return new_status.name in self.transitions

    print('Name: ', DynamicBugStatus4.in_progress)
    print('Value: ', DynamicBugStatus4.in_progress.value)
    print('Custom attribute: ', DynamicBugStatus4.in_progress.transitions)
    print('Using attribute: ', DynamicBugStatus4.in_progress.can_transition(DynamicBugStatus4.new))
