class Shoe:
    def __init__(self, dealer):
        self.running_count = 0
        self.true_count = 0
        dealer.new_shoe()

    def get_count(self):
        count = 0
        for card in self:
            if card.rank in [2, 3, 4, 5, 6]:
                count += 1
            elif card.rank in [10, "ace"]:
                count -= 1
        return count
