#!/usr/bin/env python3
import chess.pgn
import os
from tqdm import trange
import numpy as np

from util import State

data_dir = "data/"

def get_data():
  X, Y = [], []
  results = {'1/2-1/2': 0, '0-1': 1, '1-0': 1}  # determines who won
  games_parsed = 0

  for idx, data_file in enumerate(sorted(os.listdir(data_dir))[1:]):
    print("(%d/%d) Processing: %s"%(idx+1, len(os.listdir(data_dir))-1, data_file))
    pgn = open(os.path.join(data_dir, data_file))
    while 1:
      # TODO: file 13/27 crashes
      game = chess.pgn.read_game(pgn)

      if game is None:
        break

      games += 1

      res = game.headers['Result']
      if res not in results:
        continue

      winner = results[res]
      board = game.board()
      for i, move in enumerate(game.mainline_moves()):
        board.push(move)
        print(move)
        serialized_board = State(board).serialize()
        print(board)
        print(serialized_board)
        X.append(serialized_board)
        Y.append(winner)  # TODO: maybe Y can be the next move?
        exit(0)

  print("[+] %d Games Parsed"%games_parsed)
  return np.array(X), np.array(Y)



if __name__ == '__main__':
  get_data()

