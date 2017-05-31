from cell import Cell
from copy import deepcopy

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
