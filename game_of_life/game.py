from universe import Universe

class Game(object):
    '''our game mechanics, rules, terms and conditions'''
    def __init__(self, sizex, sizey, cells):
        self.u = Universe(sizex, sizey)

        # initial pattern
        self.initialize_with_pattern(cells)

        self.generation = 1

    def initialize_with_pattern(self, cells):
        for cell in cells:
            self.u.give_life(cell[0], cell[1])

    def rule_live_cell_fewer_than_two_live_neighbours_dies(self, x, y):
        '''Rule: Any live cell with fewer than two live neighbours dies, as if caused by under-population.'''
        neighbours = self.u.get_neighbours(x, y)
        alive = self.u.coords[x][y].alive
        # print "neighbours = %s" % neighbours
        # print "alive = %s" % alive
        return alive and neighbours < 2

    def rule_live_cell_two_three_live_neighbours_lives(self, x, y):
        '''Rule: Any live cell with two or three live neighbours lives on to the next generation.'''
        # do nothing
        pass

    def rule_live_cell_more_than_three_neighbours_dies(self, x, y):
        '''Rule: Any live cell with more than three live neighbours dies, as if by overcrowding.'''
        neighbours = self.u.get_neighbours(x, y)
        alive = self.u.coords[x][y].alive
        return alive and neighbours > 3

    def rule_dead_cell_three_live_neighbours_becomes_live(self, x, y):
        '''Rule: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.'''
        neighbours = self.u.get_neighbours(x, y)
        alive = self.u.coords[x][y].alive
        return not alive and neighbours == 3

    def end_of_game(self):
        '''Every game ends at some point, that's a pity'''
        print "Game demonstration ended:\nlife tries to get out of boundaries of the universe and\nwe all know there is absolutely nothing there."
        exit()

    def next_gen(self):
        '''Time machine transfers us to the next generation in just a single tick'''
        # get a copy of our universe to apply rules to - need to apply all the rules at the same time
        future_universe = self.u.copy()

        try:
            for x in xrange(self.u.boundaries["xmin"], self.u.boundaries["xmax"]+1):
                for y in xrange(self.u.boundaries["ymin"], self.u.boundaries["ymax"]+1):
                    # apply rules
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

        # switch to the new universe
        self.u = future_universe.copy()
        self.generation += 1
