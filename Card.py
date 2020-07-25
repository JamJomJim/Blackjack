class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank) + " of " + self.suit

    def __repr__(self):
        return "Card(\"" + str(self.suit) + "\", " + str(self.rank) + ")"

    def display_suit(self):
        print(" ", self.suit)