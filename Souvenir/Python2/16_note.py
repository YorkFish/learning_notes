# -*-coding:utf-8-*-

# 1.
list1 = ["aa", "bb", "cc", "dd"]
print list1

list1.append("ff")
print list1

list1.append("ee")
print list1

# 2.
print list1.pop()
print list1.pop()
print list1

for i in range(len(list1)):
    list1.pop()

print len(list1)
print list1

# 3.
list2 = ['a', 'f', 'g', 'e']
print list2

list2.append('b')
list2.append('k')
print list2

# 4.
print list2.pop(0)
print list2.pop(0)

# 5.
list3 = []
print list3
n = len(list2)
for i in range(n):
    list3.append(list2.pop(0))
    print list3
print list2
