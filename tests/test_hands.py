import unittest
from Hand import Hand
from Card import Card


class TestHands(unittest.TestCase):
    def test_get_value_hard_hand(self):
        self.assertEqual(Hand(None, [Card("spades", 1), Card("spades", 2)], False, False, 0).get_value(), 3)
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

    def test_is_soft(self):
        self.assertEqual(Hand(None, [Card("spades", "ace"), Card("spades", 2)], False, False, 0).is_soft(), True)
        self.assertEqual(Hand(None, [Card("spades", "ace"), Card("spades", 2)], False, False, 0).is_soft(), True)
        self.assertEqual(
            Hand(None,
                 [Card("spades", "ace"),
                  Card("spades", "ace"),
                  Card("spades", "ace"),
                  Card("spades", "ace"),
                  Card("spades", "ace")],
                 False, False, 0).is_soft(), True)
        self.assertEqual(Hand(None, [Card("spades", 1), Card("spades", 2)], False, False, 0).is_soft(), False)
        self.assertEqual(Hand(None, [Card("spades", 10), Card("spades", "ace")], False, False, 0).is_soft(), True)
        self.assertEqual(
            Hand(None, [Card("spades", 10), Card("spades", 5), Card("spades", "ace")], False, False, 0).is_soft(),
            False
        )

    def test_is_splitable(self):
        self.assertEqual(Hand(None, [Card("clubs", "ace"), Card("clubs", "ace")], False, False, 0).is_splitable(), True)


if __name__ == '__main__':
    unittest.main()
