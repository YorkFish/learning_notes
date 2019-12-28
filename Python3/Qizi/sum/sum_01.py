# 1.
lst_a = [1, 2, 3, 4]
print(">>> sum(lst_a) =", sum(lst_a))
print(">>> sum(lst_a, 1) =", sum(lst_a, 1))

# 2.
lst_b = [[1, 2, 3]] * 3  # 注意，第二层是浅拷贝
print(">>> lst_b =", lst_b)

# 3.
"""
下面的列表生成式可以这样理解
lst = []
for k in lst_b:
    for i in k:
        lst.append(i)
print(lst)
"""
print(">>> lst =", [i for k in lst_b for i in k])

# 4.
# 一般的，能使用 + 操作的，都可以使用 sum()
# 当然，字符串除外，因为字符串不可迭代
print(">>> lst =", sum(lst_b, []))
