
class Tile:
    EMPTY = 'o'
    SPAWN = 's'
    SOURCE = 'r'
    AGENT = 'a'
    OBSTACLE = 'x'

    def __init__(self, x, y, tile_type):
        self.x = x
        self.y = y
        self.tile_type = tile_type
        self.adjacent = {}
        

    def initAdjacent(self,grid):
        if self.y != 0:
            self.adjacent["north"] = grid.board[self.x][self.y-1]
        if self.y != grid.HEIGHT:
            self.adjacent["south"] = grid.board[self.x][self.y+1]
        if self.x != 0:
            self.adjacent["west"] = grid.board[self.x-1][self.y]
        if self.x != grid.WIDTH:
            self.adjacent["east"] = grid.board[self.x+1][self.y]
    
        
