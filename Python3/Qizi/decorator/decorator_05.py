from time import perf_counter_ns


def cal_time1(func):
    def inn(*args):
        print(">>> args =", args)
        start = perf_counter_ns()
        func(*args)
        stop = perf_counter_ns()
        print(">>> this function's run time is:", stop - start)
    return inn


@cal_time1
def add1(*args):
    print(">>> sum(args) =", sum(args))

    return None


def out(num):
    print(">> num =", num)
    def cal_time2(func):
        print(">>>> func =", func)
        def inn(*args):
            print(">>>>>> args =", args)
            start = perf_counter_ns()
            func(*args)
            stop = perf_counter_ns()
            print(">>> this function's run time is:", stop - start)
        return inn
    return cal_time2


@out(0)
def add2(*args):
    print(">>> sum(args) =", sum(args))

    return None


if __name__ == "__main__":
    add1(1, 9)
    print('-' * 40)
    add2(1,2,3)
