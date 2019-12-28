class Hero(object):
    # 类变量
    game_name = "LOL"

    def __init__(self, name):
        # 实例变量，由每个对象自行赋值，互不影响
        self.name = name

    # 实例方法
    def flash(self):
        # 局部变量
        print(f"{self.name} used flash!")

    # 类方法
    @classmethod
    def heal(cls):
        print(cls.game_name)

    @classmethod
    def heals(cls, lijing):
        print(lijing.name)


if __name__ == "__main__":
    lijing = Hero("Lijing")
    print(lijing.game_name)
    lijing.game_name = "DNF"
    print(lijing.game_name)
    lijing.flash()

    # Hero.flash() 会报错
    # 因为 Hero 无法传入一个实例对象的指针来对应形参 self

    Hero.heal()  # 类使用类方法
    lijing.heal()  # 实例使用类方法
    lijing.heals(lijing)  # 实例使用类方法访问实例变量
