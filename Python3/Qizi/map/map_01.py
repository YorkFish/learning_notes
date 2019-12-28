"""
map -> 映射
"""

# 1. normal
lst_a = [1, 2, 3, 4, 5]
lst_b = []
for i in lst_a:
    lst_b.append(i**2)
print(">>> lst_b =", lst_b)

# 2. advance
# 2.1
def mul(num):
    return num ** 2

print(map(mul, lst_a))
print(">>> square every elements in lst_a:", list(map(mul, lst_a)))

# 2.2
print(">>>", list(map(lambda x: x * x, lst_a)))
