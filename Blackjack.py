import random

suits = {"hearts", "diamonds", "spades", "clubs"}
ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "ace"}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank) + " of " + self.suit

    def __repr__(self):
        return str(self.rank) + " of " + self.suit

    def displaysuit(self):
        print(" ", self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def displaycards(self):
        print(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)


class Dealer:
    def __init__(self):
        self.deck1 = Deck()
        self.deck1.shuffle()
        self.cards = []

    def displaycards(self, start=None):
        if start is None:
            print(self.cards)
        else:
            print("Dealer has [" + str(self.cards[0]) + ", unknown]")

    def deal(self, person, number):
        person.cards = self.deck1.cards[0:number]
        self.deck1.cards = self.deck1.cards[number:]


class Player:
    def __init__(self):
        self.cards = []

    def displaycards(self):
        print("Player has", self.cards)

    def stand(self):
        temp = 1
    def hit(self):
        temp = 1
    def double(self):
        temp = 1
    def split(self):
        temp = 1

def check_value(cards):
    cards_sum = 0
    for i in range(len(cards)):
        if cards[i].rank is "ace":
            cards_sum += 11
        else:
            cards_sum += cards[i].rank
        if cards[i].rank is "ace" and cards_sum > 21:
            cards_sum -= 10
    print(cards_sum)
    return cards_sum

dealer = Dealer()
player = Player()
dealer.deal(player, 2)
dealer.deal(dealer, 2)
check_value([Card("diamonds", "ace"), Card("diamonds", "ace")])







