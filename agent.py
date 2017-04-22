# represents an agent within the environment

import random

class Agent():

    # initializes the agent's environment and state
    def __init__(self, environment, state):
        self.environment = environment
        self.state = state
        self.qtable = dict()
        self.cumulative_reward = 0

    # returns the possible actions the agent can do
    def get_actions(self):
        return environment.get_agent_actions(self)

    # returns the reward for doing the given action
    # updates state and qtable
    # takes in the value of alpha for updateing qtable
    def do_action(self, action, alpha):
        new_state, reward = environment.do_action(self, action)
        self.update_state(action, new_state, alpha)
        return environment.do_action(self, action)

    # returns the reward for action without actually doing it
    def mock_action(self, action):
        return environment.mock_action(self, action)

    # extracts an entry from the q-table, handling uninitialized entires
    def get_q(state, action):
        if state not in self.qtable:
            return 0
        elif action not in self.qtable[state]:
            return 0
        else:
            return qtable[state][action]

    # updates the state and qtable
    def update_q(action, state, next_state, alpha):
        prev_component = (1 - alpha) * self.get_q(state, action)
        self.state = next_state
        new_q = self.get_q(next_state, get_exploitative_action)

    # returns a random action
    def get_explorative_action():
        actions = self.get_actions()
        r = random.randrange(len(actions))
        return actions[r]

    # returns the action with the highest q value given the state
    def get_exploitative_action():
        actions = self.get_actions()
        result = None
        highest = -float("inf")

        for action in actions:
            if self.q(qtable, state, action) > highest:
                highest = self.q(qtable, state, action)
                result = action
        
        return result

    # picks an action using the epsilon-greedy approach
    def pick_action_epsilon(epsilon):
        r = random.random()
        if r < epsilon:
            return self.get_explorative_action()
        else:
            return self.get_exploitative_action()

    # picks an action using softmax
    def pick_action_softmax(tau):
        r = random.random()
        state = self.state
        actions = self.get_actions()

        total = 0
        for action in actions:
            total += math.e ** (self.q(qtable, state, action) / TAU)

        if total <= 1:
            return self.get_explorative_action() 
            
        probs = dict()
        for action in actions:
            probs[action] = (math.e ** (self.q(qtable, state, action) / TAU)) / total
        
        current = 0
        for action in probs:
            current += probs[action]
            if r < current:
                return action

        return self.get_explorative_action()
