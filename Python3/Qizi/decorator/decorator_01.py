def out(x):
    def inn():
        print(x)
    return inn


if __name__ == "__main__":
    func = out(1)
    func()
