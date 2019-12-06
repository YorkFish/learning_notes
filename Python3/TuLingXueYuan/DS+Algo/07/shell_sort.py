from random import randrange


def shell_sort1(lst):
    cnt = 0
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n, gap):
            cnt += 1
            j = i
            while gap <= j and lst[j] < lst[j-gap]:
                lst[j], lst[j-gap] = lst[j-gap], lst[j]
                j -= gap
        gap //= 2
    print(">>> cnt =", cnt)


def shell_sort2(lst):
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n, gap):
            while gap <= i and lst[i] < lst[i-gap]:
                lst[i], lst[i-gap] = lst[i-gap], lst[i]
                i -= gap
        gap //= 2


if __name__ == "__main__":
    lst = [randrange(10, 100) for _ in range(10)]

    print(">>> before sort:", lst)
    shell_sort1(lst)
    shell_sort2(lst)
    print(">>> after sort :", lst)
