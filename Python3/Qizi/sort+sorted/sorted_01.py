"""
sorted() 是 Python 的内置函数，不隶属于某种数据类型
sorted() 可以对所有的可迭代对象进行排序
"""

dic = {"Lily": 25, "John": 22, "Mary": 19}
print(sorted(dic.values()))
print(sorted(dic.items(), key=lambda x: x[0], reverse=True))  # 按字典的键排序
print(sorted(dic.items(), key=lambda x: x[1]))  # 按字典的值排序
