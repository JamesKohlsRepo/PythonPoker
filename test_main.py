import unittest
from main import Deck, Player, PokerGame, GameState  # Adjust to the actual file/module name

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()  # Create a new deck for each test

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), self.deck.originalDeckSize) 

    def test_shuffle(self):
        original_order = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.cards)  # Order should be different

    def test_deal(self):
        card = self.deck.deal(1)  
        self.assertIsInstance(card, list)  
        self.assertEqual(len(card), 1)  
        self.assertIsInstance(card[0], dict)  
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
        self.player3 = Player("Robot")

    def test_add_player(self):
        self.game.addPlayers(self.player1)
        self.assertEqual(len(self.game.players), 1)
        self.assertEqual(self.game.players[0].name, "James")
        
    def test_add_players(self):
        self.game.addPlayers(self.player1, self.player2, self.player3)
        self.assertEqual(len(self.game.players), 3)
        self.assertEqual(self.game.players[2].name, "Robot")

    def test_remove_players(self):
        self.game.addPlayers(self.player1, self.player2, self.player3)
        self.game.removePlayers(self.player2)
        self.assertEqual(len(self.game.players), 2)
        self.assertEqual(self.game.players[1].name, "Robot")

    def test_community_cards(self):
        self.game.deck.shuffle()
        self.game.community_cards.extend(self.game.deck.deal(5))
        self.assertEqual(len(self.game.community_cards), 5)

class TestPokerGameState(unittest.TestCase):
    def setUp(self):
        self.game = PokerGame()
        self.player1 = Player("user1")
        self.player2 = Player("user2")
        self.player3 = Player("user3")
        self.player4 = Player("user4")

    def _fourPlayerGame(self):
        self.game.addPlayers(self.player1, self.player2, self.player3, self.player4)
        self.game.deck.shuffle()

    def test_notEnoughPlayers(self):
        self.game.addPlayers(self.player1)
        self.assertEqual(self.game.advance_state(), "error, not enough players")

    def test_enoughPlayersStartGame(self):
        self.game.addPlayers(self.player1, self.player2)
        self.game.advance_state()
        self.assertEqual(self.game.current_state, GameState.PRE_FLOP)

    def test_dealtwocards(self):
        self._fourPlayerGame()
        self.game.advance_state()
        counter = 0
        for player in self.game.players:
            self.assertEqual(len(player.hand), 2) 
            counter += 2
        self.assertEqual(len(self.game.deck.cards), (self.game.deck.originalDeckSize-counter)) 

    def test_communityCardDeals(self):
        self._fourPlayerGame()
        self.game.advance_state()
        self.game.advance_state()
        self.assertEqual(self.game.current_state, GameState.FLOP)
        self.assertEqual(len(self.game.community_cards), 3)
        self.game.advance_state()
        self.assertEqual(self.game.current_state, GameState.TURN)
        self.assertEqual(len(self.game.community_cards), 4)
        self.game.advance_state()
        self.assertEqual(self.game.current_state, GameState.RIVER)
        self.assertEqual(len(self.game.community_cards), 5)

if __name__ == '__main__':
    print("\nBEGIN TESTING")
    unittest.main()