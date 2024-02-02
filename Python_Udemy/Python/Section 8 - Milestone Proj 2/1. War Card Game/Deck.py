"""
This is the script for the deck class used in card games

This will be made up of 52 cards.
"""
import random
import Card

class Deck():
    def __init__(self) -> None:
        self.all_cards = []

        # Creating the cards
        for suit in Card.suits:
            for value in Card.values:
                created_card = Card.Card(suit, value)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one_card(self):
        return self.all_cards.pop()
    