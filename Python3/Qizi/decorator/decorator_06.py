def deco1(func):
    print(">> run decorator1")
    def in_():
        print(">>>> decorator1's in")
        func()
    return in_


def deco2(func):
    print(">> run decorator2")
    def in_():
        print(">>>> decorator2's in")
        func()
    return in_


@deco2  # 西装
@deco1  # 衬衫
def main():
    print(">>> run main")

    return None


if __name__ == "__main__":
    # 装饰的过程：先执行 deco1，再执行 deco2
    # 调用的过程：先调用 deco2，再调用 deco1
    # 穿衣：先衬衫，再西装
    # 脱衣：先西装，后衬衫
    main()
