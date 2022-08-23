#!/usr/bin/env python3
import chess.pgn
import os
from tqdm import trange
import numpy as np
import torch

data_dir = "data/"

def get_data():
  X, Y = [], []
  results = {'1/2-1/2': 0, '0-1': 1, '1-0': 1}  # determines who won

  for idx, data_file in enumerate(sorted(os.listdir(data_dir))[1:]):
    print("(%d/%d) Processing: %s"%(idx+1, len(os.listdir(data_dir))-1, data_file))
    pgn = open(os.path.join(data_dir, data_file))
    while 1:
      try:
        game = chess.pgn.read_game(pgn)
      except UnicodeDecodeError:
        print("UnicodeDecodeError: skipping current file")
        continue

      if game is None:
        break

      res = game.headers['Result']
      if res not in results:
        continue

      winner = results[res]
      board = game.board()
      for i, move in enumerate(game.mainline_moves()):
        board.push(move)
        #print(move) # TODO: need to serialize moves into a suitable tensor
        # TODO: append to X and Y

  return np.array(X), np.array(Y)



if __name__ == '__main__':
  get_data()

