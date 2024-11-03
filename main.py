import json  
import random
from enum import Enum

class GameState(Enum):
    INIT = 0                
    PRE_FLOP = 1
    FLOP = 2
    TURN = 3
    RIVER = 4
    SHOWDOWN = 5
    END = 6

class Deck:
    def __init__(self):
        with open('cards.json', 'r') as file:
            self.cards = json.load(file)
        self.originalDeckSize = len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number=1):
        """ Returns: (List) cards removed from overall deck """
        delt_cards = []
        for _ in range(number):
            delt_cards.append(self.cards.pop(0)) 
        return delt_cards

class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.hand = []
        self.isHuman = False

class PokerGame:
    def __init__(self):
        self.community_cards = []
        self.deck = Deck()
        self.players = []
        self.discard = []
        self.current_state = GameState.INIT

    def addPlayers(self, *players):
        """ *players allows any number of arguments to be passed """
        for player in players:
            self.players.append(player)

    def removePlayers(self, *rm_players):
        """ Returns: (List) removed player(s) """
        removed_players = []
        for player in rm_players:
            if player in self.players:
                self.players.remove(player)
                removed_players.append(player)
            return removed_players
    
    def deal_hands(self):
        """ Deals two cards to each player """
        for player in self.players:
            player.hand.extend(self.deck.deal(2))

    def deal_community(self, count):
        """ Deals community cards"""
        self.community_cards.extend(self.deck.deal(count))

    def showdown(self):
        print()
    
    def advance_state(self):
        if self.current_state == GameState.INIT:
            if len(self.players) >= 2:
                self.deal_hands()
                #self.post_blinds()
                self.current_state = GameState.PRE_FLOP
            else:
                return("error, not enough players")
        elif self.current_state == GameState.PRE_FLOP:
            self.deal_community(3)
            self.current_state = GameState.FLOP
        elif self.current_state == GameState.FLOP:
            self.deal_community(1)
            self.current_state = GameState.TURN
        elif self.current_state == GameState.TURN:
            self.deal_community(1)
            self.current_state = GameState.RIVER
        elif self.current_state == GameState.RIVER:
            self.showdown()
            self.current_state = GameState.SHOWDOWN
        elif self.current_state == GameState.SHOWDOWN:
            self.current_state = GameState.END


    # the Blinds
    # Preflop
    # Flop
    # The Turn
    # The River
    # The Showdown

# newGame = PokerGame()

# Player_1 = Player("James")
# Player_2 = Player("Belle")

# newGame.addPlayer([Player_1, Player_2])
# for item in newGame.players:
#     print(item.name)


