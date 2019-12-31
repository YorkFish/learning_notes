# -*-coding:utf-8-*-

# 1.
print ord('c')  # 查看 'c' 的 ASCII 码

# 2.
list1 = []
print list1

for i in "happy":
    list1.append(ord(i))
    print list1
print list1

# 3.
list2 = [ord(x) for x in "happy"]
print list2

# 4.
id1 = [x for x in range(10)]
print id1
print len(id1)

# 5.
id2 = [x for x in range(50) if x%2 == 1]  # 输出 50 以内的单数
print id2

print [x**2 for x in range(10)]

id3 = [x+y for x in range(3) for y in range(3)]
print id3

# 6.
lst1 = [x+y for x in "good" for y in "best"]
print lst1

lst2 = [(x, y) for x in range(4) for y in range(3)]
print lst2

lst3 = [(x, y) for x in "good" for y in "best"]
print lst3

lst4 = [x+m for x in [1, 2, 3] for m in [100, 200, 300]]
print lst4
