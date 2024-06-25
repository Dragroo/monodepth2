import torch
import torch.nn.functional as F

# dim=1 在行上寻找最大值 返回对应列的索引
input = torch.tensor([[6, 2, 7, 0], [8, 1, 3, 1], [4, 5, 9, 10]])
print(input)
values, indices = torch.max(input, dim=0)
print(values)
print(indices)

