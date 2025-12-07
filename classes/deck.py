from classes.card import Card, CardType, CardNumber
import random

class Deck:
    def __init__(self):
        self.__deck : list[Card] = []
        self.__initialize_deck()
    
    def size(self) -> None:
        return len(self.__deck)

    def pull(self) -> Card:
        if self.size() == 0:
            return None
        
        return self.__deck.pop()
    
    def shuffle(self) -> None:
        random.shuffle(self.__deck)

    def __initialize_deck(self) -> None:
        NUM_OF_DECKS = 6

        for _ in range(NUM_OF_DECKS):
            for t in CardType:
                for n in CardNumber:
                    self.__deck.append(Card(number=n, type=t))