from random import *
from card import Card

# Deck.py
# deck class for dominion

DEBUG = False 

class Deck:

	deck_id = 0
	player = "player1"
	name = "the deck"
	total_vp = 0
        total_worth = 0
	av_worth = 0
        count = 0

        # represent the cards in a deck as a list of Card objects

        # this is the full deck - two smaller lists representing the discard and the other list

	# cards = []
        pile = [] # this is the "deck" in the traditional sense of the cards yet to play...
        discard = []
        hand = []

	money_types = ['copper', 'silver', 'gold']
	victory_types = ['estate', 'duchy', 'province']
	action_types = ['village', 'smithy']
	all_types = money_types + victory_types + action_types

	def __init__(self, deck_id=0, player="player", name="deck", cards=[]):
		self.deck_id = deck_id 
		self.player = player
		self.name = name
                if cards:
                        self.cards = cards
                else:
                        self.setupDeck() # 7 coppers, 3 estates
		self.total_vp = self.calcTotalVPs()
		self.total_worth = self.calcTotalWorth()
                self.av_worth = self.total_worth / len(self.cards)

        ###### add and remove cards ######

	# two versions of add card - one that takes a type (string) and one that takes an actual card object
	def addCard(self, card):
		if card:
			self.cards += [card]
                        self.discard += [card]
			self.count += 1
			self.av_worth += (self.av_worth*self.count + card.worth) / self.count
			self.total_vp += card.vp
		else:
			return False

	def addCardType(self, type_str):
		if type_str in Deck.all_types:
			# make a card and add it
			new_card = Card(type_str)
			self.addCard(new_card)

		else:
			return False

	# remove a card based on its unique id
	def removeCard(self, id):
                pass


        ###### helper methods for simple calculations ###### 

        # calculate the total 'worth' of the deck based on the initial list of cards passed into the constructor 
        def calcTotalWorth(self):
                total = 0
                for card in self.cards:
                        total += card.worth
                return total

        # count all the victory points in the initial list of cards
        def calcTotalVPs(self):
                total = 0
                for card in self.cards:
                        total += card.worth
                return total
       
        # not sure if this will be useful...
        def calcTotalMoney(self):
                total = 0
                for card in self.cards:
                        total += card.money
                return total
        
        # how much plyaer can buy (include action cards that directly provide money cards)
        # this should be called after all action cards are played - b/c player can gain extra cards
        def calcHandMoney(self):
                total = 0
                print(self.hand)
                for card in self.hand:
                        print(card)
                        print(">>>>" + str(card.money))
                        total += card.money
                return total


        ###### shuffling ######

        # do NOT shuffle the deck - instead shuffle the pile - let the deck be a clean copy of all cards owned

        def reshuffle(self):
                dp("reshuffle")
                if self.discard:
                        dp("actually shuffling")
                        shuffle(self.discard)
                self.cards += self.discard
                self.discard = []



        ###### game actions ######

        # prep the initial deck of 7 coppers and 3 estates
        # shuffle the pile
        def setupDeck(self):
                for i in range(7):
                        copper = Card("copper", 0, i, Card.ids['COPPER_ID'])
                        self.pile.append(copper)
                        self.cards.append(copper)
                for j in range(3):
                        estate = Card("estate", 2, j, Card.ids['ESTATE_ID'])
                        self.pile.append(estate)
                        self.cards.append(estate)
                self.count = 10
                # shuffle(self.pile)

        # discard the hand including played cards
        def cleanUp(self):
                self.discard += self.hand
                self.hand = []


        # draw hand default is 5 cards, without expansions....
        def drawHand(self):
                if not self.pile:
                        # no pile... problem...
                        return
                left_to_deal = 5
                while left_to_deal > 0:
                        dp(self.pile)
                        if len(self.pile) > 0:
                                self.hand.append(self.pile.pop())
                                left_to_deal -= 1 
                        else:
                                # need to reshuffle
                                self.reshuffle()

        # end of turn, discard hand (and all played cards)
        def handToDiscard(self):
                discard += hand
                hand = []



        ###### string related utils ######

        def __repr__(self):
                return self.name + '_' + str(self.deck_id)

        def __str__(self):
                return str(self.cards)

        def fullPrint(self):
                dp("Hand: " + self.hand)
                dp("Discard: " + self.discard)
                dp("All Cards: " + self.cards)
        

# debug print - same as print iff debug is true
def dp(print_str):
        if DEBUG:
                print(print_str)
