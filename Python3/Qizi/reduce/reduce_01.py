"""
reduce -> 规约
可以使各元素按顺序进行计算，每次计算结果会参与到下次计算中
"""

from functools import reduce


def mul(x1, x2):
    return x1 * x2


if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    print(reduce(mul, lst))  # f(f(f(1, 2), 3), 4)
