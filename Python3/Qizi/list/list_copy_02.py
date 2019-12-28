"""
简单但不完全地说：浅拷贝只能保证第一层
"""

from copy import deepcopy

# 1.1
lst_a = [1, 2, 3, [4, 5, 6]]
lst_b = lst_a.copy()
print(">>> id(lst_a) =", id(lst_a), "; lst_a =", lst_a)
print(">>> id(lst_b) =", id(lst_b), "; lst_b =", lst_b)

# 1.2
lst_a[1] = 22
print(">>> id(lst_a) =", id(lst_a), "; lst_a =", lst_a)
print(">>> id(lst_b) =", id(lst_b), "; lst_b =", lst_b)

# 1.3
lst_a[3].append(7)
print(">>> id(lst_a) =", id(lst_a), "; lst_a =", lst_a)
print(">>> id(lst_b) =", id(lst_b), "; lst_b =", lst_b)

# 2.1
print('-' * 70)
lst_c = deepcopy(lst_a)
print(">>> id(lst_a) =", id(lst_a), "; lst_a =", lst_a)
print(">>> id(lst_c) =", id(lst_c), "; lst_b =", lst_c)

# 2.2
lst_a[1] = 222
print(">>> id(lst_a) =", id(lst_a), "; lst_a =", lst_a)
print(">>> id(lst_b) =", id(lst_c), "; lst_b =", lst_c)

# 2.3
lst_a[3].append(8)
print(">>> id(lst_a) =", id(lst_a), "; lst_a =", lst_a)
print(">>> id(lst_b) =", id(lst_c), "; lst_b =", lst_c)
