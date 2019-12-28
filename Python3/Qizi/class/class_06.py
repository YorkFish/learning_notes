"""
“实例方法”只能使用“实例对象”调用
“类”和“对象”都能调用“类方法”和“静态方法”
“实例方法”、“类方法”和“静态方法”均能实现对“类变量”和“实例变量”的调用
"""

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
    def heals(cls):
        print(lijing.name)

    # 静态方法
    @staticmethod
    def ignit():
        print("used fire")

    @staticmethod
    def say_game_name():
        print(Hero.game_name)  # 在静态方法中使用类变量
        print(lijing.name)


if __name__ == "__main__":
    lijing = Hero("Lijing")
    print(lijing.game_name)
    lijing.game_name = "DNF"
    print(lijing.game_name)
    lijing.flash()

    Hero.heal()  # 类使用类方法
    lijing.heal()  # 实例使用类方法
    lijing.heals()  # 实例使用类方法访问实例变量

    Hero.ignit()  # 类可以调用静态方法
    lijing.ignit()  # 实例可以调用静态方法

    Hero.say_game_name()
    lijing.say_game_name()
