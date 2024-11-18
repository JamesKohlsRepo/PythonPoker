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
        self.handValue = HandRankings(0, [], [])
        self.isHuman = False

class HandRankings:
    def __init__(self, score, r_cards, k_cards):
        self.score = score
        self.rank_cards = r_cards
        self.kick_cards = k_cards

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
        Evaluates each player's hand and determines their best hand ranking.
        """
        for player in self.players:
            full_hand = sorted(player.hand + self.community_cards, key=lambda card: card['value'])
            player.handValue = self.checkForHighCard(full_hand)
            checks = [self.checkForFlush, self.checkForRank, self.checkForStraight]

            # Iterate over each hand ranking check
            for check in checks:
                result = check(full_hand)
                if result is not None and player.handValue.score < result.score:
                    player.handValue = result

            # Print the player's hand value
            print(f"{player.name} : {player.handValue.score} {player.handValue.rank_cards}")
        

    def checkForFlush(self, hand):
        """
        Takes a hand of 7 cards, returns all valid Flushes
        * know bug: Ace-low straight flush will not return the correct cards to consider *

        Parameters:
        hand (List of Dicts): 2 hand cards + 5 community cards 

        Returns 
        if flush found:
            HandRankings (obj): ranking (0-9), five cards that comprise the best hand, list of kicker cards
        else: 
            None
        """
        suits = {"clubs": [], "diamonds": [], "hearts": [], "spades": []}
        
        for card in hand:
            suits[card['suit']].append(card)

        # Check each suit for a flush
        for suit, cards in suits.items():
            if len(cards) >= 5:
                flush_cards = cards[-5:]
                if [card['value'] for card in cards[:5]] == [10, 11, 12, 13, 14]:
                    return HandRankings(9, flush_cards, []) # royal flush
                if [card['value'] for card in cards[:5]] == [2, 3, 4, 5, 14]:
                    return HandRankings(8, flush_cards, []) # Ace-low Straight Flush, to be fixed later
                consecutive_count = 1
                straight_flush_cards = [flush_cards[0]]
                for i in range(1, len(cards)):
                    if cards[i]['value'] == cards[i - 1]['value'] + 1:
                        consecutive_count += 1
                        straight_flush_cards.append(cards[i])
                        if consecutive_count == 5:
                            return HandRankings(8, straight_flush_cards[-5:], [])  # Straight Flush
                    else:
                        consecutive_count = 1
                        straight_flush_cards = [cards[i]]
                return HandRankings(5, flush_cards, []) # Regular Flush
        return None # No Flush found

    def checkForPairs(self, hand):
        """
        Helper function for CheckForRank, returns all pairs

        Parameters:
        hand (List of Dicts): 2 hand cards + 5 community cards 

        Returns:
        valid_pairs (list of list): cards comprising the hand
        reconstructed_list (list): cards not used in pairs, used for creating the kicker list
        """
        valid_pairs = []
        ranks = {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: []}
        for card in hand:
            ranks[card['value']].append(card)

        for rank in reversed(list(ranks.items())):
            i  = len(rank[1])
            if i >= 2:
                valid_pairs.append(rank[1])
                ranks[rank[0]] = []
                #return i
        reconstructed_list = []
        for rank in ranks.keys():
            reconstructed_list.extend(ranks[rank])
        
        return valid_pairs, reconstructed_list

    def checkForRank(self, hand):
        """
        Takes the results from CheckForPairs, then determines stuff
                
        Paramters:
        hand (List of Dicts): 2 hand cards + 5 community cards 
                
        Returns:
        if flush found:
            HandRankings (obj): ranking (0-9), five cards that comprise the best hand, list of kicker cards
        else: 
            None
        """
        results,remaining = self.checkForPairs(hand)
        results = sorted(results, key=len, reverse=True) # allows the 3 pairs to be considered first
        if len(results) == 1:
            if len(results[0]) >= 4:
                return HandRankings(7, results[0], [remaining[-1]]) # four of a kind
            else:
                if len(results[0]) == 3:
                    return HandRankings(3, results[0], [remaining[-(5-len(results[0])):]]) # three of a kind
                else:
                    return HandRankings(1, results[0], [remaining[-(5-len(results[0])):]]) # two of a kind
        elif len(results) == 2:
            if len(results[0]) == 4:
                remaining.extend(results[1])  # Extend the remaining list with results[1]
                remaining = sorted(remaining, key=lambda card: card['value'])
                return HandRankings(7, results[0], [remaining[-1]]) # four of a kind
            elif len(results[0]) == 3 and len(results[1]) == 3:
                results[1].pop() # removes the last item to make a full house
                x = results[0] + results[1]
                return HandRankings(6, x, []) # full house
            elif len(results[0]) == 3 and len(results[1]) == 2:
                x = results[0] + results[1]
                return HandRankings(6, x, []) # full house
            elif len(results[0]) == 2 and len(results[1]) == 2:
                x = results[0] + results[1]
                return HandRankings(2, x, [remaining[-1]]) # two pair
        elif len(results) == 3:
            if len(results[0]) == 3 and len(results[1]) == 2 and len(results[2]) == 2:
                x = results[0] + results[1]
                return HandRankings(6, x, []) # full house
            elif len(results[0]) == 2 and len(results[1]) == 2 and len(results[2]) == 2:
                x = results[0] + results[1]
                remaining.extend(results[2])
                remaining = sorted(remaining, key=lambda card: card['value'])
                return HandRankings(1, x, [remaining[-1]]) # two pair
        else:
            return None

    def checkForStraight(self, hand):
        """
        Checks for Straight, 5 cards in consecutive order 
                
        Paramters:
        hand (List of Dicts): 2 hand cards + 5 community cards 
                
        Returns:
        if straight found:
            HandRankings (obj): ranking (0-9), five cards that comprise the best hand, list of kicker cards
        else: 
            None
        """
        prev = hand[0]['value']
        counter = 0
        for i in range (1, len(hand)):
            if hand[i]['value'] == prev + 1:
                counter += 1
            else:
                counter = 0
            prev = hand[i]['value'] 
            if counter == 4:
                return HandRankings(4,hand[i-4:i+1], []) # straight
        return None
    
    def checkForHighCard(self, hand):
        """
        returns the last five cards, cards will be sorted
        """
        return HandRankings(0, [], hand[-5:]) # because it's pre sorted, return the last five cards


        # {done} Royal Flush 9: five cards of the same suit, ranked ace through ten
        # {done} Straight Flush 8 : five cards of the same suit and consecutively ranked
        # {done} Four of a Kind 7: four cards of the same rank
        # {done} Full House 6: three cards of the same rank and two more cards of the same rank
        # {done} Flush 5: any five cards of the same suit
        # {done} Straight 4: any five cards consecutively ranked
        # {done} Three of a Kind 3: three cards of the same rank
        # {done} Two Pair 2: two cards of the same rank and two more cards of the same rank
        # {done} One Pair 1: two cards of the same rank
        # High Card 0: five unmatched cards


    def advance_state(self):
        if self.current_state == GameState.INIT:
            if len(self.players) >= 2:
                self.deal_hands()
                #self.post_blinds()
                self.current_state = GameState.PRE_FLOP
                return("pre-flop")
            else:
                print(len(self.players))
                return("error, not enough players")
        elif self.current_state == GameState.PRE_FLOP:
            self.deal_community(3)
            self.current_state = GameState.FLOP
            return("flop")
        elif self.current_state == GameState.FLOP:
            self.deal_community(1)
            self.current_state = GameState.TURN
            return("turn")
        elif self.current_state == GameState.TURN:
            self.deal_community(1)
            self.current_state = GameState.RIVER
            return("river")
        elif self.current_state == GameState.RIVER:
            self.showdown()
            self.current_state = GameState.SHOWDOWN
            return("showdown")
        elif self.current_state == GameState.SHOWDOWN:
            self.current_state = GameState.END
            return("end")


    # the Blinds
    # Preflop
    # Flop
    # The Turn
    # The River
    # The Showdown

newGame = PokerGame()

Player_1 = Player("James")
Player_2 = Player("Belle")
Player_3 = Player("Xan")
Player_4 = Player("Phoebe")

newGame.addPlayers(Player_1, Player_2, Player_3, Player_4)
newGame.deck.shuffle()

print("\n")
# print(newGame.advance_state())
# print(newGame.advance_state())
# print(newGame.advance_state())
# print(newGame.advance_state())
# print(newGame.advance_state())
# print(newGame.advance_state())
newGame.advance_state()
newGame.advance_state()
newGame.advance_state()
newGame.advance_state()
newGame.advance_state()

print("\n")