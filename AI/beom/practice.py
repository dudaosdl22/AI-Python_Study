import torch
print(torch.__version__)
# x = torch.empty(4, 2)
# x = torch.rand(4, 2)
x = torch.zeros(4, 2, dtype=torch.long)
print(x)