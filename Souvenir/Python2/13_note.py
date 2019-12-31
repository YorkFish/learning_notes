# -*-coding:utf-8-*-

# 1.
list1 = [2, 4, 6, 2, 5, 9, 8, 7, 3, 2]
print list1.count(2)
print list1.count(11)

# 2.
ls = list1[:]
print ls

list1.remove(2)  # 删除最前面的一个 2，若没有 2 可以删除，就报错
print list1

# 3.
list1.pop(2)  # 删除索引为 2 的元素
print list1

list1.pop()  # 删除最后一个位置上的元素
print list1

# 4.
# list1[1:2] = 55  # 报错

list1[1:2] = [55]  # 将 [1, 2) 之间的元素换为 55

list1[1:3] = [66, 88]
print list1

# 5.
for i in range(len(list1)):
    print i
    print list1.pop()

print list1

# 6.
list1 = [4, 66, 88, 8, 7, 3]
i = 0
while i < len(list1):
        print i
        print list1.pop()
print list1

# 7.
list1 = [3, 4, 5, 6]
list1[1:3] = []
print list1
