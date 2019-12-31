# -*-coding:utf-8-*-

s1 = ' testof Good 110 of boy'
s2 = "python is good"
s3 = '''Person firewall software may warn
about the connection IDLE'''
s4 = """Person firewall software
may warn about the connection IDLE"""
s5 = 'hello'
s6 = '123456'
s7 = ' '
s8 = "GOOD"

# 1. split
print s1.split()  # 将 s1 中的词按空格分开并放入列表
print s1.split()[1]  # 将由 s1 变换得到的列表中的第 1 个元素输出

print s1.splitlines()  # 输出整行
print s3.splitlines()  # 输出两行，因为s3占两行

# 2. join
list1 = s2.split()
print list1
str1 = '+'
print str1.join(list1)  # python+is+good
print '-'.join(list1)  # python-is-good

# 3. 前缀与后缀
print s1.startswith(' ')  # True 以空格为前缀
print s1.startswith('oop')  # Flase 因为不是以 oop 开头，返回非

print s1.endswith('boy')  # True 以 boy 结尾
print s1.endswith('y')  # Ture 以 y 结尾
print s1.endswith('bo')  # False 因为不是以 bo 结尾，返回非

# 4. 判断字符串是否全由字母、数字组成
print s5.isalnum()  # True
print s6.isalnum()  # True

# 5. 判断字符串是否全是字母
print s5.isalpha()  # True
print s6.isalpha()  # False

# 6. 判断字符串是否全是数字
print s5.isdigit()  # False
print s6.isdigit()  # True

# 7. 判断字符串是否全是空格
print s6.isspace()  # False
print s7.isspace()  # True

# 8. 判断字符串是否全是小写
print s4.islower()  # False
print s5.islower()  # True

# 9. 判断字符串是否全是大写
print s1.isupper()  # False
print s8.isupper()  # True
