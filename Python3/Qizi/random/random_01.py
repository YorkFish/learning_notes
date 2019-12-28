import random

# 1.
print(">>> random():", random.random())  # [0, 1.0)
print(">>> randint(1, 10):", random.randint(1, 10))  # [1, 10], randint 其实是调用 randrange
print(">>> randrange(1, 10):", random.randrange(1, 10))  # [1, 10)
print(">>> uniform(1, 10):", random.uniform(1, 10))  # [1.0, 10.0)

# 2.
menus = ["蛋炒饭", "黄焖鸡米饭", "牛肉盖浇饭", "煲仔饭"]
print(">>> what to have for lunch:", random.choice(menus))
print(">>> what to have for dinner:", random.choices(menus, [1, 2, 3, 4]))  # choices 多了个 s
print(">>> what to have for dinner:", random.choices(menus, [1, 2, 3, 4], k=2))  # 加权，k= 需要写全

# 3.
print(">>> sample:", random.sample(menus, k=2))
print(">>> sample:", random.sample(menus, 2))  # k= 可以不写
