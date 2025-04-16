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

    print(f"Hello, {player.get_name()}!")

    # ask the player if they're ready to be dealt in
    # don't proceed until they answer yes (y)
    question = f"Are you ready to be dealt in?"
    ask_yes_no_question(question)

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

if __name__ == "__main__":
    main()