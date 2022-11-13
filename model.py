import torch
import torch.nn as nn
import torch.nn.functional as F

class ValueNet(nn.Module):
  def __init__(self, in_len, out_len):
    super(ValueNet, self).__init__()
    
    self.relu = nn.ReLU()
    
    self.fc1 = nn.Linear(in_len, 128)
    self.bn1 = nn.BatchNorm1d(128)
    self.fc2 = nn.Linear(128, 128)
    self.bn2 = nn.BatchNorm1d(128)
    self.fc3 = nn.Linear(128, out_len)

  def forward(self, x):
    x = self.relu(self.bn1(self.fc1(x)))
    x = self.relu(self.bn2(self.fc2(x)))
    x = torch.tanh(self.fc3(x))
    return x

def save_model(model, path):
  torch.save(model.state_dict(), path)
  print("[+] Model saved at:", path)

def load_model(model, path, val=False):
  model.load_state_dict(torch.load_state_dict(torch.load(path)))
  if val:
    model.eval()
  else:
    model.train()
  print("[+] Loaded model from:", path)

