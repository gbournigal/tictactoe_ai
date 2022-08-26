# write your code here
import random
import math


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


def winner_checker(printable_states, print_result=True, return_winner=False):
    if (printable_states[0] == printable_states[1] == printable_states[2]) and printable_states[0] != ' ':
        ended = True
        winner = printable_states[0]
        if print_result:
            print(f'{winner} wins')
    elif (printable_states[3] == printable_states[4] == printable_states[5]) and printable_states[3] != ' ':
        ended = True
        winner = printable_states[3]
        if print_result:
            print(f'{winner} wins')
    elif (printable_states[6] == printable_states[7] == printable_states[8]) and printable_states[7] != ' ':
        ended = True
        winner = printable_states[6]
        if print_result:
            print(f'{winner} wins')
    elif (printable_states[0] == printable_states[4] == printable_states[8]) and printable_states[4] != ' ':
        ended = True
        winner = printable_states[0]
        if print_result:
            print(f'{winner} wins')
    elif (printable_states[2] == printable_states[4] == printable_states[6]) and printable_states[4] != ' ':
        ended = True
        winner = printable_states[2]
        if print_result:
            print(f'{winner} wins')
    elif (printable_states[0] == printable_states[3] == printable_states[6]) and printable_states[6] != ' ':
        ended = True
        winner = printable_states[0]
        if print_result:
            print(f'{winner} wins')
    elif (printable_states[1] == printable_states[4] == printable_states[7]) and printable_states[7] != ' ':
        ended = True
        winner = printable_states[1]
        if print_result:
            print(f'{winner} wins')
    elif (printable_states[2] == printable_states[5] == printable_states[8]) and printable_states[8] != ' ':
        ended = True
        winner = printable_states[2]
        if print_result:
            print(f'{winner} wins')
    elif ' ' in printable_states:
        ended = False
        winner = 'not finished'
        if print_result:
            print('Game not finished')
    else:
        ended = True
        winner = 'draw'
        if print_result:
            print('Draw')
    if not return_winner:
        return ended
    else:
        return ended, winner


def random_picker(printable_states, first_player=False, from_medium=False):
    if not first_player:
        tick = 'O'
    else:
        tick = 'X'
    if not from_medium:
        print('Making move level "easy"')
    options = list(range(9))
    ran_choice = random.choice(options)
    while printable_states[ran_choice] != ' ':
        ran_choice = random.choice(options)
    printable_states[ran_choice] = tick
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


def ex_4():
    start_end_game = input('Input command:')
    while start_end_game != 'exit':
        if len(start_end_game.split()) != 3:
            print('Bad parameters!')
            start_end_game = input('Input command:')
        else:
            command, ply1, ply2 = start_end_game.split()
            if command == 'start':
                if ply1 and ply2 in ['user', 'easy', 'medium', 'hard']:
                    printable_states = [' ']*9
                    print()
                    print('---------')
                    print(f'| {printable_states[0]} {printable_states[1]} {printable_states[2]} |')
                    print(f'| {printable_states[3]} {printable_states[4]} {printable_states[5]} |')
                    print(f'| {printable_states[6]} {printable_states[7]} {printable_states[8]} |')
                    print('---------')
                    ended = False
                    while not ended:
                        if ply1 == 'user':
                            coordinate_picker(printable_states)
                        elif ply1=='easy':
                            random_picker(printable_states, True)
                        elif ply1=='medium':
                            medium_move(printable_states, True)
                        elif ply1=='hard':
                            hard_move(printable_states, True)
                        ended = winner_checker(printable_states, False)
                        if not ended:
                            if ply2 == 'user':
                                coordinate_picker(printable_states)
                            elif ply2=='easy':
                                random_picker(printable_states)
                            elif ply2=='medium':
                                medium_move(printable_states)
                            elif ply2=='hard':
                                hard_move(printable_states)
                            ended = winner_checker(printable_states, False)
                    winner_checker(printable_states)
                    start_end_game = input('Input command:')
                else:
                    print('Bad parameters!')
                    start_end_game = input('Input command:')
            else:
                print('Bad parameters!')
                start_end_game = input('Input command:')


def medium_move(printable_states, first_player=False):
    if not first_player:
        tick = 'O'
        enemy = 'X'
    else:
        tick = 'X'
        enemy = 'O'
    print('Making move level "medium"')
    empty_selections = [i for i in range(len(printable_states)) if printable_states[i] == ' ']
    moves_left = len(empty_selections)
    for i in empty_selections:
        printable_states[i] = tick
        result = winner_checker(printable_states, False)
        if result:
            break
        else:
            printable_states[i] = ' '
    if winner_checker(printable_states, False):
        print('---------')
        print(f'| {printable_states[0]} {printable_states[1]} {printable_states[2]} |')
        print(f'| {printable_states[3]} {printable_states[4]} {printable_states[5]} |')
        print(f'| {printable_states[6]} {printable_states[7]} {printable_states[8]} |')
        print('---------')
    else:
        for i in empty_selections:
            printable_states[i] = enemy
            result = winner_checker(printable_states, False)
            if result:
               printable_states[i] = tick
               print('---------')
               print(f'| {printable_states[0]} {printable_states[1]} {printable_states[2]} |')
               print(f'| {printable_states[3]} {printable_states[4]} {printable_states[5]} |')
               print(f'| {printable_states[6]} {printable_states[7]} {printable_states[8]} |')
               print('---------')
               break
            else:
               printable_states[i] = ' '
    if moves_left == len([i for i in range(len(printable_states)) if printable_states[i] == ' ']):
        random_picker(printable_states, first_player, from_medium=True)



def hard_move(printable_states, first_player=False):
    empty_selections = [i for i in range(len(printable_states)) if printable_states[i] == ' ']
    if not first_player:
        tick = 'O'
    else:
        tick = 'X'
    print('Making move level "hard"')
    
    bestScore = -math.inf
    bestMove = None
    for move in empty_selections:
        printable_states[move] = tick
        score = minimax(False, tick, printable_states)
        printable_states[move] = ' '
        if score > bestScore:
            bestScore = score
            bestMove = move
    printable_states[bestMove] = tick
    print('---------')
    print(f'| {printable_states[0]} {printable_states[1]} {printable_states[2]} |')
    print(f'| {printable_states[3]} {printable_states[4]} {printable_states[5]} |')
    print(f'| {printable_states[6]} {printable_states[7]} {printable_states[8]} |')
    print('---------')
    

def minimax(isMaxTurn, maximizerMark, board):
    empty_selections = [i for i in range(len(board)) if board[i] == ' ']
    state, winner = winner_checker(board, False, True)
    if (state is True and winner == 'draw'):
        return 0
    elif (state is True):
        return 1 if winner is maximizerMark else -1

    scores = []
    for move in empty_selections:
        board[move] = 'X' if len(empty_selections) % 2 != 0 else 'O'
        scores.append(minimax(not isMaxTurn, maximizerMark, board))
        board[move] = ' '

    return max(scores) if isMaxTurn else min(scores)


ex_4()
