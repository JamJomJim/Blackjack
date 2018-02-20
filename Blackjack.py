import random
suits, ranks = ["hearts", "diamonds", "spades", "clubs"], [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "ace"]

blackjack_payout = 1.5
dealer_hit_soft17 = True
number_of_decks = 2


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
        for _ in range(number_of_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(suit, rank))

    def display_cards(self):
        print(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)


class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hand = []

    def displaycards(self, start=None):
        if start is None:
            print(self.hand)
        else:
            print("Dealer has [" + str(self.hand[0]) + ", unknown]")

    def deal(self, person, numcards):
        person.hand += self.deck.cards[0:numcards]
        self.deck.cards = self.deck.cards[numcards:]

    def hit(self, dealer):
        dealer.deal(self, 1)

    def stand(self):
        pass


class Player:
    def __init__(self):
        self.hand = []
        self.bet = 0
        self.card_count = 0

    def displaycards(self):
        print("Player has", self.hand)
# FIXME the passed functions

    def stand(self):
        pass

    def hit(self, dealer):
        dealer.deal(self, 1)

    def double(self):
        pass

    def split(self):
        pass

    def surrender(self):
        pass


def check_value(hand):
    possible_values = [0]
    # this essentially sets up a binomial tree with all the possible values.
    for card in hand:
        if card.rank == "ace":
            temp_values = list(possible_values)
            for value in possible_values:
                temp_values.append(value + 1)
                temp_values.append(value + 11)
                temp_values.remove(value)
            possible_values = temp_values
        else:
            for i, value in enumerate(possible_values):
                possible_values[i] += card.rank
    # lambda sets up an anonymous function that returns a bool.
    # filter returns the values in possible_values that satisfy this function.
    # these values are then turned into a list, and possible_values is set to that list.
    possible_values = list(filter(lambda hand_value: hand_value <= 21, possible_values))
    # the highest valid hand value is then returned.
    # if the player is bust, return -1.
    return max(possible_values + [-1])


def main():

    # keep in mind that all of these prints will be deleted eventually.

    dealer = Dealer()
    player = Player()

    dealer.deal(player, 2)
    dealer.deal(dealer, 2)

    dealer.displaycards(1)
    player.displaycards()

    dealer_hand_val = check_value(dealer.hand)
    player_hand_val = check_value(player.hand)
    # test for card values
    # print(check_value([Card("hearts", "ace"), Card("hearts", 9), Card("hearts", "ace"), Card("hearts", "ace")]))
    # player moves
    over = False
    if player_hand_val == 21:
        print("Player Blackjack!")
        over = True
    while not over:
        player_hand_val = check_value(player.hand)
        print("Player points", player_hand_val)
        if player_hand_val == 21:
            print("Player Lesser Blackjack!")
            over = True
        elif player_hand_val == -1 or player_hand_val > 21:
            print("Player Bust")
            over = True
            print("Player points", player_hand_val)
        else:
            move = input("Hit or Stand?")
            if move == "stand":
                player.stand()
                player.displaycards()
                over = True
            elif move == "hit":
                player.hit(dealer)
                player.displaycards()
            elif move == "split":
                pass
            elif move == "double":
                pass
            elif move == "surrender":
                pass

    # dealer moves
    over = False
    if dealer_hand_val == 21:
        print("Dealer Blackjack!")
        over = True
    print("Dealer has", check_value(dealer.hand))
    while not over:
        dealer_hand_val = check_value(dealer.hand)
        print("Dealer hand", dealer.hand)
    # print("Dealer points", dealer_hand_val)
        if dealer_hand_val == 21:
            print("Dealer Lesser Blackjack!")
            over = True
        elif dealer_hand_val > 21:
            print("Dealer Bust with", dealer_hand_val)
            over = True
        else:
            # if the dealer hits on a soft17 or whatever
            if dealer_hand_val == 17 and "ace" in dealer.hand and dealer_hit_soft17:
                move = "hit"
            elif 1 < dealer_hand_val < 16:
                move = "hit"
            else:
                move = "stand"

            if move == "stand":
                dealer.stand()
                over = True
                print("Dealer points", dealer_hand_val)
            elif move == "hit":
                dealer.hit(dealer)
                print("Dealer points", dealer_hand_val)
        dealer.displaycards(None)
    if 21 >= dealer_hand_val > player_hand_val:
        print("Dealer wins!")
    elif dealer_hand_val < player_hand_val <= 21:
        print("Player wins!")
    else:
        print("Push")


if __name__ == '__main__':
    main()
