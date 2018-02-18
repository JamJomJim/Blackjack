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
        self.hand = []
        for suit in suits:
            for rank in ranks:
                self.hand.append(Card(suit, rank))

    def displaycards(self):
        print(self.hand)

    def shuffle(self):
        random.shuffle(self.hand)


class Dealer:
    def __init__(self):
        self.deck1 = Deck()
        self.deck1.shuffle()
        self.hand = []

    def displaycards(self, start=None):
        if start is None:
            print(self.hand)
        else:
            print("Dealer has [" + str(self.hand[0]) + ", unknown]")

    def deal(self, person, number):
        person.hand = self.deck1.hand[0:number]
        self.deck1.hand = self.deck1.hand[number:]


class Player:
    def __init__(self):
        self.hand = []

    def displaycards(self):
        print("Player has", self.hand)

    def stand(self):
        temp = 1
    def hit(self):
        temp = 1
    def double(self):
        temp = 1
    def split(self):
        temp = 1


def check_value(hand):
    hand_sum = 0
    for i in range(len(hand)):
        if hand[i].rank is "ace":
            hand_sum += 11
        else:
            hand_sum += hand[i].rank
        if hand[i].rank is "ace" and hand_sum > 21:
            hand_sum -= 10
    print(hand_sum)
    return hand_sum

dealer = Dealer()
player = Player()
dealer.deal(player, 2)
dealer.deal(dealer, 2)
print(player.hand)
check_value(player.hand)






