from time import perf_counter_ns


def cal_time1(func):
    def inn():
        start = perf_counter_ns()
        func()
        stop = perf_counter_ns()
        print(">>> this function's run time is:", stop - start)
    return inn


@cal_time1
def app():
    lst = []
    for _ in range(10000):
        lst.append("YorkFish")
    print(">>> app is finished.")

    return None


def cal_time2(func):
    def inn(x, y):
        start = perf_counter_ns()
        func(x, y)
        stop = perf_counter_ns()
        print(">>> this function's run time is:", stop - start)
    return inn


@cal_time2
def add(x, y):
    print(x + y)

    return None


if __name__ == "__main__":
    app()
    add(1, 9)
