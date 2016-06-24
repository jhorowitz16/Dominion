# Card.py

# card class for a dominion card


class Card:

        # Card IDs - one unique id for type of card
        ids = { 'COPPER_ID': 0, 'SILVER_ID' : 1, 'GOLD_ID' : 2,
                'ESTATE_ID' : 3, 'DUCHY_ID' : 4, 'PROVINCE_ID' : 5,
                'BLANK' : -1
        }

	name = ""
	cost = 0
	card_id = 0 # unique id based on the individual card
	type_id = 0 # unique id based on the type of card
	money = 0 # copper 1, silver 2, gold 3 - ... tho market 1, etc.
	vp = 0 # victory points

	worth = 0 # for AI...

        # the default card is a blank card (card_id -1 b/c not in a deck and type_id -1 b/c not a real card)
	def __init__(self, name="", cost=0, card_id=-1, type_id=-1):
		self.name = name
		self.cost = cost
		self.card_id = card_id
		self.type_id = type_id
                self.money = self.cardToMoney()
                self.worth = self.cardToWorth()

	# actions can do stuff...
	def action():
		# card draw
		# extra buys
		# extra money (included in the money value not this)
		# special stuff like attack cards later...
                pass

        # for now, everything has no money value other than the coins, which are one under their value
        def cardToMoney(self):
                if self.type_id < 3:
                        # < 3 is a money card...
                        return self.type_id + 1
                else:
                        return 0

        # for now the worth of a card is its money value
        def cardToWorth(self):
                return self.cardToMoney()

	def __repr__(self):
		return self.name + "_" + str(self.card_id)

        def __str__(self):
            return self.name + "_" + str(self.card_id)


