lst = [1, 2, 3, 4, 5]

# 1.
for i in lst:
    if i == 3:
        print("found it!")
        break
else:
    print("not found!")

# 2.
for i in lst:
    if i == 6:
        print("found it!")
        break
else:
    print("not found!")
