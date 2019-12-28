"""
并不能真正像 C, Java 那样对函数的参数类型进行严格定义
因为 Python 的变量是动态的
"""


def flash1(name, status):
    if status:
        print(f"{name} is used flash!")
    else:
        print(f"{name} keeps big move!")


def flash2(name: str, status: bool)->int:
    res = 0
    if status:
        print(f"{name} is used flash!")
        res = 1
    else:
        print(f"{name} keeps big move!")

    return res


if __name__ == "__main__":
    name = "yasuo"
    status = True

    res = flash2(name, status)
    print(">>> res =", res)
