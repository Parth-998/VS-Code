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
    print('Welcome Back!')

print(f'Your balance is ${balance}.')
