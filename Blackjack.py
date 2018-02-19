import random
#NOTE cards in the deck are going to have to be removed from play eventually and somehow
#NOTE I'm also assuming that there are going to be multiple player objects?
suits, ranks = {"hearts", "diamonds", "spades", "clubs"}, {2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "ace"}

blackjackpayout = 1.5
dealerhitsoft17 = True #note depends
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
    #I think we need a pointer that lets us know where in the deck we are, or a discard played card function
    def __init__(self):
        self.deck1 = Deck()
        self.deck1.shuffle()
        #NOTE I'm assuming that they're named "1" and stuff because we can set a value to determine the number of total decks that the dealer can have?
        self.hand = []

    def displaycards(self, start=None):
        if start is None:
            print(self.hand)
        else:
            print("Dealer has [" + str(self.hand[0]) + ", unknown]")

    def deal(self, person, numcards):
        #noTE maybe lets not do this 0-indexed, although thats just a sematic thing
        #NOTE I'm pretty sure this will keep picking the same cards over and over
        person.hand += self.deck1.hand[0:numcards]
        #adds the next set of cards to the dealers hand, NOTE shouldn't it deal sequentially? not all at once, does that even matter?
        self.deck1.hand = self.deck1.hand[numcards:]
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
#FIXME the passed functions
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
    #TODO how to handle doubles
    hand_sum = 0
    for card in hand:
        if card.rank == "ace":
            hand_sum += 11
        else:
            hand_sum += card.rank

        if card.rank == "ace" and hand_sum > 21:
            hand_sum -= 10
    return hand_sum

def main():
    dealer = Dealer()
    player = Player()
    dealer.deal(player, 2)
    dealer.deal(dealer, 2)
    dealer.displaycards(1)
    player.displaycards()
    player_hand_val = check_value(player.hand)
    dealer_hand_val = check_value(dealer.hand)

    #player moves
    if player_hand_val == 21:
        print("Player Blackjack!")
    else:
        over = False
        while not over:
            player_hand_val = check_value(player.hand)
            print("Player points", player_hand_val)
            if player_hand_val == 21:
                print("Player Lesser Blackjack!")
                over = True
            elif player_hand_val > 21:
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

    #dealer moves
    if dealer_hand_val == 21:
        print("Dealer Blackjack!")
        #exit() shouldn't mess things up, but keep this in mind, might break out of the entire program i can't remember
    else:
        over = False
        print("Dealer has", dealer_hand_val)
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
                #if the dealer hits on a soft17 or whatever
                if dealer_hand_val == 17 and "ace" in dealer.hand and dealerhitsoft17:
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
    if dealer_hand_val > player_hand_val and dealer_hand_val <= 21:
        print("Dealer wins!")
    elif dealer_hand_val < player_hand_val and player_hand_val <= 21:
        print("Player wins!")
    else:
        print("Push")

if __name__ == '__main__':
    main()