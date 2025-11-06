import random

### counters
win_counter = 0
loss_counter = 0


### Creating the deck of cards
deck_of_cards = []
suits = ['H', 'D', 'C', 'S']
card_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

for rank in card_numbers:
    for suit in suits:
        card = rank + suit
        deck_of_cards.append(card)


### Hand Value Calculator
def calculate_hand_value(hand):
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
        print('Ace is now a 1!')
    return total

### Shuffle the deck
random.shuffle(deck_of_cards)

### Card dealing
Player = []
Dealer = []

for i in deck_of_cards:
    if len(Player) <= 1:
        card = deck_of_cards.pop(0)
        Player.append(card)
        print(f"Dealt {card} to Player")
    
    if len(Dealer) == 0:
        card = deck_of_cards.pop(0)
        Dealer.append(card)
        print(f"Dealt {card} to Dealer")
    elif len(Dealer) == 1:
        card = deck_of_cards.pop(0)
        Dealer.append(card)
        print("Dealt ?? to Dealer")

### player and dealer total should go here as this is when the player and dealer variables come in
player_total = calculate_hand_value(Player)
dealer_total = calculate_hand_value(Dealer)
### Added the hidden card feature for the dealer
dealer_display = [Dealer[0], '??']

print('Player = ' + str(Player) + ', ' + 'Total = ' + str(player_total))
print('Dealer = ' + str(dealer_display) + ', ' + 'Total = ??')

# This is just a check to make sure that it works correctly which it does
# print(len(deck_of_cards))

### Autowin off of draw condition
if player_total == 21:
   win_counter += 1
   print('You Win!' + ', ' + 'Wins: ' + str(win_counter))
if dealer_total == 21:
   loss_counter += 1
   print('You Lose :(' + ', ' + 'Losses: ' + str(loss_counter))

### Player Hit, Stand Choices
if player_total <= 21:
    player_decision = input("Would you like to Hit or Stand? ")
    
### If for Hit
    if player_decision == 'Hit' or 'hit':
        card = deck_of_cards.pop(0)
        Player.append(card)
        print(f"Dealt {card} to Player")
        player_total = calculate_hand_value(Player)

if player_total >= 21:
   loss_counter += 1
   print('You Lose :(' + ', ' + 'Losses: ' + str(loss_counter))
if dealer_total == 21:
   loss_counter += 1
   print('You Lose :(' + ', ' + 'Losses: ' + str(loss_counter))

print('Player = ' + str(Player) + ', ' + 'Total = ' + str(player_total))
print('Dealer = ' + str(dealer_display) + ', ' + 'Total = ??')
