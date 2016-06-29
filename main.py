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
                        turn_results = game.takeTurn()
                        money = turn_results['money'] 
                        turn = turn_results['turn'] 
                        money_dist.append(money)
                        print('again')
                print("money distribution: " + str(money_dist))
                print('done')
                num_turns.append(turn)

        print(num_turns)
        print("average: " + str(sum(num_turns)/len(num_turns)))


        # with 2000 trials, to get a hand of 5 golds - it takes 46 turns 
        # 11 turns for first province

# turnsUntilEvent()



def turnsUntilPoints(num_points):
        num_turns = []
        # find out the average number of turns it takes to get some event
        for i in range(0, 2000):
                game = Game()
                game.setup()
                vp = 0
                vp_dist = [] # distribution of the victory points- to see the progression as the deck comp improves

                # target amount of VPs here
                while (vp < num_points):
                        turn_results = game.takeTurn()
                        turn = turn_results['turn'] 
                        vp = turn_results['vp'] 
                        vp_dist.append(vp)
                        print('again')
                print("victory point distribution: " + str(vp_dist))
                print('done')
                num_turns.append(turn)

        print(num_turns)
        print("average: " + str(sum(num_turns)/len(num_turns)))

# turnsUntilPoints(21)

def playGame():
        game = Game()
        game.setup()
        game_over = False
        while (not game_over):
                input_string = raw_input("press c to continue, q to quit: ")
                print('test')
                
                if input_string[0] == 'q':
                        game_over = True
                turn_results = game.takeTurn()

playGame()
