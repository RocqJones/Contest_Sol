import math

player1 = "Alice"
player2 = "Bob"
global current_player
current_player = player1

def check_power_of_two(number):
    log = (math.log10(number) / math.log10(2))
    return math.ceil(log) ==  math.floor(log)

def number_less_than_two(n):
    return n/2

def get_largest_power(n):
    for i in range(64):
        if 2**i > n :
            return 2**(i-1)

def switch_player():
    global current_player
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

def play(n):
    if check_power_of_two(n):
        n = number_less_than_two(n)
    else:
        n -= get_largest_power(n)

    switch_player()
    if n == 1:
        print(current_player)
    elif n > 1:
        if current_player == player1:
            print(player1)
            return
        else:
            print(player2)
            return
    else:
        play(n)


# select input
inputs = []
selected_number = int(input())
while selected_number != -1:
    n = 0
    if(len(inputs) == 0):
        inputs.append(selected_number)
    else:
        n = int(input())
        inputs.append(n)
    selected_number = n

for i in inputs:
    if i != -1:
        play(i)
