import agent

class Grid():
    SPAWN = 1
    SOURCE = 2
    AGENT = 3
    
    def __init__(self, agents):
        #initialize empty board
        self.board = []
        for i in range(0,50):
            self.board.append([0]*50)

        self.agents = agents
        #set spawn and source locations
        self.board[0][0] = Grid.SPAWN
        self.board[30][40] = Grid.SOURCE
        self.source = (30,40)
        self.spawn = (0,0)
        
        #initialize list of tuple-states
        self.states = []
        self.createStates()
        
        self.transitions = {}
        self.actions = ["up", "down", "left", "right"]
        self.transitionMap()

    def get_all_agents(self):
        return self.agents
    
    def do_action(self, agent, action):
        x, y = agent.state
        new_x, new_y =  self.transitions[agent.state][action]
        self.board[x][y] = 0
        self.board[new_x][new_y] = Grid.AGENT

    def generate_reward(self, agent_state, action):
        if self.getNextState(agent_state.coords, action) in list(self.getAdjacent(source)):
            
    
    def get_agent_actions(self, agent):
        return list(self.transitions[agent.state].keys())
        
    def transitionMap(self):
        for state in self.states:
            self.transitions[state] = self.getAdjacent(state)
                
    def getAdjacent(self, coord):
        adj =  {"right": (coord[0]+1, coord[1]), "left": (coord[0]-1, coord[1]), "down": (coord[0], coord[1]+1), "up": (coord[0], coord[1]-1)}
        for k in list(adj.keys() ):
            if (0 > adj[k][0]) or (adj[k][0]>49) or (0>adj[k][1]) or (adj[k][1]>49) or adj[k] in [self.source].extend([agent.state for agent in self.agents]):
                del adj[k]
        return adj
    
    def createStates(self):
        for x in range(50):
            for y in range(50):
                self.states.append((x, y))

    def getNextState(self, state, action):
        return self.transitions[state][action]
    

        
        
