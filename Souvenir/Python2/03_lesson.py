# -*-coding:utf-8-*-


class adds(object):
    def __init__(self, values=0):
        self.values = values

    def __add__(self, other):
        return self.values + other


class minus(object):
    def __init__(self, v=0):
        self.va = v

    def __sub__(self, other):
        return self.va - other


if __name__ == "__main__":
    # 1.
    a = adds(9)
    aa = a + 3
    print aa

    # 2.
    m = minus(4)
    print m - 2
