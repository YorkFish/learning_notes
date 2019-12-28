class Hero(object):
    game = "League of legend"

    def  __init__(self, name):
        self.name = name

    def flash(self):
        print(f"{self.name} used flash!")


class AD(Hero):
    slogan = "Everything in the world is tied to an arrow!"

    def q(self):
        print("dododo")


if __name__ == "__main__":
    ashe = AD("艾希")
    print(ashe.game)
    print(ashe.slogan)
    ashe.flash()
    ashe.q()
