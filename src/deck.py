import random
from card import Card
from player import Player

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

    def deal_single_card(self, player):
        player.add_card_to_hand(self.cards.pop())

    def deal_initial_hand(self, player, dealer):
        player.clear_hand()
        dealer.clear_hand()

        self.deal_single_card(player)
        self.deal_single_card(dealer)
        self.deal_single_card(player)
        self.deal_single_card(dealer)
    
    def hit_or_stand(self, player):
        if player.get_is_dealer() == False:
            action = ""
            while action != "stand":
                action = input("Do you want to hit or stand? ")
                if action == "hit":
                    print("")

                    self.deal_single_card(player)

                    print(f"{player.get_name()}'s hand: {player.get_hand()} - {player.get_hand_value()}")
                    if player.get_bust() == True:
                        print("")
                        print("You have busted! Better luck next time.")
                        break
                elif action == "stand":
                    break
                else:
                    raise ValueError("I don't understand. You have to type 'hit'" \
                    "or 'stand'.")
        else:
            while player.get_hand_value() < 17:
                self.deal_single_card(player)

                print(f"{player.get_name()}'s hand is now {player.get_hand()} - {player.get_hand_value()}")

                if player.get_bust() == True:
                    print("")
                    print("The dealer has busted!")
                    break