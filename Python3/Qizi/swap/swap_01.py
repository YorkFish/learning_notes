a = 1
b = 2

# 1.
print(f"a = {a}, b = {b}")

# 2.
a = a + b
b = a - b
a = a - b
print(f"a = {a}, b = {b}")

# 3. 这个比 2. 安全
a = a ^ b
b = a ^ b
a = a ^ b
print(f"a = {a}, b = {b}")

# 4.
# golang 也有
a, b = b, a
print(f"a = {a}, b = {b}")
