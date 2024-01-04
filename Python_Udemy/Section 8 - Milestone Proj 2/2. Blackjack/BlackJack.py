from Deck import Deck
from Player import Player
from Dealer import Dealer

# -------------------------------- Game Setup -------------------------------- #

def initiate_players():
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

if __name__ == "__main__":
    # -------------------------------- Game Setup -------------------------------- #
    print("Welcome to BlackJack!")
    print('------------\n')
    players = initiate_players()
    busted_players = 0

    players_turn = True
    deck = Deck()
    deck.shuffle()

    # ------------------------------- Dealer Setup ------------------------------- #
    dealer = Dealer()
    dealer.get_initial_hand(deck.deal_two_cards())
    dealer.print_initial_hand()

    # --------------------------------- Gameplay --------------------------------- #
    for player in players:
        player.get_initial_hand(deck.deal_two_cards())

    for player in players:

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
                    turn_over = True
                    busted_players += 1
                    break
            else:
                turn_over = True
                break

    # -------------------------------- Dealer Turn ------------------------------- #
    if busted_players == len(players):
        print("All players are busted.")
        print("Dealer wins!")

    else:
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

    # --------------------------------- Game End --------------------------------- #
    for player in players:
        if player.hand_value < 21 and (dealer.hand_value > 21 or player.hand_value > dealer.hand_value):
            player.add_winnings(player.bet * 2)
        elif player.hand_value > 21 or (dealer.hand_value >= player.hand_value and dealer.hand_value < 21):
            print(f"Dealer wins compared versus {player.name}.")
            print(f"{player.name} has lost {player.bet}")
            print(f"{player.name}'s bank is now {player.bank}")
        print('------------')

    