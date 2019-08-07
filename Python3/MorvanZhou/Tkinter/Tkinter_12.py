#!/usr/bin/env python3
# coding:utf-8

import tkinter as tk

window = tk.Tk()                # 窗口 object
window.title("my window")       # 标题
window.geometry("300x200")      # 窗口大小

'''
# 1. pack()
tk.Label(window, text=1).pack(side="top")
tk.Label(window, text=1).pack(side="bottom")
tk.Label(window, text=1).pack(side="left")
tk.Label(window, text=1).pack(side="right")


# 2. grid()
for i in range(4):
    for j in range(3):
        # tk.Label(window, text=1).grid(row=i, column=j)
        # tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)  # 设置控件周围横、纵空白区域保留大小
        tk.Label(window, text=1).grid(row=i, column=j, ipadx=10, ipady=10)  # 初看同上
'''


# 3. place()
# tk.Label(window, text=1).place(x=10, y=100)
tk.Label(window, text=1).place(x=10, y=100, anchor="nw")

window.mainloop()               # 循环刷新

