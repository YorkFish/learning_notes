# eval(expression, globals=None, locals=None)
str1 = "[[1, 2], [3, 4], [5, 6]]"
str2 = "{1:'a', 2:'b', 3:'c'}"
str3 = "([1, 2], (3, 4))"

# 没有必要使用 split(',') 进行还原
# 典型用途：可以将网络相应返回的数据包转化成 Python 的数据结构
print(str1)
print(str2)
print(str3)
