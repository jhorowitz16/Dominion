# Card.py

# card class for a dominion card


class Card:

        # Card IDs - one unique id for type of card
        ids = { 'COPPER': 0, 'SILVER' : 1, 'GOLD' : 2,
                'ESTATE' : 3, 'DUCHY' : 4, 'PROVINCE' : 5,
                'BLANK' : -1
        }

        # card costs all in a dictionary
        costs = { 'COPPER': 0, 'SILVER' : 3, 'GOLD' : 6,
                'ESTATE' : 2, 'DUCHY' : 5, 'PROVINCE' : 8,
                'BLANK' : -1
        }
        
        # the unique IDs are based on when they were added to the deck

        # the default card is a blank card (card_id -1 b/c not in a deck and type_id -1 b/c not a real card)
	def __init__(self, name="", card_id=-1):
		self.name = name
		self.cost = self.cardToCost() 
		self.card_id = card_id # unique id based on the individual card
		self.type_id = Card.ids[name] # unique id based on the type of card
                self.money = self.cardToMoney() # copper 1, silver 2, gold 3 - ... tho market 1, etc.
                self.worth = self.cardToWorth() # for AI...
                self.vp = self.cardToVP() # end game scoring

	# actions can do stuff...
	def action():
		# card draw
		# extra buys
		# extra money (included in the money value not this)
		# special stuff like attack cards later...
                pass

        # for now, everything has no money value other than the coins, which are one under their value
        def cardToMoney(self):
                if self.type_id == Card.ids['COPPER']:
                        return 1
                elif self.type_id == Card.ids['SILVER']:
                        return 2 
                elif self.type_id == Card.ids['GOLD']:
                        return 3 
                else: 
                        return 0 

        # for now the worth of a card is its money value
        def cardToWorth(self):
                return self.cardToMoney()

        # for now the worth of a card is only worth points if estate, duchy, or province 
        def cardToVP(self):
                if self.type_id == Card.ids['ESTATE']:
                        return 1
                elif self.type_id == Card.ids['DUCHY']:
                        return 3 
                elif self.type_id == Card.ids['PROVINCE']:
                        return 6 
                else: 
                        return 0 

        # move to a database or something ... at some point
        def cardToCost(self):
                return Card.costs[self.name] 


        ##### action card methods here #####

        # draw 2 cards, gain 1 action
        def laboratory(deck):
                deck.drawCards(2) 
                # *** also gain an action... but deal with actions later... *** 




	def __repr__(self):
                return str(self)

        # assuming 2 digits as never going to get more than 99 cards...
        # append a 0 to the front of single digit IDs
        def __str__(self):
            if self.card_id > -1 and self.card_id < 10:
                return self.name + "_0" + str(self.card_id)
            return self.name + "_" + str(self.card_id)

