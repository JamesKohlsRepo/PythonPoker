import json  
import random
from enum import Enum
# from winCalculation import determineWinner

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
        self.handValue = []
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
        """
        First, Each players cards (2 hand and 5 community) are sorted 
        """
        for player in self.players:
            full_hand = sorted(player.hand + self.community_cards, key=lambda card: card['value'])

            # check for flush should update some attribuite of the player
            self.checkForFlush(full_hand)


            #print(f"{player.name}'s sorted hand: {full_hand}")
            print("\n")

    def checkForFlush(self, hand):
        suits = {"clubs": [], "diamonds": [], "hearts": [], "spades": []}
        for card in hand:
            suit = card['suit']
            suits[suit].append(card)
        # Check each suit for a flush
        for suit, cards in suits.items():
            if len(cards) >= 5:
                # check for straight flush
                last_card_val = cards[0]['value']
                for card in cards[:1]:
                    if last_card_val != card['value'] + 1:
                        return ("Flush")
                return ("Straight / Royal Flush")


                # print(f"{suit}: ")
                # for card in cards:
                #     print(card['value'])
                #return("flush")
        # for suit in suits:
        #     if len(suit) >= 5:
        #         return(suit)
            # Step 2: Check for flush as soon as we have 5 cards of the same suit
            # if len(suits[suit]) == 5:
            #     compare_card = suits[suit][0]
            #     for x in range(1,5):
            #         if suits[suit][x]['value'] != compare_card['value']+1:
            #             return("Flush")
            #         else:
            #              compare_card = suits[suit][x]
            #     if suits[suit][-1]['value'] == 14:
            #         return("Royal Flush")
            #     else:
            #         return("Straight Flush")
        #print(suits)

                #     if suits[suit][-1].value == 14:
                #         return("Royal Fulsh")
                #     else: 
                #         return("Straight Flush")
                # else:
                #     return("Flush!")

                # full_hand is already sorted, so these are the top 5 cards in this suit
                # return suits[suit]


        # Royal Flush: five cards of the same suit, ranked ace through ten
        # Straight Flush: five cards of the same suit and consecutively ranked
        # Four of a Kind: four cards of the same rank
        # Full House: three cards of the same rank and two more cards of the same rank
        # Flush: any five cards of the same suit
        # Straight: any five cards consecutively ranked
        # Three of a Kind: three cards of the same rank
        # Two Pair: two cards of the same rank and two more cards of the same rank
        # One Pair: two cards of the same rank
        # High Card: five unmatched cards



    
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


