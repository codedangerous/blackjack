class Card:
    def __init__(self, suit, face_value):
        self.__suit = suit
        self.__face = face_value
    
    def __repr__(self):
        return f"{self.__face} of {self.__suit}"
    
    def get_value(self):
        match (self.__face):
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return 4
            case 5:
                return 5
            case 6: 
                return 6
            case 7: 
                return 7
            case 8:
                return 8
            case 9:
                return 9
            case 10:
                return 10
            case "Jack":
                return 10
            case "Queen":
                return 10
            case "King":
                return 10
            case "Ace":
                return (1, 11)
            case _:
                raise ValueError("Oops! You've tried to create a card with an " \
                "invalid face value.")