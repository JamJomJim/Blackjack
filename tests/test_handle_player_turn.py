import unittest

from Card import Card
from Dealer import Dealer
from Main import Model, Rules, evaluate_player_hand, handle_player_hand_turn
from Player import Player


class TestHandlePlayerTurn(unittest.TestCase):
    def setUp(self):
        self.model = Model(starting_amount=0, rounds_to_be_played=1000000, min_bet=10)
        self.dealer = Dealer(number_of_decks=4)
        self.player = Player(0, 10)
        self.rules = Rules(
            blackjack_payout=1.5,
            dealer_hit_soft_17=False,
            surrender=True,
            insurance=True,
            number_of_decks=4,
            penetration=0.75,
        )

    def test_player_stand_hard_17_vs_10(self):
        player_hand = self.player.hands[0]
        player_hand.cards = [Card("spades", 10), Card("spades", 7)]
        self.dealer.hand.cards = [Card("spades", 10), Card("spades", 7)]
        self.assertEqual(player_hand.get_value(), 17)
        handle_player_hand_turn(self.model, self.dealer, player_hand)
        self.assertEqual(player_hand.get_value(), 17)
        self.assertEqual(len(player_hand.cards), 2)

    def test_player_natural_blackjack(self):
        player_hand = self.player.hands[0]
        player_hand.cards = [Card("spades", 10), Card("spades", "ace")]
        self.dealer.hand.cards = [Card("spades", 10), Card("spades", 7)]
        self.assertEqual(player_hand.get_value(), 21)
        handle_player_hand_turn(self.model, self.dealer, player_hand)
        self.assertEqual(player_hand.get_value(), 21)
        self.assertEqual(len(player_hand.cards), 2)

    def test_evaluate_player_hand_natural_blackjack(self):
        player_hand = self.player.hands[0]
        self.player.place_bet(
            amount=self.player.determine_bet(self.dealer.shoe.get_true_count()),
            hand=player_hand,
            model=self.model,
        )
        player_hand.cards = [Card("spades", 10), Card("spades", "ace")]
        self.dealer.hand.cards = [Card("spades", 10), Card("spades", 7)]
        handle_player_hand_turn(self.model, self.dealer, player_hand)
        evaluate_player_hand(
            self.player.hands[0],
            self.player.hands[0].get_value(),
            self.dealer.hand.get_value(),
            self.dealer.hand.is_natural_21(),
            self.player,
            self.rules,
        )
        self.assertEqual(self.player.bankroll, 15)


if __name__ == "__main__":
    unittest.main()
