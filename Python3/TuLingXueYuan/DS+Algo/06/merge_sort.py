from random import randrange


def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst

    mid = n // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    '''合并操作，将两个有序数组 left[] 和 right[] 合并成一个大的有序数组'''
    L, R = 0, 0
    result = []
    nL, nR = len(left), len(right)
    while L < nL and R < nR:
        if left[L] < right[R]:
            result.append(left[L])
            L += 1
        else:
            result.append(right[R])
            R += 1
    if L < nL:
        result += left[L:]
    if R < nR:
        result += right[R:]
    return result


if __name__ == "__main__":
    lst = [randrange(10, 100) for _ in range(10)]

    print(">>> before sort:", lst)
    sorted_list = merge_sort(lst)
    print(">>> after sort: ", sorted_list)
