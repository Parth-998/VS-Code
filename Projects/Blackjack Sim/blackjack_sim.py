import random
import matplotlib.pyplot as plot


### Pre-Game Systems?

def run_simulation(starting_bankroll, num_hands, use_card_counting = True):

    chip_balance = starting_bankroll

    ### counters
    win_counter = 0
    loss_counter = 0
    running_count = 0
    bankroll_history = []
    
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
        if use_card_counting:
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
            elif true_count >= 4:
                bet = base_bet * 4
        
        else:
            bet = 10

        if bet > chip_balance:
            bet = chip_balance
        
        chip_balance -= bet
        
        ### Card dealing
        Player = []
        Dealer = []

        ### Realistic Dealing
        for i in range(4):
            card = deck_of_cards.pop(0)
            card_counting(card)
            if i % 2 == 0:
                Player.append(card)
            else:
                Dealer.append(card)

        ### player and dealer total should go here as this is when the player and dealer variables come in
        player_total = calculate_hand_value(Player)
        dealer_total = calculate_hand_value(Dealer)
        ### Added the hidden card feature for the dealer
        # dealer_display = [Dealer[0], '??']

        # This is just a check to make sure that it works correctly which it does
        # print(len(deck_of_cards))

        ### Player Hit, Stand, Double Down Choices
        if player_total == 21:
            if dealer_total == 21:
                chip_balance += bet
            else:
                win_counter += 1
                chip_balance += int(bet * 2.5)
            bankroll_history.append(chip_balance)
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
                    player_total = calculate_hand_value(Player)
                    break
            if player_total <= 11:
                card = deck_of_cards.pop(0)
                card_counting(card)
                Player.append(card)
                player_total = calculate_hand_value(Player)
                turns += 1
            elif player_total >= 17:
                break
            elif 12 <= player_total <= 16:
                if dealer_value >= 7:
                    card = deck_of_cards.pop(0)
                    card_counting(card)
                    Player.append(card)
                    player_total = calculate_hand_value(Player)
                    turns += 1
                else:
                    break

        if player_total > 21:
            loss_counter += 1

        ### Player side done now onto dealers turn
        if player_total <= 21:

            while dealer_total < 17:
                card = deck_of_cards.pop(0)
                card_counting(card)
                Dealer.append(card)
                dealer_total = calculate_hand_value(Dealer)
            
            if dealer_total > 21:
                win_counter += 1
                if is_double_down:
                        chip_balance += bet * 4
                else:
                    chip_balance += bet * 2
            else:
                if player_total > dealer_total:
                    win_counter += 1
                    if is_double_down:
                        chip_balance += bet * 4
                    else:
                        chip_balance += bet * 2
                elif player_total < dealer_total:
                    loss_counter += 1
                else:
                    if is_double_down:
                        chip_balance += bet * 2
                    else:
                        chip_balance += bet
        
        bankroll_history.append(chip_balance)

    ### After the for loop ends
    print("\nSIMULATION COMPLETE")
    print(f"Starting Bankroll: ${starting_bankroll:,}")
    print(f"Final Bankroll: ${chip_balance:,}")
    print(f"Profit/Loss: ${chip_balance - starting_bankroll:,}")
    print(f"Total Hands: {num_hands}")
    print(f"Wins: {win_counter}")
    print(f"Losses: {loss_counter}")
    print(f"Win Rate: {win_counter/(win_counter + loss_counter)*100:.2f}%")
    print(f"ROI: {((chip_balance - starting_bankroll)/starting_bankroll)*100:.2f}%")

    return {'final_bankroll': chip_balance,
        'profit_loss': chip_balance - starting_bankroll,
        'wins': win_counter,
        'losses': loss_counter,
        'win_rate': win_counter/(win_counter + loss_counter)*100,
        'roi': ((chip_balance - starting_bankroll)/starting_bankroll)*100,
        'bankroll_history': bankroll_history}

### 1 10k hand run per strat to vizualize and compare the outcomes per hand and overall at the end
def visualize_comparison(starting_bankroll, num_hands):
    ### Runnings Sims
    print("\nRunning Card Counting Simulation")
    counting_results = run_simulation(starting_bankroll, num_hands, use_card_counting=True)
    
    print("\nRunning Flat Betting Simulation")
    flat_results = run_simulation(starting_bankroll, num_hands, use_card_counting=False)

    ### Printing Results
    print("\nCard Counting Results")
    print(f"Final Bankroll: {counting_results['final_bankroll']}")
    print(f"Profit/Loss: {counting_results['profit_loss']}")
    print(f"Win Rate: {counting_results['win_rate']}")

    print("\nFlat Bet Results")
    print(f"Final Bankroll: {flat_results['final_bankroll']}")
    print(f"Profit/Loss: {flat_results['profit_loss']}")
    print(f"Win Rate: {flat_results['win_rate']}")

    print("\nComparison:")
    print(f"Bankroll Difference: {counting_results['final_bankroll'] - flat_results['final_bankroll']}")
    
    overall_roi = round(counting_results['roi'] - flat_results['roi'], 2)
    print(f"ROI Difference: {overall_roi}%")
    
    ### Plotting
    plot.figure(figsize = (12, 6))
    
    plot.plot(counting_results['bankroll_history'], label = 'Card Counting', linewidth = 2)
    plot.plot(flat_results['bankroll_history'], label = 'Flat Betting', linewidth = 2)
    
    plot.axhline(y=starting_bankroll, color = 'black', linestyle = '--', label = 'Starting Bankroll')

    plot.xlabel('Hand Number')
    plot.ylabel('Bankroll ($)')
    plot.title(f'Blackjack Strategy Comparison - {num_hands} Hands')
    plot.legend()
    plot.grid(True, alpha = 0.3)
    plot.xlim(0, num_hands)

    plot.savefig('blackjack_comparison.png', dpi = 500, bbox_inches = 'tight')
    plot.show()
    
    print("\nGraph saved as 'blackjack_comparison.png'")

### Monte Carlo Analysis based on 100 10k hand runs for card counting and flat bets and compared to see which is the best overall
def monte_carlo_analysis(starting_bankroll, num_hands, num_simulations):
    """
    Run Monte Carlo simulation comparing card counting vs flat betting.
    
    Arguments:
        starting_bankroll: Initial money to start with
        num_hands: Number of hands per simulation
        num_simulations: Number of times to run the simulation
    
    Returns:
        Avg Final Data Summary and Histograms(Side by Side & Overlapping)
    """


    ### Counting Finals after 100 Runs
    counting_final_bankrolls = []
    counting_final_profit_loss = []
    counting_final_win_rate = []
    
    ### Flat Finals after 100 Runs
    flat_final_bankrolls = []
    flat_final_profit_loss = []
    flat_final_win_rate = []
    
    ### Running 100 Times
    for i in range(num_simulations):
        print(f'Simulation {i+1}/{num_simulations}')
        print("\nRunning Card Counting Simulation")
        counting_results = run_simulation(starting_bankroll, num_hands, use_card_counting=True)
        counting_final_bankrolls.append(counting_results['final_bankroll'])
        counting_final_profit_loss.append(counting_results['profit_loss'])
        counting_final_win_rate.append(counting_results['win_rate'])
                
        print("\nRunning Flat Betting Simulation")
        flat_results = run_simulation(starting_bankroll, num_hands, use_card_counting=False)
        flat_final_bankrolls.append(flat_results['final_bankroll'])
        flat_final_profit_loss.append(flat_results['profit_loss'])
        flat_final_win_rate.append(flat_results['win_rate'])
    
    ### Avg from 100 Runs for Counting
    avg_counting_bankroll = sum(counting_final_bankrolls)/num_simulations
    avg_counting_profit_loss = sum(counting_final_profit_loss)/num_simulations
    avg_counting_win_rate = sum(counting_final_win_rate)/num_simulations

    ### Avg from 100 Runs for Flat
    avg_flat_bankroll = sum(flat_final_bankrolls)/num_simulations
    avg_flat_profit_loss = sum(flat_final_profit_loss)/num_simulations
    avg_flat_win_rate = sum(flat_final_win_rate)/num_simulations


    counting_wins = 0
    for i in range(num_simulations):
        if counting_final_bankrolls[i] > flat_final_bankrolls[i]:
            counting_wins += 1

    ### Printing Results
    print("\nMONTE CARLO SUMMARY")

    print("\nSummary of Card Counting Results")
    print(f"Avg Final Bankroll: {avg_counting_bankroll}")
    print(f"Avg Profit/Loss: {avg_counting_profit_loss}")
    print(f"Avg Win Rate: {avg_counting_win_rate}")

    print("\nSummary of Flat Bet Results")
    print(f"Avg Final Bankroll: {avg_flat_bankroll}")
    print(f"Avg Profit/Loss: {avg_flat_profit_loss}")
    print(f"Avg Win Rate: {avg_flat_win_rate}")

    print("\nComparison:")
    print(f"Card Counting won {counting_wins} out of {num_simulations} simulations ({counting_wins/num_simulations*100:.1f}%)")
    print(f"Average bankroll difference: ${avg_counting_bankroll - avg_flat_bankroll:,.2f}")   

    ### Plotting Histogram Overlapping
    plot.figure(figsize = (12, 6))
    
    all_data = counting_final_bankrolls + flat_final_bankrolls
    bins = plot.hist(all_data, bins=30, alpha=0)[1]

    plot.hist(counting_final_bankrolls, bins = bins, alpha = 0.6, label = 'Card Counting', color = 'blue', edgecolor = 'black', rwidth = 1.0)
    plot.hist(flat_final_bankrolls, bins = bins, alpha = 0.6, label = 'Flat Betting', color = 'orange', edgecolor = 'black', rwidth = 1.0)

    plot.axvline(x = starting_bankroll, color = 'black', linestyle = '--', linewidth = 2, label = 'Starting Bankroll')

    plot.xlabel('Final Bankroll ($)')
    plot.ylabel('Frequency (Number of Simulations)')
    plot.title(f'Monte Carlo Analysis Histogram ({num_simulations}) Simulations')
    plot.legend()
    plot.grid(True, alpha = 0.3, axis = 'y')

    plot.savefig('monte_carlo_histogram_overlapping.png', dpi = 500, bbox_inches = 'tight')
    plot.show()

    ### Plotting Histogram Side by Side
    fig, (ax1, ax2) = plot.subplots(1, 2, figsize=(16, 6))

    # Left plot for Card Counting
    ax1.hist(counting_final_bankrolls, bins=30, alpha=0.7, color='blue', edgecolor='black')
    ax1.axvline(x=starting_bankroll, color='black', linestyle='--', linewidth=2, label='Starting Bankroll')
    ax1.set_xlabel('Final Bankroll ($)')
    ax1.set_ylabel('Frequency')
    ax1.set_title('Card Counting Distribution')
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='y')

    # Right plot for Flat Betting
    ax2.hist(flat_final_bankrolls, bins=30, alpha=0.7, color='orange', edgecolor='black')
    ax2.axvline(x=starting_bankroll, color='black', linestyle='--', linewidth=2, label='Starting Bankroll')
    ax2.set_xlabel('Final Bankroll ($)')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Flat Betting Distribution')
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')

    y_max = max(ax1.get_ylim()[1], ax2.get_ylim()[1])
    x_min = min(ax1.get_xlim()[0], ax2.get_xlim()[0])
    x_max = max(ax1.get_xlim()[1], ax2.get_xlim()[1])

    ax1.set_ylim(0, y_max)
    ax2.set_ylim(0, y_max)
    ax1.set_xlim(x_min, x_max)
    ax2.set_xlim(x_min, x_max)
    
    plot.suptitle(f'Monte Carlo Analysis - {num_simulations} Simulations Per Strategy', fontsize=14)
    plot.tight_layout()

    plot.savefig('monte_carlo_histogram_side_by_side.png', dpi=500, bbox_inches='tight')
    plot.show()

if __name__ == "__main__":
    # visualize_comparison(10000, 10000) #(starting_bankroll, num_hands)
    monte_carlo_analysis(10000,10000,100) #(starting_bankroll, num_hands, num_simulations)