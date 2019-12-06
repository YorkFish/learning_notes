from random import randrange


def quick_sort(lst):
    """ this is not real quick sort """
    n = len(lst)
    if n <= 1:
        return lst

    pivot = lst[-1]
    front, rear = [], []
    for i in range(n-1):
        if lst[i] < pivot:
            front.append(lst[i])
        else:
            rear.append(lst[i])
    return quick_sort(front) + [pivot] + quick_sort(rear)


if __name__ == "__main__":
    lst = [randrange(10, 100) for _ in range(10)]

    print(">>> before sort:", lst)
    new_list = quick_sort(lst)
    print(">>> after sort: ", new_list)
