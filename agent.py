# represents an agent within the environment

import random
import math
from state import State

class Agent():

    # initializes the agent's environment and state
    def __init__(self, environment, x, y, carry, agent_type):
        self.environment = environment
        self.state = (x, y, carry) 
        self.start_state = (x, y, carry) 
        self.qtable = dict()
        self.cumulative_reward = 0
        self.capacity = 1
        self.agent_type = agent_type

    def update_position(self, x, y):
        self.state = (x, y, self.state[State.CARRY])

    # resets the agent
    def reset(self, start_state = None):
        self.state = self.start_state
        self.cumulative_reward = 0

    # returns the possible actions the agent can do
    def get_actions(self):
        return self.environment.get_agent_actions(self)

    # returns the reward for doing the given action
    # updates state and qtable
    # takes in the value of alpha for updateing qtable
    def do_action(self, action, alpha, discount_factor, reward_modifier):
        old_state = self.state 
        reward = self.environment.do_action(self, action)
        self.update_q(old_state, action, reward, alpha, discount_factor)
        self.cumulative_reward += reward_modifier * reward 
        return reward 

    # returns the reward for action without actually doing it
    def mock_action(self, action):
        return self.environment.mock_action(self, action)

    # extracts an entry from the q-table, handling uninitialized entires
    def get_q(self, state, action):
        if state not in self.qtable:
            return 0
        elif action not in self.qtable[state]:
            return 0
        else:
            return self.qtable[state][action]

    # updates the state, qtable, and cumulative reward
    def update_q(self, state, action, reward, alpha, discount_factor):
        next_state = self.state
        prev_component = (1 - alpha) * self.get_q(state, action)
        new_q = self.get_q(next_state, self.get_exploitative_action())
        update = alpha * (reward + (discount_factor * new_q))
        if not state in self.qtable:
            self.qtable[state] = dict()
        self.qtable[state][action] = prev_component + update

    # returns a random action
    def get_explorative_action(self):
        actions = self.get_actions()
        if len(actions) == 0:
            return None
        r = random.randrange(len(actions))
        return actions[r]

    # returns the action with the highest q value given the state
    def get_exploitative_action(self):
        state = self.state
        actions = self.get_actions()
        result = None
        highest = -float("inf")

        for action in actions:
            if self.get_q(state, action) > highest:
                highest = self.get_q(state, action)
                result = action

        return result

    # picks an action using the epsilon-greedy approach
    def pick_action_epsilon(self, epsilon):
        r = random.random()
        if r < epsilon:
            return self.get_explorative_action()
        else:
            return self.get_exploitative_action()

    # picks an action using softmax
    def pick_action_softmax(self, tau):
        r = random.random()
        state = self.state
        actions = self.get_actions()

        total = 0
        for action in actions:
            total += math.e ** (self.get_q(state, action) / tau)
            
        probs = dict()
        for action in actions:
            probs[action] = (math.e ** (self.get_q(state, action) / tau)) / total
        
        current = 0
        for action in probs:
            current += probs[action]
            if r < current:
                return action

        return self.get_explorative_action()
