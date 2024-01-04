from Deck import Deck
from Player import Player
from Dealer import Dealer

# ------------------------------ Game Functions ------------------------------ #

def initiate_players() -> list[Player]:
    number_of_players = 0
    players = []
    
    while True:
        try:
            number_of_players = int(input("How many players are joining us at the table? "))
        except ValueError:
            print("Please input a number.")
            continue
        else:
            print(f"\nThe number of players are {number_of_players}.")
            break
        
    for i in range(number_of_players):
        player_name = ""
        player_bank = 0

        while True:
            print(f"Welcome Player {i+1}.")
            player_name = input("What is your name? ")

            if len(player_name) == 0:
                print("Please input a name.")
                continue
            else:
                print(f"\nWelcome {player_name}")
                break

        while True:
            try:
                player_bank = int(input("How much do you want to buy in? "))
            except ValueError:
                print("Please input a number.")
                continue
            except player_bank == 0:
                print("Error. Cannot bank in 0.")
                continue
            else:
                print(f"\n{player_name} has an initial bank of {player_bank}.")
                print('------------')
                break
        
        players.append(Player(player_name,player_bank))

    return players

def dealer_setup():
    dealer = Dealer()
    dealer.get_initial_hand(deck.deal_two_cards())
    dealer.print_initial_hand()

    return dealer

def player_turn(player):
    print('\n------------')
    print(f"{player.name}'s Turn.")
    print('------------\n')

    player.print_player_status()

    player.place_bet()
    player.print_player_status()    

    while True:
        player_move = input("Do you want to Hit or Stay? ")
        if player_move.lower() not in ["hit", "stay"]:
            continue
        elif player_move.lower() == "hit":
            dealt_card = deck.deal_one_card()
            print(f'\nYou got: {str(dealt_card)}\n')

            if dealt_card.value == "Ace":
                player.choose_ace_value(dealt_card)
            else:
                player.hand_value += dealt_card.rank
        
            player.hit(dealt_card)
            player.print_player_status()

            if player.hand_value > 21:
                print("BUST!")
                break
        else:
            break

def dealer_turn(dealer):
    print("\nDealer's Turn")

    dealer.print_player_status(initial=True)

    while dealer.hand_value < 17:
        dealt_card = deck.deal_one_card()

        if dealt_card.value == "Ace":
            if dealer.hand_value + 11 > 21:
                dealer.hand_value += 1
            else:
                dealer.hand_value += 11
        else:
            dealer.hand_value += dealt_card.rank
        dealer.hit(dealt_card)
        dealer.print_player_status()

# ------------------------------ Game Execution ------------------------------ #
if __name__ == "__main__":
    # -------------------------------- Game Setup -------------------------------- #
    print("Welcome to BlackJack!")
    print('------------\n')
    players = initiate_players()
    print(type(players))

    deck = Deck()
    deck.shuffle()

    # ------------------------------- Dealer Setup ------------------------------- #
    dealer = dealer_setup()

    # --------------------------------- Gameplay --------------------------------- #
    for player in players:
        player.get_initial_hand(deck.deal_two_cards())

    for player in players:
        player_turn(player)

    # -------------------------------- Dealer Turn ------------------------------- #
    dealer_turn(dealer)

    # --------------------------------- Game End --------------------------------- #
    for player in players:
        if player.hand_value < 21 and (dealer.hand_value > 21 or player.hand_value > dealer.hand_value):
            player.add_winnings(player.bet * 2)
        elif player.hand_value > 21 or (dealer.hand_value >= player.hand_value and dealer.hand_value < 21):
            print(f"Dealer wins compared versus {player.name}.")
            print(f"{player.name} has lost {player.bet}")
            print(f"{player.name}'s bank is now {player.bank}")
        print('------------')

    