"""
sort() 属于 list
"""

lst_a = ["google", "runoob", "taobao", "facebook"]

# 1.
lst_a.sort()
print(">>> lst_a =", lst_a)

# 2.
lst_a.sort(reverse=True)
print(">>> lst_a =", lst_a)

# 3.
lst_a.sort(key=lambda x: x[1])
print(">>> lst_a =", lst_a)
