"""
参数为不可变对象，如 int, str, tuple 等时，采用的是“值传递”，相当于用形参接收参数（不影响原值）
参数为可变对象，如 list, dict 等时，采用的是“引用传递”，相当于用指针接收参数（影响原值）
"""

def func1(num):
    num -= 1
    print(">>> num =", num)
    return None


def func2(lst):
    lst[0] = 10
    print(">>> lst =", lst)
    return None


if __name__ == '__main__':
    # 1.
    num = 10
    print("before:", num)
    func1(num)
    print("after:", num)

    # 2.
    print('-' * 30)
    lst = [1, 2, 3]
    print("before:", lst)
    func2(lst)
    print("after:", lst)
