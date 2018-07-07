from card import Card
from deck import Deck
from store import Store

# Simulate an actual game (for a single person)

DEBUG = True
ASSERTS = False

class Game:

    # default switches is only mid game
    def __init__(self, switches=(0, 100)):
        # initialize the starting deck here instead
        self.deck = Deck()
        self.turn = 0
        self.deck.fullPrint(self.turn)


        self.earlyBuy = priorityBuy(Card.money_types + ['LABORATORY'])
        self.midBuy = priorityBuy(Card.money_types + ['LABORATORY'] + ['PROVINCE'])
        self.lateBuy = priorityBuy(Card.victory_types)

        self.switches = switches

        self.store = Store()

        # self.earlyBuy = priorityBuy(Card.money_types)
        # self.midBuy = priorityBuy(Card.money_types + ['PROVINCE'])
        # self.lateBuy = self.midBuy


        if ASSERTS:
            assert self.midBuy(1) == ''
            assert self.earlyBuy(3) == 'SILVER'
            assert self.earlyBuy(5) == 'LABORATORY'
            assert self.earlyBuy(6) == 'GOLD'
            assert self.earlyBuy(8) == 'GOLD'

            assert self.midBuy(1) == ''
            assert self.midBuy(3) == 'SILVER'
            assert self.midBuy(5) == 'LABORATORY'
            assert self.midBuy(6) == 'GOLD'
            assert self.midBuy(8) == 'PROVINCE'

            assert self.lateBuy(1) == ''
            assert self.lateBuy(3) == 'ESTATE'
            # assert self.lateBuy(5) == 'DUCHYzz' # test to fail
            assert self.lateBuy(6) == 'DUCHY'
            assert self.lateBuy(8) == 'PROVINCE'

    def buyCardType(self, newCard):
        """
        same as the old self.deck.addCardType(newCard)
        but ... also remove the corresponding card from the Store

        if the store buy fails,
            then will return None, otherwise the card
        """

        if not self.store.buy(newCard):
            return None
        return self.deck.addCardType(newCard)



    # ABC
    # Action
    # Buy
    # Collect
    def takeTurn(self):
        return_info = {} # for playing around with events - to get feedback in main

        self.turn += 1
        self.deck.drawHand()
        self.deck.fullPrint(self.turn) # hand right after drawing it
        return_info['money'] = self.deck.calcHandMoney()
        return_info['turn'] = self.turn
        return_info['vp'] = self.deck.total_vp

        stats = self.simpleCalcPlay()
        dp(stats)
        # self.moneyBuy(stats['money'], True)
        self.phaseBuys(stats['money']) # before turn 8, early game, before turn 10, mid game
        self.deck.cleanUp()

        return return_info


    # smart buy - switches is a tuple signaling when to switch strategies
    # ex - (5, 10) - before turn 5 early game, before turn 10 mid game, then late game (all VPs)
    # goal - find the optimal constants
    def phaseBuys(self, money):
        # init idea
        # early game - no vps no matter what
        # mid game - best buy, including provinces
        # late game - all points

        if self.turn < self.switches[0]:
            dp("early")
            newCard = self.earlyBuy(money)
        elif self.turn < self.switches[1]:
            dp("mid")
            newCard = self.midBuy(money)
        else:
            dp("late")
            newCard = self.lateBuy(money)
        dp("New Card: " + newCard) # *** multiple buys later
        self.buyCardType(newCard)




    # choose what to buy...
    # if provinces is set to true, buy provinces in addition to silvers and golds
    def moneyBuy(self, money, provinces=False):
        # money = self.deck.calcHandMoney()
        dp("money: " + str(money))
        if money >= 8 and provinces:
            dp("province")
            self.deck.addCardType('PROVINCE')
        elif money < 3:
            dp("no money, no buy")
        elif money < 6:
            dp("silver")
            self.deck.addCardType('SILVER')
        else:
            dp("gold")
            self.deck.addCardType('GOLD')


    # Calculate and play the entire hand
    # the simple playing code - play everything possible - random order
    # *** tbd strat - take into account: being able to play everything, more valuable actions (expensive first?)
    # use a dictionary to keep track of everything for all cards (not just actions)
    def simpleCalcPlay(self):
        # start with one action and one buy and no money
        stats = {'actions': 1, 'buys': 1, 'money': 0, 'vp': 0}
        i = 0
        while (i < len(self.deck.hand) and (stats['actions'] > 0)):
            # print("i is " + str(i))
            card = self.deck.hand[i]
            # dp("this card is worth " + str(card.money))
            if card.name in Card.action_types:
                stats['actions'] -= 1
                # it's an action card
                stats = card.play(self.deck, stats)
            elif card.name in Card.money_types:
                stats['money'] += card.money
            else:
                stats['vp'] += card.vp
            i += 1
                # add a play action for each card later -
                # *** - dictionary maps card names to the methods themselves...
        return stats


    # play takes a strategy function for how to play action cards (basically everything other than the buying
    def play(self, strat):
        pass

    # buy does the buying, also taking a strategy function for the best card(s) to buy
    def buy(self, strat, *args):
        strat(args)

#####################################################################################################
#####################################################################################################

# priority buy is a helper for buying
# returns a function that takes a deck and a money value
# adds a card to the deck based on the money
# priority buy itself takes a list of cards available and sorts them by price and priority
# ties broken by "priority" attribute
def priorityBuy(available):

    dp("priorityBuy")

    # 2d matrix - list of lists
    options = []
    # costs are 0 to 8 inclusive - coppers to provinces
    dp(available)
    for _ in range(0, 9):
        options.append([])
    for card_name in available:
        options[Card.costs[card_name]].append(card_name)
    dp(options)
    def selectBuy(money):
        i = money
        if i > 8:
            i = 8 # this works as long as there is one buy
        name = '' # name of the returned card
        while i > 0:
            if options[i]:
                return options[i][0] # this could be random later
            else:
                i -= 1
        # name will be null if there's nothing worth buying
        return name

    return selectBuy


# debug print - same as print iff debug is true
def dp(print_str):
    if DEBUG:
        print(print_str)
