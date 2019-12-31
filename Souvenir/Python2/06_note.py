# -*-coding:utf-8-*-

# 1. 排版
s = "Good of boy"  # 在一些 IDE 中，s. 后按 Tab 键可以查看所能用的方法
print s.rjust(20)  # 共 20 位，靠右输出，不够就用空格补全
print s.rjust(20, '*')  # 共 20 位，靠右输出，不够就用 * 补全

print s.ljust(20)  # 共 20 位，靠左输出，不够就用空格补全
print s.ljust(20, '*')  # 共 20 位，靠左输出，不够就用空格补全

print s.center(20)  # 居中输出
print s.center(20, '*')  # 居中输出，两边空格用 * 补全

print s.zfill(20)  # 靠右输出，用 0 填充空位

# 2. 索引
# 像 find()、index() 这样的函数默认是从左开始查找的，所以没有 s.lfind()、s.lindex() 这样的函数
print s.find("of")  # 找到 of 所在，取 o 的位置输出，若没有就输出 -1
print s.find("of", 1, 10)  # 在 1 到 10 之间查找 of
print s.rfind("of")  # 从右开始找

print s.index("of")  # 索引，如果找不到就报错
print s.rindex("of")  # 从右开始找

# 3. 计数
print s.count("of")  # 计数

# 4. 替换
print s.replace("of", "new")  # 替换

# 5. 除去边上的空格
print s.strip()  # 去除字符串两边的空格
print s.lstrip()  # 去除字符串左边的空格
print s.rstrip()  # 去除字符串右边的空格

# 6. Tab 换空格
print s.expandtabs()  # 将 Tab 换成等长的空格
