"""
1. 字符串是不可变对象，每次使用 + 拼接，都会生成新对象
2. join() 会先计算结果所需的内存，然后一次性申请内存空间，再把每个字符串复制过去，
没有中间字符的生成（没有中间商赚差价）

=> join() 的效率较高
"""

# from time import clock  # 目前还能用，但官方推荐下面这种
from time import perf_counter

# 1.
s = ''
start1 = perf_counter()
for i in range(100000):
    s += 'a'
stop1 = perf_counter()
print(">>> '+=' run time is:", stop1 - start1)

# 2.
lst = []
for i in range(100000):
    lst.append('a')
start2 = perf_counter()
''.join(lst)
stop2 = perf_counter()
print(">>> 'join' run time is:", stop2 - start2)
