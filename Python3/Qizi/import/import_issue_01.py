#coding:utf-8

"""
若使用
    from .prints import *
则
    ModuleNotFoundError: No module named '__main__.prints';
    '__main__' is not a package

. 所表示的根路径也是 '__main__' 的值
在入口文件中，应该避免使用相对路径进行模块导入
"""

import prints


def main():
    print(">>> this is main")


if __name__ == '__main__':
    print(">>> __name__ =", __name__)
    main()
