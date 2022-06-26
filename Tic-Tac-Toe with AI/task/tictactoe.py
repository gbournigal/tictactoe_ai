# write your code here
import random


def ex_1():
    initial_state = str(input('Enter the cells:'))
    printable_states = list(initial_state)
    for i in range(len(printable_states)):
        if printable_states[i] == '_':
            printable_states[i] = ' '

    print('---------')
    print(f'| {printable_states[0]} {printable_states[1]} {printable_states[2]} |')
    print(f'| {printable_states[3]} {printable_states[4]} {printable_states[5]} |')
    print(f'| {printable_states[6]} {printable_states[7]} {printable_states[8]} |')
    print('---------')

    coordinate_picker(printable_states)
    winner_checker(printable_states)


def from_coordinate_to_number(numbers_list):
    if numbers_list[0] == '1':
        number = int(numbers_list[1]) - 1
    if numbers_list[0] == '2':
        number = int(numbers_list[1]) + 2
    if numbers_list[0] == '3':
        number = int(numbers_list[1]) + 5
    return number


def coordinate_picker(printable_states):
    coordinates = input('Enter the coordinates:')
    if coordinates == 'start user easy':
        pass
    else:
        numbers = coordinates.split()
        try:
            if (1 <= int(numbers[0]) <= 3) and (1 <= int(numbers[1]) <= 3):
                list_number = from_coordinate_to_number(numbers)
                if printable_states[list_number] == ' ':
                    if printable_states.count('X') == printable_states.count('O'):
                        printable_states[list_number] = 'X'
                    else:
                        printable_states[list_number] = 'O'
                else:
                    print('This cell is occupied! Choose another one!')
                    coordinate_picker(printable_states)
            else:
                print('Coordinates should be from 1 to 3!')
                coordinate_picker(printable_states)

            print('---------')
            print(f'| {printable_states[0]} {printable_states[1]} {printable_states[2]} |')
            print(f'| {printable_states[3]} {printable_states[4]} {printable_states[5]} |')
            print(f'| {printable_states[6]} {printable_states[7]} {printable_states[8]} |')
            print('---------')

        except ValueError:
            print('You should enter numbers!')
            coordinate_picker(printable_states)


def winner_checker(printable_states, print_result=True):
    if (printable_states[0] == printable_states[1] == printable_states[2]) and printable_states[0] != ' ':
        ended = True
        if print_result:
            print(f'{printable_states[0]} wins')
    elif (printable_states[3] == printable_states[4] == printable_states[5]) and printable_states[3] != ' ':
        ended = True
        if print_result:
            print(f'{printable_states[3]} wins')
    elif (printable_states[6] == printable_states[7] == printable_states[8]) and printable_states[7] != ' ':
        ended = True
        if print_result:
            print(f'{printable_states[6]} wins')
    elif (printable_states[0] == printable_states[4] == printable_states[8]) and printable_states[4] != ' ':
        ended = True
        if print_result:
            print(f'{printable_states[0]} wins')
    elif (printable_states[2] == printable_states[4] == printable_states[6]) and printable_states[4] != ' ':
        ended = True
        if print_result:
            print(f'{printable_states[2]} wins')
    elif (printable_states[0] == printable_states[3] == printable_states[6]) and printable_states[6] != ' ':
        ended = True
        if print_result:
            print(f'{printable_states[0]} wins')
    elif (printable_states[1] == printable_states[4] == printable_states[7]) and printable_states[7] != ' ':
        ended = True
        if print_result:
            print(f'{printable_states[1]} wins')
    elif (printable_states[2] == printable_states[5] == printable_states[8]) and printable_states[8] != ' ':
        ended = True
        if print_result:
            print(f'{printable_states[2]} wins')
    elif ' ' in printable_states:
        ended = False
        if print_result:
            print('Game not finished')
    else:
        ended = True
        if print_result:
            print('Draw')
    return ended


def random_picker(printable_states):
    print('Making move level "easy"')
    options = list(range(9))
    ran_choice = random.choice(options)
    while printable_states[ran_choice] != ' ':
        ran_choice = random.choice(options)
    printable_states[ran_choice] = 'O'
    print('---------')
    print(f'| {printable_states[0]} {printable_states[1]} {printable_states[2]} |')
    print(f'| {printable_states[3]} {printable_states[4]} {printable_states[5]} |')
    print(f'| {printable_states[6]} {printable_states[7]} {printable_states[8]} |')
    print('---------')


def ex_2():
    printable_states = [' ']*9
    print()
    print('---------')
    print(f'| {printable_states[0]} {printable_states[1]} {printable_states[2]} |')
    print(f'| {printable_states[3]} {printable_states[4]} {printable_states[5]} |')
    print(f'| {printable_states[6]} {printable_states[7]} {printable_states[8]} |')
    print('---------')
    ended = False
    while not ended:
        coordinate_picker(printable_states)
        ended = winner_checker(printable_states, False)
        if not ended:
            random_picker(printable_states)
            ended = winner_checker(printable_states, False)
    winner_checker(printable_states)


ex_2()
