from random import randrange


def binary_search_1(lst, item):
    first = 0
    last = len(lst) - 1
    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == item:
            return True
        elif item < lst[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


def binary_search_2(lst, item):
    n = len(lst)
    if n == 0:
        return False

    mid = n // 2
    if lst[mid] == item:
        return True
    elif item < lst[mid]:
        return binary_search_2(lst[:mid], item)
    else:
        return binary_search_2(lst[mid+1:], item)


if __name__ == "__main__":
    lst = [i+randrange(0, 5) for i in range(0, 100, 5)]
    r_num = randrange(0, 100)

    print("lst =", lst)
    print(f"binary_search_1(lst, {r_num}):", binary_search_1(lst, r_num))
    print(f"binary_search_2(lst, {r_num}):", binary_search_2(lst, r_num))
