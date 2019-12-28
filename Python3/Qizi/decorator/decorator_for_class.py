def deco(clss):
    clss.x = 1
    clss.y = 2

    return clss


@deco
class Person(object):
    pass


if __name__ == "__main__":
    print(Person.__dict__)
