import torch

scalar = torch.tensor(7)
vector = torch.tensor([7, 7])
matrix = torch.tensor([[7, 8], [9, 10]])
tensor_3d = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

print("scalar:", scalar, "| ndim:", scalar.ndim, "| shape:", scalar.shape)
print("vector:", vector, "| ndim:", vector.ndim, "| shape:", vector.shape)
print("matrix:", matrix, "| ndim:", matrix.ndim, "| shape:", matrix.shape)
print("tensor_3d:", tensor_3d, "| ndim:", tensor_3d.ndim, "| shape:", tensor_3d.shape)
