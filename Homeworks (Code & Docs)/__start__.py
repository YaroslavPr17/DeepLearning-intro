import torch
print("Your CUDAs are available! Good luck :)" if torch.cuda.is_available() else "Only CPU now")