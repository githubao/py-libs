#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: baoqiang
@time: 2019/12/6 7:40 下午
"""
import itertools
import random


def run305_01():
    """
    choice
    """
    outcomes = {
        'heads': 0,
        'tails': 0,
    }

    sides = list(outcomes.keys())

    for i in range(1000000):
        outcomes[random.choice(sides)] += 1

    print('Heads:', outcomes['heads'])
    print('Tails:', outcomes['tails'])


def run305_02():
    """
    shuffle
    """
    FACE_CARDS = ('T', 'J', 'Q', 'K', 'A')
    SUITS = ('H', 'D', 'C', 'S')

    def new_deck():
        return ['{:>2}{}'.format(*c)
                for c in itertools.product(
                itertools.chain(range(2, 10), FACE_CARDS),
                SUITS, )
                ]

    def show_deck(deck):
        p_deck = deck[:]
        while p_deck:
            row = p_deck[:13]
            p_deck = p_deck[13:]

            for j in row:
                print(j, end=' ')
            print()

    deck = new_deck()
    print('Initial deck:')
    show_deck(deck)

    random.shuffle(deck)
    print('\nShuffled deck:')
    show_deck(deck)

    hands = [[], [], [], []]
    for i in range(5):
        for h in hands:
            h.append(deck.pop())

    print('\nHands:')
    for n, h in enumerate(hands):
        print('{}:'.format(n + 1), end=' ')
        for c in h:
            print(c, end=' ')
        print()

    print('\nRemaining deck:')
    show_deck(deck)


def run305_03():
    """
    sample
    """
    with open('/usr/share/dict/words', 'rt') as f:
        words = f.readlines()
    words = [w.rstrip() for w in words]

    for w in random.sample(words, 5):
        print(w)
