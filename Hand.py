class Hand:
    def __init__(self, owner, cards, has_split, has_split_aces, current_bet):
        self.owner = owner
        self.cards = cards
        self.has_surrendered = False
        self.has_split = has_split
        self.has_split_aces = has_split_aces
        self.current_bet = current_bet

    def get_value(self):
        value = 0
        contains_ace = False
        for card in self.cards:
            if card.rank == "ace":
                contains_ace = True
                value += 1
            else:
                value += card.rank

        if contains_ace and value <= 11:
            value += 10

        # the highest valid hand value is returned.
        # if the player is bust, return -1.
        return value if value <= 21 else -1

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

    def is_natural_21(self):
        value = 0
        for card in self.cards[0:2]:
            value += 11 if card.rank == "ace" else card.rank
        return value == 21

    def is_splittable(self):
        return len(self.cards) == 2 and self.cards[0].rank == self.cards[1].rank

    def hit(self, dealer):
        dealer.deal(hand=self, number_cards=1)

    def double(self, dealer, model):
        self.owner.place_bet(self.current_bet, self, model)
        dealer.deal(hand=self, number_cards=1)

    def split(self, dealer, model):

        new_hand = Hand(self.owner, [], False, False, 0)
        new_hand.has_split = True
        new_hand.cards = [self.cards[1]]
        dealer.deal(hand=new_hand, number_cards=1)
        new_hand.owner.place_bet(self.current_bet, new_hand, model)

        self.cards = self.cards[0:1]
        self.has_split = True
        dealer.deal(hand=self, number_cards=1)

        if new_hand.cards[0].rank == "ace":
            new_hand.has_split_aces = True
            self.has_split_aces = True

        self.owner.hands.append(new_hand)

    def surrender(self, game):
        game.num_surrender += 1
        self.owner.bankroll += self.current_bet / 2
        self.has_surrendered = True

    def stand(self):
        pass

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self.cards)
