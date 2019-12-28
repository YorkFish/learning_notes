"""
输出的时候不能更改下划线的位置
    十进制默认隔 3 位
    其他进制默认隔 4 位
"""

# 1.
num1 = 1_000_000
print("num1 =", num1)

# 2.
num2 = 0xFF_FF
print("num2 = %x" % num2)

# 3.
num3 = 1000000
print("num3_decimal     = {:_}".format(num3))
print("num3_binary      = {:_b}".format(num3))
print("num3_octal       = {:_o}".format(num3))
print("num3_hexadecimal = {:_x}".format(num3))
print("num3_hexadecimal = {:_X}".format(num3))

