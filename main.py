from card import Card
from deck import Deck 
from game import Game

# main.py
# for generic testing 





def turnsUntilEvent():
        num_turns = []
        # find out the average number of turns it takes to get some event
        for i in range(0, 2000):
                game = Game()
                game.setup()
                money = 0
                money_dist = [] # distribution of the money - to see the progression as the deck comp improves

                # target amount of money here
                while (money < 8):
                        money = game.takeTurn()['money'] 
                        turn = game.takeTurn()['turn'] 
                        money_dist.append(money)
                        print('again')
                print("money distribution: " + str(money_dist))
                print('done')
                num_turns.append(turn)

        print(num_turns)
        print("average: " + str(sum(num_turns)/len(num_turns)))


        # with 2000 trials, to get a hand of 5 golds - it takes 46 turns 
        # 11 turns for first province

turnsUntilEvent()
