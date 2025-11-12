import random
import time


### Pre-Game Systems?

def play_blackjack(chip_balance, player_name):
    print(f'Welcome to Blackjack, {player_name}!')

    ### counters
    win_counter = 0
    loss_counter = 0

    # Player betting
    def player_betting():
        nonlocal chip_balance
        while True:
            player_bet = int(input(f'How much would you like to bet {player_name}? Ex(250) '))
            if player_bet > chip_balance:
                print("You don't have that much.")
                continue
            else:
                chip_balance -= player_bet
                break
        return player_bet
    
    # chip distribution calculator
    def show_chips():
        orange_chips = chip_balance//1000
        remainder = chip_balance % 1000
        purple_chips = remainder//500
        remainder = remainder % 500
        black_chips = remainder//100
        remainder = remainder % 100
        green_chips = remainder//25
        remainder = remainder % 25
        red_chips = remainder//5
        remainder = remainder % 5
        white_chips = remainder//1
        remainder = remainder % 1

        print(f'Total Chip Balance in $: ${chip_balance:,}')
        print('Chips:')
        print(f'Orange Chips($1000): {orange_chips}')
        print(f'Purple Chips($500): {purple_chips}')
        print(f'Black Chips($100): {black_chips}')
        print(f'Green Chips($25): {green_chips}')
        print(f'Red Chips($5): {red_chips}')
        print(f'White Chips($1): {white_chips}')

    ### Main Game Logic

    ### Creating the deck of cards
    deck_of_cards = []
    suits = ['H', 'D', 'C', 'S']
    card_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

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
    show_chips()

    ### while True here is for the replayability
    while True:
        ### when to reshuffle deck
        if len(deck_of_cards) == 52:
            ### Shuffle the deck at the beginning once it's made
            random.shuffle(deck_of_cards)
        
        elif len(deck_of_cards) < 6:
            deck_of_cards = []
            for rank in card_numbers:
                for suit in suits:
                    card = rank + suit
                    deck_of_cards.append(card)
            random.shuffle(deck_of_cards)
            print('The deck has been reset and reshuffled!')

        ### This is a test
        # print(deck_of_cards)

        ### Player Betting Prompt
        bet = player_betting()
        
        ### Card dealing
        Player = []
        Dealer = []

        for i in deck_of_cards:
            if len(Player) <= 1:
                card = deck_of_cards.pop(0)
                Player.append(card)
                print(f"Dealt {card} to {player_name}")
                time.sleep(0.5)
            
            if len(Dealer) == 0:
                card = deck_of_cards.pop(0)
                Dealer.append(card)
                print(f"Dealt {card} to Dealer")
                time.sleep(0.5)

            elif len(Dealer) == 1:
                card = deck_of_cards.pop(0)
                Dealer.append(card)
                print("Dealt ?? to Dealer")
                time.sleep(0.5)

        ### player and dealer total should go here as this is when the player and dealer variables come in
        player_total = calculate_hand_value(Player)
        dealer_total = calculate_hand_value(Dealer)
        ### Added the hidden card feature for the dealer
        dealer_display = [Dealer[0], '??']

        print(f'{player_name} = ' + str(Player) + ', ' + 'Total = ' + str(player_total))
        print('Dealer = ' + str(dealer_display) + ', ' + 'Total = ??')

        # This is just a check to make sure that it works correctly which it does
        # print(len(deck_of_cards))

        ### Autowin off of draw condition
        # if player_total == 21:
        #     win_counter += 1
        #     print('You Win!' + ', ' + 'Wins: ' + str(win_counter))
        # if dealer_total == 21:
        #     loss_counter += 1
        #     print('You Lose :(' + ', ' + 'Losses: ' + str(loss_counter))

        ### Player Hit, Stand, Double Down Choices
        turns = 0

        while player_total < 21:
            if turns == 0:
                player_decision = input("Would you like to Hit, Stand or Double Down(DD)? ")
            else:
                player_decision = input("Would you like to Hit, or Stand? ")
            
        ### Player Hit, Stand, Double Down cont
            if player_decision.lower() == 'hit':
                card = deck_of_cards.pop(0)
                Player.append(card)
                time.sleep(0.5)
                print(f"Dealt {card} to {player_name}")
                player_total = calculate_hand_value(Player)
                print(f'{player_name} = ' + str(Player) + ', ' + 'Total = ' + str(player_total))
                turns += 1
            
            elif player_decision.lower() == 'dd':
                if bet <= chip_balance:
                    chip_balance -= bet
                    card = deck_of_cards.pop(0)
                    Player.append(card)
                    time.sleep(0.5)
                    print(f"Dealt {card} to {player_name}")
                    player_total = calculate_hand_value(Player)
                    print(f'{player_name} = ' + str(Player) + ', ' + 'Total = ' + str(player_total))
                    break
                else:
                    print("You don't have enough chips to Double Down." )
                    continue

            elif player_decision.lower() == 'stand':
                break

        print('Dealer = ' + str(dealer_display) + ', ' + 'Total = ??')

        if player_total > 21:
            print('Dealer = ' + str(Dealer) + ', ' + 'Total = ' + str(dealer_total))
            loss_counter += 1
            time.sleep(0.5)
            print('You Lose :(' + ', ' + 'Losses: ' + str(loss_counter))
            show_chips()

        ### Player side done now onto dealers turn
        if player_total <= 21:
            print('Dealer = ' + str(Dealer) + ', ' + 'Total = ' + str(dealer_total))

            while dealer_total < 17:
                card = deck_of_cards.pop(0)
                Dealer.append(card)
                print(f"Dealt {card} to Dealer")
                time.sleep(0.5)
                dealer_total = calculate_hand_value(Dealer)
                print('Dealer = ' + str(Dealer) + ', ' + 'Total = ' + str(dealer_total))
            
            if dealer_total > 21:
                win_counter += 1
                if player_decision.lower() == 'dd':
                        chip_balance += 2 * (bet * 2)
                else:
                    chip_balance += bet * 2
                print('You Win!' + ', ' + 'Wins: ' + str(win_counter))
                show_chips()
                ### if dealer stops and player doesn't bust
            else:
                if player_total > dealer_total:
                    win_counter += 1
                    if player_decision.lower() == 'dd':
                        chip_balance += 2 * (bet * 2)
                    else:
                        chip_balance += bet * 2
                    print('You Win!' + ', ' + 'Wins: ' + str(win_counter))
                    show_chips()
                elif player_total < dealer_total:
                    loss_counter += 1
                    print('You Lose :(' + ', ' + 'Losses: ' + str(loss_counter))
                    show_chips()
                else:
                    print("It's a push")
                    if player_decision.lower() == 'dd':
                        chip_balance += bet * 2
                    else:
                        chip_balance += bet
                    show_chips()

        play_again = input('Do you want to play another hand? (Y/N) ')
        if play_again.lower() != 'y':
            print('Thanks for playing!')
            return chip_balance