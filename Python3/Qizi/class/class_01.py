class Hero(object):
    def __init__(self, name, slogan):
        self.name = name
        self.slogan = slogan

    def saySlogan(self):
        print(self.slogan)

    def flash(self):
        print(f"{self.name} used flash!")


if __name__ == "__main__":
    lijing = Hero("lijing", "My hands, you will!")
    lijing.saySlogan()
    lijing.flash()
    print(lijing.__dict__)
