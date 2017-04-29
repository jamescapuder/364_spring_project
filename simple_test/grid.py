import random
from agent import Agent

"""
The Grid class defines the Grid that the agent operate in
"""
class Grid():
    HEIGHT = 6
    WIDTH = 15
    OBSTACLES = [(2, 2), (2, 3), (3, 2), (3, 3), (6, 2), (6, 3)]
    ABSORBING_STATE = (-1, -1)
    DEFAULT_REWARD = -0.1

    """
    Constructs a new Grid
    """
    def __init__(self):
        random.seed(12345)
        
        self.states = []
        self.terminalStates = []
        self.actions = []
        self.transitions = {}
        self.rewards = {}

        self.createStates()
        self.createActions()
        self.createTransitions()
        self.createRewards()

    def reset(self):
        self.agent.reset()

    def get_agent_actions(self, agent):
        return ["up", "down", "left", "right"]

    def do_action(self, agent, action):
        state = self.agent.state
        new_state = self.generateNextState(state, action)
        agent.update_position(new_state)
        return self.generateReward(state, action)

    def get_all_agents(self):
        result = [None]
        self.agent = Agent(self, (0, 0))
        result[0] = self.agent
        return result

    """
    Fills self.states and self.terminalStates with the necessary information
    """
    def createStates(self):
        for x in range(Grid.WIDTH):
            for y in range(Grid.HEIGHT):
                if (x, y) not in Grid.OBSTACLES:
                    self.states.append((x, y))
        self.states.append(Grid.ABSORBING_STATE)

        self.terminalStates.append((Grid.WIDTH - 1, Grid.HEIGHT - 2))
        self.terminalStates.append((Grid.WIDTH - 1, Grid.HEIGHT - 1))

    """
    Fills self.actions with the necessary information
    """
    def createActions(self):
        self.actions.extend(["up", "down", "left", "right"])

    """
    Fills self.transitions with the necessary information
    """
    def createTransitions(self):
        for state in self.states:
            self.transitions[state] = {}
            for action in self.actions:
                self.transitions[state][action] = {}
                for nextState in self.states:
                    prob = self.transitionProb(state, action, nextState)
                    self.transitions[state][action][nextState] = prob

    """
    Fills self.rewards with the necessary information
    """
    def createRewards(self):
        for state in self.states:
            self.rewards[state] = {}
            for action in self.actions:
                self.rewards[state][action] = Grid.DEFAULT_REWARD
                if state == (Grid.WIDTH - 1, Grid.HEIGHT - 1): self.rewards[state][action] = 1.0
                if state == (Grid.WIDTH - 1, Grid.HEIGHT - 2): self.rewards[state][action] = -1.0
                if state == Grid.ABSORBING_STATE: self.rewards[state][action] = 0.0

    """
    Computes the probability of transitioning from state to nextState after taking action

    state: the current state
    action: the chosen action
    nextState: the next state
    """
    def transitionProb(self, state, action, nextState):
        # terminal states are absorbing
        if state in self.terminalStates or state == Grid.ABSORBING_STATE:
            return 1.0 if nextState == Grid.ABSORBING_STATE else 0.0

        expected = None
        left = None
        right = None
        if action == "up":
            expected = (state[0], state[1] + 1)
            left = (state[0] - 1, state[1])
            right = (state[0] + 1, state[1])
        elif action == "down":
            expected = (state[0], state[1] - 1)
            left = (state[0] + 1, state[1])
            right = (state[0] - 1, state[1])
        elif action == "left":
            expected = (state[0] - 1, state[1])
            left = (state[0], state[1] - 1)
            right = (state[0], state[1] + 1)
        elif action == "right":
            expected = (state[0] + 1, state[1])
            left = (state[0], state[1] + 1)
            right = (state[0], state[1] - 1)

        if expected not in self.states:
            expected = state
        if left not in self.states:
            left = state
        if right not in self.states:
            right = state

        prob = 0.0
        if expected == nextState:
            prob += 1.0 
        if left == nextState:
            prob += 0.0
        if right == nextState:
            prob += 0.0

        return prob

    """
    Generates a new start state
    """
    def generateStartState(self):
        return (0, 0)

    """
    Generates a next state after taking an action in a given state

    state: the current state
    action: the chosen action
    """
    def generateNextState(self, state, action):
        validNext = []
        for nextState in self.states:
            if self.transitions[state][action][nextState] > 0:
                validNext.append(nextState)

        rand = random.random()
        for nextState in validNext:
            prob = self.transitions[state][action][nextState]
            if rand < prob:
                return nextState
            else:
                rand -= prob

        # make sure we return a state (due to Pythons float precision)
        return validNext[-1]

    """
    Generates a reward earned for taking an action in a state, resulting in a next state

    state: the current state
    action: the chosen action
    """
    def generateReward(self, state, action):
        return self.rewards[state][action]
