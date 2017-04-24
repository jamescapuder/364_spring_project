
class Tile:
    EMPTY = 0
    SPAWN = 1 
    SOURCE = 2
    AGENT = 3
    OBSTACLE = 4

    def __init__(self, grid, x, y, tile_type):
        self.x = x
        self.y = y
        self.coords = (x, y)
        self.grid=grid
        self.tile_type = tile_type
        self.adjacent = {}
        self.initAdjacent()

    def initAdjacent(self):
        if self.y != 0:
            self.adjacent["north"] = self.grid[self.x][self.y-1]
        if self.y != self.grid.HEIGHT:
            self.adjacent["south"] = self.grid[self.x][self.y+1]
        if self.x != 0:
            self.adjacent["west"] = self.grid[self.x-1][self.y]
        if self.x != self.grid.WIDTH:
            self.adjacent["east"] = self.grid[self.x+1][self.y]
    
        
