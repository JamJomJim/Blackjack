import unittest

from Card import Card
from Dealer import Dealer
from Main import Rules, handle_dealer_turn
from Player import Player


class TestHandleDealerTurn(unittest.TestCase):
    def setUp(self):
        self.dealer = Dealer(number_of_decks=4)
        self.rules = Rules(
            blackjack_payout=1.5,
            dealer_hit_soft_17=False,
            surrender=True,
            insurance=True,
            number_of_decks=4,
            penetration=0.75,
        )

    def test_dealer_hit_hard_15(self):
        self.dealer.hand.cards = [Card("spades", 10), Card("spades", 5)]
        self.assertEqual(self.dealer.hand.get_value(), 15)
        handle_dealer_turn(self.dealer, self.rules)
        self.assertNotEqual(self.dealer.hand.get_value(), 15)

    def test_dealer_stand_hard_17(self):
        self.dealer.hand.cards = [Card("spades", 10), Card("spades", 7)]
        self.assertEqual(self.dealer.hand.get_value(), 17)
        handle_dealer_turn(self.dealer, self.rules)
        self.assertEqual(self.dealer.hand.get_value(), 17)

    def test_dealer_stand_hard_20(self):
        self.dealer.hand.cards = [Card("spades", 10), Card("spades", 10)]
        self.assertEqual(self.dealer.hand.get_value(), 20)
        handle_dealer_turn(self.dealer, self.rules)
        self.assertEqual(self.dealer.hand.get_value(), 20)

    def test_dealer_stand_soft_17(self):
        self.rules.dealer_hit_soft_17 = False
        self.dealer.hand.cards = [Card("spades", "ace"), Card("spades", 6)]
        self.assertEqual(self.dealer.hand.get_value(), 17)
        handle_dealer_turn(self.dealer, self.rules)
        self.assertEqual(self.dealer.hand.get_value(), 17)
        self.assertEqual(len(self.dealer.hand.cards), 2)

    def test_dealer_hit_soft_17(self):
        self.rules.dealer_hit_soft_17 = True
        self.dealer.hand.cards = [Card("spades", "ace"), Card("spades", 6)]
        self.assertEqual(self.dealer.hand.get_value(), 17)
        handle_dealer_turn(self.dealer, self.rules)
        self.assertNotEqual(len(self.dealer.hand.cards), 2)


if __name__ == "__main__":
    unittest.main()
