import picture

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
                if board[y][x].tile_type == 'o': # Empty
                    self.tiles[x][y].changeFillColor((255, 255, 255))
                if board[y][x].tile_type == 's': # Spawn
                    self.tiles[x][y].changeFillColor((0, 0, 255))
                if board[y][x].tile_type == 'r': # Source
                    self.tiles[x][y].changeFillColor((255, 255, 0))
                if board[y][x].tile_type == "a": # Agent
                    self.tiles[x][y].changeFillColor((255, 0, 0))
                if board[y][x].tile_type == "x": # Obstacle
                    self.tiles[x][y].changeFillColor((0, 255, 0))
        self.pic.display()

    def createBoard(self):
        A = []
        for i in range(self.width):
            A.append([0] * self.height)
        return A
