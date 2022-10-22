#!/usr/bin/env python3
import chess.pgn
import os
from tqdm import trange
import numpy as np

from util import State

data_dir = "data/"

# TODO: g_limit will be the size of train data, if test=True then the rest of the data will be for evaluation
def get_data(g_limit=None, test=False):
  X, Y = [], []
  results = {'1/2-1/2': 0, '0-1': 1, '1-0': 1}  # determines who won

  for idx, data_file in enumerate(sorted(os.listdir(data_dir))[1:]):
    print("(%d/%d) Processing: %s"%(idx+1, len(os.listdir(data_dir))-1, data_file))
    pgn = open(os.path.join(data_dir, data_file))
    game_idx = 0
    while 1:
      try:
        game = chess.pgn.read_game(pgn)
      except UnicodeDecodeError:
        print("UnicodeDecodeError: skipping current file")
        continue

      if game is None:
        break
      if g_limit is not None and game_idx >= g_limit:
        break

      game_idx += 1
      print("Extracting data from game:", game_idx)
      res = game.headers['Result']
      if res not in results:
        continue

      winner = results[res]
      board = game.board()

      n_moves = 0
      for i, m in enumerate(game.mainline_moves()):
        n_moves += 1
      print("Parsing %d moves"%n_moves)

      next_move = None
      for i, move in enumerate(game.mainline_moves()):
        print("Move", i, end="\r")
        board.push(move)
        #serialized_board = State(board).serialize()
        X_temp = State(board).to_net_input()
        X.append(serialized_board)  # TODO: X should not just be the board, but the STATE
        #Y.append(winner)
        if i != 0:
          next_move = move
        if next_move is not None:
          Y.append(next_move) # TODO: need to preprocess Y into tensor (size of all possible moves? map move strings to array and make it classification? maybe make it regression?)

      del X[-1]

    print("%d games parsed"%game_idx)
    break

  return np.array(X), np.array(Y)



if __name__ == '__main__':
  X, Y = get_data()
  print(len(X), "boards (X)")
  print(len(Y), "next moves (Y)")

