"""
两个魔法方法：__iadd__(), __add__()
  可变对象，如 list,  set 等，两个方法都有
不可变对象，如 tuple, int 等，只有 __add__()

+= 优先调用 __iadd__()，若没有，则调用 __add__()

__iadd__() 是由 extend 实现的
    def __iadd__(self, values):
        self.extend(values)
        return self
"""

# 1.
a1 = [1, 2]
b1 = (2, 3)
print(">>> id(a1) =", id(a1))
a1 += b1
print(">>> id(a1) =", id(a1))

# 2.
a2 = [1, 2]
b2 = (2, 3)
print(">>> id(a2) =", id(a2))
try:
    a2 = a2 + b2
except TypeError:
    print('can only concatenate list (not "tuple") to list')
