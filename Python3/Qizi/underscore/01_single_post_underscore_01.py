"""
Python 中没有对 public 和 private 进行严格的定义
为了区分，社区的程序员达成了一个约定：
当看到以下划线开头的变量或方法时，最好将只在内部使用该变量或方法
"""

class Hero(object):
    def __init__(self, name, chinesename):
        self.name = name
        # self.chinesename = chinesename
        self._chinesename = chinesename


if __name__ == "__main__":
    yasuo = Hero("yasuo", "压缩")
    print(yasuo.name)
    print(yasuo._chinesename)
