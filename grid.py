

class Grid():
    SPAWN = 1
    SOURCE = 2
    AGENT = 3
    
    def __init__(self):
        #initialize empty board
        self.board = []
        for i in range(0,50):
            self.board.append([0]*50)

        #set spawn and source locations
        self.board[0][0] = Grid.SPAWN
        self.board[30][40] = Grid.SOURCE

        #initialize list of tuple-states
        self.states = []
        self.createStates()

        self.transitions = {}
        self.actions = ["up", "down", "left", "right"]
        self.transitionMap()

    def isValidAction(self, state, action):
        return self.transitions[state][action] not in [Grid.SOURCE, Grid.AGENT]


    def transitionMap(self):
        for state in self.states:
            self.transitions[state] = self.getAdjacent(state)
            
    
    def getAdjacent(self, coord):
        return {"right": (coord[0]+1, coord[1]), "left": (coord[0]-1, coord[1]), "down": (coord[0], coord[1]+1), "up": (coord[0], coord[1]-1)}
        
    def createStates(self):
        for x in range(0,50):
            for y in range(0,50):
                self.states.append((x, y))
        #self.states.append(Grid.ABSORBING_STATE)

    
        
        
        

if __name__=="__main__":
    g = Grid()
    for l in g.board:
        print(*l)
    print(g.transitions)
