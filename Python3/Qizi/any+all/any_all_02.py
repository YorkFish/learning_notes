"""
By default, an object is considered true unless its class defines
either a __bool__() method that returns False or a __len__() method that returns zero
上面这段可以用 if xxx: print('y') 判断，或者写个函数

用途：any(f(i) for i in mylist)
"""

def test(elements):
    lst = []
    for element in elements:
        lst.append(True if element else False)
    return lst


if __name__ == "__main__":
    lst = [0, '', False, None, [], (), {}, set()]
    print(list(map(lambda x: True if x else False, lst)))
    print(test(lst))
