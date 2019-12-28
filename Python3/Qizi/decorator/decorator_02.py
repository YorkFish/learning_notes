from time import perf_counter


def out(func):
    def inn():
        start = perf_counter()
        func()
        stop = perf_counter()
        print(">>> this function's run time is:", stop - start)
    return inn


def append_str1():
    lst = []
    for i in range(10000):
        lst.append("YorkFish")

    return None


# 装饰器就是在不改变函数原有功能且不改变原有代码逻辑下，增加函数的功能
@out
def append_str2():
    lst = []
    for i in range(10000):
        lst.append("YorkFish")

    return None


if __name__ == "__main__":
    # 1.
    func = out(append_str1)
    func()

    # 2.
    append_str2()
