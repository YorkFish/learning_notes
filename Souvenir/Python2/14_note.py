# -*-coding:utf-8-*-

# 1.
m = [
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
]
print type(m)
print m
print m[0]
print m[0][0]
print m[0][1]
print m[2]

# 2.
size = len(m)
for i in range(size):
    for j in range(size):
            print m[i][j]

# 3.
ok = []
for i in range(size):
    for j in range(size):
        e = m[i][j] + 100
        ok.append(e)
        print ok
print ok

# 4.
n = [('tom', 44, 1.7), ('jim', 55, 1.8)]
print n

for (name, age, high) in n:
    print age

for (name, age, high) in n:
    print "the name is:", name
