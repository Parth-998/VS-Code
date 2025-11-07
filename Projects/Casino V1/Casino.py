### Counter
balance = 0


### Starting Prompts
new_or_returning_player = input('Are you a New or Returning player? ')

if new_or_returning_player.lower() == 'new':
    print('Welcome In!')
    balance = int(input('How much would you like to Deposit today? '))
    while True:
        depo_input = input(f'You have deposited ${balance}. Would you like to deposit more? (Y/N) ')
        if depo_input.lower() == 'y':
            balance_addon = int(input('How much more would you like to deposit? '))
            balance += balance_addon
            print(f'You now have ${balance}.')
        if depo_input.lower() == 'n':
            break
elif new_or_returning_player.lower() == 'returning':
    player_name = input('What is your name? ')
    # Reading and writing file goes here?
    # This is based on what I said in the comments below
    print(f'Welcome Back {player_name}!')
    print(f'Your current balance is: {balance}')
    while True:
        depo_input = input('Would you like to deposit more? (Y/N) ')
        if depo_input.lower() == 'y':
            balance_addon = int(input('How much more would you like to deposit? '))
            balance += balance_addon
            print(f'You now have ${balance}.')
        if depo_input.lower() == 'n':
            break
    # Need to add more but unsure as to what to add to keep player data from previous sessions.
    # Will figure it out and update.
    # Maybe could be something like reading and writing onto a blank file with the player name
    # as a search query and then taking the number and displaying it?


print(f'Your balance is ${balance}.')

