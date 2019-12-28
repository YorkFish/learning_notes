"""
1. 可以使属性变量私有，不会被派生类去继承，仅自己可以使用
2. 可以避免派生类和父类属性名称的冲突
3. 如果类内的方法也加上了前置双下划线，那么它也无法在外部用“实例.方法名”访问
"""

class Hero:
    def __init__(self, name, chinesename):
        self.name = name
        self.__chinesename = chinesename

    def __flash(self):
        print("F!")


if __name__ == "__main__":
    garen = Hero("garen", "盖伦")

    # 1.
    print(garen.name)
    print(dir(garen))

    # 2.1
    try:
        print(garen.__chinesename)
    except AttributeError as e:
        print(e)

    # 2.2
    print(garen._Hero__chinesename)

    # 3.
    try:
        garen.__flash()
    except AttributeError as e:
        print(e)
