"""
字符串、整型、浮点、布尔都是副本
list, dict 以及其他定义的 class 都是别名

记法：常量赋值产生副本，其他产生别名
"""

# 1.
a = b = 3
c = 3
print(a is b)
print(a is c)

# 2.
lst_a = lst_b = [1, 2, 3]
lst_c = [1, 2, 3]
print(lst_a is lst_b)
print(lst_a is lst_c)
