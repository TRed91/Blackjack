from classes.player import Player
from classes.card import Card, CardNumber, CardType
from classes.deck import Deck
import unittest

class Test_Player(unittest.TestCase):
    def test_player_takes_card(self):
        player = Player("John")
        
        self.assertEqual(len(player.hand), 0)

        deck = Deck()

        player.take_card(deck)
        player.take_card(deck)
        
        self.assertEqual(len(player.hand), 2)

    def test_counts_points_when_empty(self):
        player = Player("John")
        
        self.assertEqual(player.calculate_points(), 0)

    def test_counts_points(self):
        player = Player("John")
        player.hand = [
            Card(CardNumber.FOUR, CardType.DIAMONDS),
            Card(CardNumber.SIX, CardType.SPADES)
        ]
        
        self.assertEqual(player.calculate_points(), 10)

        player.hand.append(Card(CardNumber.KING, CardType.HEARTS))
        self.assertEqual(player.calculate_points(), 20)

        player.hand.append(Card(CardNumber.ACE, CardType.HEARTS))
        self.assertEqual(player.calculate_points(), 21)



if __name__ == "__main__":
    unittest.main()