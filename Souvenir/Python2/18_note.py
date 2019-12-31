# -*-coding:utf-8-*-

# 1.
dict1 = {}
print dict1

dict1[1] = "apple"
print dict1

dict1[2] = "orange"
print dict1

dict1[3] = "grape"
print dict1

# 2.
dict1['a'] = "aa"
print dict1

# dict1[b] = "bb"  # 报错

# 3.
dict1['A'] = "bb"  # 排序有一定规律，按照哈希 code 排
dict1['a'] = "cc"
dict1['b'] = "DD"

print dict1['a']
print "the dict1 is:", (dict1)

# 4.
del dict1[1]
del dict1[2]
del dict1[3]

print dict1
print "the dict of value is %(a)s, %(b)s" % {'a': "aa", 'b': "bb"}
