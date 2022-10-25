import torch
import torch.nn as nn
import torch.nn.functional as F

# TODO: write this (output tensor of single value from tanh)
class ValueNet(nn.Module):
  def __init__(self):
    super(PolicyNet, self).__init__()

  def forward(x):
    return x

def save_model(model, path):
  torch.save(model.state_dict(), path)
  print("Model saved at:", path)

def load_model(model, path, val=False)
  model.load_state_dict(torch.load(path))
  if val:
    model.eval()
  else:
    model.train()
  print("Loaded model from:", path)

