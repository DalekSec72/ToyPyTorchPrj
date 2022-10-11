# -*- coding: utf-8 -*-

# Taehun Kim <th6424@gmail.com>, 2022


import torch


def describe(x):
    print(f"type: {x.type()}")
    print(f"shape: {x.shape}")
    print(f"value: {x}")

def problem_1():
    return torch.Tensor(3, 3).unsqueeze(0)

def problem_2():
    return problem_1().squeeze(0)

def problem_3():
    return torch.rand(5, 3) * (7 - 3)

def problem_4():
    return torch.rand(5, 3).normal_()

def problem_5():
    return torch.nonzero(torch.Tensor([1, 1, 1, 0, 1]))

def problem_6():
    return torch.rand(3, 1).expand(-1, 4)

def problem_7():
    # bmm((3, 4, 5) , (3, 5, 4)) -> (3, 4, 4)
    a = torch.rand(3, 4, 5)
    b = torch.rand(3, 5, 4)

    return torch.bmm(a, b)

def problem_8():
    a = torch.rand(3, 4, 5)
    b = torch.rand(5, 4)

    return torch.matmul(a, b)


if __name__ == "__main__":
    for i in range(1, 9):
        print(f"===== problem {i} =====")
        describe(locals()[f"problem_{i}"]())
        print()

