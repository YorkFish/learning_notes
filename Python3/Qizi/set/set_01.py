"""
intersection, union set, difference set

tips: 有时候，对于列表，可以先 set(list)，再用上面的“交、并、差”
"""

set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(">>> set_a & set_b =", set_a & set_b)  # 交集
print(">>> set_a | set_b =", set_a | set_b)  # 并集
print(">>> set_a - set_b =", set_a - set_b)  # 差集
print(">>> set_a ^ set_b =", set_a ^ set_b)  # 对称差集
