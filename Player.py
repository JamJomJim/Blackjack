from Hand import Hand


class Player:
    def __init__(self, model):
        self.hands = [Hand(self, [], False, False, 0)]
        self.bankroll = model.starting_amount
        self.bet = model.min_bet

    def display_cards(self):
        print("Player has", self.hands)

    def clear_hand(self):
        self.hands = [Hand(self, [], False, False, 0)]

    def place_bet(self, amount, hand):
        print("Player placed bet of $", amount)
        self.bankroll -= amount
        hand.current_bet += amount

    def determine_bet(self, count):
        return self.bet * (1 if count <= 2 else count)

    def has_natural_21(self):
        self.hands.cards[0:2]