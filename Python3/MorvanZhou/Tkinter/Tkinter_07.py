#!/usr/bin/env python3
# coding:utf-8

import tkinter as tk

window = tk.Tk()                # 窗口 object
window.title("my window")       # 标题
window.geometry("300x200")      # 窗口大小

l = tk.Label(window, bg="yellow", 
        width=20, text="empty") # width 是字符的宽度
l.pack()

def print_selection_1():
    if (var1.get()==1) & (var2.get()==0):
                                # & 按位与运算符
                                # var1.get() == 1 就是 var1 获得的变量 onvalue=1，
                                # var1.get() == 0 即是 var1 获得的变量 offvalu=0
        l.config(text="I love only Python")
    elif (var1.get()==0) & (var2.get()==1):
        l.config(text="I love only C++")
    elif (var1.get()==0) & (var2.get()==0):
        l.config(text="I do not love either")
    else:
        l.config(text="I love both")

def print_selection_2():        # 用 and 效果一样
    if var1.get()==1 and var2.get()==0:
        l.config(text="I love only Python")
    elif var1.get()==0 and var2.get()==1:
        l.config(text="I love only C++")
    elif var1.get()==0 and var2.get()==0:
        l.config(text="I do not love either")
    else:
        l.config(text="I love both")

var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text="Python", variable=var1, onvalue=1, offvalue=0, command=print_selection_2)
                                # onvalue 和 Tkinter_05.py 的部件 radiobutton 中的 value 相似，
                                # 当我们选中了这个 checkbutton，onvalue 的值 1 就会放入到 var1 中，然后 var1 将其赋值给参数 variable
                                # offvalue 用法相似，
                                # 但是 offvalue 是在没有选中这个 checkbutton 时，把值 0 放入 var1，然后赋值给参数 variable
c2 = tk.Checkbutton(window, text="C++", variable=var2, onvalue=1, offvalue=0, command=print_selection_2)
c1.pack()
c2.pack()

window.mainloop()               # 循环刷新

