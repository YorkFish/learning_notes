# -*-coding:utf-8-*-

s2 = "python is good"
s5 = "	hello"  # hello 前加了 Tab 键
s8 = "GOOD"

# 1. 大写与小写
print s2.upper()  # 将字符串改为大写
print s2.isupper()  # False 判断字符串是否都为大写
print s2.upper().isupper()  # True 改为大写后判断是否为大写

if s2.islower():
    print "good"  # V
else:
    print "bad"

# 2. 标题化 of 之类的词也会被更改
print s2.title()  # 将字符串每个单词首字母改为大写
print s2.istitle()  # False 判断字符串每个首字母是否为大写

# 3. 计数
print s2.count('o')  # 计算字符串中有多少个o

# 4. 首字母大写
print s2.capitalize()  # Python is good

# 5. 前面会输出一个制表符长度
print s5
print s5.expandtabs()

# 6. 转换函数
print s8.repalce('O', 'o')  # GooD

# 7. 切片
print s8[0]  # G
print s8[0:3]  # GOO
print s8[:]  # GOOD
