import unittest

from Card import Card
from Hand import Hand
from Main import find_best_move
from ValidMovesEnum import Move


class TestFindBestMove(unittest.TestCase):

    soft_13 = Hand(None, [Card("spades", "ace"), Card("spades", 2)], False, False, 0)
    soft_16 = Hand(None, [Card("spades", "ace"), Card("spades", 5)], False, False, 0)
    hard_9 = Hand(None, [Card("spades", 6), Card("spades", 3)], False, False, 0)
    hard_17 = Hand(
        None,
        [Card("spades", 2), Card("spades", 5), Card("spades", 10)],
        False,
        False,
        0,
    )
    ace_pair = Hand(
        None,
        [Card("spades", "ace"), Card("spades", "ace")],
        False,
        False,
        0,
    )

    def test_find_best_move(self):
        self.assertEqual(
            find_best_move(count=0, player_hand=self.soft_13, dealer_hand=self.soft_16),
            Move.HIT.value,
        )
        self.assertEqual(
            find_best_move(count=0, player_hand=self.hard_17, dealer_hand=self.soft_16),
            "stand",
        )
        self.assertEqual(
            find_best_move(count=0, player_hand=self.ace_pair, dealer_hand=self.hard_9),
            "split",
        )


if __name__ == "__main__":
    unittest.main()
