"""
Python 中的变量的查找思想：先局部，后全局，最后内置
可以了解一下 getatt
"""

# eval(expression, globals=None, locals=None)
# 1.
a = 1
ret = eval("a+1", {'a': 2})
print(">>> ret =", ret)

# 2.
b = 1
ret = eval("b+1", {'b': 2}, {'b': 3})
print(">>> ret =", ret)
