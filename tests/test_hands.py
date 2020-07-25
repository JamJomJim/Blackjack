import unittest
from Main import Hand, Card


class TestHands(unittest.TestCase):
    def test_hard_hand(self):
        self.assertEqual(Hand(None, [Card("spades", 1), Card("spades", 2)], False, False, 0).get_value(), 3)

    def test_soft_hand(self):
        self.assertEqual(Hand(None, [Card("spades", "ace"), Card("spades", 2)], False, False, 0).get_value(), 13)
        self.assertEqual(Hand(None, [Card("spades", "ace"), Card("spades", "ace")], False, False, 0).get_value(), 12)
        self.assertEqual(Hand(None, [Card("spades", "ace"), Card("spades", 10)], False, False, 0).get_value(), 21)
        self.assertEqual(
            Hand(None, [Card("spades", "ace"), Card("spades", 1), Card("spades", 1)], False, False, 0).get_value(),
            13
        )
        self.assertEqual(
            Hand(None, [Card("spades", "ace"), Card("spades", "ace"), Card("spades", 1)], False, False, 0).get_value(),
            13
        )


if __name__ == '__main__':
    unittest.main()
