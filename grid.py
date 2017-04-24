from agent import Agent
from state import State
from spawn import Spawn
from source import Source

class Grid():
    EMPTY = 'o'
    SPAWN = 's'
    SOURCE = 'r'
    AGENT = 'a'
    OBSTACLE = 'x'

    WIDTH = 5
    HEIGHT = 5

    def __init__(self):
        self.agents = list()
        self.spawns = list()
        self.sources = list()
        
        # TODO: read board from file
        self.board = []
        for i in range(Grid.HEIGHT):
            self.board.append([])
            for j in range(Grid.WIDTH):
                if (i == 1 and j == 2) or (i == 2 and j == 1):
                    self.board[i].append(Grid.AGENT)
                    self.agents.append(Agent(self, State(j, i)))
                if i == 3 and j == 3:
                    self.board[i].append(Grid.SOURCE)
                    self.sources[(j, i)] = Source(self, j, i)
                if i == 0 and j == 0:
                    self.board[i].append(Grid.SPAWN)
                    self.spawns[(j, i)] = Spawn(self, j, i)
                else:
                    self.board[i].append(Grid.EMPTY)

        self.actions = {"north": self.valid_north,
                        "south": self.valid_south,
                        "west": self.valid_west,
                        "east": self.valid_east,
                        "gather": self.valid_gather,
                        "stow": self.valid_stow}

    def get_agent_actions(agent):
        result = []
        for action in self.actions:
            if self.actions[action](agent):
                result.append(action)
        return result
"""        
    def valid_north(self, agent):
        return self.tile_type(self.north(agent.state.coords), Grid.EMPTY)

    def valid_south(self, agent):
        return self.tile_type(self.south(agent.state.coords), Grid.EMPTY)
        
    def valid_west(self, agent):
        return self.tile_type(self.west(agent.state.coords), Grid.EMPTY)

    def valid_east(self, agent):
        return self.tile_type(self.east(agent.state.coords), Grid.EMPTY)

    def north(self, coords):
        return (coords[0], coords[1] - 1)

    def south(self, coords):
        return (coords[0], coords[1] + 1)

    def west(self, coords):
        return (coords[0] - 1, coords[1])

    def east(self, coords):
        return (coords[0] + 1, coords[1])

    def tile_type(self, coords, expected):
        return self.grid

    def valid_gather(self, agent):
        return not agent.state.is_carrying and self.valid_interaction(agent.state.x, agent.state.y Grid.SOURCE)

    def valid_stow(self, agent:
        return agent.state.is_carrying and self.valid_stow(agent.state.x, agent.state.y Grid.STOW)

    def valid_interaction(self, x, y, i_type):
        return (self.inbounds_north(x, y) and self.board[x][y-1] == i_type or\
               (self.inbounds_south(x, y) and self.board[x][y+1] == i_type or\
               (self.inbounds_west(x, y) and self.board[x-1][y] == i_type or\
               (self.inbounds_east(x, y) and self.board[x+1][y] == i_type or\
""" # TODO: instead of all the above, create tile class that stores adjacent tiles and their types
       
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
