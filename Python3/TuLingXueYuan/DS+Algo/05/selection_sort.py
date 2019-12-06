from random import randrange


def selection_sort(lst):
    n = len(lst)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        if min_idx != i:
            lst[i], lst[min_idx] = lst[min_idx], lst[i]


if __name__ == "__main__":
    lst = [randrange(10, 100) for i in range(10)]

    print(">>> before sort:", lst)
    selection_sort(lst)
    print(">>> after sort: ", lst)
