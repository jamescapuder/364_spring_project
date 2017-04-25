from agent import Agent
from tile import Tile
from state import State
from spawn import Spawn
from source import Source

class Grid():

    
    def __init__(self, fpath):
        self.agents = list()
        self.spawns = list()
        self.sources = list()
        
        # TODO: read board from file
        preBoard = [list(l)[:-1] for l in open(fpath, 'r')]
        self.WIDTH = len(preBoard[0])-1
        self.HEIGHT = len(preBoard)-1
        self.board = []
        
        for x in range(0, self.WIDTH+1):
            self.board.append( [])
            for y in range(0,self.HEIGHT+1):
                self.board[x].append( Tile(y, x, preBoard[y][x]) )
        
        self.initTileAdjacent()

    def reset(self):
        self.reset_all(self.agents)
        self.reset_all(self.spawns)
        self.reset_all(self.sources)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].reset()

    def reset_all(self, components):
        for c in components:
            c.reset()

    def initTileAdjacent(self):
        for x in self.board:
            for y in x:
                y.initAdjacent(self)
                
    def get_tile(self, x, y):
        return self.board[x][y]
