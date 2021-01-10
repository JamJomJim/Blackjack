import time

from basic_strategy.hard_hand_strategy import hard_hand_strategy
from basic_strategy.soft_hand_strategy import soft_hand_strategy
from basic_strategy.splitting_hand_strategy import splitting_hand_strategy
from Dealer import Dealer
from Player import Player


class Rules:
    def __init__(
        self,
        blackjack_payout,
        dealer_hit_soft_17,
        surrender,
        insurance,
        number_of_decks,
        penetration,
    ):
        self.blackjack_payout = blackjack_payout
        self.dealer_hit_soft_17 = dealer_hit_soft_17
        self.surrender = surrender
        self.insurance = insurance
        self.number_of_decks = number_of_decks
        # Needs to be at a point where the dealer won't run out of cards. Otherwise bugs.
        self.penetration = penetration


class Model:
    def __init__(self, starting_amount, rounds_to_be_played, min_bet):
        self.starting_amount = starting_amount
        self.rounds_to_be_played = rounds_to_be_played
        self.min_bet = min_bet
        self.total_bet = 0


def find_best_move(count, player_hand, dealer_hand):
    d_index = 9 if dealer_hand.cards[0].rank == "ace" else dealer_hand.cards[0].rank - 2

    current_count = round(count + 3)
    # The strategy tables are for a true count from -3 to 3. This ensures that the current count is within those bounds
    if current_count > 3:
        current_count = 6
    elif current_count < -3:
        current_count = 0

    if player_hand.is_splittable():
        p_index = abs(
            (9 if player_hand.cards[0].rank == "ace" else player_hand.cards[0].rank - 2)
            - 9
        )
        if splitting_hand_strategy[current_count][p_index][d_index] == "Y":
            return "split"

    p_index = abs(player_hand.get_value() - 20)
    if player_hand.is_soft():
        best_move = soft_hand_strategy[current_count][p_index][d_index]

    else:
        best_move = hard_hand_strategy[current_count][p_index][d_index]

    if best_move == "double" and (len(player_hand.cards) > 2 or player_hand.has_split):
        best_move = "hit"

    return best_move


def handle_dealer_turn(dealer, rules):
    while True:
        dealer_hand_val = dealer.hand.get_value()

        if dealer_hand_val == -1 or dealer_hand_val == 21:
            return dealer_hand_val

        if dealer_hand_val <= 16 or (
            rules.dealer_hit_soft_17 and dealer_hand_val == 17 and dealer.hand.is_soft()
        ):
            dealer.hand.hit(dealer)
        else:
            dealer.hand.stand()
            return dealer_hand_val


def handle_player_hand_turn(model, dealer, hand):
    while not hand.has_split_aces:
        player_hand_val = hand.get_value()

        if player_hand_val == -1 or player_hand_val >= 21:
            return

        move = find_best_move(
            dealer.shoe.get_true_count(),
            player_hand=hand,
            dealer_hand=dealer.hand,
        )

        if move == "stand":
            hand.stand()
            return
        elif move == "hit":
            hand.hit(dealer)
        elif move == "split":
            hand.split(dealer=dealer, model=model)
        elif move == "double":
            hand.double(dealer=dealer, model=model)
            return
        elif move == "surrender":
            hand.surrender()
            return
        else:
            raise ValueError("An invalid move was made.")


def print_stats(player, model, time_played):
    print(f"\nEnded with ${str(player.bankroll)} dollars")
    print(model.total_bet)
    print("{:.3%}".format(player.bankroll / model.total_bet))
    print(f"{str(model.rounds_to_be_played)} hands in {str(time_played)} seconds!")


def evaluate_player_hand(hand, dealer_hand_val, dealer_natural_21, player, rules):
    player_hand_val = hand.get_value()
    if (
        player_hand_val == -1
        or 21 >= dealer_hand_val > player_hand_val
        or hand.has_surrendered
    ):
        return

    if hand.is_natural_21():
        if dealer_natural_21:
            player.bankroll += hand.current_bet
        else:
            player.bankroll += hand.current_bet * (1 + rules.blackjack_payout)

    elif dealer_hand_val < player_hand_val <= 21:
        player.bankroll += hand.current_bet * 2
    else:
        player.bankroll += hand.current_bet


def handle_game_logic(model, rules, dealer, player):
    dealer_hand_val = handle_dealer_turn(dealer, rules)
    dealer_natural_21 = dealer.hand.is_natural_21()
    for hand in player.hands:
        handle_player_hand_turn(model, dealer, hand)
        evaluate_player_hand(hand, dealer_hand_val, dealer_natural_21, player, rules)


def check_needs_new_shoe(rules, dealer):
    if len(dealer.shoe.cards) / (rules.number_of_decks * 52) < (1 - rules.penetration):
        dealer.new_shoe()


def main():
    start = time.time()
    model = Model(starting_amount=0, rounds_to_be_played=10000, min_bet=10)
    rules = Rules(
        blackjack_payout=1.5,
        dealer_hit_soft_17=False,
        surrender=True,
        insurance=True,
        number_of_decks=4,
        penetration=0.75,
    )

    dealer = Dealer(number_of_decks=rules.number_of_decks)
    player = Player(starting_amount=model.starting_amount, base_bet=model.min_bet)

    current_round = 0
    while current_round < model.rounds_to_be_played:
        player.place_bet(
            amount=player.determine_bet(dealer.shoe.get_true_count()),
            hand=player.hands[0],
            model=model,
        )

        dealer.deal(hand=player.hands[0], number_cards=2)
        dealer.deal(hand=dealer.hand, number_cards=2)

        handle_game_logic(model, rules, dealer, player)

        player.clear_hand()
        dealer.clear_hand()

        check_needs_new_shoe(rules, dealer)

        current_round += 1

    print_stats(player, model, time_played=round(time.time() - start, 4))


if __name__ == "__main__":
    import cProfile

    cProfile.run("main()")
    # main()
