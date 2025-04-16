from player import Player
from deck import Deck
from card import Card

def main():
    # create the dealer and player
    dealer = Player(True)
    player = Player()
    
    #set the dealer's name 
    dealer.set_name("Sleazy McDice")

    # ask the player for their name and set it
    player_name = input("Welcome to the table! What's your name? ")
    print_divider()
    player.set_name(player_name)

    # build the deck and shuffle it
    deck = Deck()
    deck.build_deck()
    deck.shuffle_deck()

    print(f"Hello, {player.get_name()}! I'm {dealer.get_name()}, your dealer.")

    # ask the player if they're ready to be dealt in
    # don't proceed until they answer yes (y)
    question = f"Are you ready to be dealt in?"
    ask_yes_no_question(question)
    print_divider()

    # deal the initial hand
    deck.deal_initial_hand(player, dealer)

    # reveal the players hand/value and reveail the dealer's first card/value
    print(f"{player.get_name()}'s hand: {player.get_hand()} - {player.get_hand_value()}")
    print(f"{dealer.get_name()} is showing {dealer.get_hand()[0]} - {dealer.get_hand()[0].get_value()}")

    print_divider()

    # ask the player if they want to hit or stand
    deck.hit_or_stand(player)

    print_divider()

    # once they're done, the deal should play regardless of whether or
    # not the player busted
    print(f"{dealer.get_name()} reveals his second card. It's a {dealer.get_hand()[1]}.")
    print("")
    print(f"{dealer.get_name()}'s hand: {dealer.get_hand()} - {dealer.get_hand_value()}")
    deck.hit_or_stand(dealer)

    print_divider()

def ask_yes_no_question(question):
    not_ready = True
    while not_ready:
        answer = input(f"{question} (y or n): ").lower()
        if answer == "y":
            not_ready = False
        elif answer == "n":
            not_ready = True
        else:
            print("Sorry, I couldn't understand that. Please answer " \
            "y or n")

def hit_or_stand():
    pass

def print_divider():
    print("")
    print("==========")
    print("")

if __name__ == "__main__":
    main()