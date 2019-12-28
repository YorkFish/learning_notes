def say():
    print(">>> hello, I'm YorkFish.")


class Test1(object):
    pass


class Test2(object):
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        # __call__ 可以让实例对象能够像函数一样加小括号进行调用
        print(">>> Hello, I am YorkFish.")


if __name__ == "__main__":
    say()
    print(">>> callable(say)?:", callable(say))

    print(">>> callable(Test1)?:", callable(Test1))

    t1 = Test1()
    print(">>> callable(t1)?:", callable(t1))  # 实例对象不可调用

    t2 = Test2()
    print(">>> callable(t2)?:", callable(t2))
    t2()
