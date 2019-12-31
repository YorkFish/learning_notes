# -*-coding:utf-8-*-

import string

# 1. string -> int, base 默认为 10
print string.atoi("123", base=10)  # 将十进制的 123 以十进制输出
print string.atoi("123", base=8)  # 将八进制的 123 以十进制输出
print string.atoi("123", base=16)  # 将十六进制的 123 以十进制输出

# 2. string -> long, base 默认为 10
# 除了数据类型，其余类似 string.atoi
print string.atol("123", base=10)  # 123L
print string.atol("123", base=8)
print string.atol("123", base=16)

# 3. string -> float, base 默认为 10
# 除了数据类型，其余类似 string.atoi
print string.atof("123")  # 123.0

# 4. 回车
t = "hi \npython"
print t

# 5. 制表符
tt = "hello \tworld"
print tt

# 6. 转义符
## 6.1
road1 = "c:\\python"  # \
print road1

road2 = r"c:\python"
print road2

## 6.2
s1 = 'let\' go'  # '
print s1

s2 = "let\" go"  # "
print s2

## 6.3 单双引号搭配
s3 = 'let"s go'
print s3

s4 = "let's go"
print s4

# 7. format
str1 = "I am %s!"
print str1 % "boy"  # I am boy!

str2 = "1 %c 1 %c %d"
print str2 % ('+', '=', 2)

str3 = "my age is %d"
print str3 % 99  # my age is 99

str4 = "the e of %e"
print str4 % 123456789  # the e of 1.234568e+08

str5 = "the f of %f"
print str5 % 12345  # the f of 12345.000000

str6 = "the l of %d"
print str6 % 123456789L  # the l of 123456789

dict1 = {"name": "test", "age": 55}
print "my name is %(name)s, and the age is %(age)d" % dict1
