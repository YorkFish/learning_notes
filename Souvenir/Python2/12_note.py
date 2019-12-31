# -*-coding:utf-8-*-

# 1. range
list1 = range(1, 10)
print list1  # 与 Python3 较为不同
print list1[2:8]

print len(list1)

# 2.
list2 = []
print list2

# 3.
for i in range(10):  # 通过 for 循环追加
    list2.append(i)
print list2

# 4.
list3 = [22, 33, 44]
print list3
print list3[0]

for i in range(3):
    print list3[i]

for i in range(len(list3)):
    print list3[i]

# 5.
print list3 * 3

print list2 + list3

list4 = list2 + list3
print list4

# 6.
print 33 in list3
if (33 in list3):  # 加不加括号都行，加了后看上去清楚
    pass

# 7. 添加
list3.append(55)  # 扩展 加单项
print list3

list1.append([66, 77])  # 加列表
print list1

list1 = [22, 33, 44, 55]
list1.extend([66, 77])  # 追加 加多个单项

# 8. 排序
list5 = [2, 4, 7, 1, 3, 9, 5, 8, 6, 0]
list5.sort()  # 顺序排序
list5.reverse()  # 倒序排序
list5.index(6)  # 索引 6 所在地位置

# 9. 插入
list5.insert(2, 20)  # 在索引为 2 的位置之前插入元素 20

# 10. 删除
print list5

del list5[4]  # 删除索引为 4 的元素
print list5

del list5[5:]  # 删除索引为 5 以及其后的所有元素
print list5

del list5[2:3]  # 删除索引为 [2, 3) 的元素，这里就是删除 list5[2]
print list5
