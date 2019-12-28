"""
array 不常用
numpy 的 ndarray 比较常用
"""

from array import array


# 1.
arr = array('q', (100, 200, 300))
print(arr)

# 2.
arr[0] = 101
arr[1] = 201
arr[2] = 301
print(arr)
