"""
不同类型的数值，只要大小相等，Python 就认为它们相等
"""

# 1.
num_a = 1
num_b = 1.0
print(">>> num_a == num_b?:", num_a == num_b)

# 2.
lst_a = [1, 2]
lst_b = [1.0, 2.0]
print(">>> lst_a == lst_b?:", lst_a == lst_b)

# 3.
t_a = (1, 2)
t_b = (1.0, 2.0)
print(">>> t_a == t_b?:", t_a == t_b)
