import unittest
from src.card import Card
from src.card_game import *

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card = Card("spades", 1)
        self.card1 = Card("clubs", 3)
        self.card2 = Card("diamonds", 8)
        self.cards = [self.card1, self.card2]
        self.cardgame = CardGame.check_for_ace(self, self.card)

    def test_check_for_ace(self):
        check_is_ace = CardGame.check_for_ace(self, self.card)
        self.assertEqual(True, check_is_ace)

    def test_highest_card(self):
        higher_card = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card2, higher_card)

    def test_cards_total(self):
        cards_total = CardGame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 11", cards_total)





