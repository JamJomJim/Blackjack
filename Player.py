from Hand import Hand


class Player:
    def __init__(self, starting_amount, base_bet):
        self.hands = [Hand(self, [], False, False, 0)]
        self.bankroll = starting_amount
        self.base_bet = base_bet

    def display_cards(self):
        return
        # print("Player has", self.hands)

    def clear_hand(self):
        self.hands = [Hand(self, [], False, False, 0)]

    def place_bet(self, amount, hand, model):
        # print("Player placed bet of $", amount)
        model.total_bet += amount
        self.bankroll -= amount
        hand.current_bet += amount

    def determine_bet(self, count):
        return self.base_bet * (1 if count <= 2 else count * 3)
