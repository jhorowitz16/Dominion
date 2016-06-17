from card import Card
from deck import Deck 

# main.py
# for generic testing 

def card_tests():
        temp_hand_list = []
        for i in range(7):
                copper = Card("copper", 0, i, Card.ids['COPPER_ID'])
                temp_hand_list.append(copper)
        for j in range(3):
                estate = Card("estate", 2, j, Card.ids['ESTATE_ID'])
                temp_hand_list.append(estate)
        # print(temp_hand_list)


        # ... now add them to a deck...
        my_deck = Deck(0, "player1", "my_deck", temp_hand_list)
        print(my_deck)
        
        my_deck.shuffleDeck()
        print(my_deck)

card_tests()