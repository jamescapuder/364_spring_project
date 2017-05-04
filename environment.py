from grid import Grid
from tile import Tile
from state import State

class Environment():
    def __init__(self, fname):
        self.grid = Grid(fname, self)
        self.done = False

    # get ready for a new episode    
    def reset(self):
        self.grid.reset()
        self.done = False 

    def get_all_agents(self):
        return self.grid.agents

    def get_agent_actions(self, agent):
        result = []
        tile = self.grid.get_tile(agent.state[State.X], agent.state[State.Y])
        for direction in tile.adjacent:
            adj_tile = tile.adjacent[direction]
            tile_type = adj_tile.tile_type
            if tile_type == Tile.EMPTY or tile_type == Tile.GOAL or tile_type == Tile.PENALTY:
                result.append(direction)
            elif agent.state[State.CARRY] < agent.capacity and tile_type == Tile.SOURCE:
                if agent.agent_type == Tile.AGENT or agent.agent_type == Tile.GATHERER:
                    result.append("gather")
            elif agent.state[State.CARRY] > 0 and tile_type == Tile.SPAWN:
                if agent.agent_type == Tile.AGENT or agent.agent_type == Tile.CARRIER:
                    result.append("stow")
            elif agent.agent_type == Tile.GATHERER and adj_tile.tile_type == Tile.CARRIER:
                for adj_agent in self.grid.agents:
                    if adj_agent.state[0] == adj_tile.coords[0] and adj_agent.state[1] == adj_tile.coords[1]:
                        agent.handoffee = adj_agent
                        break
                result.append("handoff")
        return result
                
    # return the reward of the action
    def do_action(self, agent, action):
        source_tile = self.grid.get_tile(agent.state[State.X], agent.state[State.Y])
        if action == "gather":
            agent.state = (agent.state[State.X], agent.state[State.Y], agent.state[State.CARRY] + 1)
            if self.grid.get_tile(agent.state[State.X], agent.state[State.Y]).num_adjacent_agents() > 0:
                agent.reduced_reward = True
            return 0 
        elif action == "stow":
            agent.state = (agent.state[State.X], agent.state[State.Y], agent.state[State.CARRY] - 1)
            return 1 
        elif action == None:
            return 0 
        elif action == "handoff":
            target_agent = agent.handoffee
            target_agent.state = (target_agent.state[0], target_agent.state[1], target_agent.state[State.CARRY] + 1)
            agent.state = (agent.state[0], agent.state[1], agent.state[State.CARRY]  - 1)
            return 0.5
        else:
            dest_tile = source_tile.adjacent[action]
            source_tile.tile_type = Tile.EMPTY 
            dest_tile.tile_type = agent.agent_type
            agent.update_position(dest_tile.x, dest_tile.y)
            
            if dest_tile.init_type == Tile.GOAL:
                self.done = True
                return 1
            if dest_tile.init_type == Tile.PENALTY:
                self.done = True
                return -1

            return 0

    # returns the reward without actually doing it
    def mock_action(self, agent, action):
        if action == "gather":
            return 1
        elif action == "stow":
            return 2
        else:
            source_tile = self.grid.get_tile(agent.state[State.X], agent.state[State.Y])
            dest_tile = source_tile.adjacent[action]
            
            if dest_tile.init_type == Tile.GOAL:
                return 1
            if dest_tile.init_type == Tile.PENALTY:
                return -1
            return -0.1 

