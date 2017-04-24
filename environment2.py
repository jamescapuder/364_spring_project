from agent import Agent
from grid import Grid
from state import State

class Environment():
    def __init__(self):
        self.agents = []
        self.grid = Grid(self.agents)

    # get ready for a new episode    
    def reset(self):
        self.grid.reset()

    def get_all_agents(self):
        return self.agents

    def get_agent_actions(self, agent):
        return self.grid.get_agent_actions(agent)

    # return the reward of the action
    def do_action(self, agent, action):
        return self.grid.do_action(agent, action)

    # returns the reward without actually doing it
    def mock_action(self, agent, action):
        return self.grid.mock_action(agent, action)


