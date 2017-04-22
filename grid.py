TEST = False

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
        self.source = (30,40)
        #initialize list of tuple-states
        self.states = []
        self.createStates()
        
        self.transitions = {}
        self.actions = ["up", "down", "left", "right"]
        self.transitionMap()

    def isValidAction(self, state, action):
        in_actions =  action in self.transitions[state].keys()
        if in_actions:
            return self.transitions[state][action] != self.source
        return False

        
    def transitionMap(self):
        for state in self.states:
            self.transitions[state] = self.getAdjacent(state)
                
    def getAdjacent(self, coord):
        adj =  {"right": (coord[0]+1, coord[1]), "left": (coord[0]-1, coord[1]), "down": (coord[0], coord[1]+1), "up": (coord[0], coord[1]-1)}
        for k in list(adj.keys() ):
            if (0 > adj[k][0]) or (adj[k][0]>49) or (0>adj[k][1]) or (adj[k][1]>49):
                del adj[k]
        return adj
    
    def createStates(self):
        for x in range(50):
            for y in range(50):
                self.states.append((x, y))

    def getNextState(self, state, action):
        return self.transitions[state][action]
    

        
        

if __name__=="__main__":
    g = Grid()
    for l in g.board:
        print(*l)
    if TEST:
        with open("estres.txt", "w") as f:
            for k,v in g.transitions.items():
                line = '{}, {}'.format(k, v)
                print(line, file=f)
                f.write("\n")
