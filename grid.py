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
        #Given an agent and a selected action, update the agent's state to reflect the change, return the reward
        x, y = agent.state.coords
        new_x, new_y =  self.transitions[agent.state.coords][action]
        reward = self.generate_reward(agent, action)
        agent.state.updateCoords(new_x, new_y)
        self.board[x][y] = 0
        self.board[new_x][new_y] = Grid.AGENT
        return reward

    def generate_reward(self, agent, action):
        #Given agent and action, returns the reward.
        #Default is 0, agent neither picked up or dropped resources
        #Reward is 10 if agent moves to source neighbor and agent.state.is_carrying == False (picks up resource)
        #Reward is 20 if agent moves to spawn neighbor and agent.state.is_carrying == True (drops off resource)
        if self.getNextState(agent.state.coords, action) in list(self.getAdjacent(self.source)):
            if not agent.state.is_carrying:
                agent.state.is_carrying = True
                return 10
            elif self.getNextState(agent.state.coords, action) in list(self.getAdjacent(self.spawn)):
                if agent.state.is_carrying:
                    agent.state.is_carrying = False
                    return 20
            else:
                return 0
                    
    def get_agent_actions(self, agent):
        #Given an agent, returns the list of valid actions given their current state 
        return list(self.transitions[agent.state.coords].keys())
        
    def transitionMap(self):
        for state in self.states:
            self.transitions[state] = self.getAdjacent(state)
                
    def getAdjacent(self, coord):
        #Given an x,y coordinate tuple, returns a dictionary mapping actions to resulting coordinates. Invalid actions are removed from the dictionary
        adj =  {"right": (coord[0]+1, coord[1]), "left": (coord[0]-1, coord[1]), "down": (coord[0], coord[1]+1), "up": (coord[0], coord[1]-1)}
        for k in list(adj.keys() ):
            if (0 > adj[k][0]) or (adj[k][0]>49) or (0>adj[k][1]) or (adj[k][1]>49) or adj[k] in [self.source].extend([agent.state.coords for agent in self.agents]):
                del adj[k]
        return adj
    
    def createStates(self):
        for x in range(50):
            for y in range(50):
                self.states.append((x, y))

    def getNextState(self, state, action):
        return self.transitions[state][action]
    

        
        
