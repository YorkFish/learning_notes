def add_two(x, y):
    res = x + y
    print(f">>> {x} + {y} = {res}")

    return res


def tmp1(x, y, func):
    func(x, y)

    return None


def tmp2(x, y):
    def two_sum():
        print(f">>> {x} + {y} = {x + y}")
    return two_sum  # 其实就是“函数指针”


if __name__ == "__main__":
    # 1.
    print(">>> 2 * add_two(1, 2) =", 2 * add_two(1, 2))

    # 2.
    new_func = add_two
    print(">>> new_func is add_two:", new_func is add_two)
    new_func(3, 4)

    # 3.
    tmp1(5, 6, add_two)

    # 4.
    tmp2(7, 8)()
