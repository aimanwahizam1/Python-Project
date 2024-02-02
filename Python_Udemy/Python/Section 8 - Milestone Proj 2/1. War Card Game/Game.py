"""
This is the script for the game logic for War

- Compare played cards
    - Check who won and add played cards to player hand
    - If similar then go to "War"
        - I.E. each player plays 5 cards and compare top card
            - If player can't play 5 cards during war, they lose
- Check who has won
    - Which player no longer has cards loses

Need to create:
- 2 players
- Deck of cards
"""
import Player
import Deck

# ----------------------------------- Setup ---------------------------------- #
player_one = Player.Player("One")
player_two = Player.Player("Two")

new_deck = Deck.Deck()
new_deck.shuffle()

# Split the deck and hand to players
for i in range(26):
    player_one.add_cards(new_deck.deal_one_card())
    player_two.add_cards(new_deck.deal_one_card())

game_over = False
round_number = 0

while not game_over:
    round_number += 1
    print(f'Round {round_number}')

    # Game over logic
    if not player_one.hand or not player_two.hand:
        if not player_one.hand:
            print(f'{player_two.name} has won!')
        else:
            print(f'{player_one.name} has won!')
        game_over = True
        break

    # Start a new round
    player_one_cards = []
    player_two_cards = []

    player_one_cards.append(player_one.play_one())
    player_two_cards.append(player_two.play_one())

    # Compare cards and see if at war
    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR!")
            if len(player_one.hand) < 5:
                print(f'{player_two.name} has won! Since {player_one.name} is unable to war.')
                game_over = True
                break
            elif len(player_two.hand) < 5:
                print(f'{player_one.name} has won! Since {player_two.name} is unable to war.')
                game_over = True
                break
            else:
                for i in range(5):
                    player_one_cards.append(player_one.play_one())
                    player_two_cards.append(player_two.play_one())
