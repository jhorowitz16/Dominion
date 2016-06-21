

# Simulate an actual game (for a single person)

DEBUG = True 

class Game:

        deck = None 
        turn = 0

        def __init__(self, deck):
                self.deck = deck


        def setup(self):
                # put the starting setup here ... AND ADD EVERYONE TO PILE
                pass
                for card in deck:
                        self.deck.pile += card

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
                money = self.deck.calcHandMoney()
                dp("money: " + str(money))
                
                self.deck.cleanUp()


# debug print - same as print iff debug is true
def dp(print_str):
        if DEBUG:
                print(print_str)
