import agent

class Grid():
    SPAWN = 1
    SOURCE = 2
    AGENT = 3

    WIDTH = 5
    HEIGHT = 5

    def __init__(self, agents):
        # initialize empty board
        self.board = []
        for i in range(0, Grid.HEIGHT):
            self.board.append([0] * Grid.WIDTH)

        #initialize agents
        self.agents = agents
        self.add_agents_to_board()
        
        #set spawn and source locations
        self.board[0][0] = Grid.SPAWN
        self.board[2][2] = Grid.SOURCE
        self.sources = [(2, 2)]
        self.spawns = [(0, 0)]
        
        #initialize list of tuple-states
        self.states = []
        self.createStates()
        
        self.transitions = {}
        self.actions = ["up", "down", "left", "right"]
        self.transitionMap()


    def add_agents_to_board(self):
        # Adds the Agent representations to the board
        for agent in self.agents:
            self.board[agent.state.x][agent.state.y] = Grid.AGENT
    
    def get_all_agents(self):
        return self.agents

    def mock_action(self, agent, action):
        #Given an agent and an action, returns the reward without actually changing the agent's state
        return generate_reward(agent, action)
    
    def do_action(self, agent, action):
        #Given an agent and a selected action, update the agent's state to reflect the change, return the reward
        x, y = agent.state.coords
        new_x, new_y =  self.transitions[agent.state.coords][action]
        reward = self.generate_reward(agent, action)
        if reward==20:
            agent.state.is_carrying = False
        if reward ==10:
            agent.state.is_carrying = True
        agent.state.updateCoords(new_x, new_y)
        self.board[x][y] = 0
        self.board[new_x][new_y] = Grid.AGENT
        return reward

    def generate_reward(self, agent, action):
        #Given agent and action, returns the reward.
        #Default is 0, agent neither picked up or dropped resources
        #Reward is 10 if agent moves to source neighbor and agent.state.is_carrying == False (picks up resource)
        #Reward is 20 if agent moves to spawn neighbor and agent.state.is_carrying == True (drops off resource)
        if self.getNextState(agent.state.coords, action) in list(self.getAdjacent(self.sources[0])):
            if not agent.state.is_carrying:
                return 10
        elif self.getNextState(agent.state.coords, action) in list(self.getAdjacent(self.spawns[0])):
            if agent.state.is_carrying:
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
        adj =  {None: (coord[0], coord[1]), "right": (coord[0]+1, coord[1]), "left": (coord[0]-1, coord[1]), "down": (coord[0], coord[1]+1), "up": (coord[0], coord[1]-1)}
        for k in list(adj.keys() ):
            if (0 > adj[k][0]) or (adj[k][0]>=Grid.WIDTH) or (0>adj[k][1]) or (adj[k][1]>=Grid.HEIGHT) or adj[k] in self.sources + [agent.state.coords for agent in self.agents]:
                del adj[k]
        return adj
    
    def createStates(self):
        for x in range(Grid.WIDTH):
            for y in range(Grid.HEIGHT):
                self.states.append((x, y))

    def getNextState(self, state, action):
        return self.transitions[state][action]

