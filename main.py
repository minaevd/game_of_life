from game_of_life.game import Game
from time import sleep

# import os, subprocess
# def cls():
#     '''trying to clear screen'''
#     os.system('cls' if os.name == 'nt' else 'clear')
#     # subprocess.call("clear")
#     # os.system('clear')
#     # print("\033[2J\033[1;1H")


if __name__ == '__main__':

    cells = [
          (11, 12)
        , (12, 13)
        , (13, 11)
        , (13, 12)
        , (13, 13)
    ]

    # setup the game
    game = Game(25, 25, cells)

    for i in xrange(100):
        # cls()

        # draw a map of the Universe
        print "Generation %s" % game.generation
        game.u.draw()

        # time lapse to the next generation
        game.next_gen()

        # not so fast
        sleep(0.05)
