from Deck import Deck
from Hand import Hand
from Player import Player
from Shoe import Shoe


class Dealer(Player):
    def __init__(self, game, model):
        super().__init__(model)
        self.game = game
        self.deck = None
        self.hand = Hand(self, [], False, False, 0)
        self.shoe = Shoe(self)

    def display_cards(self):
        print("Dealer has", self.hand)

    def deal(self, hand, number_cards):
        hand.cards += self.deck.cards[0:number_cards]
        self.shoe.running_count += self.shoe.get_count()
        self.shoe.true_count = self.shoe.running_count / self.game.number_of_decks
        self.deck.cards = self.deck.cards[number_cards:]

    def clear_hand(self):
        self.hand = Hand(self, [], False, False, 0)

    def new_shoe(self):
        self.deck = Deck(self.game.number_of_decks)
        self.deck.shuffle()