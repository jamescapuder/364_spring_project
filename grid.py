from agent import Agent
from tile import Tile
from state import State
from spawn import Spawn
from source import Source

class Grid():

    
    def __init__(self, fpath, environment):
        self.agents = list()
        self.spawns = list()
        self.sources = list()
        self.environment = environment
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

    def initTileAdjacent(self):
        for x in self.board:
            for y in x:
                y.initAdjacent(self)
                if y.tile_type == Tile.SOURCE:
                    self.sources.append(Source(y.x, y.y))
                if y.tile_type == Tile.SPAWN:
                    self.spawns.append(Spawn(y.x, y.y))
                if y.tile_type == Tile.AGENT:
                    self.agents.append(Agent(self.environment, State(y.x, y.y)))
                
    def get_tile(self, x, y):
        return self.board[x][y]
