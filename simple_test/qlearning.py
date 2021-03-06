# qlearning.py
# Uses q-learning to perform in a given environment
# Updated from hw4 to support multiple agents in one environmenmt

import matplotlib.pyplot as plt
from grid import Grid

ENV_FILE = "adam_board.txt"
#ENV_FILE = "test_grid.txt"

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
    epsilon1 = qlearning(Grid(), NUM_EPISODES, DISCOUNT_FACTOR, EPSILON_MODE, EPSILON1)
    epsilon2 = qlearning(Grid(), NUM_EPISODES, DISCOUNT_FACTOR, EPSILON_MODE, EPSILON2)
    #softmax = qlearning(Environment(ENV_FILE), NUM_EPISODES, DISCOUNT_FACTOR, SOFTMAX_MODE)
    
    episodes = range(1, NUM_EPISODES + 1) 
    plt.scatter(episodes, epsilon1, s=20, label="epsilon 0.05")
    plt.scatter(episodes, epsilon2, s=10, label="epsilon 0.1")
    #plt.scatter(episodes, softmax, s=5, label="softmax")
    plt.legend()
    plt.title("Cumulative Reward Over Time")
    plt.xlabel("Number of Episodes")
    plt.ylabel("Cumulative Reward")
    plt.show()

# Returns a list of cumulative rewards for each of the num_episodes it runs
def qlearning(environment, num_episodes, discount_factor, mode, epsilon=0):
    agents = environment.get_all_agents()

    results = []

    for i in range(num_episodes):
        environment.reset()
        if i % 100 == 0:
            print("episode", i)
        results.append(qlearn_episode(agents, discount_factor, mode, epsilon))
    return results

# Q-learns for a single episode
def qlearn_episode(agents, discount_factor, mode, epsilon):
    # run the simulation
    for steps in range(1, NUM_STEPS + 1):
        if agents[0].state == agents[0].environment.ABSORBING_STATE:
            break
        # give each agent a turn
        for agent in agents:
            action = pick_action(agent, mode, epsilon, TAU)
            agent.do_action(action, get_alpha(steps), discount_factor, get_reward_modifier(steps)) 

    return agents[0].cumulative_reward

# computes alpha for updating qtable
def get_alpha(num_steps):
    return 1 / num_steps

# gets the reward modifier for adding to cumulative reward
def get_reward_modifier(num_steps):
    return DISCOUNT_FACTOR ** num_steps

# picks an action using either softmac or the epsilon-greedy approach
def pick_action(agent, mode, epsilon, tau):
    if mode == EPSILON_MODE:
        return agent.pick_action_epsilon(epsilon)
    elif mode == SOFTMAX_MODE:
        return agent.pick_action_softmax(tau)

if __name__ == "__main__":
    main()
