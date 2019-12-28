"""
variable object and unvariable object

i =  5      i += 2
i -> 5      i --     5 -> Garbage collection
                |
                 --> 7
以上这种是不可变对象！
常见的不可变对象有：str, int, float, complex, tuple, bool

lst = [0, 1, 2, 3]
lst[0] = 10
上面这一步操作是在原内存地址修改，没有创建新对象
常见的可变对象有：list, dict, set
"""
