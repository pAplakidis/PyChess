#!/usr/bin/env python3
import chess.pgn

if __name__ == '__main__':
  pgn = open("data/KingBase2018/KingBase2018-01.pgn")
  first_game = chess.pgn.read_game(pgn)
  second_game = chess.pgn.read_game(pgn)

  print("Parsing: ", first_game.headers["Event"])
  board = first_game.board()
  print(board)
  print()
  for move in first_game.mainline_moves():
    board.push(move)
    print(board)
    print()

