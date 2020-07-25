import unittest

from Dealer import Dealer
from Player import Player


class TestFindBestMove(unittest.TestCase):

    def test_new_shoe(self):
        dealer = Dealer(number_of_decks=4)
        self.assertEqual(len(dealer.shoe.cards), 4*52)

    def test_deal(self):
        dealer = Dealer(number_of_decks=4)
        player = Player(base_bet=10, starting_amount=0)

        deck_copy = dealer.shoe.cards.copy()
        dealer.deal(dealer.hands[0], 2)
        dealer.deal(player.hands[0], 2)
        self.assertEqual(len(dealer.shoe.cards), 4 * 52 - 4)
        self.assertEqual(dealer.hands[0].cards, deck_copy[0:2])
        self.assertEqual(player.hands[0].cards, deck_copy[2:4])


if __name__ == '__main__':
    unittest.main()
