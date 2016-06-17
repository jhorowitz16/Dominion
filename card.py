# Card.py

# card class for a dominion card


class Card:

        # Card IDs - one unique id for type of card
        ids = { 'COPPER_ID': 0, 'SILVER_ID' : 1, 'GOLD_ID' : 2,
                'ESTATE_ID' : 3, 'DUCHY_ID' : 4, 'PROVINCE_ID' : 5
        }

	name = ""
	cost = 0
	card_id = 0 # unique id based on the individual card
	type_id = 0 # unique id based on the type of card
	money = 0 # copper 1, silver 2, gold 3 - ... tho market 1, etc.
	vp = 0 # victory points

	worth = 0 # for AI...

	def __init__(self, name="", cost=0, card_id=0, type_id=0):
		self.name = name
		self.cost = cost
		self.card_id = card_id
		self.type_id = type_id

	# actions can do stuff...
	def action():
		# card draw
		# extra buys
		# extra money (included in the money value not this)
		# special stuff like attack cards later...
                pass

	def __repr__(self):
		return self.name + "_" + str(self.card_id)

        def __str__(self):
            return self.name + "_" + str(self.card_id)


