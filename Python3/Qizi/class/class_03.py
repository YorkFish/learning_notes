class Hero(object):
    # 类变量
    game_name = "LOL"

    def __init__(self, name):
        # 实例变量，由每个对象自行赋值，互不影响
        self.name = name


if __name__ == "__main__":
    lijing = Hero("Lijing")
    print(lijing.game_name)
    print(lijing.name)

    garen = Hero("Garen")
    print(garen.game_name)
    print(garen.name)
