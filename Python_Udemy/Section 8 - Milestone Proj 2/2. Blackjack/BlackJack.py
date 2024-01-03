from Deck import Deck
from Player import Player
from Dealer import Dealer

# -------------------------------- Game Setup -------------------------------- #
game_over = False
player_one = Player("One", 100)
dealer = Dealer()
deck = Deck()

deck.shuffle()

player_one.get_initial_hand(deck.deal_two_cards())
player_one.print_player_status()

dealer.get_initial_hand(deck.deal_two_cards())
dealer.print_initial_hand()

# --------------------------------- Gameplay --------------------------------- #

# Place bets
player_one.place_bet()
player_one.print_player_status()

# Player turn
while True:
    player_move = input("Do you want to Hit or Stay? ")

    if player_move.lower() not in ["hit", "stay"]:
        continue
    elif player_move.lower() == "hit":
        dealt_card = deck.deal_one_card()
        print(f'You got: {str(dealt_card)}\n')

        if dealt_card.value == "Ace":
            player_one.choose_ace_value()
        else:
            player_one.hand_value += dealt_card.rank
    
        player_one.hit(dealt_card)
        player_one.print_player_status()

        if player_one.hand_value > 21:
            print("BUST!\n")
            game_over = True
            break
    else:
        break

while not game_over:
    print("\nDealer's Turn")

    dealer.print_player_status()

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
    else:
        game_over = True
        break

if (dealer.hand_value >= player_one.hand_value and dealer.hand_value < 21) or player_one.hand_value > 21:
    print("Dealer Wins!")
elif player_one.hand_value < 21 and (player_one.hand_value > dealer.hand_value or dealer.hand_value > 21):
    print(f'Player {player_one.name} Wins!')
    player_one.add_winnings(player_one.bet * 2)
