#!/usr/bin/env python3
import os
import random
def display_board(board, players, clear=True):
    '''
    display the game board
    '''
    if clear:
        os.system('clear')
    if not players == '':
        player1_display = "Player 1: "
        player1_name = players[0][0]
        player1_fill = " "*(10-len(player1_name))
        player1_char = players[0][1]
        player2_display = "Player 2: "
        player2_name = players[1][0]
        player2_fill = " "*(10-len(player2_name))
        player2_char = players[1][1]
        line1_addon = f" \t {player1_display}{player1_name}{player1_fill}:\t {player1_char}"
        line2_addon = f" \t {player2_display}{player2_name}{player2_fill}:\t {player2_char}"
    else:
        line1_addon = ""
        line2_addon = ""

    line1 = f" {board[0]} | {board[1]} | {board[2]}{line1_addon}"
    line2 = f"---+---+---{line2_addon}"
    line3 = f" {board[3]} | {board[4]} | {board[5]}"
    line5 = f" {board[6]} | {board[7]} | {board[8]}"
    playboard = [line1, line2, line3,"---+---+---", line5]
    for l in playboard:
        print(l)
def place_marker(board, marker, position):
    '''
    place the marker at the right position
    '''
    if not marker in ["O", "X"]:
        print("ERROR: invalid Marker")
        return False, board
    elif not position in list(range(1,10)):
        print("ERROR: invalid position")
        return False, board
    elif len(board) != 9:
        print("ERROR: invalid Board")
        return False, board
    else:
        board[position-1] = marker
        return True, board
def win_check(board, mark):
    '''
    check if there is a winner
    '''
    winmark = mark*3
    # get the rows
    row1 = board[0]+board[1]+board[2]
    row2 = board[3]+board[4]+board[5]
    row3 = board[6]+board[7]+board[8]
    # get the columns
    col1 = board[0]+board[3]+board[6]
    col2 = board[1]+board[4]+board[7]
    col3 = board[2]+board[5]+board[8]
    # get the diagonales
    diag1 = board[0]+board[4]+board[8]
    diag2 = board[2]+board[4]+board[6]
    #Build winner list
    winner_list = [row1, row2, row3, col1, col2, col3, diag1, diag2]
    # check winmark against list
    return winmark in winner_list
def choose_first(players, keep=False):
    '''
    set up the users and look who starts the Game
    '''
    if not keep:
        players[0][0] = input("please enter the Name of Player 1:")
        p1_item = " "
        while p1_item not in ['O', 'X']:
            p1_item = input(f"please enter the game item for {players[0][0]} (O or X) : ").upper()
            if p1_item not in ['O', 'X']:
                print("you have to select X or O")
        players[0][1] = p1_item
        if players[0][1] == 'X':
            players[1][1] = 'O'
        else:
            players[1][1] = 'X'
        players[1][0] = players[0][0]
        while players[0][0] == players[1][0]:
            players[1][0] = input("please enter the Name of Player 2:")
            if players[0][0] == players[1][0]:
                print("you cannot have the same Name as Player 1")
    start_player = random.randint(0, 1)
    return players, start_player
def keep_player():
    '''
    ask if the players should be kept for a new game
    '''
    answer = 'X'
    while answer not in ['Y', 'N']:
        answer = input("would you like to keep the Players ? (Y/N)").upper()
        if answer not in ['Y', 'N']:
            print("wrong answer - answer has to be Y or N")
    return answer == 'Y'
def space_check(board, position):
    '''
    check if the field on the board is still free
    '''
    if not board[position-1] == ' ':
        print("this possition is not free anymore")
    return board[position-1] == ' '
def full_board_check(board):
    '''
    check if there are still empty fields
    true if the board is full
    false if there are still open fields
    '''
    return ' ' not in board
def player_choice(board, player):
    '''
    get the nex choise for a player
    '''
    p_choise = 'q'
    while p_choise not in range(1,19):
        p_choise = input(f"(X to quit / H for help)\n{player} : please select a field (1-9) > ")
        if p_choise.isdigit():
            p_choise = int(p_choise)
            if not space_check(board, p_choise):
                p_choise = "q"
        else:
            if p_choise.upper() == 'X':
                return 'X'
            elif p_choise.upper() == 'H':
                print("\n here a small help how to chouse a field \n")
                help_board = ['1','2','3','4','5','6','7','8','9']
                display_board(help_board, '', False)
            else:
                print("you have to select a number from 1 to 9 or X")
    return p_choise
def replay():
    '''
    check if a new game should be started
    '''
    answer = 'X'
    while answer not in ['Y', 'N']:
        answer = input("would you like to play again ? (Y/N)").upper()
        if answer not in ['Y', 'N']:
            print("wrong answer - anser has to be Y or N")
    return answer == 'Y'
##########################
# MAIN
##########################
print('Welcome to Tic Tac Toe!')
playon = True
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
players = [['P1',' '],['P2', ' ']]
turn = 0
keep_the_players = False
# Run until they wanna stop
while playon:
    # Game not finish
    finish = False
    #set up the players and check who is 1st
    players, who_next = choose_first(players, keep_the_players)
    # stay in the game while it is not finish
    have_a_winner = False
    while not finish:
        # 1st display the board
        display_board(board, players)
        # special message on the 1st turn
        if turn == 0:
            print(f"{players[who_next][0]} you start the Game")
            turn += 1
        else:
            print(f"{players[who_next][0]} : you go next")
        #get the next choise & check it
        choise_ok = False
        run_choise = True
        # run until the choise is valid
        while run_choise:
            next_choise = player_choice(board, players[who_next][0])
            if next_choise != 'X':
                if space_check(board, next_choise):
                    run_choise = False
                else:
                    run_choise = True
            else:
                run_choise = False
        # if the choise was X - quit the game
        if next_choise == 'X':
            print("you quit the Game")
            break
        placement_ok, board = place_marker(board, players[who_next][1],next_choise)
        # check if the actual player has won
        if win_check(board, players[who_next][1]):
            display_board(board, players)
            print("*"*20)
            print("We have a Winner !!!!")
            print(f"Congratulation {players[who_next][0]} !!!")
            print("*"*20)
            finish = True
        # check, if the board is full and we have a draw
        if full_board_check(board):
            if not have_a_winner:
                display_board(board, players)
                print("*"*20)
                print("this game was a draw :(")
                print("*"*20)
                finish = True
        # calculate the next player
        who_next += 1
        if who_next == 2:
            who_next = 0
    playon = replay()
    if playon:
        turn = 0
        keep_the_players = keep_player()
