import picture
from tile import Tile

class Gui:
    def __init__(self, grid):
        self.board = grid.board
        self.height = len(grid.board)
        self.width = len(grid.board[0])
        self.pic = picture.Picture((self.width * 80, self.height * 80))
        self.pic.setFillColor((255, 255, 255))
        self.pic.setOutlineColor((0,0,0))

        self.tiles = self.createBoard()
        for y in range(self.height):
            for x in range(self.width):
                self.tiles[x][y] = self.pic.drawRectFill(x * 80, y * 80, 80, 80)
        self.updateBoard(grid)

    def updateBoard(self, grid):
        board = grid.board
        for y in range(self.height):
            for x in range(self.width):
                if board[y][x].tile_type == Tile.EMPTY: # Empty
                    self.tiles[x][y].changeFillColor((255, 255, 255)) # White
                if board[y][x].tile_type == Tile.SPAWN: # Spawn
                    self.tiles[x][y].changeFillColor((0, 0, 255)) # Blue
                if board[y][x].tile_type == Tile.SOURCE: # Source
                    self.tiles[x][y].changeFillColor((255, 255, 0)) # Gold
                if board[y][x].tile_type == Tile.AGENT: # Agent
                    self.tiles[x][y].changeFillColor((0, 255, 0)) # Green
                if board[y][x].tile_type == Tile.OBSTACLE: # Obstacle
                    self.tiles[x][y].changeFillColor((80, 80, 80)) # Grey
                if board[y][x].tile_type == Tile.CARRIER: # carrier
                    self.tiles[x][y].changeFillColor((120, 255, 120)) # Light green
                if board[y][x].tile_type == Tile.GATHERER: # gatherer
                    self.tiles[x][y].changeFillColor((0, 165, 0)) # Dark green
        self.pic.display()

    def createBoard(self):
        A = []
        for i in range(self.width):
            A.append([0] * self.height)
        return A
