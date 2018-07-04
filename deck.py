from random import *
from card import Card

# Deck.py
# deck class for dominion

# DEBUG = False
DEBUG = True

class Deck:

    # represent the cards in a deck as a list of Card objects
    # there is no full deck object - all cards are saved in pile, discard or hand
    # cards = []
    # pile is the "deck" in the traditional sense of the cards yet to play...


    def __init__(self, deck_id=0, player="player", name="deck"):
        dp("INIT")
        self.deck_id = deck_id
        self.player = player
        self.name = name

        self.hand = []
        self.discard = []
        self.pile = []
        dp("USING SETUP DECK")
        self.setupDeck() # 7 coppers, 3 estates

        self.total_vp = self.calcTotalVPs()
        self.total_worth = self.calcTotalWorth()
        self.av_worth = self.total_worth / len(self.pile)
        self.count = 0

      ###### add and remove cards ######

    # two versions of add card - one that takes a type (string) and one that takes an actual card object
    def addCard(self, card):
        if card:
            self.discard += [card]
            self.count += 1
            self.av_worth += (self.av_worth*self.count + card.worth) / self.count
            self.total_vp += card.vp
        else:
            dp("card not found")
            return False

    def addCardType(self, type_str):
        if type_str in Card.all_types:
            # make a card and add it
            new_card = Card(type_str, self.count)
            self.addCard(new_card)
        else:
            dp("card type not found")
            return False

    # remove a card based on its unique id
    def removeCard(self, id):
            pass


    ###### helper methods for simple calculations ######

    # calculate the total 'worth' of the deck based on the initial list of cards passed into the constructor
    def calcTotalWorth(self):
        total = 0
        for card in self.pile:
            total += card.worth
        return total

    # count all the victory points in the initial list of cards
    def calcTotalVPs(self):
        total = 0
        everything = self.pile + self.discard + self.hand
        for card in everything:
            total += card.worth

        return total

    # not sure if this will be useful...
    def calcTotalMoney(self):
        total = 0
        for card in self.pile:
            total += card.money
        return total

    # how much plyaer can buy (include action cards that directly provide money cards)
    # this should be called after all action cards are played - b/c player can gain extra cards
    def calcHandMoney(self):
        total = 0
        for card in self.hand:
            total += card.money
        return total


    ###### shuffling ######

    # actually shuffle the pile... no more deck
    def reshuffle(self):
        dp("reshuffle")
        if len(self.discard) > 1:
            dp("actually shuffling")
            shuffle(self.discard)
        self.pile += self.discard
        self.discard = []



    ###### game actions ######

    # prep the initial deck of 7 coppers and 3 estates
    # shuffle the pile
    def setupDeck(self):
        for i in range(7):
            copper = Card("COPPER", i)
            self.pile.append(copper)
        for j in range(7, 10):
            estate = Card("ESTATE", j)
            self.pile.append(estate)
        self.count = 10
        shuffle(self.pile)

    # discard the hand including played cards
    def cleanUp(self):
        self.discard += self.hand
        self.hand = []


    # draw an integer number of cards (5 for hand)
    # give number of cards as a parameter
    def drawCards(self, numCards):
        if not self.pile:
            # no pile... problem... need to shuffle
            self.reshuffle()
        left_to_deal = numCards
        while left_to_deal > 0:
            dp(self.pile)
            if len(self.pile) > 0:
                  self.hand.append(self.pile.pop())
                  left_to_deal -= 1
            else:
                  # need to reshuffle
                  self.reshuffle()

    # draw hand default is 5 cards, without expansions....
    def drawHand(self):
        self.drawCards(5)

    # end of turn, discard hand (and all played cards)
    def handToDiscard(self):
        discard += hand
        hand = []



    ###### string related utils ######

    def __repr__(self):
        return self.name + '_' + str(self.deck_id)

    def __str__(self):
        return str(self.pile)

    def fullPrint(self, turn=-1):
        if turn > -1:
            dp("\n\n=================== turn " + str(turn) + " ====================")
        else:
            dp("\n\n===============================================")
        dp("Hand: " + str(self.hand))
        dp("Pile: " + str(self.pile))
        dp("Discard: " + str(self.discard))

# debug print - same as print iff debug is true
def dp(print_str):
      if DEBUG:
            print(print_str)
