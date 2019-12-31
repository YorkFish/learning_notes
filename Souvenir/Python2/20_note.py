# -*-coding:utf-8-*-

# 1.
dict1 = {'a': "aaa", 'b': "bbb", 'c': "ccc"}
print dict1

# 2.
if 'a' in dict1.keys():
    print dict1['a']

print dict1.values()

if "aaa" in dict1.values():
    print "The values of aaa is exist."

# 3.
print dict1['b']
print dict1.get('b')
print dict1.get('c', "ddd")
print dict1.get('d', "ddd")

# 4.
dict2 = {"aa": "hehe", "bb": "haha"}
print dict2

dict1.update(dict2)
print dict1

# 5.
dict3 = {"cc":"good", "dd":"best"}
print dict3

for k in dict3:
    dict2[k] = dict3[k]
print dict2

# 6.
dict4 = {}
print dict4

dict4.setdefault('k')
print dict4

dict4['k'] = "happy"
print dict4

print dict4.setdefault('s',"apple")
print dict4
