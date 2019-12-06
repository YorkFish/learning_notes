from random import randrange


def quick_sort(lst, start, stop):
    if stop <= start:
        return

    mid = lst[start]
    low, high = start, stop
    while low < high:
        while low < high and mid <= lst[high]:
            high -= 1
        lst[low] = lst[high]

        while low < high and lst[low] < mid:
            low += 1
        lst[high] = lst[low]

    lst[low] = mid
    quick_sort(lst, start, low-1)
    quick_sort(lst, low+1, stop)


def quick_sort2(lst, start, stop):
    if stop <= start:
        return

    pivot = lst[stop]
    low, high = start, stop
    while low < high:
        while low < high and lst[low] < pivot:
            low += 1
        lst[high] = lst[low]

        while low < high and pivot <= lst[high]:
            high -= 1
        lst[low] = lst[high]

    lst[low] = pivot
    quick_sort(lst, start, low-1)
    quick_sort(lst, low+1, stop)


if __name__ == "__main__":
    lst = [randrange(10, 100) for _ in range(10)]

    print(">>> before sort:", lst)
    # quick_sort1(lst, 0, len(lst)-1)
    quick_sort2(lst, 0, len(lst)-1)
    print(">>> after sort: ", lst)
