import random

def is_correct_input(value):
    return value in ['0', '1']

def get_coin_side():
    return random.choice(['Heads', 'Tails'])

def get_side_name(side):
    if side == '0':
        return 'Heads'
    elif side == '1':
        return 'Tails'

# def view_side(bet_name):
#     print(f"My bet is {bet_name}.")

# def get_result(bet, coin_side):
#     if bet == coin_side:
#         return 'win'
#     else:
#         return 'lose'

# def view_result(result):
#     print(f"You {result}!")

def play():
    print("Start 'coin toss'")
    while True:
        bet = input("Input your bet (0 for 'Heads' or 1 for 'Tails'): ")
        if is_correct_input(bet):
            break
        else:
            print("Invalid input. Please enter 0 or 1.")
    bet_name = get_side_name(bet)
    view_side(bet_name)
    coin_side = get_coin_side()
    print(f"Coin is {coin_side}.")
    result = get_result(bet_name, coin_side)
    view_result(result)

play()
