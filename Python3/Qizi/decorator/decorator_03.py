from time import perf_counter


def test1():
    lst = []
    for _ in range(10000):
        lst.append("YorkFish")

    return None


def cal_time1(func):
    start = perf_counter()
    func()
    stop = perf_counter()
    print(">>> this function's run time is:", stop - start)

    return None


def cal_time2(func):
    def inn():
        start = perf_counter()
        func()
        stop = perf_counter()
        print(">>> this function's run time is:", stop - start)
    return inn


@cal_time2  # 有顺序，要写在 cal_time2() 下面
def test2():
    num = 0
    for i in range(10000):
        num += i

    return None


if __name__ == "__main__":
    cal_time1(test1)

    new_func = cal_time2(test1)
    new_func()

    test2()
