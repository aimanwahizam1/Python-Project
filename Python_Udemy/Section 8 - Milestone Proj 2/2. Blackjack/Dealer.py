
from Player import Player

class Dealer(Player):
    def __init__(self) -> None:
        Player.__init__(self, "Dealer")

    def show_initial_hand(self):
        return f"FACE DOWN, {str(self.hand[-1])}"

    def print_initial_hand(self) -> str:
        print(f'\n{self.name}:\nHand: {self.show_initial_hand()}\n')

    def print_player_status(self) -> str:
        cards = list(map(str, self.hand))

        print(f'{self.name}:')
        print(f'Hand: {cards}')
        self.calculate_initial_hand_value()
        print(f'Hand Value: {self.hand_value}')
        print('------------')