# 1.
lst1 = ['a', 'c', 'c', 'b', 'a', 'd', 'a', 'b']
lst2 = list(set(lst1))
print(">>> lst2 =", lst2)

# 2.
print(">>> right answer:", sorted(list(set(lst1)),
                                  key=lambda x: lst1.index(x)))
print(">>> lst2 =", lst2)

# 3.
lst2.sort(key=lst1.index)
print(">>> lst2 =", lst2)
