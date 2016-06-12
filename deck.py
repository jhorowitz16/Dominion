# Deck.py

# deck class for dominion


class Deck

	count = 0
	player = null
	name = "the deck"
	total_vp = 0
	av_worth = 0

        # represent the cards in a deck as a list of Card objects

        # this is the full deck - two smaller lists representing the discard and the other list

	cards = []


	money_types = ['copper', 'silver', 'gold']
	victory_types = ['estate', 'duchy', 'province']
	action_types = ['village', 'smithy']
	all_types = money_types + victory_types + action_types

	def __init__(self, count=0, player="player", name="deck", total_vp=0, av_worth=0, cards=[]):
		self.count = count
		self.player = player
		self.name = name
		self.total_vp = total_vp
		self.av_worth = av_worth


	# two versions of add card - one that takes a type (string) and one that takes an actual card object
	def addCard(self, card):
		if card:
			cards += card
			count += 1
			av_worth += (av_worth*count + card.worth) / count
			total_vp += card.vp
		else:
			return false

	def addCardType(self, type_str):
		if type_str in all_types:
			# make a card and add it
			new_card = Card(type_str)
			addCard(self, new_card)

		else:
			return false

	# remove a card based on its unique id
	def removeCard(self, id):
		self.cards.
