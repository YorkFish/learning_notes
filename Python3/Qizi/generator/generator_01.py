def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b  # 相当于挂起；可以看成一种不退出的 return
        a, b = b, a+b
        n += 1


if __name__ == "__main__":
    # 1.
    lst = [x*x for x in range(10)]
    print(">>> lst =", lst)

    # 2.
    y1 = fib(10)
    for i in y1:
        print(i, end=' ')
    print()

    # 3.
    y2 = fib(10)
    try:
        n = next(y2)
        while n:
            print(n, end=' ')
            n = next(y2)
    except StopIteration:
        print("\nover")
