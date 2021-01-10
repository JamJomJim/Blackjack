import unittest

from Card import Card
from Dealer import Dealer
from Main import (
    Model,
    Rules,
    evaluate_player_hand,
    handle_game_logic,
    handle_player_hand_turn,
)
from Player import Player


class TestHandleGameLogic(unittest.TestCase):
    def setUp(self):
        self.model = Model(starting_amount=0, rounds_to_be_played=1000000, min_bet=10)
        self.rules = Rules(
            blackjack_payout=1.5,
            dealer_hit_soft_17=False,
            surrender=True,
            insurance=True,
            number_of_decks=4,
            penetration=0.75,
        )
        self.dealer = Dealer(number_of_decks=4)
        self.player = Player(0, 10)

    def test_player_win(self):
        self.player.place_bet(
            amount=self.player.determine_bet(self.dealer.shoe.get_true_count()),
            hand=self.player.hands[0],
            model=self.model,
        )
        self.dealer.hand.cards = [Card("spades", 10), Card("spades", 7)]
        self.player.hands[0].cards = [Card("spades", 10), Card("spades", 10)]
        handle_game_logic(self.model, self.rules, self.dealer, self.player)
        self.assertEqual(self.player.bankroll, 10)

    def test_player_double_down(self):
        self.player.place_bet(
            amount=self.player.determine_bet(self.dealer.shoe.get_true_count()),
            hand=self.player.hands[0],
            model=self.model,
        )
        self.dealer.hand.cards = [
            Card("spades", 10),
            Card("spades", 10),
            Card("spades", 10),
        ]
        self.player.hands[0].cards = [Card("spades", 6), Card("spades", 5)]
        handle_game_logic(self.model, self.rules, self.dealer, self.player)
        self.assertGreaterEqual(self.player.bankroll, 20)

    def test_player_split_aces(self):
        self.player.place_bet(
            amount=self.player.determine_bet(self.dealer.shoe.get_true_count()),
            hand=self.player.hands[0],
            model=self.model,
        )
        self.dealer.hand.cards = [
            Card("spades", 10),
            Card("spades", 10),
            Card("spades", 10),
        ]
        self.player.hands[0].cards = [Card("spades", "ace"), Card("spades", "ace")]
        handle_game_logic(self.model, self.rules, self.dealer, self.player)
        self.assertGreaterEqual(self.player.bankroll, 20)

    def test_both_natural_blackjack(self):
        self.player.place_bet(
            amount=self.player.determine_bet(self.dealer.shoe.get_true_count()),
            hand=self.player.hands[0],
            model=self.model,
        )
        self.dealer.hand.cards = [Card("spades", 10), Card("spades", "ace")]
        self.player.hands[0].cards = [Card("spades", 10), Card("spades", "ace")]
        handle_game_logic(self.model, self.rules, self.dealer, self.player)
        self.assertEqual(self.player.bankroll, 0)

    def test_player_natural_blackjack(self):
        self.player.place_bet(
            amount=self.player.determine_bet(self.dealer.shoe.get_true_count()),
            hand=self.player.hands[0],
            model=self.model,
        )
        self.dealer.hand.cards = [Card("spades", 10), Card("spades", 10)]
        self.player.hands[0].cards = [Card("spades", 10), Card("spades", "ace")]
        handle_game_logic(self.model, self.rules, self.dealer, self.player)

        self.assertEqual(self.player.bankroll, 15)

    def test_player_20_vs_natural_blackjack(self):
        self.player.place_bet(
            amount=self.player.determine_bet(self.dealer.shoe.get_true_count()),
            hand=self.player.hands[0],
            model=self.model,
        )
        self.dealer.hand.cards = [Card("spades", 10), Card("spades", "ace")]
        self.player.hands[0].cards = [Card("spades", 10), Card("spades", 10)]
        handle_game_logic(self.model, self.rules, self.dealer, self.player)

        self.assertEqual(self.player.bankroll, -10)


if __name__ == "__main__":
    unittest.main()
