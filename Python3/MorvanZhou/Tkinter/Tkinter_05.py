#!/usr/bin/env python3
# coding:utf-8

import tkinter as tk

window = tk.Tk()                # 窗口 object
window.title("my window")       # 标题
window.geometry("300x200")      # 窗口大小

var = tk.StringVar()
l = tk.Label(window, bg="yellow", width=20, text="empty")
l.pack()

def print_selection():
    l.config(text="you have selected" + var.get())

r1 = tk.Radiobutton(window, text="Option A", variable=var, value='A', command=print_selection)
                                # variable=var, value='A' 的意思是
                                # 若鼠标选中了这个选项，就把 value 的值 A 放到变量 var 中，然后赋值给 variable
r1.pack()

r2 = tk.Radiobutton(window, text="Option B", variable=var, value='B', command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window, text="Option C", variable=var, value='C', command=print_selection)
r3.pack()

window.mainloop()               # 循环刷新

