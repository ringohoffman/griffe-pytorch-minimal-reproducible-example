import torch

linear = torch.nn.Linear(5, 3)

torch.save(linear, "state_dict.pth")
