# 1.
lst_a = [1, 2, 3]
lst_b = lst_a
print(">>> id(lst_a) =", id(lst_a), "; lst_a =", lst_a)
print(">>> id(lst_b) =", id(lst_b), "; lst_b =", lst_b)

# 2.
lst_a[1] = 22
print(">>> id(lst_a) =", id(lst_a), "; lst_a =", lst_a)
print(">>> id(lst_b) =", id(lst_b), "; lst_b =", lst_b)

# 3.
lst_a = [4, 5, 6]
print(">>> id(lst_a) =", id(lst_a), "; lst_a =", lst_a)  # *
print(">>> id(lst_b) =", id(lst_b), "; lst_b =", lst_b)
