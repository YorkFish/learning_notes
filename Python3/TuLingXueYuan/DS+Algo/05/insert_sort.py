from random import randrange


def insert_sort(lst):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break


if __name__ == "__main__":
    lst = [randrange(10, 100) for i in range(10)]

    print(">>> before sort:", lst)
    insert_sort(lst)
    print(">>> after sort: ", lst)
