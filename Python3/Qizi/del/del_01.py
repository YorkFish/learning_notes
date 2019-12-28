"""
del 不会去操作内存，它只是删除了变量（如下方的 lst_a）的引用
当某片内存空间没有引用的时候，该片空间会自动释放
"""

lst_a = [1, 2, 3]
lst_b = lst_a
print(">>> id(lst_a) =", id(lst_a))
print(">>> id(lst_b) =", id(lst_b))

del lst_a
print(">>> lst_b =", lst_b)
