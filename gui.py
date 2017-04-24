import grid
import picture
import time
import copy

class Gui: #Changed to take in grid class
    def __init__(self, grid):
        self.board = grid.board
        self.finished = False
        self.height = len(self.board)
        self.width = len(self.board[0])
        self.pic = picture.Picture((self.width * 10, self.height * 10))
        self.pic.setFillColor((255, 255, 255))
        self.pic.setOutlineColor((0,0,0))

        new = copy.copy(self.board)
        self.states = [new]

        self.tiles = self.createBoard()
        for i in range(self.width):
            for j in range(self.height):
                self.tiles[i][j] = self.pic.drawRectFill(i * 10, j * 10, 10, 10)

    def createBoard(self):
        A = []
        for i in range(self.width):
            A.append([0] * self.height)
        return A

    def step(self, grid):
        new = copy.copy(grid.board)
        self.states.append(new)

    # Change how it checks to get it from manager instead of board
    def updateBoard(self, board):
        #self.board = board
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
    print(gui.states)

    f = []
    for i in range(10):
        f.append([0] * 10)
    f[0][0] = 1
    f[1][0] = 2
    f[0][1] = 3

    gui.step(f)
    print(gui.states)
    # g[0][2] = 3
    # gui.step(g)
    # g[0][3] = 3
    # gui.step(g)
    # g[0][4] = 3
    # gui.step(g)

    gui.displayEpisode()
#main()
