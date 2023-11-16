# Two players at same computer
# Board will be a 3x3 grid
# X or O
# 1. Ask player 1 if they want to be X or O
    # a. Player 2 auto assigned the other
# 2. Player 1 will place symbol 
    # a. Then player 2
    # NOTE: make sure cant overwrite a tile with a symbol already
# 3. After 5 turns, game will start to check for win condition
    # a. after 9 turns (or on 10th turn) if no win condition has been set, end the game on draw

# ---------------------------------------------------------------------------- #
#                                   Functions                                  #
# ---------------------------------------------------------------------------- #

# ------------------------- Board Set Up and Display ------------------------- #

def display_board(board):
    print("Current board: ")

    print("|", board[1], "|", board[2], "|", board[3], "|")
    print("|", board[4], "|", board[5], "|", board[6], "|")
    print("|",board[7], "|", board[8], "|", board[9], "|")

# -------------------------------- Game Start -------------------------------- #

# Asks Player 1 if they want to be X or O
# Player 2 will get the other symbol
def game_start():
    valid_choice = False

    while not valid_choice:
        player_one_choice = input('Player 1: Do you want to play as X or O?')

        if player_one_choice.lower() not in ("x", "o"):
            print("Invalid Choice.")
        else:
            valid_choice = True

    if valid_choice:
        if player_one_choice.lower() == "x":
            player_two_choice = "O"
        else:
            player_two_choice = "X"
        print(f'Player 1 is {player_one_choice.upper()}.')
        print(f'Player 2 is {player_two_choice.upper()}.')

        return player_one_choice, player_two_choice

# --------------------------- Place Symbol on Board -------------------------- #

# Take symbol of player 1 and 2
# Depending on turn counter, determines which player and symbol to place
# Check for invalid placement (in range and not an existing placement)

def place_symbol(player_one, player_two, turn, board):
    valid_move = False

    if turn % 2 == 0:
        print("Player One's Turn.")
        symbol = player_one

    else:
        print("Player Two's Turn.")
        symbol = player_two
        
    while not valid_move:
        player_placement = input("Where on the board will you like to place your symbol? Enter a valid tile between 1-9.")

        # Check if input is between 1-9
        if not player_placement.isnumeric():
            print("Invalid input.")

        # Check if input is between 1-9
        elif int(player_placement) not in range(1,10):
            print("Invalid input.")

        else:
            # Check if tile is occupied
            if board[int(player_placement)] != " ":
                print("This tile is already occupied.")

            else:
                board[int(player_placement)] = symbol.upper()
                valid_move = True

# ---------------------------- Win Condition Check --------------------------- #

def check_win(is_game_over, board):

    # Check rows
    for i in range(1, 10, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            print("Game Over.")
            is_game_over = True
        
    # Check columns
    for i in range(1,4):
        if board[i] == board[i+3] == board[i+6] != " ":
            print("Game Over.")
            is_game_over = True
    
    # Check diagonals
    if board[1] == board[5] == board[9] != " " or board[3] == board[5] == board[7] != " ":
            print("Game Over.")
            is_game_over = True

    if is_game_over:
        if turn_counter % 2 == 0:
            print("Player One has won!")
        else:
            print("Player Two has won!")

    return is_game_over

# -------------------------------- Check Draw -------------------------------- #

def check_draw(turn, is_game_over):
    if turn == 9 and not is_game_over:
        print("Game Over.")
        print("Tied Game.")
        is_game_over = True

    return is_game_over

# -------------------------------- Play Again -------------------------------- #

# This is only if game is over

def play_again():
    valid_choice = False
    play_again_choice = input("Do you want to play again? Y/N.")

    while not valid_choice:
        if play_again_choice.upper() not in ["Y", "N"]:
            print("Invalid Input.")
        else:
            valid_choice = True


    if play_again_choice.upper() == "Y":
        print("Playing Again...")
        return False
    else:
        return True

# -------------------------------- Reset Game -------------------------------- #

def reset_game():
    turn = 0

    board = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " "
    }

    return turn, board

# ---------------------------------------------------------------------------- #
#                                     Main                                     #
# ---------------------------------------------------------------------------- #

def main(turn, board):

    display_board(board)
    
    game_over = False
    
    player_one_symbol, player_two_symbol = game_start()

    while not game_over:
        place_symbol(player_one_symbol,player_two_symbol, turn, board)
        display_board(board)
        game_over = check_win(game_over, board)
        turn += 1
        game_over = check_draw(turn, game_over)

    if game_over:
        game_over = play_again()
        print("Thanks for playing.")
        if not game_over:
            new_turn, new_board = reset_game()
            main(new_turn, new_board)

# ------------------------------- Calling Main ------------------------------- #

if __name__ == "__main__":
    turn_counter = 0

    game_board = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " "
    }

    main(turn_counter, game_board)
