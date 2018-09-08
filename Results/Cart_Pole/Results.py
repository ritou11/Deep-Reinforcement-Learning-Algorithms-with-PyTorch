import time

from DQN_Agents.DDQN_Agent import DDQN_Agent
from DQN_Agents.DQN_Agent import DQN_Agent
from DQN_Agents.DQN_Agent_With_Fixed_Q_Targets import DQN_Agent_With_Fixed_Q_Targets
from DQN_Agents.DQN_With_Prioritised_Experience_Replay import DQN_With_Prioritised_Experience_Replay
from Open_AI_Gym_Environments.Cart_Pole_Environment import Cart_Pole_Environment
from Utilities import print_two_lines, save_score_results, visualise_results_by_agent
import numpy as np

SEED = 100
ROLLING_SCORE_LENGTH = 100
AVERAGE_SCORE_REQUIRED = 195
EPISODES_TO_RUN = 500
FILE_TO_SAVE_DATA_RESULTS = "Episode_results_by_agent.npy"

hyperparameters = {
    "learning_rate": 5e-4,
    "batch_size": 64,
    "buffer_size": int(1e5),
    "fc_units": [30, 30],
    "epsilon": 0.05,
    "gamma":  0.99,
    "tau": 1e-3,
    "update_every_n_steps": 1,
    "alpha": 0.5,
    "incremental_priority": 1e-5
}

results = {}


agent_number = 1

agents = [DQN_Agent, DQN_Agent_With_Fixed_Q_Targets, DDQN_Agent, DQN_With_Prioritised_Experience_Replay]
#
ENVIRONMENT = Cart_Pole_Environment()
#
# for agent_class in agents:
#
#     agent_name = agent_class.__name__
#     print("\033[1m" + "{}: {}".format(agent_number, agent_name) + "\033[0m")
#
#     agent = agent_class(ENVIRONMENT, SEED, hyperparameters,
#                         ROLLING_SCORE_LENGTH, AVERAGE_SCORE_REQUIRED, agent_name)
#     game_scores, rolling_scores = agent.run_game_n_times(num_episodes_to_run=EPISODES_TO_RUN)
#     results[agent_name] = [game_scores, rolling_scores]
#     agent_number += 1
#     print_two_lines()
#
#
# save_score_results(FILE_TO_SAVE_DATA_RESULTS, results)
#

# results = np.load(FILE_TO_SAVE_DATA_RESULTS)
# results = results.item()
#
#
# visualise_results_by_agent(agents, results, AVERAGE_SCORE_REQUIRED)

start = time.time()

agent_class = DQN_With_Prioritised_Experience_Replay
agent_name = agent_class.__name__
print("\033[1m" + "{}: {}".format(agent_number, agent_name) + "\033[0m")

agent = agent_class(ENVIRONMENT, SEED, hyperparameters,
                    ROLLING_SCORE_LENGTH, AVERAGE_SCORE_REQUIRED, agent_name, rank_prio=True)
game_scores, rolling_scores = agent.run_game_n_times(num_episodes_to_run=EPISODES_TO_RUN, save_model=False)
results[agent_name] = [game_scores, rolling_scores]
agent_number += 1
print_two_lines()

print(time.time() - start)
#

start = time.time()

agent_class = DQN_With_Prioritised_Experience_Replay
agent_name = agent_class.__name__
print("\033[1m" + "{}: {}".format(agent_number, agent_name) + "\033[0m")

agent = agent_class(ENVIRONMENT, SEED, hyperparameters,
                    ROLLING_SCORE_LENGTH, AVERAGE_SCORE_REQUIRED, agent_name, rank_prio=False)
game_scores, rolling_scores = agent.run_game_n_times(num_episodes_to_run=EPISODES_TO_RUN, save_model=False)
results[agent_name] = [game_scores, rolling_scores]
agent_number += 1
print_two_lines()

print(time.time() - start)