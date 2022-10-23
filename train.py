import torch
import numpy as np
from tqdm import trange

from util import *
from model import *
from data_proc import *

model_path = "models/pnet.pth"

def train(model, X_train, Y_train, X_test=None, Y_test=None):
  lr = 0.001
  epochs = 100
  BS = 128

  loss = nn.CrossEntropyLoss()
  optim = torch.optim.Adam(model.parameters(), lr=lr)

  for epoch in epochs:
    print("[+] Epoch", epoch+1)
    for i in (t := trange(0, len(X_train), BS)):
      X = torch.tensor(X_train).float().to(device)
      Y = torch.tensor(Y_train).float().to(device)

      optim.zero_grad()
      out = model(X)
      # TODO: write this

def eval():
  pass


if __name__ == '__main__':
  device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
  print(device)

  X_train, Y_train = get_data(1000)
  model = PolicyNet().to(device).train()
  train(model, X_train, Y_train)
  save_model(model, model_path)

