from card import Card
from deck import Deck

# Simulate an actual game (for a single person)

DEBUG = True 

class Game:

        def __init__(self):
                # initialize the starting deck here instead
                self.deck = Deck()
                self.turn = 0
                self.deck.fullPrint(self.turn)

        # note the constructor already initialized the deck, plus it is already shuffled 
        def setup(self):
                pass
        

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
                print(stats)
                self.moneyBuy(stats['money'], True)
                self.deck.cleanUp()

                return return_info 


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
                        print("i is " + str(i))
                        card = self.deck.hand[i]
                        dp("this card is worth " + str(card.money))
                        if card.name in Deck.action_types:
                                stats['actions'] -= 1
                                # it's an action card
                                card.play(self.deck, stats) 
                        elif card.name in Deck.money_types:
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


# debug print - same as print iff debug is true
def dp(print_str):
        if DEBUG:
                print(print_str)
