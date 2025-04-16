import random
from card import Card

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

class Deck:
    def __init__(self):
        self.cards = []

    def build_deck(self):
        for suit in suits:
            for face in faces:
                card = Card(suit, face)
                self.cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.cards)