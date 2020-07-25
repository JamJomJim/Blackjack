import time

from Dealer import Dealer
from Player import Player
from Shoe import Shoe
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
        self.is_manual = is_manual


def find_best_move(shoe, player_hand, dealer_hand):
    player_cards = player_hand.cards
    d_index = dealer_hand[0:1].get_value() - 2
    current_count = round(shoe.true_count)

    # The strategy tabled are for a true count from -3 to 3. This ensures that the current count is within those bounds
    if current_count > 3:
        current_count = 3
    elif current_count < -3:
        current_count = -3

    # can the hand be split
    if len(player_cards) == 2 and player_cards[0].rank == player_cards[1].rank:
        p_index = abs(player_cards[0:1].get_value() - 11)
        if splitting_hand_strategy[current_count][p_index][d_index] == "Y":
            return "split"

    p_index = abs(player_hand.get_value() - 20)
    # If the hand is soft
    if player_cards.is_soft():
        best_move = soft_hand_strategy[current_count][p_index][d_index]
    # If the hand is hard
    else:
        best_move = hard_hand_strategy[current_count][p_index][d_index]

    if best_move == "double" and (len(player_cards) > 2 or player_hand.has_split):
        best_move = "hit"

    return best_move


def main():
    start = time.time()
    game = Game(blackjack_payout=1.5,
                dealer_hit_soft17=False,
                surrender=True,
                insurance=True,
                number_of_decks=6,
                penetration=0.75)

    model = Model(starting_amount=0, rounds_to_be_played=10000, min_bet=10, is_manual=True)
    dealer = Dealer(game=game, model=model)
    player = Player(model)

    while game.current_round < model.rounds_to_be_played:

        player.place_bet(amount=player.bet, hand=player.hands[0])

        dealer.deal(hand=player.hands[0], number_cards=2)
        # player.hands[0].cards = [Card("spades", "ace"), Card("spades", "ace")]
        player.display_cards()

        dealer.deal(hand=dealer.hand, number_cards=2)
        dealer.display_cards()

        print("\n")

        # Checks for dealer blackjack
        # Verify these rules
        if dealer.hand.get_value() == 21:
            print("Dealer Blackjack!")
            continue

        # Player's turn
        for hand in player.hands:
            hand_done = False
            while not hand_done and not hand.has_split_aces:
                player_hand_val = hand.get_value()
                print("Player has ", hand, "worth", player_hand_val)
                if player_hand_val == 21:
                    print("Player has 21!")
                    hand_done = True
                elif player_hand_val == -1 or player_hand_val > 21:
                    print("Player Bust")
                    hand_done = True
                else:
                    if model.is_manual:
                        move = input("What do you want to do?\n")
                    else:
                        move = find_best_move(shoe=dealer.shoe, player_hand=hand, dealer_hand=dealer.hand.cards)

                    if move == "stand":
                        print("Player Stands.")
                        game.num_stand += 1
                        hand_done = True
                    elif move == "hit":
                        hand.hit(dealer)
                        print("Player hits.")
                    elif move == "split":
                        print("Player splits.")
                        hand.split(dealer)
                        player.display_cards()
                    elif move == "double":
                        print("Player doubles.")
                        hand.double(dealer=dealer)
                        print("Player has ", hand, "worth", hand.get_value())
                        hand_done = True
                    elif move == "surrender":
                        hand.surrender(game)
                        print("No surrender yet")
                        hand_done = True
                    else:
                        print("you can't do that")

        # Dealer's turn
        dealer_done = False
        while not dealer_done:
            dealer_hand_val = dealer.hand.get_value()
            print("Dealer hand: ", dealer.hand)

            if dealer_hand_val == 21:
                print("Dealer Lesser Blackjack!")
                dealer_done = True
            elif dealer_hand_val == -1:
                print("Dealer busts with", dealer_hand_val)
                dealer_done = True
            else:
                # if the dealer hits on a soft17 or whatever, this is searching for a card instead of a rank
                if game.dealer_hit_soft17 and dealer_hand_val == 17 and dealer.hand.cards.is_soft():
                    move = "hit"
                elif dealer_hand_val <= 16:
                    move = "hit"
                else:
                    move = "stand"

                if move == "stand":
                    dealer.hand.stand()
                    dealer_done = True
                    print("Dealer stands with", dealer.hand.get_value())
                else:
                    dealer.hand.hit(dealer)
                    print("Dealer hits to make", dealer.hand.get_value())

        for hand in player.hands:
            player_hand_val = hand.get_value()
            dealer_hand_val = dealer.hand.get_value()

            print("Player has " + str(player_hand_val))
            print("Dealer has " + str(dealer_hand_val))

            if player_hand_val == 21 and len(hand.cards) == 2 and not(dealer_hand_val == 21 and len(dealer.hand.cards) == 2):
                player.bankroll += hand.current_bet * 2.5
                print("Player Blackjack!!\n")
                print("Player wins $" + str(hand.current_bet * 2.5), "\n")

            elif 21 >= dealer_hand_val > player_hand_val or player_hand_val == -1:
                print("Dealer wins!\n")
            elif dealer_hand_val < player_hand_val <= 21:
                player.bankroll += hand.current_bet * 2
                print("Player wins $" + str(hand.current_bet * 2), "\n")
            else:
                player.bankroll += hand.current_bet

                print("Push\n")

        player.clear_hand()
        dealer.clear_hand()

        print("Current bankroll: $", player.bankroll)
        print("Running count: " + str(dealer.shoe.running_count), "True count:" + str(dealer.shoe.true_count))
        print("Cards remaining in deck: " + str(len(dealer.deck.cards)) + "\n")

        if len(dealer.deck.cards) / (game.number_of_decks * 52) < (1 - game.penetration):
            print("New Deck!")
            dealer.shoe = Shoe(dealer)

        game.current_round += 1

    print("\nEnded with $" + str(player.bankroll) + " dollars")
    print(str(model.rounds_to_be_played) + " hands in " + str(round(time.time() - start, 4)) + " seconds!")
    return player.bankroll


if __name__ == '__main__':
    # total = 0
    # for i in range(100):
    #     total += main()
    # print(total / 100)

    main()

