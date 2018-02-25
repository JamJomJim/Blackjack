import random
import time
import math
import numpy

# getters and setters would make things look nicer, just a refactoring thing, also its more proper
# fix bets so that they're respond dynamically to counts
# we could make count values an attribute of a card
# how aggressive the bets are flag


# surrender > split > double > hit > stand

suits, ranks = ["hearts", "diamonds", "spades", "clubs"], [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "ace"]
# player 17 -> 5 in hard totals
hard_hand_strategy = \
    [
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # -3
            ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
            ['hit',    'double', 'double', 'double', 'double', 'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']],
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # -2
            ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
            ['hit',    'double', 'double', 'double', 'double', 'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']],
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # -1
            ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
            ['hit',    'double', 'double', 'double', 'double', 'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']],
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # 0
            ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
            ['hit',    'double', 'double', 'double', 'double', 'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']],
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # 1
            ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
            ['hit',    'double', 'double', 'double', 'double', 'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']],
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # 2
            ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
            ['hit',    'double', 'double', 'double', 'double', 'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']],
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # 3
            ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
            ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
            ['hit',    'double', 'double', 'double', 'double', 'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']]]

# Large at top, small going downward
# player 8 for soft totals
soft_hand_strategy = \
    [
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand',  'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'double', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['double', 'double', 'double', 'double', 'double', 'stand', 'stand', 'hit', 'hit', 'hit'],
            ['hit', 'double', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],                  # -3
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit']],
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand',  'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'double', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['double', 'double', 'double', 'double', 'double', 'stand', 'stand', 'hit', 'hit', 'hit'],
            ['hit', 'double', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],                  # -2
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit']],
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand',  'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'double', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['double', 'double', 'double', 'double', 'double', 'stand', 'stand', 'hit', 'hit', 'hit'],
            ['hit', 'double', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],                 # -1
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit']],
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand',  'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'double', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['double', 'double', 'double', 'double', 'double', 'stand', 'stand', 'hit', 'hit', 'hit'],
            ['hit', 'double', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],                 # 0
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit']],
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand',  'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'double', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['double', 'double', 'double', 'double', 'double', 'stand', 'stand', 'hit', 'hit', 'hit'],
            ['hit', 'double', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],                 # 1
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit']],
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand',  'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'double', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['double', 'double', 'double', 'double', 'double', 'stand', 'stand', 'hit', 'hit', 'hit'],
            ['hit', 'double', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],                 # 2
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit']],
        [  # 2        3         4        5        6       7         8       9       10       A
            ['stand', 'stand', 'stand', 'stand', 'stand',  'stand', 'stand', 'stand', 'stand', 'stand'],
            ['stand', 'stand', 'stand', 'stand', 'double', 'stand', 'stand', 'stand', 'stand', 'stand'],
            ['double', 'double', 'double', 'double', 'double', 'stand', 'stand', 'hit', 'hit', 'hit'],
            ['hit', 'double', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],                 # 3
            ['hit', 'hit', 'double', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit'],
            ['hit', 'hit', 'hit', 'double', 'double', 'hit', 'hit', 'hit', 'hit', 'hit']]]

# player 10 for splitting
splitting_hand_strategy = \
    [
        [  # 2        3        4       5       6       7      8        9       10       A
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'Y',    'Y',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'N',    'N',    'N',     'N'],     # -3
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N']],

        [  # 2        3        4       5       6       7      8        9       10       A
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'Y',    'Y',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'N',    'N',    'N',     'N'],     # -2
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N']],

        [  # 2        3        4       5       6       7      8        9       10       A
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'Y',    'Y',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'N',    'N',    'N',     'N'],     # -1
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N']],

        [  # 2        3        4       5       6       7      8        9       10       A
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'Y',    'Y',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'N',    'N',    'N',     'N'],     # 0
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N']],

        [  # 2        3        4       5       6       7      8        9       10       A
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'Y',    'Y',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'N',    'N',    'N',     'N'],     # 1
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N']],

        [  # 2        3        4       5       6       7      8        9       10       A
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'Y',    'Y',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'N',    'N',    'N',     'N'],     # 2
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N']],

        [  # 2        3        4       5       6       7      8        9       10       A
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'Y',    'Y',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'Y',    'Y',    'Y',     'Y'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'Y',    'N',    'N',    'N',     'N'],     # 3
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'N',    'N',    'N',    'N',    'N',    'N',     'N'],
            ['N',     'N',     'N',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N'],
            ['Y',     'Y',     'Y',    'Y',    'Y',    'N',    'N',    'N',    'N',     'N']]]


def find_best_move(game, shoe, player, dealer, hand):
    if dealer.hand[0][0].rank == "ace":
        dealer_value = 11
    else:
        dealer_value = dealer.hand[0][0].rank
    if player.hand[hand][0].rank == "ace":
        player_value = 11
    else:
        player_value = player.hand[0][0].rank
    try:
        if len(player.hand[hand]) == 2 and player.hand[hand][0].rank == player.hand[hand][1].rank \
                and splitting_hand_strategy[shoe.true_count + 3][abs(11 - player_value)][dealer_value - 2] == 'Y':
            strat = 'split'
        elif is_soft(player.hand[hand]):
            player_value = check_value(player.hand[hand])
            strat = soft_hand_strategy[shoe.true_count + 3][abs(20 - player_value)][dealer_value - 2]
        else:
            player_value = check_value(player.hand[hand])
            strat = hard_hand_strategy[shoe.true_count + 3][abs(20 - player_value)][dealer_value - 2]

        if strat != 'None':
            return strat

    except IndexError:
        game.wrong_bs += 1
        print("here")
        return 'stand'


class Game:
    def __init__(self, blackjack_payout, dealer_hit_soft17, surrender, insurance, number_of_decks, penetration):
        self.blackjack_payout = blackjack_payout
        self.dealer_hit_soft17 = dealer_hit_soft17
        self.surrender = surrender
        self.insurance = insurance
        self.number_of_decks = number_of_decks
        self.penetration = penetration
        # stats class eventually?
        # for stat in stats print stat
        self.current_round = 0
        self.wrong_bs = 0
        self.num_hits = 0
        self.num_stand = 0
        self.num_double = 0
        self.num_split = 0
        self.num_surrender = 0


class Model:
    def __init__(self, starting_amount, rounds_to_be_played, min_bet, is_manual):
        self.starting_amount = starting_amount
        self.rounds_to_be_played = rounds_to_be_played
        self.min_bet = min_bet
        self.is_manual = is_manual


class Shoe:
    def __init__(self, dealer, game):
        self.cards_seen = 0
        self.running_count = 0
        self.true_count = 0
        dealer.new_decks(game)


def check_value(hand):
    possible_values = [0]
    # this essentially sets up a binomial tree with all the possible values.
    for card in hand:
        if card.rank == "ace":
            temp_values = list(possible_values)
            for value in possible_values:
                temp_values.append(value + 1)
                temp_values.append(value + 11)
                temp_values.remove(value)
            possible_values = temp_values
        else:
            for i, value in enumerate(possible_values):
                possible_values[i] += card.rank
    # lambda sets up an anonymous function that returns a bool.
    # filter returns the values in possible_values that satisfy this function.
    # these values are then turned into a list, and possible_values is set to that list.
    possible_values = list(filter(lambda hand_value: hand_value <= 21, possible_values))
    # the highest valid hand value is then returned.
    # if the player is bust, return -1.
    return max(possible_values + [-1])


def is_soft(hand):
    possible_values = [0]
    for card in hand:
        if card.rank == "ace":
            temp_values = list(possible_values)
            for value in possible_values:
                temp_values.append(value + 1)
                temp_values.append(value + 11)
                temp_values.remove(value)
            possible_values = temp_values
        else:
            for i, value in enumerate(possible_values):
                possible_values[i] += card.rank
    if len(list(filter(lambda hand_value: hand_value <= 21, possible_values))) > 1:
        return True


def count(dealer_hand, player_hand, shoe, game):

    # this needs to be changed to work after every card dealt instead of a game to game basis

    temp_hand = dealer_hand
    for hand in player_hand:
        temp_hand += hand

    for card in temp_hand:
        if card.rank != "ace":
            if 2 <= int(card.rank) <= 6:
                shoe.running_count += 1

            elif 7 <= int(card.rank) <= 9:
                shoe.running_count += 0

            else:
                shoe.running_count -= 1
        else:
            shoe.running_count -= 1

    shoe.true_count = math.floor(shoe.running_count / (game.number_of_decks * 52 - shoe.cards_seen))


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank) + " of " + self.suit

    def __repr__(self):
        return str(self.rank) + " of " + self.suit

    def displaysuit(self):
        print(" ", self.suit)


class Deck:
    def __init__(self, game):
        self.cards = []
        for _ in range(game.number_of_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(suit, rank))

    def display_cards(self):
        print(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)


class Dealer:
    def __init__(self):
        self.deck = None
        self.hand = [[]]

    def displaycards(self, start=None):
        if start is None:
            print(self.hand)
        else:
            print("Dealer has [" + str(self.hand[0][0]) + ", unknown]")

    def deal(self, person, hand, number_cards):
        person.hand[hand] += self.deck.cards[0:number_cards]
        self.deck.cards = self.deck.cards[number_cards:]

    def hit(self, dealer, hand):
        self.deal(dealer, hand, 1)

    def stand(self):
        pass

    def clear_hand(self):
        self.hand[0] = []

    def new_decks(self, game):
        self.deck = Deck(game)
        self.deck.shuffle()


class Player:
    def __init__(self, model):
        self.hand = [[]]
        self.bankroll = model.starting_amount
        self.bet = model.min_bet
        self.current_bet = [0, 0, 0, 0, 0, 0, 0, 0]
        self.total_bet = 0

    def displaycards(self, i):
        print("Player has", self.hand[i])

    def hit(self, game, dealer, hand):
        dealer.deal(self, hand, 1)
        game.num_hits += 1

    def double(self, game, dealer, hand):
        self.place_bet(self.bet, hand)
        dealer.deal(self, hand, 1)
        game.num_double += 1

    def split(self, game, dealer, i):
        temp_hand = [self.hand[i][0]]
        del self.hand[i][-1]
        self.hand.append(temp_hand)
        dealer.deal(self, -1, 1)
        dealer.deal(self, i, 1)
        self.place_bet(self.bet, i + 1)
        game.num_split += 1

    def surrender(self, game):
        game.num_surrender += 1
        self.stand(game)

    def clear_hand(self):
        self.hand = [[]]

    def place_bet(self, amount, hand):
        self.bankroll -= amount
        self.current_bet[hand] += amount
        self.total_bet += amount
        # self.current_bet[hand] += amount

    def show_bankroll(self):
        print("We got", self.bankroll, "dollars boii!")

    def choose_bet(self):
        # fancy code resulting in self.bet being changed based off running or total count id remember
        pass

    def manipulate_bankroll(self, bet, hand):
        self.bankroll += bet
        print(self.current_bet[hand])
        self.current_bet[hand] = 0


def main():
    start = time.time()
    # Game(blackjack_payout, dealer_hit_soft17, surrender, insurance, number_of_decks, penetration)
    game = Game(1.5, True, True, True, 6, 0.75)
    # Model(starting_amount, rounds_to_be_played, is_manual):
    model = Model(0, 100000, 10, False)
    dealer = Dealer()
    player = Player(model)
    shoe = Shoe(dealer, game)
    while game.current_round < model.rounds_to_be_played:

        player.place_bet(player.bet, 0)

        dealer.deal(player, 0, 2)
        # player.hand[0] = [Card("hearts", 2), Card("hearts", 2)]
        dealer.deal(dealer, 0, 2)
        dealer.displaycards(1)
        player.displaycards(0)

    # test for card values
    # print(check_value([Card("hearts", "ace"), Card("hearts", 9), Card("hearts", "ace"), Card("hearts", "ace")]))

        # dealer moves
        dealer_hand_val = check_value(dealer.hand[0])
        over = False
        if dealer_hand_val == 21:
            # print("Dealer Blackjack!")
            over = True

        while not over:
            dealer_hand_val = check_value(dealer.hand[0])
            # print("Dealer hand: ", dealer.hand[0])

            if dealer_hand_val == 21:
                # print("Dealer Lesser Blackjack!")
                over = True
            elif dealer_hand_val > 21 or dealer_hand_val == -1:
                # print("Dealer busts with", dealer_hand_val)
                over = True
            else:
                # if the dealer hits on a soft17 or whatever, this is searching for a card instead of a rank
                if game.dealer_hit_soft17 and dealer_hand_val == 17 and is_soft(dealer.hand[0]):
                    move = "hit"
                elif 1 < dealer_hand_val <= 16:
                    move = "hit"
                else:
                    move = "stand"

                if move == "stand":
                    dealer.stand()
                    over = True
                    # print("Dealer stands with", dealer_hand_val)

                elif move == "hit":
                    dealer.hit(dealer, 0)
                    # print("Dealer hits to make", dealer_hand_val)

                else:
                    # print("Empty deck! Dealer has", dealer_hand_val)
                    over = True

        dealer_hand_val = check_value(dealer.hand[0])
        # player moves
        for i, hand in enumerate(player.hand):
            player_hand_val = check_value(player.hand[i])
            over = False
            while not over:
                if player_hand_val == 21:
                    print("Player Blackjack!")
                    player.manipulate_bankroll(player.current_bet[i] * 2.5, i)
                    break
                time.sleep(0)  # helpful for debugging time.sleep(seconds)
                player_hand_val = check_value(player.hand[i])
                if player_hand_val == 21:
                    print("Player Lesser Blackjack!")
                    over = True
                elif player_hand_val == -1 or player_hand_val > 21:
                    print("Player Bust")
                    over = True
                else:
                    print("Player has a", player_hand_val)
                    if model.is_manual:
                        move = input("What do you want to do?\n")
                    else:
                        move = find_best_move(game, shoe, player, dealer, i)

                    if move == "stand":
                        print("Player Stands.")
                        game.num_stand += 1
                        over = True
                    elif move == "hit":
                        player.hit(game, dealer, i)
                        print("Player hits.")
                        player.displaycards(i)
                    elif move == "split":
                        print("Player splits.")
                        player.split(game, dealer, i)
                        print(player.current_bet)
                        player.displaycards(i)
                    elif move == "double":
                        print("Player doubles.")
                        player.double(game, dealer, i)
                        player.displaycards(i)
                        over = True
                    elif move == "surrender":
                        player.surrender(game)
                        print("No surrender yet")
                        over = True
                    else:
                        print("you can't do that")

            player_hand_val = check_value(player.hand[i])
            print("Dealer has a " + str(dealer_hand_val))
            if 21 >= dealer_hand_val > player_hand_val:
                print("Dealer wins!\n")
                player.current_bet[i] = 0
            elif dealer_hand_val < player_hand_val <= 21:
                print("Player wins!\n")
                player.manipulate_bankroll(player.current_bet[i] * 2, i)
            elif dealer_hand_val < 0 and dealer_hand_val == player_hand_val:
                print("You're both losers.")
                player.current_bet[i] = 0
            else:
                player.manipulate_bankroll(player.current_bet[i], i)
                print("Push\n")
        count(dealer.hand[0], player.hand, shoe, game)
        player.choose_bet()

        player.clear_hand()
        dealer.clear_hand()

        player.show_bankroll()
        print(shoe.running_count, shoe.true_count)

        if len(dealer.deck.cards) / (game.number_of_decks * 52) < (1 - game.penetration):
            print("New Deck!")
            shoe = Shoe(dealer, game)
        game.current_round += 1

    print("\nEnded with " + str(player.bankroll) + " dollars")
    print(str(model.rounds_to_be_played) + " hands in " + str(round(time.time() - start, 4)) + " seconds!")
    print("Couldn't find basic strategy " + str(game.wrong_bs) + " times...\n")

    print("Stand: " + str(game.num_stand))
    print("Hit: " + str(game.num_hits))
    print("Double: " + str(game.num_double))
    print("Split: " + str(game.num_split))
    print("Surrender: " + str(game.num_surrender))

    print(player.bankroll/player.total_bet)


if __name__ == '__main__':
    main()
