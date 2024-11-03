import json  
import random

class Deck:
    def __init__(self):
        with open('cards.json', 'r') as file:
            self.cards = json.load(file)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number=1):
        delt_cards = []
        for _ in range(number):
            delt_cards.append(self.cards.pop()) 
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

    def addPlayer(self, players):
        for player in players:
            self.players.append(player) 


# newGame = PokerGame()

# Player_1 = Player("James")
# Player_2 = Player("Belle")

# newGame.addPlayer([Player_1, Player_2])
# for item in newGame.players:
#     print(item.name)


