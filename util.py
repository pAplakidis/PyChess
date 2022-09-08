import chess
import numpy as np

class State:
  def __init__(self, board=None):
    if board is None:
      self.board = chess.Board()
    else:
      self.board = board

  def serialize(self):
    serialized_board = np.zeros(64, np.uint8)
    values = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6, \
              "p": 9, "n":10, "b":11, "r":12, "q":13, "k": 14}

    for i in range(64):
      piece = self.board.piece_at(i)
      if piece is not None:
        serialized_board[i] = values[piece.symbol()]
        # TODO: handle special stuff (castling and en passaint)

    return serialized_board

  def edges(self):
    return list(self.board.legal_moves)
