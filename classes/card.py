from enum import Enum

class CardType(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

class CardNumber(Enum):
    ACE = "Ace"
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"


class Card:
    def __init__(self, number : CardNumber ,type : CardType):
        self.number = number
        self.type = type
    
    