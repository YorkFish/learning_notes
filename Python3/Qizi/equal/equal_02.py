"""
dict 通过检查键值和哈希来确定两个键是否相同
若有相等的键，键取最前面的，值取最后面的
"""

# 1.
dic1 = {1:'a', 1.0:'b'}
dic2 = {1.0:'a', 1:'b'}
print(">>> dic1:", dic1)
print(">>> dic2:", dic2)

# 2.
print(">>> hash(1) =", hash(1))
print(">>> hash(1.0) =", hash(1.0))
