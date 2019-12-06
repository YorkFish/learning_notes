from random import randrange


def bubble_sort(lst):
    for j in range(len(lst)-1, 0, -1):
        for i in range(j):
            if lst[i+1] < lst[i]:
                lst[i+1], lst[i] = lst[i], lst[i+1]


if __name__ == "__main__":
    lst = [randrange(10, 100) for i in range(10)]

    print(">>> before sort:", lst)
    bubble_sort(lst)
    print(">>> after sort: ", lst)
