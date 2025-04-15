class Player:
    def __init__(self, is_dealer=False):
        self.__name = None
        self.__is_dealer = is_dealer
        
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
