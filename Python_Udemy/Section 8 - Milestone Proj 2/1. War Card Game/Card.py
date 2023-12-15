"""
This is the script for the card class used in card games

It will have:
- Suit
- Value (2 - Ace)
- Rank for comparison (2 -> 2, lowest) (Ace -> 14, highest)
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
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14
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
    
# Example testing
""" two_hearts = Card("Hearts", "Two")
print(two_hearts)
print(two_hearts.suit)
print(two_hearts.value)
print(two_hearts.rank) """