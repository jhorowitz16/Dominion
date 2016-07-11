from card import Card
from deck import Deck 
from game import Game

# main.py
# for generic testing 


DEBUG = False 


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
      for i in range(0, 2000):
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
      av_turns = sum(num_turns)/len(num_turns)
      dp("average: " + str(av_turns))
      return av_turns


def findOptimalSwitches():
    opt_e = 0 # early
    opt_l = 0 # late
    for opt_e in range(1, 10):
        print("--------------------")
        for opt_l in range(5, 15):
            result = turnsUntilPoints(27, (opt_e, opt_l)) 
            print(">>> " + str(opt_e) + " " + str(opt_l) + "    " + str(result))


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
