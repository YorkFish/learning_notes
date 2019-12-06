# coding:utf-8

import sys
from time import perf_counter_ns


def cal_time(func):
    def in_():
        start = perf_counter_ns()
        name = func()
        stop = perf_counter_ns()
        print(f">>> {name}'s cost times: {stop - start}\n")
    return in_


@cal_time
def solve1():
    for cocks in range(101):
        for hens in range(101):
            for chicks in range(301):
                if cocks + hens + chicks == 100 \
                        and 5*cocks + 3*hens + chicks/3 == 100:
                    print(f"公鸡 {cocks:>2} 只，母鸡 {hens:>2} 只，小鸡 {chicks} 只")
    return sys._getframe().f_code.co_name


@cal_time
def solve2():
    for cocks in range(20):
        for hens in range(33):
            chicks = 100 - cocks - hens
            if chicks % 3 == 0 and 5*cocks + 3*hens + chicks//3 == 100:
                print(f"公鸡 {cocks:>2} 只，母鸡 {hens:>2} 只，小鸡 {chicks} 只")
    return sys._getframe().f_code.co_name


if __name__ == "__main__":
    solve1()
    solve2()
