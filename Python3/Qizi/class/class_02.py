class Hero(object):
    # 类变量
    game_name = "LOL"


if __name__ == "__main__":
    lijing = Hero()
    print(lijing.game_name)

    lijing.game_name = "DNF"
    print(lijing.game_name)

    del lijing.game_name
    print(lijing.game_name)
