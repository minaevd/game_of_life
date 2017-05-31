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
