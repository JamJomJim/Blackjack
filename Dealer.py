from Hand import Hand
from Player import Player
from Shoe import Shoe


class Dealer:
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.hand = Hand(self, [], False, False, 0)
        self.shoe = None
        self.new_shoe()

    def clear_hand(self):
        self.hand.cards = []

    def display_cards(self):
        print("Dealer has", self.hand)

    def deal(self, hand, number_cards):
        dealt_cards = self.shoe.cards[0:number_cards]
        for card in dealt_cards:
            if card.rank in [2, 3, 4, 5, 6]:
                self.shoe.running_count += 1
            elif card.rank in [10, "ace"]:
                self.shoe.running_count -= 1
        hand.cards += dealt_cards
        self.shoe.cards = self.shoe.cards[number_cards:]

    def new_shoe(self):
        self.shoe = Shoe(self.number_of_decks)
        self.shoe.shuffle()
