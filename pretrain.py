#!/usr/bin/env python3
import chess
import chess.pgn
import numpy as np
from tqdm.notebook import trange
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot

import torch
import torch.nn as nn
import torch.functional as F
from torch.utils.tensorboard import SummaryWriter

from util import *
from data_proc import *
from model import *


def train(model, X_train, Y_train, X_test=None, Y_test=None, writer=None):
  model.train()
  
  lr = 1e-3
  epochs = 100
  BS = 512

  losses, accuracies = [], []

  loss_func = nn.MSELoss()  # find a better loss (output is in [-1,1])
  optim = torch.optim.Adam(model.parameters(), lr=lr)

  for epoch in range(epochs):
    print("[+] Epoch", epoch+1)
    epoch_losses = []
    for i in (t := trange(0, len(X_train), BS)):
      X = torch.tensor(X_train[i:i+BS]).float().to(device)
      Y = torch.tensor(Y_train[i:i+BS]).float().to(device)

      optim.zero_grad()
      out = model(X)
      loss = loss_func(out, Y).mean()
      loss.backward()
      optim.step()

      # TODO: evaluate after each epoch
      writer.add_scalar('training loss', loss.item()/1000, epoch*len(X_train)+i)
      epoch_losses.append(loss.item())
      t.set_description("loss %.2f"%(loss))
      
    avg_loss = np.array(epoch_losses).mean()
    print("[~] Avg Epoch Loss %.2f"%(avg_loss))
    losses.append(avg_loss)

  print("[+] Training Done!")
  plt.plot(losses)
  plt.show()

def eval(model, X_test, Y_test):
  model.eval()


if __name__ == '__main__':
  device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
  print(device)

  data_path = "data/preprocessed/full_dataset.npz"
  model_path = "models/chess_model.pth"
  writer = SummaryWriter("tensorboard_runs/pretrain_exp1")

  data = np.load(data_path)
  X_train, Yt = data.f.arr_0, data.f.arr_1

  Y_train = []
  for y in Yt:
    Y_train.append([y])
  Y_train = np.array(Y_train)

  print(X_train.shape)
  print(Y_train.shape)
  print(X_train)
  print(Y_train)


  model = ValueNet(X_train.shape[1], 1).to(device)
  print(model)

  train(model, X_train, Y_train, writer=writer)
  save_model(model, model_path)

