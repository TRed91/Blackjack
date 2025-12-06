from classes.deck import Deck
from classes.card import CardNumber, CardType
import unittest

class Test_Deck(unittest.TestCase):
    def test_deck_initializes(self):
        deck = Deck()

        self.assertEqual(deck.size(), 13 * 4 * 6)

if __name__ == "__main__":
    unittest.main()