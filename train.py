#!/usr/bin/env python3
import os
import random
import numpy as np
from collections import deque
from torch.utils.tensorboard import SummaryWriter
from util import State

import chess
import pygame
import gym
from gym import spaces

import gym_chess  # TODO: check this out [https://pypi.org/project/gym-chess/]

# TODO: define the environment using gym and chess
class Environment(gym.Env):
  # TODO: either use pygame or terminal for gameplay
  metadata = {"render_modes": ["human", "array"], "render_fps": 4}

  def __init__(self):
    self.window_size = 512  # size of pygame window
    self.board = chess.Board()

    # TODO: need to use chess library here
    self.observation_space = spaces.Dict(
      {
      }
    )


# TODO: define the DQN agent
class Agent:
  def __init__(self):
    pass

  def act(self, state):
    pass

  def cache(self, experience):
    pass

  def recall(self):
    pass

  def learn(self):
    pass


if __name__ == '__main__':
  env = gym.make('Chess-v0')
  print(env.render())
  env.reset()

  done = False
  while not done:
    action = random.sample(env.legal_moves, 1)
    env.step(action)
    print(env.render(mode="unicode"))

  env.close()

