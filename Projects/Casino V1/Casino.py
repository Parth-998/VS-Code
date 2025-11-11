import time
from Black_Jack_Game import blackjack
import sys
sys.path.append(r'Projects\Casino V1\Black_Jack_Game')
import blackjack


### Counter
balance = 0
chip_balance = 0

### Defs

### Chip Buying
def buy_chips():
    global balance, chip_balance, player_name

    if chip_balance > 0:
        print(f'You Current Chip Balance is: ${chip_balance:,}')
        pass

    chip_buying = input('Would you like to buy chips? (Y/N) ')

    if chip_buying.lower() == 'y':
        while True:
            try:
                chips = int(input(f'How many $ of chips would you like to buy? Current Balance: ${balance:,} '))
                if chips > 0:
                    break
                else:
                    print('no negative numbers')
            except ValueError:
                print('error about invalid input (decimals, letters, etc.)')
        
        if chips <= balance:
            chip_balance += chips
            balance -= chips
            
            with open('Projects\Casino V1\Data Files\players.txt', 'r') as file:
                lines = file.readlines()
            updated_lines = []
            for line in lines:
                name, saved_balance, saved_chips = line.strip().split(',')
                if name == player_name:
                    updated_lines.append(f'{player_name},{balance},{chip_balance}\n')
                else:
                    updated_lines.append(line)
            with open('Projects\Casino V1\Data Files\players.txt', 'w') as file:
                file.writelines(updated_lines)
            
            # chip distribution calculator
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

            print(f'Remaining Balance: ${balance:,}')
            print(f'Total Chip Balance in $: ${chip_balance:,}')
            print('Chips:')
            print(f'Orange Chips($1000): {orange_chips}')
            print(f'Purple Chips($500): {purple_chips}')
            print(f'Black Chips($100): {black_chips}')
            print(f'Green Chips($25): {green_chips}')
            print(f'Red Chips($5): {red_chips}')
            print(f'White Chips($1): {white_chips}')


        else:
            print('HAHA BROKIE!')
            time.sleep(0.5)
            print('What do you think you are doing here!')
            print('Hey Everyone! Look at this person. Coming in here with no money to their name.')
            time.sleep(0.5)
            print('Security take them out please.')
            print('Let us forget this even happened.')

    elif chip_buying.lower() == 'n':
        pass


while True:
    ### Starting Prompts
    new_or_returning_player = input('Are you a New or Returning player? ')

    ### New Player
    if new_or_returning_player.lower() == 'new':
        player_name = input('What is your name? Ex: "John Smith" ')
        
        name_exists = False
        with open('Projects\Casino V1\Data Files\players.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, saved_balance, chips = line.strip().split(',')
                chips = int(chips)
                if name == player_name:
                    name_exists = True
                    break
        
        if name_exists:
            print("This name already exists! Please try logging in as a returning player.")
            continue

        print(f'Welcome In {player_name}!')
        
        while True:
            try:
                balance = int(input('How much would you like to Deposit today? '))
                if balance > 0:
                    break
                else:
                    print('no negative numbers')
            except ValueError:
                print('error about invalid input (decimals, letters, etc.)')
        while True:
            depo_input = input(f'You have deposited ${balance:,}. Would you like to deposit more? (Y/N) ')
            if depo_input.lower() == 'y':
                while True:
                    try:
                        balance_addon = int(input('How much more would you like to deposit? '))
                        if balance_addon > 0:
                            break
                        else:
                            print('no negative numbers')
                    except ValueError:
                        print('error about invalid input (decimals, letters, etc.)')
                balance += balance_addon
                print(f'You now have ${balance:,}.')
                # Store this next to the player name with the final amount
            if depo_input.lower() == 'n':
                break
        # Store the player name in a file
        with open('Projects\Casino V1\Data Files\players.txt', 'a') as file:
            file.write(f'{player_name},{balance},{chip_balance}\n')
        break

    ### Returning Player
    elif new_or_returning_player.lower() == 'returning':
        
        player_name = input('What is your name? Ex: "John Smith" ')
        player_found = False

        with open('Projects\Casino V1\Data Files\players.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, saved_balance, chips = line.strip().split(',')
                if name == player_name:
                    player_found = True
                    balance = int(saved_balance)
                    chip_balance = int(chips)
        
        if not player_found:
            print("Player not found! Please register as a new player.")
            continue

        print(f'Welcome Back {player_name}!')
        print(f'Your Current Balance is: ${balance:,}')
        print(f'You Current Chip Balance is: ${chip_balance:,}')

        while True:
            depo_input = input('Would you like to deposit more money? (Y/N) ')
            if depo_input.lower() == 'y':
                while True:
                    try:
                        balance_addon = int(input('How much more would you like to deposit? '))
                        if balance_addon > 0:
                            break
                        else:
                            print('no negative numbers')
                    except ValueError:
                        print('error about invalid input (decimals, letters, etc.)')
                balance += balance_addon
                print(f'You now have ${balance:,}.')
                # Store this next to the player name with the final amount
            if depo_input.lower() == 'n':
                break
        # Balance updating
        with open('Projects\Casino V1\Data Files\players.txt', 'r') as file:
            lines = file.readlines()
        updated_lines = []
        for line in lines:
            name, saved_balance, chips = line.strip().split(',')
            if name == player_name:
                updated_lines.append(f'{player_name},{balance},{chip_balance}\n')
            else:
                updated_lines.append(line)
        with open('Projects\Casino V1\Data Files\players.txt', 'w') as file:
            file.writelines(updated_lines)
        
        break

### New Player Chip Buying
if new_or_returning_player.lower() == 'new':
    buy_chips()

print(f'Your balance is ${balance:,}.')

### Main Menu

while True:
    print('Main Menu')
    print('1. Games')
    print('2. Chip Buying')
    print('3. Cash Out Chips')
    print('4. Show Balances')
    print('5. Save & Exit')
    while True:
        try:
            menu_selection = int(input('Please type the # of the menu option. Ex: "1" '))
            if menu_selection >= 1 and menu_selection <= 5:
                break
            else:
                print("Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number")

    if menu_selection == 1:
        print('Games:')
        print('1. BlackJack')
        game_selection = int(input('Please type the # of the game. Ex: "1" '))
        if game_selection == 1:
            #take the player to blackjack. I forgot how to do this.
            chip_balance = blackjack.play_blackjack(chip_balance, player_name)
        # This else clause is temp until I add more games.
        else:
            pass
    
    elif menu_selection == 2:
        buy_chips()
    
    elif menu_selection == 3:
        print(f'Your Chip Balance is: ${chip_balance:,}')
        chip_cash_out = input('Are you sure you want to Cash Out now? (Y/N) ')
        if chip_cash_out.lower() == 'y':
            balance += chip_balance
            chip_balance = 0
            
            with open('Projects\Casino V1\Data Files\players.txt', 'r') as file:
                lines = file.readlines()

            updated_lines = []
            for line in lines:
                name, saved_balance, saved_chips = line.strip().split(',')
                if name == player_name:
                    updated_lines.append(f'{player_name},{balance},{chip_balance}\n')
                else:
                    updated_lines.append(line)

            with open('Projects\Casino V1\Data Files\players.txt', 'w') as file:
                file.writelines(updated_lines)


        elif chip_cash_out.lower() == 'n':
            pass
            # I want this to go back to the main menu
    
    elif menu_selection == 4:
        print(f'Your Cash Balance is: ${balance:,}')
        print(f'Your Chip Balance is: ${chip_balance:,}')
    
    elif menu_selection == 5:
        print('Updating records now')
        with open('Projects\Casino V1\Data Files\players.txt', 'r') as file:
            lines = file.readlines()

        updated_lines = []
        for line in lines:
            name, saved_balance, saved_chips = line.strip().split(',')
            if name == player_name:
                updated_lines.append(f'{player_name},{balance},{chip_balance}\n')
            else:
                updated_lines.append(line)

        with open('Projects\Casino V1\Data Files\players.txt', 'w') as file:
            file.writelines(updated_lines)
        time.sleep(1)
        print('Records have been updated.')
        time.sleep(0.5)
        print('Thanks for coming and have a nice day!')
        break

