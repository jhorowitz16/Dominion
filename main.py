from card import Card
from deck import Deck 
from game import Game

# main.py
# for generic testing 


DEBUG = False 


def turnsUntilEvent():
      num_turns = []
      # find out the average number of turns it takes to get some event
      for i in range(0, 200):
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
                dp('again')
            dp("money distribution: " + str(money_dist))
            dp('done')
            num_turns.append(turn)

      dp(num_turns)
      dp("average: " + str(sum(num_turns)/len(num_turns)))


      # with 2000 trials, to get a hand of 5 golds - it takes 46 turns 
      # 11 turns for first province

# turnsUntilEvent()


def turnsUntilPoints(num_points, switches=(0,100)):
      num_turns = []
      # find out the average number of turns it takes to get some event
      for i in range(0, 150):
            game = Game(switches)
            game.setup()
            vp = 0
            vp_dist = [] # distribution of the victory points- to see the progression as the deck comp improves

            # target amount of VPs here
            while (vp < num_points):
                turn_results = game.takeTurn()
                turn = turn_results['turn'] 
                vp = turn_results['vp'] 
                vp_dist.append(vp)
            dp("victory point distribution: " + str(vp_dist))
            num_turns.append(turn)

      dp(num_turns)
      av_turns = (0.0 + sum(num_turns))/len(num_turns)
      dp("average: " + str(av_turns))
      return av_turns


def findOptimalSwitches():
    opt_e = 0 # early
    opt_l = 0 # late

    best_result = 100
    best_e = -1
    best_l = -1

    for e in range(0, 10):
        print("--------------------")
        for l in range(5, 16):
            result = turnsUntilPoints(27, (e, l)) 
            print(">>> " + str(e) + " " + str(l) + "    " + str(result))
            if best_result > result:
                best_e, best_l = e, l
                best_result = result

    print("best: " + str(best_result) + " with " + str((best_e, best_l)))

def playGame():
      game = Game()
      game.setup()
      game_over = False
      while (not game_over):
            input_string = raw_input("\npress c to continue, q to quit: ")
            
            if input_string[0] == 'q':
                game_over = True # later will implement actual game over conditions - based on piles
                break
            turn_results = game.takeTurn()


# debug print - same as print iff debug is true
def dp(print_str):
    if DEBUG:
        print(print_str)


findOptimalSwitches()
# nurnsUntilPoints(27)
# playGame()
