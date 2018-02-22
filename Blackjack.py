import random
import math
import numpy

# getters and setters would make things look nicer, just a refactoring thing, also its more proper
# fix bets so that they're respond dynamically to counts
# we could make count values an attribute of a card
# how aggressive the bets are flag
# have it autoplay - for now have it just hit or something, following BS can come later.
# add in basic strategy


# surrender > split > double > hit > stand

suits, ranks = ["hearts", "diamonds", "spades", "clubs"], [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "ace"]
# player 5-17 in hard totals
hard_hand_strategy = \
[
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
[
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
[
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
[
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
[
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
[
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
[
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']]]

# player 8 for soft totals
soft_hand_strategy = \
[
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']]]


# player 10 for splitting
splitting_hand_strategy = \
[
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']],
 [
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
  ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']]]



blackjack_payout = 1.5
dealer_hit_soft17 = True
surrender = True
insurance = True
number_of_decks = 6
penetration = 0.5

# this could be used for statistics
current_penetration = 0


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
    def __init__(self):
        self.cards = []
        for _ in range(number_of_decks):
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
        self.new_deck()
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

    def new_deck(self):
        self.deck = Deck()
        self.deck.shuffle()


class Player:
    def __init__(self):
        self.hand = []
        self.bankroll = 200
        self.bet = 5

        self.cards_seen = 0
        self.decks_remaining = number_of_decks
        self.running_count = 0
        self.true_count = 0

    def displaycards(self):
        print("Player has", self.hand)
# FIXME the passed functions

    def update_decks_remaining(self):
        self.decks_remaining = (math.floor((52 * number_of_decks - self.cards_seen)/52) +
            math.ceil((52 * number_of_decks - self.cards_seen)/52))/2

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

    def count(self, dealer_hand, player_hand):

        #this needs to be changed to work after every card dealt instead of a game to game basis

        temp_hand = dealer_hand + player_hand

        for card in temp_hand:
            if card.rank != "ace":
                if 2 <= int(card.rank) <= 6:
                    self.running_count += 1

                elif 7 <= int(card.rank) <= 9:
                    self.running_count += 0

                else:
                    self.running_count -= 1
            else:
                self.running_count -= 1

        self.true_count = math.floor(self.running_count / self.decks_remaining) # or a different rounding method

    def place_bet(self):
        self.bankroll -= self.bet
        return self.bet

    def show_bankroll(self):
        print("We got", self.bankroll, "dollars boii!")

    def choose_bet(self):
        #fancy code resulting in self.bet being changed based off running or total count id remember
        pass

    def manipulate_bankroll(self, bet):
        if bet < 1:
            pass
        else:
            self.bankroll += 2 * bet

    def see_card(self, cards_seen):
        self.cards_seen += cards_seen


def main():

    # keep in mind that all of these prints will be deleted eventually.

    dealer = Dealer()
    player = Player()

    while True:

        bet = player.place_bet()

        dealer.deal(player, 2)
        dealer.deal(dealer, 2)

        dealer.displaycards(1)
        player.displaycards()
        player.see_card(4)

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
                move = input("Hit or Stand?\n")
                if move == "stand":
                    player.stand()
                    player.displaycards()
                    print("Player stands with", player_hand_val)
                    over = True
                elif move == "hit":
                    player.hit(dealer)
                    print("Player hits.")
                    player.see_card(1)
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
                    player.see_card(1)
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
        player.count(dealer.hand, player.hand)
        player.update_decks_remaining()
        player.choose_bet()

        player.clear_hand()
        dealer.clear_hand()

        print("Decks left:", player.decks_remaining)
        player.show_bankroll()
        print(player.running_count, player.true_count)

        if len(dealer.deck.cards) / (number_of_decks * 52) < (1 - penetration):
            print("New Deck!")
            dealer.new_deck()
            # resetting counts and such
            player.running_count, player.true_count, player.cards_seen, player.decks_remaining \
                = 0, 0, 0, number_of_decks


if __name__ == '__main__':
    main()
