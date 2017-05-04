# qlearning.py
# Uses q-learning to perform in a given environment
# Updated from hw4 to support multiple agents in one environmenmt

import matplotlib.pyplot as plt
from environment import Environment
from gui import Gui
import time
import curses

curses_enabled = False 
gui_enabled = False 


#ENV_FILE = "test_grid.txt"
#ENV_FILE = "dilemma.txt"
ENV_FILE = "emergence.txt"


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
TAU = 0.1

# q-learns the grid environment with epsilon-greedy and softmax
# approaches for selecting actions and graphs the results
def main():
    epsilon1 = qlearning(Environment(ENV_FILE), NUM_EPISODES, DISCOUNT_FACTOR, EPSILON_MODE, EPSILON1)
    epsilon2 = qlearning(Environment(ENV_FILE), NUM_EPISODES, DISCOUNT_FACTOR, EPSILON_MODE, EPSILON2)
    softmax = qlearning(Environment(ENV_FILE), NUM_EPISODES, DISCOUNT_FACTOR, SOFTMAX_MODE)

    agents = Environment(ENV_FILE).get_all_agents()

    episodes = range(1, NUM_EPISODES + 1)

    plt.figure(1)
    for i in range(len(agents)):
        plt.subplot(len(agents),len(agents),i+1)
        plt.scatter(episodes, epsilon1[i], s=20, label="epsilon 0.05")
        plt.scatter(episodes, epsilon2[i], s=10, label="epsilon 0.1")
        plt.scatter(episodes, softmax[i], s=5, label="softmax")
        plt.legend()
        num = str(i+1)
        plt.title("Cumulative Reward Over Time: Agent " + num)
        plt.xlabel("Number of Episodes")
        plt.ylabel("Cumulative Reward")

    #Total system reward
    epsilon1_total = [0]*NUM_EPISODES
    epsilon2_total = [0]*NUM_EPISODES
    softmax_total = [0]*NUM_EPISODES
    for i in range(len(agents)):
        curr_agent = epsilon1[i]
        for j in range(len(curr_agent)):
            epsilon1_total[j] += curr_agent[j]
        curr_agent = epsilon2[i]
        for j in range(len(curr_agent)):
            epsilon2_total[j] += curr_agent[j]
        curr_agent = softmax[i]
        for j in range(len(curr_agent)):
            softmax_total[j] += curr_agent[j]

    plt.subplot(len(agents),len(agents),len(agents)+1)
    plt.scatter(episodes, epsilon1_total, s=20, label="epsilon 0.05")
    plt.scatter(episodes, epsilon2_total, s=10, label="epsilon 0.1")
    plt.scatter(episodes, softmax_total, s=5, label="softmax")
    plt.legend()
    plt.title("Cumulative Reward Over Time: All Agents")
    plt.xlabel("Number of Episodes")
    plt.ylabel("Cumulative Reward")

    plt.tight_layout()
    plt.show()

# Returns a list of cumulative rewards for each of the num_episodes it runs
def qlearning(environment, num_episodes, discount_factor, mode, epsilon=0):
    agents = environment.get_all_agents()

    results = {}
    for i in range(len(agents)):
        results[i] = []

    for i in range(num_episodes):
        environment.reset()
        if i % 100 == 0:
            print("episode", i)
        episode_rewards = (qlearn_episode(agents, discount_factor, mode, epsilon, i))
        for agent in episode_rewards.keys():
            results[agent].append(episode_rewards[agent])
    return results

# Q-learns for a single episode
def qlearn_episode(agents, discount_factor, mode, epsilon, episode):
    # run the simulation
    if gui_enabled and (episode == 0 or episode == 999):
        gui = Gui(agents[0].environment.grid)
    for steps in range(1, NUM_STEPS + 1):
        #time.sleep(0.5)
        if curses_enabled:
            screen = init_curses()
        if agents[0].environment.done:
            break
        # give each agent a turn
        for agent in agents:
            action = pick_action(agent, mode, epsilon, TAU)
            agent.do_action(action, get_alpha(steps), discount_factor, get_reward_modifier(steps)) 
        if curses_enabled: 
            curses_step(screen, agents[0].environment.grid.board)
        if gui_enabled and (episode == 0 or episode == 999):
            gui.updateBoard(agents[0].environment.grid)
    if curses_enabled:
        kill_curses(screen)
    rewards = {}
    for i in range (len(agents)):
        rewards[i] = agents[i].cumulative_reward
    return rewards

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


# CURSES METHODS
def init_curses():
    stdscr = curses.initscr()
    curses.noecho()
    stdscr.clear()
    stdscr.keypad(True)
    return stdscr

def kill_curses(stdscr):
    stdscr.keypad(False)
    curses.echo()
    # restore the terminal to its original state
    curses.endwin()

def curses_step(stdscr, board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            stdscr.addch(y,x, board[y][x].tile_type)
    stdscr.refresh()
    
if __name__ == "__main__":
    main()
