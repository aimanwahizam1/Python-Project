# Global variables
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
turn = 1
current_player = 1


# Ask the two players which symbol and see who goes first
# Returns 1 or 2 (player who goes first)
def player_start():
    valid_input = False

    while not valid_input:
        player1 = input('Player 1: X or O?')

        if player1.lower() in ["x", "o"]:
            valid_input = True

            if player1.lower() == "x":
                print("Player 1 goes first.")
                return 1
            else:
                print("Player 2 goes first.")
                return 2
            
        else:
            print("Not a valid choice.")

# Display board
def display_board(board):
    print("Current board: ")

    print(board[1], "|", board[2], "|", board[3], "|")
    print(board[4], "|", board[5], "|", board[6], "|")
    print(board[7], "|", board[8], "|", board[9], "|")

    return board

#display_board(board)

# Turn mechanic
def player_turn(player,board, turn):

    if turn % 2 == 1:
        player_symbol = 'x'
    else:
        player_symbol = 'o'

    player_turn = player
    valid_move = False

    print(f"It is Player {player_turn}'s turn")

    while not valid_move:
        player_input = input("Choose a valid tile: ")

        if player_input.isdigit() == False:
            print('Invalid Input')
        
        elif int(player_input) not in range(1,10):
            print('Not a valid tile')


        elif board[int(player_input)] != " ":
            print("This tile is occupied")
            
        else:
            board[int(player_input)] = player_symbol
            valid_move = True
    
    turn += 1 

    if player == 1:
        player = 2
    else:
        player = 1

    return board, turn, player

# Game logic
def is_game_over(board):

    #Row check
    for i in range(1,10,3): #1,4,7
        if board[i] == board[i+1] == board[i+2] and board[i] != " ":
            return True

    #Column check
    for i in range(1,4): #1,2,3
            if board[i] == board[i+3] == board[i+6] and board[i] != " ":
                return True
        
    #Diagonal check
    if board[1] == board[5] and board[9] != " ":
            return True
    if board[3] == board[5] and board[7] != " ":
        return True
        
    return False

# Ask to play again
def play_again():
    valid_input = ["Y", "N"]
    valid = False

    while not valid:
        player_input = input('Do you want to play again? Y or N')

        if player_input.upper() not in valid_input:
            print("Invalid input.")
        else:
            valid = True
    
    if valid:
        if player_input.upper() == 'Y':
            return True
        return False

# Main
def main(current_player, turn, board):
    game_active = True
    current_player = player_start()

    while game_active:
        display_board(board)
        board, turn, current_player = player_turn(current_player,board, turn)
        display_board(board)
        if is_game_over(board):
            game_active = False;

    if not game_active:
        game_active = play_again()
        if game_active:
            print("Playing again...")
            main(current_player, turn, board)


main(current_player,turn,board)