from grid import Grid
from tile import Tile

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
        tile = self.grid.get_tile(agent.state.coords)
        for direction in tile.adjacent:
            adj_tile = tile.adjacent[direction]
            tile_type = adj_tile.tile_type
            if tile_type == Tile.EMPTY or tile_type == Tile.GOAL or tile_type == Tile.PENALTY:
                result.append(direction)
            elif agent.state.carry < agent.state.capacity and tile_type == Tile.SOURCE:
                result.append("gather")
            elif agent.state.carry > 0 and tile_type == Tile.SPAWN:
                result.append("stow")

        return result
                
    # return the reward of the action
    def do_action(self, agent, action):
        #print(self.grid)
        source_tile = self.grid.get_tile(agent.state.coords)
        #print("Action:", action)
        if action == "gather":
            agent.state.carry += 1
            return 1
        elif action == "stow":
            agent.state.carry -= 1
            return 2
        elif action == None:
            return -0.1
        else:
            dest_tile = source_tile.adjacent[action]
            source_tile.tile_type = source_tile.init_type 
            dest_tile.tile_type = Tile.AGENT
            agent.update_position(dest_tile.coords)
            
            if dest_tile.init_type == Tile.GOAL:
                self.done = True
                return 1
            if dest_tile.init_type == Tile.PENALTY:
                self.done = True
                return -1

            return -0.1

    # returns the reward without actually doing it
    def mock_action(self, agent, action):
        if action == "gather":
            return 10
        elif action == "stow":
            return 20
        else:
            return 0

