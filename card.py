# Card.py
# card class for a dominion card


class Card:

    # moved from deck

    money_types = ['COPPER', 'SILVER', 'GOLD']
    victory_types = ['ESTATE', 'DUCHY', 'PROVINCE']
    action_types = ['VILLAGE', 'SMITHY', 'LABORATORY']
    all_types = money_types + victory_types + action_types



    # Card IDs - one unique id for type of card
    ids = { 'COPPER': 0, 'SILVER' : 1, 'GOLD' : 2,
    'ESTATE' : 3, 'DUCHY' : 4, 'PROVINCE' : 5,
    'BLANK' : -1,
    'LABORATORY': 6 
    }
    # card costs all in a dictionary
    costs = { 'COPPER': 0, 'SILVER' : 3, 'GOLD' : 6,
    'ESTATE' : 2, 'DUCHY' : 5, 'PROVINCE' : 8,
    'BLANK' : -1,
    'LABORATORY': 5
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
        # print("I am worth : " + str(self.money))


    # actions can do stuff...
    def action():
        # card draw
        # extra buys
        # extra money (included in the money value not this)
        # special stuff like attack cards later...
        pass

    # for now, everything has no money value other than the coins, which are one under their value
    def cardToMoney(self):
        # print(str(self.name) + " is a " + str(self.type_id) + " rather than " + str(Card.ids['COPPER']))
        if self.type_id == Card.ids['COPPER']:
            # print("card to money")
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
    # Note: every action card must take and return an "effects" dictionary
    # effects dictionary has actions and buys (for now)


    # generic play - all cards must have a play - just many of them do nothing
    # everything called through here
    def play(self, deck, stats):
        if self.name not in Card.action_types: # double check
            return stats
        playMethod = getattr(self, self.name.lower())
        return playMethod(deck, stats)



    # draw 2 cards, gain 1 action
    def laboratory(self, deck, stats):
        deck.drawCards(2) 
        stats['actions'] += 1 # gain an action
        return stats 





    def __repr__(self):
        return str(self)

    # assuming 2 digits as never going to get more than 99 cards...
    # append a 0 to the front of single digit IDs
    def __str__(self):
        if self.card_id > -1 and self.card_id < 10:
            return self.name + "_0" + str(self.card_id)
        return self.name + "_" + str(self.card_id)

