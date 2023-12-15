"""
This is the script for the player class used in card games

Player will be able to:
- Hold cards in hand - with a top and bottom
    - Remove/"Play" cards from top
    - Add cards to bottom
- Remove cards from hand
- Gain either single or multiple cards to hand
"""

class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.hand = []

    def play_one(self):
        return self.hand.pop(0)

    def add_cards(self, new_cards):
        # Adding multiple cards
        if type(new_cards) == type([]):
            self.hand.extend(new_cards)
        # Adding single card
        else:
            self.hand.append(new_cards)

    def __str__(self) -> str:
        return f'Player {self.name} has {len(self.hand)} cards.'
    