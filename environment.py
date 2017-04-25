from grid import Grid
from tile import Tile

class Environment():
    def __init__(self, fname):
        self.grid = Grid(fname, self)

    # get ready for a new episode    
    def reset(self):
        self.grid.reset()

    def get_all_agents(self):
        return self.grid.agents

    def get_agent_actions(self, agent):
        result = []
        tile = self.grid.get_tile(agent.state.coords)

        print(len(tile.adjacent.keys()))
        for direction in tile.adjacent:
            adj_tile = tile.adjacent[direction]
            print(adj_tile.tile_type) 
            if adj_tile.tile_type == Tile.EMPTY:
                result.append(direction)
            elif agent.state.is_carrying < agent.state.capacity and adj_tile.tile_type == Tile.SOURCE:
                result.append("gather")
            elif agent.state.is_carrying > 0 and adj_tile.tile_type == Tile.SPAWN:
                result.append("stow")

        return result
                
    # return the reward of the action
    def do_action(self, agent, action):
        source_tile = self.grid.get_tile(agent.state.coords)

        if action == "gather":
            agent.state.is_carrying += 1
            return 10
        elif action == "stow":
            agent.state.is_carrying -= 1
            return 20
        elif action == None:
            return 0
        else:
            dest_tile = source_tile.adjacent[action]
            source_tile.tile_type = Tile.EMPTY
            dest_tile.tile_type = Tile.AGENT
            agent.update_position(dest_tile.coords)
            return 0

    # returns the reward without actually doing it
    def mock_action(self, agent, action):
        if action == "gather":
            return 10
        elif action == "stow":
            return 20
        else:
            return 0

