def func(arg, *args, **kwargs):
    print(f">>> arg = {arg}, type(arg) = {type(arg)}")
    print(f">>> args = {args}, type(args) = {type(args)}")
    print(f">>> kwargs = {kwargs}, type(kwargs) = {type(kwargs)}")


if __name__ == "__main__":
    func(1, 2, 2, 2, 2, student="Tom", teacher="Jerry")
