from Hand import Hand
from Player import Player
from Shoe import Shoe


class Dealer(Player):
    def __init__(self, game, model):
        super().__init__(model)
        self.game = game
        self.hand = Hand(self, [], False, False, 0)
        self.shoe = None
        self.new_shoe()

    def deal(self, hand, number_cards):
        hand.cards += self.shoe.cards[0:number_cards]
        self.shoe.cards = self.shoe.cards[number_cards:]

    def new_shoe(self):
        self.shoe = Shoe(self.game.number_of_decks)
        self.shoe.shuffle()
