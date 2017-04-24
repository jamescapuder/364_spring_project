from grid import Grid

class Environment():
    def __init__(self):
        self.grid = Grid()

    # get ready for a new episode    
    def reset(self):
        self.grid.reset()

    def get_all_agents(self):
        return self.grid.agents

    def get_agent_actions(self, agent):
        result = []
        tile = grid.get_tile(agent.state.coords)

        for direction in tile.adjacent:
            adj_tile = tile.adjacent[direction]
            if adj_tile.type == Tile.EMPTY:
                result.append(direction)
            elif agent.state.carry < agent.capacity and adj_tile.type == Tile.SOURCE:
                result.append("gather")
            elif agent.state.carry > 0 and adj_tile.type == Tile.SPAWN:
                result.append("stow")

        return result
                
    # return the reward of the action
    def do_action(self, agent, action):
        if action == "gather":
            return 10
        elif action == "stow":
            return 20
        elif action == None:
            return 0
        else:
            return 0

    # returns the reward without actually doing it
    def mock_action(self, agent, action):
        if action == "gather":
            return 10
        elif action == "stow":
            return 20
        else:
            return 0


