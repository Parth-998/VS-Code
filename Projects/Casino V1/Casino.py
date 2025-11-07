### Counter
balance = 0
chip_balance = 0

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
        print(f'Your current Balance is: ${balance:,}')
        print(f'You current Total Chip Balance is: ${chip_balance:,}')

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

print(f'Your balance is ${balance:,}.')


### Chip Buying
if chip_balance > 0:
    print(f'You current Total Chip Balance is: ${chip_balance:,}')
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
            name, saved_balance, chips = line.strip().split(',')
            if name == player_name:
                updated_lines.append(f'{player_name},{balance},{chip_balance}\n')
            else:
                updated_lines.append(line)
        with open('Projects\Casino V1\Data Files\players.txt', 'w') as file:
            file.writelines(updated_lines)
        
        # chip distribution calculator
        orange_chips = chip_balance//1000
        remainder = chip_balance % 1000
        purple_chips = chip_balance//500
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
        print('What do you think you are doing here!')
        print('Hey Everyone! Look at this person. Coming in here with no money to their name.')
        print('Security take them out please.')
        print('Let us forget this even happened.')

elif chip_buying.lower() == 'n':
    pass
