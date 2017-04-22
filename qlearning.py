# qlearning.py
# Eren Guendelsberger
# Spring 2017
# Uses q-learning to perform in a given environment

from grid import Grid
import matplotlib.pyplot as plt
import random
import math

# number of iterations to run q-learning
NUM_EPISODES = 1000

# higher values include information from more steps
DISCOUNT_FACTOR = 0.99

# constants for action selection mode
EPSILON_MODE = 0
EPSILON1 = 0.05
EPSILON2 = 0.10
SOFTMAX_MODE = 1
TAU = 0.01

# q-learns the grid environment with epsilon-greedy and softmax
# approaches for selecting actions and graphs the results
def main():
    epsilon1 = qlearning(Grid(), NUM_EPISODES, DISCOUNT_FACTOR, EPSILON_MODE, EPSILON1)
    epsilon2 = qlearning(Grid(), NUM_EPISODES, DISCOUNT_FACTOR, EPSILON_MODE, EPSILON2)
    softmax = qlearning(Grid(), NUM_EPISODES, DISCOUNT_FACTOR, SOFTMAX_MODE)
    
    episodes = range(1, NUM_EPISODES + 1) 
    plt.scatter(episodes, epsilon1, s=20, label="epsilon 0.05")
    plt.scatter(episodes, epsilon2, s=10, label="epsilon 0.1")
    plt.scatter(episodes, softmax, s=5, label="softmax")
    plt.legend()
    plt.title("Cumulative Reward Over Time")
    plt.xlabel("Number of Episodes")
    plt.ylabel("Cumulative Reward")
    plt.show()

# Returns a list of cumulative rewards for each of the num_episodes it runs
def qlearning(environment, num_episodes, discount_factor, mode, epsilon=0):
    results = []
    qtable = dict()

    for i in range(num_episodes):
        results.append(qlearn_episode(environment, qtable, discount_factor, mode, epsilon))

    return results

# Q-learns for a single episode
# While we don't reach an absorbing state,
# pick an action based on the Q-table and
# update the table and comulative reward
def qlearn_episode(environment, qtable, discount_factor, mode, epsilon):
    cumulative_reward = 0 
    state = environment.generateStartState()
   
    steps = 0
    while state != environment.ABSORBING_STATE:
        action = pick_action(environment, qtable, state, mode, epsilon)
        next_state = environment.generateNextState(state, action)
        reward = environment.generateReward(state, action)
        cumulative_reward += (discount_factor ** steps) * reward 
        update_qtable(environment, qtable, steps+1, discount_factor, state, action, next_state, reward)
        state = next_state
        steps += 1 

    return cumulative_reward

# Updates the q-table using the bellman equation
def update_qtable(environment, qtable, steps, discount_factor, state, action, next_state, reward):
    alpha = 1 / steps
    previous = (1 - alpha) * q(qtable, state, action) 
    new_q = q(qtable, next_state, get_exploitative_action(next_state, environment.actions, qtable)) 
    update = alpha * (reward + (discount_factor * new_q))
    
    if not state in qtable:
        qtable[state] = dict()
    
    qtable[state][action] = previous + update

# picks an action using either softmac or the epsilon-greedy approach
def pick_action(environment, qtable, state, mode, epsilon):
    r = random.random()

    if mode == SOFTMAX_MODE:
        total = 0
        for action in environment.actions:
            total += math.e ** (q(qtable, state, action) / TAU)

        if total == 0:
            return get_explorative_action(environment.actions) 
            
        probs = dict()
        for action in environment.actions:
            probs[action] = (math.e ** (q(qtable, state, action) / TAU)) / total
        
        current = 0
        for action in probs:
            current += probs[action]
            if r < current:
                return action

    elif mode == EPSILON_MODE:
        exploitative_action = get_exploitative_action(state, environment.actions, qtable)
        explorative_action = get_explorative_action(environment.actions)
        if r < epsilon:
            return explorative_action
        else:
            return exploitative_action

# returns the action with the highest q value given the state
def get_exploitative_action(state, actions, qtable):
    result = None
    highest = -float("inf")

    for action in actions:
        if q(qtable, state, action) > highest:
            highest = q(qtable, state, action)
            result = action
    
    return result

# returns a random action
def get_explorative_action(actions):
    r = random.randrange(len(actions))
    return actions[r]

# extract an entry from the q-table, handling uninitialized cells
def q(qtable, state, action):
    if state not in qtable:
        return 0 
    elif action not in qtable[state]:
        return 0 
    else:
        return qtable[state][action]

if __name__ == "__main__":
    main()

