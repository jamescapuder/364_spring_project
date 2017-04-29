import grid
import picture
import time
import copy

class Gui: #Changed to take in grid class
    def __init__(self, grid):
        self.board = grid.board
        self.height = grid.height
        self.width = grid.width
        #self.board = grid  # Remove for testing
        #self.height = len(grid)
        #self.width  = len(grid[0])
        self.pic = picture.Picture((self.width * 50, self.height * 50))
        self.pic.setFillColor((255, 255, 255))
        self.pic.setOutlineColor((0,0,0))

        new = copy.copy(self.board)
        self.states = [new]

        self.tiles = self.createBoard()
        for i in range(self.width):
            for j in range(self.height):
                self.tiles[i][j] = self.pic.drawRectFill(i * 50, j * 50, 50, 50)
        self.newUpdate(grid)


    def newUpdate(self, grid):
        board = grid.board
        #board = grid
        for i in range(self.width):
            for j in range(self.height):
                if board[i][j] == 0:
                    self.tiles[i][j].changeFillColor((255, 255, 255))
                if board[i][j] == 1:
                    self.tiles[i][j].changeFillColor((0, 0, 255))
                if board[i][j] == 2:
                    self.tiles[i][j].changeFillColor((255, 255, 0))
                if board[i][j] == 3:
                    self.tiles[i][j].changeFillColor((255, 0, 0))
        self.pic.display()

    def createBoard(self):
        A = []
        for i in range(self.width):
            A.append([0] * self.height)
        return A

    def step(self, grid): #CHANGE
        new = copy.copy(grid.board)
        #new = copy.copy(grid)
        self.states.append(new)

    # Change how it checks to get it from manager instead of board
    def updateBoard(self, board):
        self.board = board
        for i in range(self.width):
            for j in range(self.height):
                if board[i][j] == 0:
                    self.tiles[i][j].changeFillColor((255,255,255))
                if board[i][j] == 1:
                    self.tiles[i][j].changeFillColor((0,0,255))
                if board[i][j] == 2:
                    self.tiles[i][j].changeFillColor((255,255,0))
                if board[i][j] == 3:
                    self.tiles[i][j].changeFillColor((255,0,0))

    def displayEpisode(self):
        for state in self.states:
             self.updateBoard(state)
             self.pic.display()
             time.sleep(1)
        input()

#0 empty
#1 spawn
#2 resource
#3 agent
def main(): # for testing
    g = []
    for i in range(10):
        g.append([0]*10)

    g[0][0] = 1
    g[1][0] = 2

    gui = Gui(g)

    f = []
    for i in range(10):
        f.append([0] * 10)
    f[0][0] = 1
    f[1][0] = 2
    f[0][1] = 3

    #gui.step(f)
    #print(gui.states)
    # g[0][2] = 3
    # gui.step(g)
    # g[0][3] = 3
    # gui.step(g)
    # g[0][4] = 3
    # gui.step(g)
    time.sleep(1)
    gui.newUpdate(f)
#main()
