import torch
import numpy as np
from tqdm import trange

from util import *
from model import *
from data_proc import *

model_path = "models/pnet.pth"

def train(model, X_train, Y_train, X_test=None, Y_test=None):
  pass

def eval():
  pass


if __name__ == '__main__':
  device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
  print(device)

  X_train, Y_train = get_data(1000)
  model = PolicyNet().to(device).train()
  train(model, X_train, Y_train)
  save_model(model, model_path)

