# -*-coding:utf-8-*-

# 1.
list1 = [4, 3, 2, 5]
list1.sort()
print list1

# 2.
dict1 = {'a': "app", 'c': "cpp", 'b': "bpp"}
print dict1

print sorted(dict1.items(), key=lambda d: d[0])
print sorted(dict1.items(), key=lambda d: d[1])
print dict1

# 3.
sort_dict = sorted(dict1.items(), key=lambda d: d[0])
print sort_dict

# 4.
import copy

dict2 = {"aa": "apple", "bb": {"gg": "grape", 'b': "balana"}}
print dict2

dict3 = copy.deepcopy(dict2)
print dict3

dict3["bb"]['b'] = "good"
print dict3

dict4 = copy.copy(dict2)
print dict4

dict4["bb"]['b'] = "best"
print dict2
