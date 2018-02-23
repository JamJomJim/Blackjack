import random
import math
import numpy

# getters and setters would make things look nicer, just a refactoring thing, also its more proper
# fix bets so that they're respond dynamically to counts
# we could make count values an attribute of a card
# how aggressive the bets are flag
# have it autoplay - for now have it just hit or something, following BS can come later.


# surrender > split > double > hit > stand

suits, ranks = ["hearts", "diamonds", "spades", "clubs"], [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "ace"]
# player 17 -> 5 in hard totals
hard_hand_strategy = \
[
 [  # 2        3         4        5        6       7         8       9       10       A
  ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # -3
  ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
  ['hit',    'double', 'double', 'double', 'double','hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']],
 [  # 2        3         4        5        6       7         8       9       10       A
  ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # -2
  ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
  ['hit',    'double', 'double', 'double', 'double','hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']],
 [  # 2        3         4        5        6       7         8       9       10       A
  ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # -1
  ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
  ['hit',    'double', 'double', 'double', 'double','hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']],
 [  # 2        3         4        5        6       7         8       9       10       A
  ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # 0
  ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
  ['hit',    'double', 'double', 'double', 'double','hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']],
 [  # 2        3         4        5        6       7         8       9       10       A
  ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # 1
  ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
  ['hit',    'double', 'double', 'double', 'double','hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']],
 [  # 2        3         4        5        6       7         8       9       10       A
  ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # 2
  ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
  ['hit',    'double', 'double', 'double', 'double','hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit']],
 [  # 2        3         4        5        6       7         8       9       10       A
  ['stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand', 'stand'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['stand', 'stand', 'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],       # 3
  ['hit',    'hit',  'stand', 'stand', 'stand',  'hit',   'hit',   'hit',   'hit',   'hit'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'double'],
  ['double', 'double', 'double', 'double', 'double', 'double', 'double', 'double', 'hit', 'hit'],
  ['hit',    'double', 'double', 'double', 'double','hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
  ['hit',    'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit',   'hit'],
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

class Game:
    def __init__(self, blackjack_payout, dealer_hit_soft17, surrender, insurance, number_of_decks, penetration):
        self.blackjack_payout = blackjack_payout
        self.dealer_hit_soft17 = dealer_hit_soft17
        self.surrender = surrender
        self.insurance = insurance
        self.number_of_decks = number_of_decks
        self.penetration = penetration
        self.round = 0


class Model:
    def __init__(self, starting_amount, rounds_to_be_played, is_manual):
        self.starting_amount = starting_amount
        self.rounds_to_be_played = rounds_to_be_played
        self.is_manual = is_manual


class Shoe:
    def __init__(self, dealer, game):
        self.cards_seen = 0
        self.running_count = 0
        self.true_count = 0
        dealer.new_decks(game)


def find_best_move(player_value, dealer_value):
    strat = hard_hand_strategy[player_value][dealer_value][true_count]
    if strat != "None":
        return strat
    else:
        return "hit"


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


def count(dealer_hand, player_hand, shoe, game):

    # this needs to be changed to work after every card dealt instead of a game to game basis

    temp_hand = dealer_hand + player_hand

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
        self.hand = []

    def displaycards(self, start=None):
        if start is None:
            print(self.hand)
        else:
            print("Dealer has [" + str(self.hand[0]) + ", unknown]")

    def deal(self, person, number_cards):
        person.hand += self.deck.cards[0:number_cards]
        self.deck.cards = self.deck.cards[number_cards:]

    def hit(self, dealer):
        dealer.deal(self, 1)
        # i think this can all be "self"

    def stand(self):
        pass

    def clear_hand(self):
        self.hand = []

    def new_decks(self, game):
        self.deck = Deck(game)
        self.deck.shuffle()


class Player:
    def __init__(self, model):
        self.hand = []
        self.bankroll = model.starting_amount
        self.bet = 5

    def displaycards(self):
        print("Player has", self.hand)

    def stand(self):
        pass

    def hit(self, dealer):
        dealer.deal(self, 1)

    def double(self):
        pass

    def split(self):
        pass

    def surrender(self):
        pass

    def clear_hand(self):
        self.hand = []

    def place_bet(self):
        self.bankroll -= self.bet
        return self.bet

    def show_bankroll(self):
        print("We got", self.bankroll, "dollars boii!")

    def choose_bet(self):
        # fancy code resulting in self.bet being changed based off running or total count id remember
        pass

    def manipulate_bankroll(self, bet):
        if bet < 1:
            pass
        else:
            self.bankroll += 2 * bet


def main():
    game = Game(1.5, True, True, True, 1, 0.5)
    model = Model(200, 100, False)
    dealer = Dealer()
    player = Player(model)
    shoe = Shoe(dealer, game)
    while game.round < model.rounds_to_be_played:

        bet = player.place_bet()

        dealer.deal(player, 2)
        dealer.deal(dealer, 2)

        dealer.displaycards(1)
        player.displaycards()

        dealer_hand_val = check_value(dealer.hand)
        player_hand_val = check_value(player.hand)
    # test for card values
    # print(check_value([Card("hearts", "ace"), Card("hearts", 9), Card("hearts", "ace"), Card("hearts", "ace")]))
    # player moves

        over = False
        if player_hand_val == 21:
            print("Player Blackjack!")
            over = True
        while not over:
            player_hand_val = check_value(player.hand)
            if player_hand_val == 21:
                print("Player Lesser Blackjack!")
                over = True
            elif player_hand_val == -1 or player_hand_val > 21:
                print("Player Bust")
                over = True
            else:
                print("Player has a", player_hand_val)
                if model.is_manual:
                    move = input("Hit or Stand?\n")
                else:
                    move = find_best_move(player_hand_val, dealer_hand_val)
                if move == "stand":
                    player.stand()
                    player.displaycards()
                    print("Player stands with", player_hand_val)
                    over = True
                elif move == "hit":
                    player.hit(dealer)
                    print("Player hits.")
                    player.displaycards()
                elif move == "split":
                    player.see_card(2)
                    pass
                elif move == "double":
                    player.double()
                    pass
                elif move == "surrender":
                    player.surrender()
                    pass

        # dealer moves
        over = False
        if dealer_hand_val == 21:
            print("Dealer Blackjack!")
            over = True

        while not over:
            dealer_hand_val = check_value(dealer.hand)
            print("Dealer hand: ", dealer.hand)

            if dealer_hand_val == 21:
                print("Dealer Lesser Blackjack!")
                over = True
            elif dealer_hand_val > 21 or dealer_hand_val == -1:
                print("Dealer busts with", dealer_hand_val)
                over = True
            else:
                # if the dealer hits on a soft17 or whatever, this is searching for a card instead of a rank
                # if dealer_hand_val == 17 and dealer.hand.("ace") and dealer_hit_soft17:
                # move = "hit"
                if 1 < dealer_hand_val < 16:
                    move = "hit"
                else:
                    move = "stand"

                if move == "stand":
                    dealer.stand()
                    over = True
                    print("Dealer stands with", dealer_hand_val)

                elif move == "hit":
                    dealer.hit(dealer)
                    print("Dealer hits to make", dealer_hand_val)

                else:
                    print("Empty deck! Dealer has", dealer_hand_val)
                    over = True
        # how does this handle busting when values are -1?
        if 21 >= dealer_hand_val > player_hand_val:
            print("Dealer wins!\n")
            bet *= -1
            player.manipulate_bankroll(bet)
        elif dealer_hand_val < player_hand_val <= 21:
            print("Player wins!\n")
            player.manipulate_bankroll(bet)
        elif dealer_hand_val < 0 and dealer_hand_val == player_hand_val:
            print("You're both losers.")
        else:
            print("Push\n")

        # need to have the special payout for hitting a blackjack off the bat, maybe a flag in the manipulate function
        count(dealer.hand, player.hand, shoe, game)
        player.choose_bet()

        player.clear_hand()
        dealer.clear_hand()

        player.show_bankroll()
        print(shoe.running_count, shoe.true_count)

        if len(dealer.deck.cards) / (game.number_of_decks * 52) < (1 - game.penetration):
            print("New Deck!")
            shoe = Shoe(dealer, game)
        game.round += 1
    print(player.bankroll)


if __name__ == '__main__':
    main()
