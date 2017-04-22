# represents an agent within the environment

class Agent():

    # initializes the agent's environment and state
    def __init__(self, environment, x, y):
        self.environment = environment
        self.x = x
        self.y = y
        self.carry = False

    # returns the agent's state
    def get_state(self):
        return [self.x, self.y, self.carry]

    # returns the possible actions the agent can do
    def get_actions(self):
        return environment.get_agent_actions(self)

    # returns the reward for doing the given action
    def do_action(action):
        return environment.do_action(self, action)
