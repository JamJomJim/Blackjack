import random
from Card import Card

suits, ranks = ["hearts", "diamonds", "spades", "clubs"], [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "ace"]

base_deck = [Card("hearts", 2), Card("hearts", 3), Card("hearts", 4), Card("hearts", 5), Card("hearts", 6),
             Card("hearts", 7), Card("hearts", 8), Card("hearts", 9), Card("hearts", 10),
             Card("hearts", 10), Card("hearts", 10), Card("hearts", 10), Card("hearts", "ace"),

             Card("diamonds", 2), Card("diamonds", 3), Card("diamonds", 4), Card("diamonds", 5), Card("diamonds", 6),
             Card("diamonds", 7), Card("diamonds", 8), Card("diamonds", 9), Card("diamonds", 10),
             Card("diamonds", 10), Card("diamonds", 10), Card("diamonds", 10), Card("diamonds", "ace"),

             Card("spades", 2), Card("spades", 3), Card("spades", 4), Card("spades", 5), Card("spades", 6),
             Card("spades", 7), Card("spades", 8), Card("spades", 9), Card("spades", 10),
             Card("spades", 10), Card("spades", 10), Card("spades", 10), Card("spades", "ace"),

             Card("clubs", 2), Card("clubs", 3), Card("clubs", 4), Card("clubs", 5), Card("clubs", 6),
             Card("clubs", 7), Card("clubs", 8), Card("clubs", 9), Card("clubs", 10),
             Card("clubs", 10), Card("clubs", 10), Card("clubs", 10), Card("clubs", "ace")
             ]


class Shoe:
    def __init__(self, number_of_decks):
        self.running_count = 0
        self.true_count = 0
        self.cards = []
        for _ in range(number_of_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

