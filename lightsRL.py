from __future__ import division
import math
import random
import numpy as np
import constants as c

########################################
# lightsRL
#
# Class that serves as a reinforcement learning module
# to check for performance of the car with respect to
# streetlights.
########################################
class lightsRL():
    ########################################
    # __init__
    #
    # Constructor that initializes state and action tables
    # needed to run SARSA Q-learning algorithm.
    #
    # @param self: The instance of the class to use.
    # @param agent: The agent that is going to be trained.
    ########################################
    def __init__(self, agent):
        self.agent = agent
        self.state_space = init_state_space()
        self.av_table = init_state_actions(state_space)
        self.av_count = init_sa_count(av_table)
    
    ########################################
    # init_state_space
    #
    # Creates a list of all the possible states.
    #
    # @param self: The instance of the class to use.
    # @return: a list of all possible states
    ########################################
    def init_state_space(self):
        states = []
        for state in range(1, 4):
            states.append(state)
        return states

    ########################################
    # init_state_actions
    #
    # Creates a dictionary (key-value pairs) of all possible state-actions
    # and their values. This creates our Q-value look up table.
    #
    # @param self: The instance of the class to use.
    # @return: a dictionary of all possible state-actions and their values
    ########################################
    def init_state_actions(self):
        av = {}
        for state in self.state_space:
            for action in range(1, 5):
                av[(state, action)] = 0.0
        return av

    ########################################
    # init_sa_count
    #
    # Setup a dictionary of state-actions to record how many times we've
    # experienced a given state-action pair. We need this to re-calculate
    # reward averages.
    #
    # @param self: The instance of the class to use.
    # @return: a dictionary of state-actions count
    ########################################
    def init_sa_count(self):
        counts = {}
        for sa in self.av_table:
            counts[sa] = 0
        return counts
    
    ########################################
    # qsv
    #
    # Returns Q-value/avg rewards for each action given a state.
    #
    # @param state: the current state of the agent
    # @param av_table: a dictionary of state-actions and their values
    # @return: Q-value/avg rewards for each action given a state
    ########################################
    def qsv(self, state):
        q_rewards = {}
        for action in range (1, 5):
            q_rewards.append(self.av_table[(state, action)])
        return np.array(q_rewards)
    
    ########################################
    # next_step
    #
    # The next step is calculated based on the current state and the action
    # chosen.
    #
    # @param state: the current state of the agent
    # @param dec: action that agent makes at current state
    # @param lanes: an array of lanes' objects
    # @return: a tuple of the type (new_state, reward)
    ########################################
    def next_step(self, state, action, lanes):
        # Set current reward to 0 by default
        reward = 0

        # Set new state to 1 by default
        new_state = 1

        # Make agent take chosen action

        # Action = Increment velocity by 10
        if (action == 1):
            self.agent.increment_speed()
            self.agent.update()

        # Action = Decrement velocity by 10
        elif (action == 2):
            self.agent.decrement_speed()
            self.agent.update()

        # Action = Change to the lane to the left
        elif (action == 3):
            for i in range(len(lanes)):
                if (self.agent.get_lane() == lanes[i] and i != 0):
                    self.agent.change_lanes(lanes[i - 1])
            self.agent.update()

        # Action = Change to the lane to the right
        elif (action == 4):
            for i in range(len(lanes)):
                if (self.agent.get_lane() == lanes[i] and i != len(lanes) - 1):
                    self.agent.change_lanes(lanes[i + 1])
            self.agent.update()

        # Action = Stop
        else:
            self.agent.stop_car()
            self.agent.update()

        # Determine new state
        distance_to_light = self.agent.distance_to_light()
        # Off quadrant
        if (distance_to_light > c.MAX_SPEED or distance_to_light == -1):
            new_state = 1
        else:
            # If beyond light, then off quadrant
            if (not self.agent.approaching_to_light()):
                new_state = 1
            # On quadrant
            else:
                lane = self.agent.get_lane()

                # Green light
                if (lane.is_light_green()):
                    new_state = 2
                # Yellow light
                elif (lane.is_light_yellow()):
                    new_state = 3
                # Red light
                else:
                    new_state = 4

        # If original state was to be on the stoplights quadrant with
        # a green light and new state is to be off the stoplights quadrant,
        # give a positive reward
        if (state == 2 and new_state == 1):
            reward = 1
        # If original state was to be on the stoplights quadrant with
        # a yellow light and new state is to be off the stoplights quadrant,
        # give a positive reward
        elif (state == 2 and new_state == 1):
            reward = 1
        # If original state was to be on the stoplights quadrant with
        # a red light and new state is to be off the stoplights quadrant,
        # give a negative reward
        elif (state == 2 and new_state == -1):
            reward = 1

        return (new_state, reward)

    ########################################
    # run_simulation
    #
    # Runs one step of the simulation and updates state action tables'
    # values
    #
    # @param self: The instance of the class to use.
    # @param epsilon: value to toogle between exploration and exploitation
    # @param lanes: an array of lanes' objects
    # @return: mean reward up until current simulation
    ########################################
    def run_simulation(self, epsilon, lanes):
        # Get current state
        state = 0 #Change this to actual state

        # Epsilon greedy action selection
        action_probs = qsv(state, self.av_table)
        if (random.random() < epsilon):
            action = random.randint(1, 5)
        else:
            action = np.argmax(action_probs)

        # Build current state-action
        sa = (state, action)

        # Increment the count of the state-action
        self.av_count[sa] += 1

        # Make next step and get new state and reward
        state, reward = next_step(state, action, lanes)

        # Update average of action taken
        k = self.av_count[sa]
        old_avg = self.av_table[sa]
        new_avg = old_avg + (1.0 / k) * (reward - old_avg)
        self.av_table[sa] = new_avg

        # Calculate mean reward
        mean_reward = np.average(self.av_table, weights = np.array(\
                            [self.av_count[i] / np.sum(av_count) for\
                            i in range(len(self.av_count))]))

        return mean_reward