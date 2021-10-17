import random

PLAY_BOARD = [str(num) for num in range(1, 101)]
PLAY_BOARD_COMP = [num for num in range(100)]
PLAYERS_MARKS = ['X', 'O']
STEP = 1


def replay():
    """Asks the players to play again."""
    decision = ''
    while decision not in ('y', 'n'):
        decision = input('Would you like to play again? Type "y" or "n"').lower()

    return decision == 'y'


def choose_first():
    """Randomly returns the player's mark that goes first."""
    return PLAYERS_MARKS[random.choice((0, 1))]


def space_check(board, position):
    """Returns boolean value whether the cell is free or not."""
    return board[position] not in PLAYERS_MARKS


def player_choice(board, player_mark):
    """Gets player's next position and check if it's appropriate to play."""
    position = 0

    while position not in [num for num in range(1, 101)]:
        try:
            position = \
                int(input(f'Player "{player_mark}", choose your next position from 1 to 100: '))
        except ValueError as exc:
            print(f'Wrong value: {exc}. Please, try again.')

    position -= 1
    if space_check(board, position):
        return position

    return False


def computer_random_choice(board, board_comp, player_mark):
    """Gets computer's next position and check if it's appropriate to play."""
    position = random.choice(board_comp)

    print(f'Computer choose {position + 1}')

    if space_check(board, position):
        return position

    return False


def first_step(board, board_comp, player_mark, comp_move):
    """We fill in everything around which there are no labels."""
    global STEP
    for i in board_comp:
        if comp_move < i:
            up = (i // 10) == 0
            down = (i // 10) == 9
            left = (i % 10) == 0
            right = (i % 10) == 9

            if not up:
                if (i - 10) not in board_comp:
                    continue

            if not down:
                if (i + 10) not in board_comp:
                    continue

            if not left:
                if (i - 1) not in board_comp:
                    continue

            if not right:
                if (i + 1) not in board_comp:
                    continue

            if not up and not left:
                if (i - 11) not in board_comp:
                    continue

            if not up and not right:
                if (i - 9) not in board_comp:
                    continue

            if not down and not left:
                if (i + 9) not in board_comp:
                    continue

            if not down and not left:
                if (i + 11) not in board_comp:
                    continue

            comp_move = i
            position = i
            return position, comp_move
            break

    STEP = 2
    return -1, -1


def second_step(board, board_comp, player_mark, comp_move):
    """We fill in everything that does not stand between the marks and will not lead to a loss."""
    global STEP

    for i in board_comp:
        if comp_move < i:

            board_new = board.copy()
            board_comp_new = board_comp.copy()
            place_marker(board_new, board_comp_new, player_mark, i)
            if player_mark == 'X':
                mark = 'O'
            else:
                mark = 'X'

            if not between(board, board_comp, player_mark, comp_move, i) and not between(board, board_comp, mark,
                                                                                         comp_move, i) and loss_check(
                board_new, player_mark):
                comp_move = i
                position = i
                return position, comp_move
                break

    STEP = 3
    return -1, -1


def third_step(board, board_comp, player_mark, comp_move):
    """We fill in everything that does not stand between the computer marks and will not lead to a loss."""
    global STEP

    for i in board_comp:
        if comp_move < i:

            board_new = board.copy()
            board_comp_new = board_comp.copy()
            place_marker(board_new, board_comp_new, player_mark, i)
            if player_mark == 'X':
                mark = 'O'
            else:
                mark = 'X'

            if not between(board, board_comp, mark, comp_move, i) and loss_check(board_new, player_mark):
                comp_move = i
                position = i
                return position, comp_move
                break

    STEP = 4
    return -1, -1


def fourth_step(board, board_comp, player_mark, comp_move):
    """We fill in everything that will not lead to a loss."""
    global STEP

    for i in board_comp:
        if comp_move < i:

            board_new = board.copy()
            board_comp_new = board_comp.copy()
            place_marker(board_new, board_comp_new, player_mark, i)

            if loss_check(board_new, player_mark):
                comp_move = i
                position = i
                return position, comp_move
                break

    STEP = 5
    return -1, -1


def fifth_step(board, board_comp, player_mark, comp_move):
    """We fill everything."""
    for i in board_comp:
        comp_move = i
        position = i
        return position, comp_move
        break

    return -1, -1


def between(board, board_comp, player_mark, comp_move, pos):
    """Checks if there are identical marks around."""
    up = (pos // 10) == 0
    down = (pos // 10) == 9
    left = (pos % 10) == 0
    right = (pos % 10) == 9

    i = pos

    if not up and not down:
        if board[i - 10] == board[i + 10] == player_mark:
            return True

    if not left and not right:
        if board[i - 1] == board[i + 1] == player_mark:
            return True

    if not up and not left and not down and not right:
        if board[i - 11] == board[i + 11] == player_mark:
            return True

    if not up and not right and not down and not left:
        if board[i - 9] == board[i + 9] == player_mark:
            return True

    return False


def computer_choice(board, board_comp, player_mark, comp_move):
    """Moves to a certain step as the game board is filled."""
    print(STEP)
    if STEP == 1:
        position, comp_move = first_step(board, board_comp, player_mark, comp_move)
        if position != -1 and comp_move != -1:
            return position, comp_move

    if STEP == 2:
        position, comp_move = second_step(board, board_comp, player_mark, comp_move)
        if position != -1 and comp_move != -1:
            return position, comp_move

    if STEP == 3:
        position, comp_move = third_step(board, board_comp, player_mark, comp_move)
        if position != -1 and comp_move != -1:
            return position, comp_move

    if STEP == 4:
        position, comp_move = fourth_step(board, board_comp, player_mark, comp_move)
        if position != -1 and comp_move != -1:
            return position, comp_move

    if STEP == 5:
        position, comp_move = fifth_step(board, board_comp, player_mark, comp_move)
        if position != -1 and comp_move != -1:
            return position, comp_move


def display_board(board_list):
    """Prints the game board."""
    print(f'-----------------------------')
    print(
        f'{board_list[0]} |{board_list[1]} |{board_list[2]} |{board_list[3]} |{board_list[4]} |{board_list[5]} |'
        f'{board_list[6]} |{board_list[7]} |{board_list[8]} |{board_list[9]}')
    print(f'-----------------------------')
    for i in range(1, 10):
        print(
            f'{board_list[i * 10]}|{board_list[i * 10 + 1]}|{board_list[i * 10 + 2]}|{board_list[i * 10 + 3]}|'
            f'{board_list[i * 10 + 4]}|{board_list[i * 10 + 5]}|{board_list[i * 10 + 6]}|{board_list[i * 10 + 7]}|'
            f'{board_list[i * 10 + 8]}|{board_list[i * 10 + 9]}')
        print(f'-----------------------------')


def clear_screen():
    """Clears the game screen via adding new rows."""
    print('\n' * 100)


def player_input():
    """Gets player's input string to choose the game mark to play."""
    player = ''
    while player not in ('X', 'O'):
        player = input('Please, choose your marker: X or O: ').upper()

    if player == 'X':
        computer = 'O'
    else:
        computer = 'X'

    return player, computer


def place_marker(board, board_comp, marker, position):
    """Puts a player mark to appropriate position."""
    print(position)
    board[position] = marker
    board_comp.remove(position)
    print(board_comp)


def loss_check(board, mark):
    """Returns boolean value whether the player loses the game."""
    flag = False

    for i in range(10):
        for j in range(6):
            if (board[i * 10 + j] == board[i * 10 + j + 1] == board[i * 10 + j + 2] == board[i * 10 + j + 3] == board[
                i * 10 + j + 4] == mark) or (
                    board[i + j * 10] == board[i + j * 10 + 1] == board[i + j * 10 + 2] == board[i + j * 10 + 3] ==
                    board[i + j * 10 + 4] == mark):
                flag = True

    if not flag:
        for i in range(6):
            for j in range(6):
                if (board[i * 10 + j] == board[i * 10 + j + 11] == board[i * 10 + j + 22] == board[i * 10 + j + 33] ==
                    board[i * 10 + j + 44] == mark) or (
                        board[i * 10 + j + 4] == board[i * 10 + j + 13] == board[i * 10 + j + 22] == board[
                        i * 10 + j + 31] == board[i * 10 + j + 40] == mark):
                    flag = True

    return flag


def full_board_check(board):
    """Returns boolean value whether the game board is full of game marks."""
    return len(set(board)) == 2


def switch_player(mark):
    """Switches player's marks to play next turn."""
    return 'O' if mark == 'X' else 'X'


def check_game_finish(board, mark):
    """Return boolean value is the game finished or not."""
    if loss_check(board, mark):
        print(f'The player with the mark "{mark}" loses!')
        return True

    if full_board_check(PLAY_BOARD):
        print('The game ended in a draw.')
        return True

    return False


print('Welcome to Tic Tac Toe!')

PLAYER_MARK, COMPUTER_MARK = player_input()
CURRENT_PLAYER_MARK = choose_first()
COMP_MOVE = -1
print(PLAYER_MARK, COMPUTER_MARK, CURRENT_PLAYER_MARK)

print(f'Player with mark "{CURRENT_PLAYER_MARK}" goes first.')

while True:
    display_board(PLAY_BOARD)
    if CURRENT_PLAYER_MARK == COMPUTER_MARK:
        print(f'Turn of the player with the mark "{CURRENT_PLAYER_MARK}":')
        PLAYER_POSITION, COMP_MOVE = computer_choice(PLAY_BOARD, PLAY_BOARD_COMP, CURRENT_PLAYER_MARK, COMP_MOVE)
        # PLAYER_POSITION = player_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)
        place_marker(PLAY_BOARD, PLAY_BOARD_COMP, CURRENT_PLAYER_MARK, PLAYER_POSITION)

    if CURRENT_PLAYER_MARK == PLAYER_MARK:
        print(f'Turn of the player with the mark "{CURRENT_PLAYER_MARK}":')
        # PLAYER_POSITION = computer_random_choice(PLAY_BOARD, PLAY_BOARD_COMP, CURRENT_PLAYER_MARK)
        PLAYER_POSITION = player_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)
        place_marker(PLAY_BOARD, PLAY_BOARD_COMP, CURRENT_PLAYER_MARK, PLAYER_POSITION)

    if check_game_finish(PLAY_BOARD, CURRENT_PLAYER_MARK):
        display_board(PLAY_BOARD)
        if not replay():
            break
        else:
            PLAY_BOARD = [str(num) for num in range(1, 101)]
            PLAY_BOARD_COMP = [num for num in range(100)]
            PLAYER_MARKS = player_input()
            CURRENT_PLAYER_MARK = choose_first()
    else:
        CURRENT_PLAYER_MARK = switch_player(CURRENT_PLAYER_MARK)
    clear_screen()
