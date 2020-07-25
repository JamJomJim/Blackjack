class Hand:
    def __init__(self, owner, cards, has_split, has_split_aces, current_bet):
        self.owner = owner
        self.cards = cards
        self.has_split = has_split
        self.has_split_aces = has_split_aces
        self.current_bet = current_bet

    def get_value(self):
        possible_values = [0]
        # this essentially sets up a binomial tree with all the possible values.
        for card in self.cards:
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

    def is_soft(self):
        possible_values = [0]
        for card in self.cards:
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
        if len(list(filter(lambda hand_value: hand_value <= 21, possible_values))) > 1:
            return True
        else:
            return False

    def is_splitable(self):
        return len(self.cards) == 2 and self.cards[0].rank == self.cards[1].rank

    def hit(self, dealer):
        dealer.deal(hand=self, number_cards=1)

    def double(self, dealer):
        self.owner.place_bet(self.owner.bet, self)
        dealer.deal(hand=self, number_cards=1)

    def split(self, dealer):

        new_hand = Hand(self.owner, [], False, False, 0)
        new_hand.has_split = True
        new_hand.cards = [self.cards[1]]
        dealer.deal(hand=new_hand, number_cards=1)
        new_hand.owner.place_bet(self.owner.bet, new_hand)

        self.cards = self.cards[0:1]
        self.has_split = True
        dealer.deal(hand=self, number_cards=1)

        if new_hand.cards[0].rank == "ace":
            new_hand.has_split_aces = True
            self.has_split_aces = True

        self.owner.hands.append(new_hand)

    def surrender(self, game):
        game.num_surrender += 1
        self.stand()

    def stand(self):
        pass

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self.cards)
