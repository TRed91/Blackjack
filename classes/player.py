from classes.card import Card, CardNumber
from classes.deck import Deck
from classes.results import PlayerResult

class Player:
    
    def __init__(self, name : str, is_human : bool = True):
        self.name : str = name
        self.is_human : bool = is_human
        self.hand : list[Card] = []
        self.points : int = 0
        self.result : PlayerResult = PlayerResult.NONE
    

    def take_card(self, deck : Deck) -> None:
        self.hand.append(deck.pull())


    def has_blackjack(self) -> bool:
        if (self.hand[0].number == CardNumber.ACE and (
            self.hand[1].number == CardNumber.TEN or 
            self.hand[1].number == CardNumber.JACK or 
            self.hand[1].number == CardNumber.QUEEN or 
            self.hand[1].number == CardNumber.KING)):
            return True
        if ((self.hand[0].number == CardNumber.TEN or 
            self.hand[0].number == CardNumber.JACK or 
            self.hand[0].number == CardNumber.QUEEN or 
            self.hand[0].number == CardNumber.KING) and
            self.hand[1].number == CardNumber.ACE):
            return True
        
        return False

    
    def calculate_points(self) -> None:
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

        self.points = total

    
    def __get_card_value(self, card : Card) -> int:
        if (card.number == CardNumber.KING or 
            card.number == CardNumber.QUEEN or 
            card.number == CardNumber.JACK or
            card.number == CardNumber.TEN):
            return 10
        
        return int(card.number.value)