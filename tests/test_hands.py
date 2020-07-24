import unittest
from Main import Hand


class TestHands(unittest.TestCase):
    def test_hard_hand(self):
        self.assertEqual(Hand(), 12)


if __name__ == '__main__':
    unittest.main()
