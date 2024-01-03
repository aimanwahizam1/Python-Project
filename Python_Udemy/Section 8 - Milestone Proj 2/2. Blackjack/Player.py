"""
This is the script for the player class used in Blackjack

Player will be able to:
- Hold cards (initially given 2 face up cards)
- "Hit" receive a card from deck
- "Hold" do not receive any other cards, and end turn
"""

class Player():
    def __init__(self, name, bank=None) -> None:
        self.name = name
        self.bank = bank
        self.hand = []
        self.hand_value = 0
        self.bet = 0

    def get_initial_hand(self, new_cards):
        self.hand.extend(new_cards)

    def hit(self, new_card):
        self.hand.append(new_card)

    def choose_ace_value(self, new_card):
        print("\nYou have an unresolved Ace value.")
        if new_card.value == "Ace":
            while True:
                try:
                    user_input = int(input("Would you like this Ace to be 1 or 11? "))
                    if user_input not in [1,11]:
                        print("Please input either 1 or 11.")
                        continue
                except ValueError:
                    print("Please input a number that is either 1 or 11.")
                else:
                    print(f'This Ace is worth {user_input}.\n')
                    self.hand_value += user_input
                    break

    def calculate_initial_hand_value(self):
        if self.hand_value == 0:
            for card in self.hand:
                if card.value == "Ace":
                    self.choose_ace_value(card)
                else:
                    self.hand_value += card.rank
        else:
            pass
    
    def place_bet(self):
        while True:
            try:
                print(f'Your current bank is {self.bank}.')
                bet = int(input("Place a bet: "))

                if bet > self.bank:
                    print("Insufficient amount. Place another bet.")
                    continue
            except ValueError:
                print("Please input a number.")
            else:
                print(f'You have bet {bet}.\n')
                self.bank -= bet
                self.bet = bet
                break

    def add_winnings(self, winnings):
        self.bank += winnings
        self.bet = 0
        print(f'Congratulations. You have won {winnings}. Your new bank balance is {self.bank}.')


    def print_player_status(self) -> str:
        cards = list(map(str, self.hand))

        print(f'Player: {self.name}')
        print(f'Hand: {cards}')
        print(f'Bank: {self.bank}')
        self.calculate_initial_hand_value()
        if self.bet != 0:
            print(f'Bet: {self.bet}')
        print(f'Hand Value: {self.hand_value}')
        print('------------\n')
