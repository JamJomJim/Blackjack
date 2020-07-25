from Hand import Hand
from Player import Player
from Shoe import Shoe


class Dealer(Player):
    def __init__(self, game, model):
        super().__init__(model)
        self.game = game
        self.hands = [Hand(self, [], False, False, 0)]
        self.shoe = None
        self.new_shoe()

    def display_cards(self):
        print("Dealer has", self.hands)

    def deal(self, hand, number_cards):
        dealt_cards = self.shoe.cards[0:number_cards]
        for card in dealt_cards:
            if card.rank in [2, 3, 4, 5, 6]:
                self.shoe.running_count += 1
            elif card.rank in [10, "ace"]:
                self.shoe.running_count -= 1
        self.shoe.true_count = self.shoe.running_count / (len(self.shoe.cards) / 52)
        hand.cards += dealt_cards
        self.shoe.cards = self.shoe.cards[number_cards:]

    def new_shoe(self):
        self.shoe = Shoe(self.game.number_of_decks)
        self.shoe.shuffle()
