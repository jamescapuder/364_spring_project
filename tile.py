
class Tile:
    # Tiles used in our real simulation
    EMPTY = 'o'
    SPAWN = 's'
    SOURCE = 'r'
    AGENT = 'a'
    OBSTACLE = 'x'
    GATHERER = 'g'
    CARRIER = 'c'
    THIEF = 't'
    # Test tiles
    GOAL = 'd'
    PENALTY = 'p'

    def __init__(self, x, y, tile_type):
        self.x = x
        self.y = y
        self.coords = (x, y)
        self.init_type = tile_type
        self.tile_type = tile_type
        self.adjacent = {}

    def __str__(self):
        return str(self.tile_type)

    def initAdjacent(self,grid):
        if self.y != 0:
            self.adjacent["north"] = grid.board[self.y-1][self.x]
        if self.y != grid.height - 1:
            self.adjacent["south"] = grid.board[self.y+1][self.x]
        if self.x != 0:
            self.adjacent["west"] = grid.board[self.y][self.x-1]
        if self.x != grid.width - 1:
            self.adjacent["east"] = grid.board[self.y][self.x+1]

    def num_adjacent_agents(self):
        return len([x for x in self.adjacent.values() if x.tile_type=='a'])

    def adjacent_agents(self):
        return [x for x in self.adjacent.values() if (x.tile_type=='g' or x.tile_type=='c')]

    def reset(self):
        self.tile_type = self.init_type
    
        
