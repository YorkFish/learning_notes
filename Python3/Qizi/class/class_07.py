class Hero(object):
    def __init__(self, name):
        self.name = name


# 以下三种方式效果相同
class AD1(Hero):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class AD2(Hero):
    def __init__(self, name, gender):
        Hero.__init__(self, name)
        self.gender = gender


class AD3(Hero):
    def __init__(self, name, gender):
        super(AD3, self).__init__(name)
        self.gender = gender


if __name__ == "__main__":
    ashe = AD1("艾希", "female")
    print(ashe.__dict__)

    jinx = AD2("金克丝", "female")
    print(jinx.__dict__)
    
    vayne = AD3("薇恩", "female")
    print(vayne.__dict__)
