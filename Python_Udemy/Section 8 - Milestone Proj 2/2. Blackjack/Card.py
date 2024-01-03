"""
This is the script for the card class used in card games

It will have:
- Suit
- Value (2 - Ace)
    - Ace can either be chosen to have a value of 1 or 11
- Rank for comparison (2 -> 2, lowest) (Ace -> 11, highest)
"""

# ----------------------------- Global Variables ----------------------------- #

value_rank_map = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 12
}

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
values = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

class Card():
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value
        self.rank = value_rank_map[value]

    def __str__(self) -> str:
        return self.value + " of " + self.suit