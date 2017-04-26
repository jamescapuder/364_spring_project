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
        self.width = len(preBoard[0])
        self.height = len(preBoard)
        self.board = []
        
        for i in range(0, self.height):
            self.board.append([])
            for j in range(0, self.width):
                # Tile's constructor takes in x, y, type
                self.board[i].append(Tile(j, i, preBoard[i][j]))

        print(self.board[1][1].x, self.board[1][1].y)
        self.initTileAdjacent()

    def __str__(self):
        result = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                result += str(self.board[i][j]) + ", "
            result += "\n"
        return result

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
                if y.tile_type == Tile.SOURCE:
                    self.sources.append(Source(y.x, y.y))
                if y.tile_type == Tile.SPAWN:
                    self.spawns.append(Spawn(y.x, y.y))
                if y.tile_type == Tile.AGENT:
                    self.agents.append(Agent(self.environment, State(y.x, y.y)))
                
    def get_tile(self, coord):
        return self.board[coord[1]][coord[0]]
