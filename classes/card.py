from enum import Enum

class CardType(Enum):
    HEARTS = "H"
    DIAMONDS = "D"
    CLUBS = "C"
    SPADES = "S"

class CardNumber(Enum):
    ACE = "A"
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = "T"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"


class Card:
    
    def __init__(self, number : CardNumber ,type : CardType):
        self.number = number
        self.type = type
    
    