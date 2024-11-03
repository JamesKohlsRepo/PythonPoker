import unittest
from main import Deck, Player, PokerGame  # Adjust to the actual file/module name

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()  # Create a new deck for each test

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 52)  # Assuming a standard deck size

    def test_shuffle(self):
        original_order = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.cards)  # Order should be different

    def test_deal(self):
        initial_deck_size = len(self.deck.cards)
        card = self.deck.deal(1)  # Deal one card, returns a list with one item
        self.assertIsInstance(card, list)  # Expect a list
        self.assertEqual(len(card), 1)  # List should contain exactly one card
        self.assertIsInstance(card[0], dict)  # The first (and only) item should be a dictionary
        self.assertIn('suit', card[0])
        self.assertIn('value', card[0])

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("TestPlayer")

    def test_player_initialization(self):
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.hand, [])
        self.assertFalse(self.player.isHuman)

class TestPokerGame(unittest.TestCase):
    def setUp(self):
        self.game = PokerGame()
        self.player1 = Player("James")
        self.player2 = Player("Belle")

    def test_add_player(self):
        self.game.addPlayer([self.player1, self.player2])
        self.assertEqual(len(self.game.players), 2)
        self.assertEqual(self.game.players[0].name, "James")
        self.assertEqual(self.game.players[1].name, "Belle")

    def test_community_cards(self):
        self.game.deck.shuffle()
        for _ in range(5):  # Deal 5 community cards as in poker
            self.game.community_cards.append(self.game.deck.deal())
        self.assertEqual(len(self.game.community_cards), 5)

if __name__ == '__main__':
    unittest.main()