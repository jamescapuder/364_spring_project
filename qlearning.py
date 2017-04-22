# qlearning.py
# Uses q-learning to perform in a given environment
# Updated from hw4 to support multiple agents in one environmenmt

import matplotlib.pyplot as plt
import random
import math

# number of iterations to run q-learning
NUM_EPISODES = 1000

# number of steps to run each episode
NUM_STEPS = 1000

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
    epsilon1 = qlearning(Environment(), NUM_EPISODES, DISCOUNT_FACTOR, EPSILON_MODE, EPSILON1)
    epsilon2 = qlearning(Environment(), NUM_EPISODES, DISCOUNT_FACTOR, EPSILON_MODE, EPSILON2)
    softmax = qlearning(Environment(), NUM_EPISODES, DISCOUNT_FACTOR, SOFTMAX_MODE)
    
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
    agents = environment.get_all_agents()

    # TODO: for now we are just summing the results for each individual angent, perhaps it might be worthwhile to graph separately?
    results = []
    qtable = dict()
    for agent in agents:
        qtable[agent] = dict()

    for i in range(num_episodes):
        results.append(qlearn_episode(agents, qtable, discount_factor, mode, epsilon))

    return results

# Q-learns for a single episode
# While we don't reach an absorbing state,
# pick an action based on the Q-table and
# update the table and comulative reward
def qlearn_episode(agents, qtable, discount_factor, mode, epsilon):
    # dictionary mapping each agent to its cumulative reward
    cumulative_reward = dict()
    # dictionary mapping each agent to its state
    state = dict() 
    # initialize the state and reward of  each agent
    for agent in agents:
        cumulative_reward[agent] = 0
        state[agent] = agent.get_state()

    # run the simulation
    for i in range(NUM_STEPS):
        # give each agent a turn
        for agent in agents:
            action = pick_action(agent, agent.get_actions(), qtable[agent], mode, epsilon)
            reward = agent.do_action(action) 
            next_state = agent.get_state() 
            cumulative_reward[agent] += (discount_factor ** steps) * reward 
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
def pick_action(agent, mode, tune):
    if mode == EPSILON_MODE:
        return agent.pick_action_epsilon(tune)
    elif mode == SOFTMAX_MODE:
        return agent.pick_action_softmax(tune)

if __name__ == "__main__":
    main()
