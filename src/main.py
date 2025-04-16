from player import Player
from deck import Deck

def main():
    # create the dealer and player
    dealer = Player(True)
    player = Player()
    
    #set the dealer's name 
    dealer.set_name("Sleazy McDice")

    # ask the player for their name and set it
    player_name = input("Welcome to the table! What's your name? ")
    player.set_name(player_name)

    # build the deck and shuffle it
    deck = Deck()
    deck.build_deck()
    deck.shuffle_deck()

if __name__ == "__main__":
    main()