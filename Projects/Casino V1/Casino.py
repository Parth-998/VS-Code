### Counter
balance = 0

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
                name, saved_balance = line.strip().split(',')
                if name == player_name:
                    name_exists = True
                    break
        
        if name_exists:
            print("This name already exists! Please try logging in as a returning player.")
            continue

        print(f'Welcome In {player_name}!')
        
        balance = int(input('How much would you like to Deposit today? '))
        while True:
            depo_input = input(f'You have deposited ${balance:,}. Would you like to deposit more? (Y/N) ')
            if depo_input.lower() == 'y':
                balance_addon = int(input('How much more would you like to deposit? '))
                balance += balance_addon
                print(f'You now have ${balance:,}.')
                # Store this next to the player name with the final amount
            if depo_input.lower() == 'n':
                break
        # Store the player name in a file
        with open('Projects\Casino V1\Data Files\players.txt', 'a') as file:
            file.write(f'{player_name},{balance}\n')
        break

    ### Returning Player
    elif new_or_returning_player.lower() == 'returning':
        
        player_name = input('What is your name? Ex: "John Smith" ')
        player_found = False

        with open('Projects\Casino V1\Data Files\players.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, saved_balance = line.strip().split(',')
                if name == player_name:
                    player_found = True
                    balance = int(saved_balance)
        
        if not player_found:
            print("Player not found! Please register as a new player.")
            continue

        print(f'Welcome Back {player_name}!')
        print(f'Your current balance is: ${balance:,}')

        while True:
            depo_input = input('Would you like to deposit more? (Y/N) ')
            if depo_input.lower() == 'y':
                balance_addon = int(input('How much more would you like to deposit? '))
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
            name, saved_balance = line.strip().split(',')
            if name == player_name:
                updated_lines.append(f'{player_name},{balance}\n')
            else:
                updated_lines.append(line)
        with open('Projects\Casino V1\Data Files\players.txt', 'w') as file:
            file.writelines(updated_lines)
        
        break

print(f'Your balance is ${balance:,}.')


### Chip Buying

