
class Tile:
    # Tiles used in our real simulation
    EMPTY = 'o'
    SPAWN = 's'
    SOURCE = 'r'
    AGENT = 'a'
    OBSTACLE = 'x'
    # Test tiles
    GOAL = 'g'
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

    def reset(self):
        self.tile_type = self.init_type
    
        
