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

class HandRankings:
    def __init__(self, score, cards):
        self.score = score
        self.cards = cards

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


    def checkForFlush(self, hand):
        suits = {"clubs": [], "diamonds": [], "hearts": [], "spades": []}
        
        for card in hand:
            suits[card['suit']].append(card)

        # Check each suit for a flush
        for suit, cards in suits.items():
            if len(cards) >= 5:
                if [card['value'] for card in cards[:5]] == [10, 11, 12, 13, 14]:
                    return 9  # Royal Flush
                if [card['value'] for card in cards[:5]] == [2, 3, 4, 5, 14]:
                    return 8  # Ace-low Straight Flush
                consecutive_count = 1
                for i in range(1, len(cards)):
                    if cards[i]['value'] == cards[i - 1]['value'] + 1:
                        consecutive_count += 1
                        if consecutive_count == 5:
                            return 8  # Straight Flush
                    else:
                        consecutive_count = 1
                return 5  # Regular Flush
        return None # No Flush found

    def checkForRank(self, hand):
        valid_pairs = []
        prev_val = hand[0]['value']
        consecutive_count = 1
        for i in range(1, len(hand)):
            if hand[i]['value'] == prev_val:
                consecutive_count += 1
            else:
                prev_val = hand[i]['value']
                print(f"new val {prev_val}")
                if consecutive_count == 4:
                    valid_pairs.append(HandRankings(7, hand[i - 4:i]))
                    consecutive_count = 1
                elif consecutive_count == 3:
                    valid_pairs.append(HandRankings(3, hand[i - 3:i]))
                    consecutive_count = 1
                elif consecutive_count == 2:
                    valid_pairs.append(HandRankings(2, hand[i - 2:i]))
                    consecutive_count = 1
        if len(valid_pairs) >= 1:
            return valid_pairs[0].score
        else: 
            return None

        # {done} Royal Flush 9: five cards of the same suit, ranked ace through ten
        # {done} Straight Flush 8 : five cards of the same suit and consecutively ranked
        # {done} Four of a Kind 7: four cards of the same rank
        # Full House 6: three cards of the same rank and two more cards of the same rank
        # {done} Flush 5: any five cards of the same suit
        # Straight 4: any five cards consecutively ranked
        # Three of a Kind 3: three cards of the same rank
        # Two Pair 2: two cards of the same rank and two more cards of the same rank
        # One Pair 1: two cards of the same rank
        # High Card 0: five unmatched cards



    
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


