import time

from Dealer import Dealer
from Player import Player
from basic_strategy.hard_hand_strategy import hard_hand_strategy
from basic_strategy.soft_hand_strategy import soft_hand_strategy
from basic_strategy.splitting_hand_strategy import splitting_hand_strategy


class Game:
    def __init__(self, blackjack_payout, dealer_hit_soft17, surrender, insurance, number_of_decks, penetration):
        self.blackjack_payout = blackjack_payout
        self.dealer_hit_soft17 = dealer_hit_soft17
        self.surrender = surrender
        self.insurance = insurance
        self.number_of_decks = number_of_decks
        self.penetration = penetration
        # stats class eventually?
        # for stat in stats print stat
        self.current_round = 0
        self.wrong_bs = 0
        self.num_hits = 0
        self.num_stand = 0
        self.num_double = 0
        self.num_split = 0
        self.num_surrender = 0


class Model:
    def __init__(self, starting_amount, rounds_to_be_played, min_bet, is_manual):
        self.starting_amount = starting_amount
        self.rounds_to_be_played = rounds_to_be_played
        self.min_bet = min_bet
        self.total_bet = 0
        self.is_manual = is_manual


def find_best_move(count, player_hand, dealer_hand):
    d_index = 9 if dealer_hand.cards[0].rank == "ace" else dealer_hand.cards[0].rank - 2

    current_count = round(count + 3)
    # The strategy tables are for a true count from -3 to 3. This ensures that the current count is within those bounds
    if current_count > 3:
        current_count = 6
    elif current_count < -3:
        current_count = 0

    if player_hand.is_splittable():
        p_index = abs((9 if player_hand.cards[0].rank == "ace" else player_hand.cards[0].rank - 2) - 9)
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


def main():
    start = time.time()
    model = Model(starting_amount=0, rounds_to_be_played=10000, min_bet=10, is_manual=False)
    game = Game(blackjack_payout=1.5,
                dealer_hit_soft17=False,
                surrender=True,
                insurance=True,
                number_of_decks=4,
                # Needs to be at a point where the dealer won't run out of cards. Otherwise bugs.
                penetration=0.75)

    dealer = Dealer(number_of_decks=game.number_of_decks)
    player = Player(starting_amount=model.starting_amount, base_bet=model.min_bet)

    while game.current_round < model.rounds_to_be_played:

        player.place_bet(amount=player.determine_bet(dealer.shoe.true_count), hand=player.hands[0], model=model)

        dealer.deal(hand=player.hands[0], number_cards=2)
        # player.display_cards()

        dealer.deal(hand=dealer.hands[0], number_cards=2)
        # dealer.display_cards()

        # print("\n")

        # Checks for dealer blackjack
        # Verify these rules
        if dealer.hands[0].get_value() == 21:
            # print("Dealer Blackjack!")
            continue

        # Player's turn
        for hand in player.hands:
            hand_done = False
            while not hand_done and not hand.has_split_aces:
                player_hand_val = hand.get_value()
                # print("Player has ", hand, "worth", player_hand_val)
                if player_hand_val == 21:
                    # print("Player has 21!")
                    hand_done = True
                elif player_hand_val == -1 or player_hand_val > 21:
                    # print("Player Bust")
                    hand_done = True
                else:
                    if model.is_manual:
                        move = input("What do you want to do?\n")
                    else:
                        move = find_best_move(dealer.shoe.true_count, player_hand=hand, dealer_hand=dealer.hands[0])

                    if move == "stand":
                        # print("Player Stands.")
                        game.num_stand += 1
                        hand_done = True
                    elif move == "hit":
                        hand.hit(dealer)
                        # print("Player hits.")
                    elif move == "split" and hand.is_splittable():
                        # print("Player splits.")
                        hand.split(dealer=dealer, model=model)
                        # player.display_cards()
                    elif move == "double":
                        # print("Player doubles.")
                        hand.double(dealer=dealer, model=model)
                        # print("Player has ", hand, "worth", hand.get_value())
                        hand_done = True
                    elif move == "surrender":
                        hand.surrender(game)
                        # print("No surrender yet")
                        hand_done = True
                    else:
                        raise ValueError('An invalid move was made.')

        # Dealer's turn
        dealer_done = False
        while not dealer_done:
            dealer_hand_val = dealer.hands[0].get_value()
            # print("Dealer hand: ", dealer.hands)

            if dealer_hand_val == 21:
                # print("Dealer Lesser Blackjack!")
                dealer_done = True
            elif dealer_hand_val == -1:
                # print("Dealer busts with", dealer_hand_val)
                dealer_done = True
            else:
                if game.dealer_hit_soft17 and dealer_hand_val == 17 and dealer.hands.cards.is_soft():
                    move = "hit"
                elif dealer_hand_val <= 16:
                    move = "hit"
                else:
                    move = "stand"

                if move == "stand":
                    dealer.hands[0].stand()
                    dealer_done = True
                    # print("Dealer stands with", dealer.hands[0].get_value())
                else:
                    dealer.hands[0].hit(dealer)
                    # print("Dealer hits to make", dealer.hands[0].get_value())

        for hand in player.hands:
            player_hand_val = hand.get_value()
            dealer_hand_val = dealer.hands[0].get_value()

            # print("Player has " + str(player_hand_val))
            # print("Dealer has " + str(dealer_hand_val))
            if hand.has_surrendered:
                continue
            elif 21 >= dealer_hand_val > player_hand_val or player_hand_val == -1:
                continue
            elif hand.is_natural_21():
                if not(dealer.hands[0].is_natural_21()):
                    player.bankroll += hand.current_bet * (1 + game.blackjack_payout)
                    # print("Player Blackjack!!\n")
                    # print("Player wins $" + str(hand.current_bet * game.blackjack_payout), "\n")
                else:
                    # print("both have blackjacks")
                    player.bankroll += hand.current_bet

                # print("Dealer wins!\n")
            elif dealer_hand_val < player_hand_val <= 21:
                player.bankroll += hand.current_bet * 2
                # print("Player wins $" + str(hand.current_bet * 2), "\n")
            else:
                player.bankroll += hand.current_bet

                # print("Push\n")

        player.clear_hand()
        dealer.clear_hand()

        # print("Current bankroll: $", player.bankroll)
        # print("Running count: " + str(dealer.shoe.running_count), "True count:" + str(dealer.shoe.true_count))
        # print("Cards remaining in deck: " + str(len(dealer.shoe.cards)) + "\n")

        if len(dealer.shoe.cards) / (game.number_of_decks * 52) < (1 - game.penetration):
            # print("New Deck!")
            dealer.new_shoe()

        game.current_round += 1

    print("\nEnded with $" + str(player.bankroll) + " dollars")
    print(model.total_bet)
    print('{:.3%}'.format(player.bankroll/model.total_bet))
    print(str(model.rounds_to_be_played) + " hands in " + str(round(time.time() - start, 4)) + " seconds!")
    return player.bankroll


if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')

