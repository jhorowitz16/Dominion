

# Simulate an actual game (for a single person)

class Game:
        
        deck = None 
        turn = 0

        def __init__(self, deck):
                self.deck = deck


        def setup(self):
                # put the starting setup here ... AND ADD EVERYONE TO PILE

        # ABC
        # Action
        # Buy
        # Collect
        def takeTurn(self):
                self.turn += 1
                print("turn " + str(self.turn))
                self.deck.drawHand()
                print(this.deck)

