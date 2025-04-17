class Player:
    def __init__(self, is_dealer=False):
        self.__name = None
        self.__is_dealer = is_dealer
        self.__bust = False
        
        self.__hand = []
    
    def set_name(self, name):
        # no need to set the name if it's set already
        if not self.__name:
            if not isinstance(name, str):
                raise ValueError("Oops! Your name has to be in string format.")

            self.__name = name
        else:
            raise ValueError("Sorry. You already told me your name and I'm too stubborn " \
            "to learn a new one.")
    
    def get_name(self):
        return self.__name
    
    def get_is_dealer(self):
        return self.__is_dealer
    
    def set_bust(self):
        self.__bust = True
    
    def get_bust(self):
        return self.__bust
    
    def add_card_to_hand(self, card):
        self.__hand.append(card)
    
    def get_hand(self):
        return self.__hand
    
    def clear_hand(self):
        self.__hand.clear()
    
    def get_hand_value(self):
        total_value = 0
        aces_in_hand = 0
        for card in self.__hand:
            if card.get_face() == "Ace":
                aces_in_hand += 1
            else:
                total_value += card.get_value()
        if aces_in_hand > 0:
            for i in range(0, aces_in_hand):
                if total_value + 11 <= 21:
                    total_value += 11
                else:
                    total_value += 1
        if total_value > 21:
            self.set_bust()
        return total_value