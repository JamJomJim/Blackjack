import unittest

from Card import Card
from Hand import Hand


class TestHands(unittest.TestCase):
    def test_get_value_hard_hand(self):
        self.assertEqual(
            Hand(
                None, [Card("spades", 10), Card("spades", 2)], False, False, 0
            ).get_value(),
            12,
        )
        self.assertEqual(
            Hand(
                None, [Card("spades", "ace"), Card("spades", 2)], False, False, 0
            ).get_value(),
            13,
        )
        self.assertEqual(
            Hand(
                None, [Card("spades", "ace"), Card("spades", "ace")], False, False, 0
            ).get_value(),
            12,
        )
        self.assertEqual(
            Hand(
                None, [Card("spades", "ace"), Card("spades", 10)], False, False, 0
            ).get_value(),
            21,
        )
        self.assertEqual(
            Hand(
                None,
                [Card("spades", "ace"), Card("spades", 12), Card("spades", 2)],
                False,
                False,
                0,
            ).get_value(),
            15,
        )
        self.assertEqual(
            Hand(
                None,
                [Card("spades", "ace"), Card("spades", "ace"), Card("spades", 2)],
                False,
                False,
                0,
            ).get_value(),
            14,
        )

    def test_is_soft(self):
        self.assertEqual(
            Hand(
                None, [Card("spades", "ace"), Card("spades", 2)], False, False, 0
            ).is_soft(),
            True,
        )
        self.assertEqual(
            Hand(
                None, [Card("spades", "ace"), Card("spades", 2)], False, False, 0
            ).is_soft(),
            True,
        )
        self.assertEqual(
            Hand(
                None,
                [
                    Card("spades", "ace"),
                    Card("spades", "ace"),
                    Card("spades", "ace"),
                    Card("spades", "ace"),
                    Card("spades", "ace"),
                ],
                False,
                False,
                0,
            ).is_soft(),
            True,
        )
        self.assertEqual(
            Hand(
                None, [Card("spades", 1), Card("spades", 2)], False, False, 0
            ).is_soft(),
            False,
        )
        self.assertEqual(
            Hand(
                None, [Card("spades", 10), Card("spades", "ace")], False, False, 0
            ).is_soft(),
            True,
        )
        self.assertEqual(
            Hand(
                None,
                [Card("spades", 10), Card("spades", 5), Card("spades", "ace")],
                False,
                False,
                0,
            ).is_soft(),
            False,
        )

    def test_is_splittable(self):
        self.assertEqual(
            Hand(
                None, [Card("clubs", 3), Card("clubs", "ace")], False, False, 0
            ).is_splittable(),
            False,
        )
        self.assertEqual(
            Hand(
                None, [Card("clubs", 10), Card("clubs", 10)], False, False, 0
            ).is_splittable(),
            True,
        )
        self.assertEqual(
            Hand(
                None, [Card("clubs", "ace"), Card("clubs", "ace")], False, False, 0
            ).is_splittable(),
            True,
        )

    def test_is_natural_21(self):
        self.assertEqual(
            Hand(
                None, [Card("clubs", "ace"), Card("clubs", "ace")], False, False, 0
            ).is_natural_21(),
            False,
        )
        self.assertEqual(
            Hand(
                None, [Card("clubs", "ace"), Card("clubs", 10)], False, False, 0
            ).is_natural_21(),
            True,
        )


if __name__ == "__main__":
    unittest.main()
