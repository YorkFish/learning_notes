# -*-coding:utf-8-*-

# 1.
dict1 = {'a': "app", 'b': "bpp", 'k': "kpp", 'd': "dpp"}
print dict1
print dict1['k']

del dict1['k']
print dict1

# 2.
print dict1.pop('d')
print dict1

# 3.
dict1.clear()
print dict1

# 4.
dict1 = {'a': "app", 'b': "bpp", 'k' :"kpp", 'd' :"dpp"}
print dict1

for k in dict1:
    print "dict1[%c] = %s" % (k, dict1[k])

# 5.
print dict1.items()

for (k,v) in dict1.items():
    print "dict1[%c] = %s" % (k, v)

for (k,v) in zip(dict1.iterkeys(), dict1.itervalues()):
    print "dict1[%c] = %s" % (k, v)

# 6.
dict2 = {'a': "aa", 'b': ("apple", "orange"), 'c': {'d': "dd", 'f': "ff"}}
print dict2
print dict2['c']['d']
print dict2['b'][0]
print dict2['b'][1]
