# 1.
lst_a = ['a1', 'b1', 'c1']
lst_b = ['a2', 'b2', 'c2']
for a, b in zip(lst_a, lst_b):
    print(">>> a, b =", a, b)

# 2.
# 看着像木桶原理
lst_c = ['a3', 'b3', 'c3', 'd3', 'e3']
lst_d = ['a4', 'b4', 'c4']
for c, d in zip(lst_c, lst_d):
    print(">>> c, d =", c, d)
