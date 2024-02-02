from random import shuffle

# 1. Shuffle cups
# 2. Take user guess
# 3. Check user guess

# -------------------------------- Shuffle Cup ------------------------------- #

# cup_list format = [,0,]
# two empty values one 0 value

def shuffle_cup(cup_list):
    shuffle(cup_list)
    return(cup_list)

# -------------------------------- User Input -------------------------------- #

def user_guess():
    guess = input("Guess a number between 1 and 3: ")
    print(f'{guess=}')

    if guess not in ["1", "2", "3"]:
        print("Invalid Guess.")
        guess = user_guess()
    
    return int(guess)

# -------------------------------- Check Guess ------------------------------- #

def check_guess(shuffled_cups, guess):
    if shuffled_cups[guess - 1] == 0:
        print("Well done! You got the ball.")

    else:
        print("Better luck next time.")
    
    print(shuffled_cups)

# ------------------------------- Play the game ------------------------------ #
def main():
    cups = ["",0,""]
    
    shuffled_cups = shuffle_cup(cups)
    guess = user_guess()
    check_guess(shuffled_cups, guess)

    pass

# The below makes it that if RAN DIRECTLY (i.e. not imported) function main() will run 
# But if it was being imported, then the main() will not be ran.
# This is good because e.g. import this file into another game, it wont run the whole ball cup game but still allows you to use the other methods made in this file for this game
# E.g. can use ball cup in game.check_guess() method in an import without running the whole game itself

if __name__ == '__main__':
    main()