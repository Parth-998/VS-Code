import random
import time


### Pre-Game Systems?

def run_simulation(starting_bankroll, num_hands):

    chip_balance = starting_bankroll

    ### counters
    win_counter = 0
    loss_counter = 0
    running_count = 0
    
    ### Card Counting Calculator
    def card_counting(card):
        nonlocal running_count
        rank = card[:-1]
        if rank in ['2', '3', '4', '5', '6']:
            running_count += 1
        elif rank in ['7', '8', '9']:
            running_count += 0
        elif rank in ['10', 'J', 'Q', 'K', 'A']:
            running_count -= 1
        decks_remaining = len(deck_of_cards)/52
        if decks_remaining > 0:
            true_count = running_count/decks_remaining
        else:
            true_count = 0
        return true_count
        

    ### Main Game Logic

    ### Creating the deck of cards
    num_decks = 6
    deck_of_cards = []
    suits = ['H', 'D', 'C', 'S']
    card_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    for i in range(num_decks):
        for rank in card_numbers:
            for suit in suits:
                card = rank + suit
                deck_of_cards.append(card)

    ### Hand Value Calculator
    def calculate_hand_value(hand, show_ace_message = False):
        total = 0
        count_ace = 0
        for card in hand:
            rank = card[:-1]
            if rank.isdigit():
                total += int(rank)
            elif rank in ['J', 'Q', 'K']:
                total += 10
            elif rank == 'A':
                count_ace += 1
                total += 11
        
        while total > 21 and count_ace > 0:
            total -= 10
            count_ace -= 1
            if show_ace_message:
                print('Ace is now a 1!')
                show_ace_message = False
        return total

    ### chips get shown here once before the game starts
    # show_chips()

    ### while True here is for the replayability
    for hand_num in range(num_hands):
        if hand_num % 100 == 0:
            print(f"Progress: {hand_num}/{num_hands} hands completed") 
        
        if chip_balance <= 0:
            print(f"Bankrupt at hand {hand_num}!")
            break

        ### when to reshuffle deck
        if len(deck_of_cards) == 52 * num_decks:
            random.shuffle(deck_of_cards)
        
        elif len(deck_of_cards) < 60:
            deck_of_cards = []
            for i in range(num_decks):
                for rank in card_numbers:
                    for suit in suits:
                        card = rank + suit
                        deck_of_cards.append(card)
            random.shuffle(deck_of_cards)
            running_count = 0
            print('The deck has been reset and reshuffled!')

        ### This is a test
        # print(deck_of_cards)

        ### Sim Betting
        decks_remaining = len(deck_of_cards) / 52
        if decks_remaining > 0:
            true_count = running_count / decks_remaining
        else:
            true_count = 0
        
        base_bet = 10
        if true_count <= 1:
            bet = base_bet
        elif true_count == 2:
            bet = base_bet * 2
        elif true_count == 3:
            bet = base_bet * 3
        else:
            bet = base_bet * 4

        if bet > chip_balance:
            bet = chip_balance
        
        chip_balance -= bet
        
        ### Card dealing
        Player = []
        Dealer = []

        for i in range(2):
            card = deck_of_cards.pop(0)
            card_counting(card)
            Player.append(card)
            # print(f"Dealt {card} to {player_name}")
        
        for i in range(2):
            card = deck_of_cards.pop(0)
            card_counting(card)
            Dealer.append(card)
            # print(f"Dealt {card} to Dealer")

        ### player and dealer total should go here as this is when the player and dealer variables come in
        player_total = calculate_hand_value(Player)
        dealer_total = calculate_hand_value(Dealer)
        ### Added the hidden card feature for the dealer
        dealer_display = [Dealer[0], '??']

        # print(f'{player_name} = ' + str(Player) + ', ' + 'Total = ' + str(player_total))
        # print('Dealer = ' + str(dealer_display) + ', ' + 'Total = ??')

        # This is just a check to make sure that it works correctly which it does
        # print(len(deck_of_cards))

        ### Player Hit, Stand, Double Down Choices
        if player_total == 21:
            # print('Dealer = ' + str(Dealer) + ', ' + 'Total = ' + str(dealer_total))
            if dealer_total == 21:
                # print("Both have Blackjack! It's a push")
                chip_balance += bet
            else:
                # print('Blackjack! You Win!')
                win_counter += 1
                chip_balance += int(bet * 2.5)  # Blackjack traditionally pays 3:2
            # show_chips()
            continue
        
        ### Dealer Value Checker
        dealer_up_card = Dealer[0]
        dealer_rank = dealer_up_card[:-1]

        if dealer_rank.isdigit():
            dealer_value = int(dealer_rank)
        elif dealer_rank in ['J', 'Q', 'K']:
            dealer_value = 10
        elif dealer_rank == 'A':
            dealer_value = 11

        ### Basic Automated Strategy
        is_double_down = False

        turns = 0
        
        while player_total < 21:
            #print(f"DEBUG: player_total={player_total}, dealer_value={dealer_value}, turns={turns}")
            if turns == 0 and player_total in [10, 11] and bet <= chip_balance:
                if dealer_value <= 9:
                    is_double_down = True
                    chip_balance -= bet
                    card = deck_of_cards.pop(0)
                    card_counting(card)
                    Player.append(card)
                    # print(f"Dealt {card} to {player_name}")
                    player_total = calculate_hand_value(Player)
                    # print(f'{player_name} = ' + str(Player) + ', ' + 'Total = ' + str(player_total))
                    break
            if player_total <= 11:
                card = deck_of_cards.pop(0)
                card_counting(card)
                Player.append(card)
                # print(f"Dealt {card} to {player_name}")
                player_total = calculate_hand_value(Player)
                # print(f'{player_name} = ' + str(Player) + ', ' + 'Total = ' + str(player_total))
                turns += 1
            elif player_total >= 17:
                break
            elif 12 <= player_total <= 16:
                if dealer_value >= 7:
                    card = deck_of_cards.pop(0)
                    card_counting(card)
                    Player.append(card)
                    # print(f"Dealt {card} to {player_name}")
                    player_total = calculate_hand_value(Player)
                    # print(f'{player_name} = ' + str(Player) + ', ' + 'Total = ' + str(player_total))
                    turns += 1
                else:
                    break


        # print('Dealer = ' + str(dealer_display) + ', ' + 'Total = ??')

        if player_total > 21:
            # print('Dealer = ' + str(Dealer) + ', ' + 'Total = ' + str(dealer_total))
            loss_counter += 1
            # print('You Lose :(' + ', ' + 'Losses: ' + str(loss_counter))
            # show_chips()

        ### Player side done now onto dealers turn
        if player_total <= 21:
            # print('Dealer = ' + str(Dealer) + ', ' + 'Total = ' + str(dealer_total))

            while dealer_total < 17:
                card = deck_of_cards.pop(0)
                card_counting(card)
                Dealer.append(card)
                # print(f"Dealt {card} to Dealer")
                dealer_total = calculate_hand_value(Dealer)
                # print('Dealer = ' + str(Dealer) + ', ' + 'Total = ' + str(dealer_total))
            
            if dealer_total > 21:
                win_counter += 1
                if is_double_down:
                        chip_balance += bet * 4
                else:
                    chip_balance += bet * 2
                # print('You Win!' + ', ' + 'Wins: ' + str(win_counter))
                # show_chips()
                ### if dealer stops and player doesn't bust
            else:
                if player_total > dealer_total:
                    win_counter += 1
                    if is_double_down:
                        chip_balance += bet * 4
                    else:
                        chip_balance += bet * 2
                    # print('You Win!' + ', ' + 'Wins: ' + str(win_counter))
                    # show_chips()
                elif player_total < dealer_total:
                    loss_counter += 1
                    # print('You Lose :(' + ', ' + 'Losses: ' + str(loss_counter))
                    # show_chips()
                else:
                    # print("It's a push")
                    if is_double_down:
                        chip_balance += bet * 2
                    else:
                        chip_balance += bet
                    # show_chips()

    # After the for loop ends
    print("\n=== SIMULATION COMPLETE ===")
    print(f"Starting bankroll: ${starting_bankroll:,}")
    print(f"Final bankroll: ${chip_balance:,}")
    print(f"Profit/Loss: ${chip_balance - starting_bankroll:,}")
    print(f"Total hands: {num_hands}")
    print(f"Wins: {win_counter}")
    print(f"Losses: {loss_counter}")
    print(f"Win rate: {win_counter/(win_counter+loss_counter)*100:.2f}%")
    print(f"ROI: {((chip_balance - starting_bankroll)/starting_bankroll)*100:.2f}%")

if __name__ == "__main__":
    run_simulation(10000, 10000)  # Start with $10k, run 1000 hands