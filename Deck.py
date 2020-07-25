import random
from Card import Card

suits, ranks = ["hearts", "diamonds", "spades", "clubs"], [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "ace"]


class Deck:
    def __init__(self, number_of_decks):
        self.cards = []
        for _ in range(number_of_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(suit, rank))

    def display_cards(self):
        print(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)