import unittest
from src.card import Card
from src.card_game import *

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card = Card("spades", 1)
        self.card1 = Card("clubs", 3)
        self.card2 = Card("diamonds", 8)
        self.cards = [self.card1, self.card2]
        # self.cardgame = CardGame.check_for_ace(self, self.card)

    def test_check_for_ace(self):
        self.assertEqual(True, card_game.check_for_ace(self.card))







