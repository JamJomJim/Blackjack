import unittest
from Hand import Hand
from Card import Card
from Main import find_best_move


class TestFindBestMove(unittest.TestCase):

    def test_find_best_move(self):
        self.assertEqual(
            find_best_move(
                0,
                Hand(None, [Card("spades", "ace"), Card("spades", 2)], False, False, 0),
                Hand(None, [Card("spades", "ace"), Card("spades", 5)], False, False, 0)
            ),
            "hit"
        )
        self.assertEqual(
            find_best_move(
                0,
                Hand(None, [Card("spades", 2), Card("spades", 5), Card("spades", 10)], False, False, 0),
                Hand(None, [Card("spades", "ace"), Card("spades", 5)], False, False, 0)
            ),
            "stand"
        )
        self.assertEqual(
            find_best_move(
                0,
                Hand(None, [Card("spades", "ace"), Card("spades", "ace")], False, False, 0),
                Hand(None, [Card("spades", 6), Card("spades", 3)], False, False, 0)
            ),
            "split"
        )


if __name__ == '__main__':
    unittest.main()
