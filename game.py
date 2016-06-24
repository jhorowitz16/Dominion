from card import Card
from deck import Deck

# Simulate an actual game (for a single person)

DEBUG = True 

class Game:

        turn = 0

        def __init__(self):
                # initialize the starting deck here instead
                self.deck = Deck()

        # note the constructor already initialized the deck, plus it is already shuffled 
        def setup(self):
                pass
        # ABC
        # Action
        # Buy
        # Collect
        def takeTurn(self):
                self.turn += 1
                dp("===================\nturn #" + str(self.turn))
                self.deck.drawHand()
                dp("hand: " + str(self.deck.hand))
                dp("pile: " + str(self.deck.pile))
                self.moneyBuy() 
                self.deck.cleanUp()


        # choose what to buy...
        # for now, return a card object (or a string if not buying anything)
        def moneyBuy(self):
                money = self.deck.calcHandMoney()
                dp("money: " + str(money))
                if money < 3:
                        return
                elif money < 6:
                        dp("silver")
                        self.deck.addCardType('silver')
                else:
                        dp("gold")
                        self.deck.addCardType('gold')

# debug print - same as print iff debug is true
def dp(print_str):
        if DEBUG:
                print(print_str)
