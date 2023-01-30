import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 0

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 8,
    "B": 6,
    "C": 4,
    "D": 2,
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
    return winnings

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    # Generate a selection of symbols to put inside each slot reel
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    # 
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]   
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ") 
            else:               
                print(column[row]) 
            
def get_number_of_lines():
    while True:
        lines = input("Please enter the number of lines to bet on from 1 to " + str(MAX_LINES) + ". ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print("Enter a value from 1 to " + str(MAX_LINES) + '.')
        else:
            print('Please enter a number.')
    return lines

def get_deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Cannot enter 0 or below")
        else:
            print("Please enter a number")
            
    return amount

def get_bet(lines,balance):
    while True:
        bet = input("How much would you like to bet? $")
        if bet.isdigit():
            bet = int(bet)
            print(f'You are betting ${bet} on {lines} slots. Total bet is ${bet*lines}')
            if MIN_BET < bet <= MAX_BET and bet*lines <= balance:
                break
            elif bet*lines > balance:
                print(f"Amount must be below your balance. (${balance})")
            else:
                print(f"Amount must be between (${MIN_BET} - ${MAX_BET})")
        else:
            print('Please enter a number.')            
    return bet

def get_additional_deposit():
    while True:
        amount = input("How much would you like to add to your balance? $")
        if amount.isdigit():
            amount = int(amount)
            break
        else:
            print("Please enter a number")
            
    return amount

def retry(balance):
    while True:
        additional = get_additional_deposit()
        balance += additional
        
        lines = get_number_of_lines()
        bet = get_bet(lines,balance)
        slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
        print_slot_machine(slots)
        winnings = check_winnings(slots,lines,bet,symbol_value)
        
        if winnings == 0:
            print('You Lose')
        else:
            print(f"You won ${winnings}")
        
        balance += winnings
        balance -= bet
        
        print(f'Your total balance left is ${balance}')


        play_again = input('Do you want to play again ( Y , N )? ')
        if play_again == 'N':
            break

    print(f'Thanks for playing. Your total balance left is ${balance}')
         
def main():
    balance = get_deposit()
    lines = get_number_of_lines()
    bet = get_bet(lines,balance)

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings = check_winnings(slots,lines,bet,symbol_value)
    balance += winnings
    balance -= bet*lines
    
    if winnings == 0:
        print('You Lose')
    else:
        print(f"You won ${winnings}")
        
    print(f'Your total balance left is ${balance}')
            
    play_again = input('Do you want to play again ( Y , N )? ')
    if play_again == 'Y' or play_again == 'y':
        retry(balance)
    else:
        print(f'Thanks for playing. Your total balance left is ${balance}')
main()