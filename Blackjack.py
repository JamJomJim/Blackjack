import random
import time

# fix bets so that they're respond dynamically to counts
# how aggressive the bets are flag


# surrender > split > double > hit > stand

suits, ranks = ["hearts", "diamonds", "spades", "clubs"], [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "ace"]
# player 20 -> 4 in hard totals
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
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
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
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
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
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
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
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
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
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
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
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
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
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
            ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']]]

# Large at top, small going downward
# player A-9 through A-2 for soft totals
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


class Deck:
    def __init__(self, number_of_decks):
        self.cards = []
        for _ in range(number_of_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(suit, rank))

    def display_cards(self):
        print(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)


class Shoe:
    def __init__(self, dealer):
        self.running_count = 0
        self.true_count = 0
        dealer.new_shoe()


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


class Hand:
    def __init__(self, person):
        self.owner = person
        self.cards = []
        self.has_split = False
        self.has_split_aces = False
        self.current_bet = 0

    def hit(self, dealer):
        dealer.deal(hand=self, number_cards=1)

    def double(self, dealer):
        self.owner.place_bet(self.owner.bet, self)
        dealer.deal(hand=self, number_cards=1)

    def split(self, dealer):

        new_hand = Hand(self.owner)
        new_hand.has_split = True
        new_hand.cards = [self.cards[1]]
        dealer.deal(hand=new_hand, number_cards=1)
        new_hand.owner.place_bet(self.owner.bet, new_hand)

        self.cards = self.cards[0:1]
        self.has_split = True
        dealer.deal(hand=self, number_cards=1)

        if new_hand.cards[0].rank == "ace":
            new_hand.has_split_aces = True
            self.has_split_aces = True

        self.owner.hands.append(new_hand)

    def surrender(self, game):
        game.num_surrender += 1
        self.stand()

    def stand(self):
        pass

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self.cards)


class Dealer:
    def __init__(self, game):
        self.game = game
        self.deck = None
        self.hand = Hand(self)
        self.shoe = Shoe(self)

    def display_cards(self):
        print("Dealer has", self.hand)

    def deal(self, hand, number_cards):
        hand.cards += self.deck.cards[0:number_cards]
        self.shoe.running_count += get_count(self.deck.cards[0:number_cards])
        self.shoe.true_count = self.shoe.running_count / self.game.number_of_decks
        self.deck.cards = self.deck.cards[number_cards:]

    def clear_hand(self):
        self.hand = Hand(self)

    def new_shoe(self):
        self.deck = Deck(self.game.number_of_decks)
        self.deck.shuffle()


class Player:
    def __init__(self, model):
        self.hands = [Hand(self)]
        self.bankroll = model.starting_amount
        self.bet = model.min_bet

    def display_cards(self):
        print("Player has", self.hands)

    def clear_hand(self):
        self.hands = [Hand(self)]

    def place_bet(self, amount, hand):
        print("Player placed bet of $", amount)
        self.bankroll -= amount
        hand.current_bet += amount


def find_best_move(shoe, player_hand, dealer_hand):
    player_cards = player_hand.cards
    d_index = check_value(dealer_hand[0:1]) - 2
    current_count = round(shoe.true_count)

    # The strategy tabled are for a true count from -3 to 3. This ensures that the current count is within those bounds
    if current_count > 3:
        current_count = 3
    elif current_count < -3:
        current_count = -3

    # can the hand be split
    if len(player_cards) == 2 and player_cards[0].rank == player_cards[1].rank:
        p_index = abs(check_value(player_cards[0:1]) - 11)
        if splitting_hand_strategy[current_count][p_index][d_index] == "Y":
            return "split"

    p_index = abs(check_value(player_cards) - 20)
    # If the hand is soft
    if is_soft(player_cards):
        best_move = soft_hand_strategy[current_count][p_index][d_index]
    # If the hand is hard
    else:
        best_move = hard_hand_strategy[current_count][p_index][d_index]

    if best_move == "double" and (len(player_cards) > 2 or player_hand.has_split):
        best_move = "hit"

    return best_move


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
    else:
        return False


def get_count(cards):
    count = 0
    for card in cards:
        if card.rank in [2, 3, 4, 5, 6]:
            count += 1
        elif card.rank in [10, "ace"]:
            count -= 1
    return count


def main():
    start = time.time()
    game = Game(blackjack_payout=1.5,
                dealer_hit_soft17=False,
                surrender=True,
                insurance=True,
                number_of_decks=6,
                penetration=0.75)

    model = Model(starting_amount=0, rounds_to_be_played=10000, min_bet=10, is_manual=False)
    dealer = Dealer(game=game)
    player = Player(model)

    while game.current_round < model.rounds_to_be_played:

        player.place_bet(amount=player.bet, hand=player.hands[0])

        dealer.deal(hand=player.hands[0], number_cards=2)
        # player.hands[0].cards = [Card("spades", "ace"), Card("spades", "ace")]
        player.display_cards()

        dealer.deal(hand=dealer.hand, number_cards=2)
        dealer.display_cards()

        print("\n")

        # Checks for dealer blackjack
        # Verify these rules
        if check_value(dealer.hand.cards) == 21:
            print("Dealer Blackjack!")
            continue

        # Player's turn
        for hand in player.hands:
            hand_done = False
            while not hand_done and not hand.has_split_aces:
                player_hand_val = check_value(hand.cards)
                print("Player has ", hand, "worth", player_hand_val)
                if player_hand_val == 21:
                    print("Player has 21!")
                    hand_done = True
                elif player_hand_val == -1 or player_hand_val > 21:
                    print("Player Bust")
                    hand_done = True
                else:
                    if model.is_manual:
                        move = input("What do you want to do?\n")
                    else:
                        move = find_best_move(shoe=dealer.shoe, player_hand=hand, dealer_hand=dealer.hand.cards)

                    if move == "stand":
                        print("Player Stands.")
                        game.num_stand += 1
                        hand_done = True
                    elif move == "hit":
                        hand.hit(dealer)
                        print("Player hits.")
                    elif move == "split":
                        print("Player splits.")
                        hand.split(dealer)
                        player.display_cards()
                    elif move == "double":
                        print("Player doubles.")
                        hand.double(dealer=dealer)
                        print("Player has ", hand, "worth", check_value(hand.cards))
                        hand_done = True
                    elif move == "surrender":
                        hand.surrender(game)
                        print("No surrender yet")
                        hand_done = True
                    else:
                        print("you can't do that")

        # Dealer's turn
        dealer_done = False
        while not dealer_done:
            dealer_hand_val = check_value(dealer.hand.cards)
            print("Dealer hand: ", dealer.hand)

            if dealer_hand_val == 21:
                print("Dealer Lesser Blackjack!")
                dealer_done = True
            elif dealer_hand_val == -1:
                print("Dealer busts with", dealer_hand_val)
                dealer_done = True
            else:
                # if the dealer hits on a soft17 or whatever, this is searching for a card instead of a rank
                if game.dealer_hit_soft17 and dealer_hand_val == 17 and is_soft(dealer.hand.cards):
                    move = "hit"
                elif dealer_hand_val <= 16:
                    move = "hit"
                else:
                    move = "stand"

                if move == "stand":
                    dealer.hand.stand()
                    dealer_done = True
                    print("Dealer stands with", check_value(dealer.hand.cards))
                else:
                    dealer.hand.hit(dealer)
                    print("Dealer hits to make", check_value(dealer.hand.cards))

        for hand in player.hands:
            player_hand_val = check_value(hand.cards)
            dealer_hand_val = check_value(dealer.hand.cards)

            print("Player has " + str(player_hand_val))
            print("Dealer has " + str(dealer_hand_val))

            if player_hand_val == 21 and len(hand.cards) == 2 and not(dealer_hand_val == 21 and len(dealer.hand.cards) == 2):
                player.bankroll += hand.current_bet * 2.5
                print("Player Blackjack!!\n")
                print("Player wins $" + str(hand.current_bet * 2.5), "\n")

            elif 21 >= dealer_hand_val > player_hand_val or player_hand_val == -1:
                print("Dealer wins!\n")
            elif dealer_hand_val < player_hand_val <= 21:
                player.bankroll += hand.current_bet * 2
                print("Player wins $" + str(hand.current_bet * 2), "\n")
            else:
                player.bankroll += hand.current_bet

                print("Push\n")

        player.clear_hand()
        dealer.clear_hand()

        print("Current bankroll: $", player.bankroll)
        print("Running count: " + str(dealer.shoe.running_count), "True count:" + str(dealer.shoe.true_count))
        print("Cards remaining in deck: " + str(len(dealer.deck.cards)) + "\n")

        if len(dealer.deck.cards) / (game.number_of_decks * 52) < (1 - game.penetration):
            print("New Deck!")
            dealer.shoe = Shoe(dealer)

        game.current_round += 1

    print("\nEnded with $" + str(player.bankroll) + " dollars")
    print(str(model.rounds_to_be_played) + " hands in " + str(round(time.time() - start, 4)) + " seconds!")
    return player.bankroll


if __name__ == '__main__':
    # total = 0
    # for i in range(100):
    #     total += main()
    # print(total / 100)

    main()

