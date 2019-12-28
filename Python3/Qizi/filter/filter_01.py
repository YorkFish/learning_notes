# 1. normal
lst_a = [1, 2, 3, 4, 5, 6, 7, 8]
lst_b = []
for i in lst_a:
    if i % 2 == 0:
        lst_b.append(i)
print(">>> lst_b =", lst_b)

# 2. advance
lst_c = filter(lambda x: x % 2 == 0, lst_a)
print(">>> lst_c =", list(lst_c))
