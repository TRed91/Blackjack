from classes.card import Card, CardNumber
from classes.deck import Deck

class Player:
    def __init__(self, name : str, is_human : bool = True):
        self.name : str = name
        self.is_human : bool = is_human
        self.hand : list[Card] = []
        self.points : int = 0
    
    def take_card(self, deck : Deck) -> None:
        self.hand.append(deck.pull())
    
    def calculate_points(self) -> int:
        if len(self.hand) == 0:
            return 0
        
        ace_count = 0
        total = 0
        for card in self.hand:
            
            value = 0
            
            if card.number == CardNumber.ACE:
                ace_count += 1
            else:
                value = self.__get_card_value(card)

            total += value
        
        for _ in range(ace_count):
            if total + 11 > 21:
                total += 1
            else:
                total += 11

        return total
    
    def __get_card_value(self, card : Card) -> int:
        if (card.number == CardNumber.KING or 
            card.number == CardNumber.QUEEN or 
            card.number == CardNumber.JACK):
            return 10
        
        return card.number.value[0]