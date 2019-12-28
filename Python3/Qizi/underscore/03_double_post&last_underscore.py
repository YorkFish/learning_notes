"""
文件名中有 &，在命令行运行时需要加引号，下面两种方法均能在 windows10 下运行
$ python "03_double_post&last_underscore".py
$ python "03_double_post&last_underscore.py"
"""

class Hero:
    def __init__(self, name, chinesename):
        self.name = name
        self.chinesename = chinesename


if __name__ == "__main__":
    # 1.
    # 1.1 执行 __new__()，生成一个实例对象
    # 1.2 执行 __init__()，对生成的对象进行初始化
    garen = Hero("garen", "盖伦");

    # 2.
    # len() 会调用类中的 __lenth__() 魔法方法
    name = "garen"
    print(len(name))

    # what's more?
    # __call__(), __boll__(), __str__(), __del__() ...
