def func():
    global a
    a = 2
    print(">>> a =", a)


def func1():
    n = 1
    def func2():
        nonlocal n  # don't use "global n" in this
        n *= 2
    print(">>> n =", n)
    func2()
    print(">>> n =", n)


if __name__ == "__main__":
    # 1.
    a = 1
    func()
    print("<<< a =", a)

    # 2.
    func1()
