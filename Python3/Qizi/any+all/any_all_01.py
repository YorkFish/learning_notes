"""
any(), all() 都是用来判断可迭代对象的
简单地说，
  any() 是有人 True，那就 True
  all() 是大家 True，才是 True
"""

# 1. any()
# 只要有 0, '', False, None, [], (), {}, set() 以外的元素，就返回 True
print(">>> any([0, '', False, None, [], (), {}, set()])) =",
      any([0, '', False, None, [], (), {}, set()]))
print(">>> any([0, '', 1]) =", any([0, '', 1]))
print(">>> any([]) =", any([]))  # [], (), {}, set() 都返回 False

# 2. all()
# 只有所有元素都在 0, '', False, None, [], (), {}, set() 之外，才返回 True
# 换句话说，元素中没有 0, '', False, None, [], (), {}, set()，才返回 True
print(">>> all(('a', '', 'b')) =", all(('a', '', 'b')))
print(">>> all(()) =", all(()))  # [], (), {}, set() 都返回 True
print(">>> all([1]) =", all([1]))
print(">>> all([1, None]) =", all([1, None]))
