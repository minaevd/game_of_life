from copy import deepcopy
from time import sleep

# import os, subprocess

def cls():
    '''trying to clear screen'''
    # os.system('cls' if os.name == 'nt' else 'clear')
    # subprocess.call("clear")
    # os.system('clear')
    print("\033[2J\033[1;1H")

class Universe(object):
    def __init__(self, sizex, sizey):
        # set Universe size (we know it's limited even though it's growing at the speed of light)
        self.sizex = sizex
        self.sizey = sizey

        self.coords = []

        # life doesn't appear in the middle of nowhere, so let's not try to check it there
        self.boundaries = {
            "xmin": sizex/2,
            "ymin": sizey/2,
            "xmax": sizex/2,
            "ymax": sizey/2
        }

        # initialize universe with dead cells
        for x in xrange(self.sizex):
            self.coords.append([])
            for y in xrange(self.sizey):
                self.coords[x].append(Cell(x,y,False))

    def draw(self):
        '''draw a map of our Universe'''
        print '+',
        for x in xrange(1,len(self.coords)+1):
            print (x) % 10,
        print '+'
        for x in xrange(len(self.coords)):
            print (x+1) % 10,
            for y in xrange(len(self.coords[x])):
                cell = self.coords[x][y]
                print cell.get_symbol(),
            print '|'
        print '+',
        for x in xrange(1,len(self.coords)+1):
            print '-',
        print '+'

    def get_neighbours(self, xctr, yctr):
        '''count live neighbours for a given cell'''
        alive = 0
        for x in xrange(xctr-1, xctr+2):
            for y in xrange(yctr-1, yctr+2):
                if x == xctr and y == yctr:
                    continue
                cell = self.coords[x][y]
                if cell.alive:
                    alive += 1
        return alive

    def give_life(self, x, y):
        '''give life to a new microorganism'''
        self.coords[x][y].be_born()
        self.update_boundaries(x, y)

    def take_life(self, x, y):
        '''take life away: that is unfortunate but life is life'''
        self.coords[x][y].die()
        self.update_boundaries(x, y)

    def update_boundaries(self, x, y):
        '''update boundaries where our life exists'''
        if x <= self.boundaries["xmin"]:
            self.boundaries["xmin"] = max(0, x-1)
        if x >= self.boundaries["xmax"]:
            self.boundaries["xmax"] = min(self.sizex, x+1)
        if y <= self.boundaries["ymin"]:
            self.boundaries["ymin"] = max(0, y-1)
        if y >= self.boundaries["ymax"]:
            self.boundaries["ymax"] = min(self.sizey, y+1)

    def copy(self):
        '''copy the universe'''
        return deepcopy(self)


class Cell(object):
    '''our only microorganism'''
    def __init__(self, x, y, alive=True):
        # set location
        self.x = x
        self.y = y
        # is it alive
        self.alive = alive
        # how would we like to show alive cell on our map
        self.symbol = '@'

    def die(self):
        self.alive = False

    def be_born(self):
        self.alive = True

    def get_symbol(self):
        if self.alive:
            return '@'
        else:
            return '.'

class Game(object):
    def __init__(self, sizex, sizey):
        self.u = Universe(sizex, sizey)

        # initial pattern
        self.u.give_life(11, 12)
        self.u.give_life(12, 13)
        self.u.give_life(13, 11)
        self.u.give_life(13, 12)
        self.u.give_life(13, 13)
        self.generation = 1

        # draw initial field
        print "Initial state"
        self.u.draw()


    def rule_live_cell_fewer_than_two_live_neighbours_dies(self, x, y):
        neighbours = self.u.get_neighbours(x, y)
        alive = self.u.coords[x][y].alive
        # print "neighbours = %s" % neighbours
        # print "alive = %s" % alive
        return alive and neighbours < 2

    def rule_live_cell_two_three_live_neighbours_lives(self, x, y):
        # do nothing
        pass

    def rule_live_cell_more_than_three_neighbours_dies(self, x, y):
        neighbours = self.u.get_neighbours(x, y)
        alive = self.u.coords[x][y].alive
        return alive and neighbours > 3

    def rule_dead_cell_three_live_neighbours_becomes_live(self, x, y):
        neighbours = self.u.get_neighbours(x, y)
        alive = self.u.coords[x][y].alive
        return not alive and neighbours == 3

    def end_of_game(self):
        print "Game demonstration ended:\nlife tries to get out of boundaries of the universe and\nwe all know there is absolutely nothing there."
        exit()

    def next_gen(self):
        future_universe = self.u.copy()

        try:
            for x in xrange(self.u.boundaries["xmin"], self.u.boundaries["xmax"]+1):
                for y in xrange(self.u.boundaries["ymin"], self.u.boundaries["ymax"]+1):
                    if self.rule_live_cell_fewer_than_two_live_neighbours_dies(x,y):
                        # print "(%s, %s) dies" % (x,y)
                        future_universe.take_life(x, y)
                    if self.rule_live_cell_two_three_live_neighbours_lives(x,y):
                        pass
                    if self.rule_live_cell_more_than_three_neighbours_dies(x,y):
                        future_universe.take_life(x, y)
                    if self.rule_dead_cell_three_live_neighbours_becomes_live(x,y):
                        future_universe.give_life(x, y)

        except IndexError:
            self.end_of_game()

        self.u = future_universe.copy()
        print "Generation %s" % self.generation
        self.u.draw()
        self.generation += 1

if __name__ == '__main__':

    game = Game(25, 25)

    for i in xrange(100):
        cls()
        game.next_gen()
        sleep(0.1)
