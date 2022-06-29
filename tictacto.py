# Simple Tic-tac-toe in Python
# Author: Kevin Ocampo

def display_board(board = ['1','2','3','4','5','6','7','8','9']):
    print('-'*13)
    print(f'|{board[0]:^3}|{board[1]:^3}|{board[2]:^3}|')
    print('-'*13)
    print(f'|{board[3]:^3}|{board[4]:^3}|{board[5]:^3}|')
    print('-'*13)
    print(f'|{board[6]:^3}|{board[7]:^3}|{board[8]:^3}|')
    print('-'*13)

def instruct_user():
    print("Welcome to Kevin's Tic-tac-toe game!")
    print("Each space is represented by a number on the board as shown below:")
    display_board()
    print("Choose the location where you want to place your X or O by entering ")
    print("the corresponding number.")
    print("This is a two-player game. Each player will be ")
    print("asked to enter their move right after each other.\n")

def player_menu():
    valid_choices = ['X', 'O']
    choice = 0

    while choice not in valid_choices:
        choice = input("First player, do you want to be X or O? Please enter X or O: ")
    
    return choice == 'X'

def get_choice(player,first_symbol,board):
    valid_choices = [1,2,3,4,5,6,7,8,9]
    choice = 0
    occupied = True
    user_choice = 'A'

    if player == 1 and first_symbol:
        symbol = 'X'
    elif player == 1 and first_symbol == False:
        symbol = 'O'
    elif player == 2 and first_symbol:
        symbol = 'O'
    else:
        symbol = 'X'

    while occupied == True:
        while choice not in valid_choices:
            user_choice = input(f'Player {player}, please enter the position (1-9) you want to place your {symbol}: ')
            if user_choice.isdigit():
                choice = int(user_choice)
            

        if board[choice-1] == 'X' or board[choice-1] == 'O':
            choice = 0
            print("Sorry that position is already occupied!")
        else:
            occupied = False
    
    return [choice, symbol]

def mark_board(board, game_position):
    new_board = board
    new_board[game_position[0] - 1] = game_position[1]
    return new_board

def check_win(board, first_player_is_x):
    first_row = ''.join(board[0:3])
    second_row = ''.join(board[3:6])
    third_row = ''.join(board[6:9])
    first_column_list = board[0] + board[3] + board[6]
    first_column = ''.join(first_column_list)
    second_column_list = board[1] + board[4] + board[7]
    second_column = ''.join(second_column_list)
    third_column_list = board[2] + board[5] + board[8]
    third_column = ''.join(third_column_list)
    left_top_to_bottom_right_list = board[0] + board[4] + board[8]
    left_top_to_bottom_right = ''.join(left_top_to_bottom_right_list)
    right_top_to_bottom_left_list = board[2] + board[4] + board[6]
    right_top_to_bottom = ''.join(right_top_to_bottom_left_list)

    if 'XXX' in [first_row, second_row, third_row, first_column, second_column, third_column, left_top_to_bottom_right, right_top_to_bottom]:
        if first_player_is_x:
            print("Player 1 has won!")
        else:
            print("Player 2 has won!")
        return True
    elif 'OOO' in [first_row, second_row, third_row, first_column, second_column, third_column, left_top_to_bottom_right, right_top_to_bottom]:
        if first_player_is_x == False:
            print("Player 1 has won!")
        else:
            print("Player 2 has won!")
        return True

def game():
    
    valid_choices = ['Y', 'N']
    win = False
    first_player_is_x = False
    board = ['1','2','3','4','5','6','7','8','9']
    game_position  = []
    play_choice = 0
    current_player_counter = 0
    replay_flag = False
    

    instruct_user()
    first_player_is_x = player_menu()



    while (play_choice != 'N'):
        if replay_flag:
            first_player_is_x = player_menu()
            replay_flag = False
        display_board(board)
        if current_player_counter % 2 == 0:
            game_position = get_choice(1, first_player_is_x, board)
            board = mark_board(board, game_position)
        else:
            game_position = get_choice(2, first_player_is_x, board)
            board = mark_board(board, game_position)  
        current_player_counter += 1
        win = check_win(board,first_player_is_x)

        if win:
            display_board(board)
            play_choice = 0
            current_player_counter = 0
            board = ['1','2','3','4','5','6','7','8','9']
            while play_choice not in valid_choices:
                play_choice = input('Do you want to play again? Enter Y for yes or N for no: ')
                if play_choice == 'Y':
                    replay_flag = True
        
        if (current_player_counter == 9):
            print("It's a Draw! Game over!")
            play_choice = 0
            current_player_counter = 0
            board = ['1','2','3','4','5','6','7','8','9']
            while play_choice not in valid_choices:
                play_choice = input('Do you want to play again? Enter Y for yes or N for no: ')
                if play_choice == 'Y':
                    replay_flag = True



game()