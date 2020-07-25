import random
from Card import Card

suits, ranks = ["hearts", "diamonds", "spades", "clubs"], [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "ace"]


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

    def get_count(self):
        count = 0
        for card in self.cards:
            if card.rank in [2, 3, 4, 5, 6]:
                count += 1
            elif card.rank in [10, "ace"]:
                count -= 1
        return count
