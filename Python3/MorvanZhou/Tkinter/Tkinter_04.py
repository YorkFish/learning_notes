#!/usr/bin/env python3
# coding:utf-8

import tkinter as tk

window = tk.Tk()                        # 窗口 object
window.title("my window")               # 标题
window.geometry("400x300")              # 窗口大小

var1 = tk.StringVar()
l = tk.Label(window, bg="yellow", width=4, textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())   # 取出光标处的值
    var1.set(value)

b1 = tk.Button(window, text="insert print selection", width=20, height=2, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))

lb = tk.Listbox(window, listvariable=var2)

list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert("end", item)

lb.insert(0, "first")
lb.insert(2, "second")
lb.delete(2)
lb.pack()

window.mainloop()                       # 循环刷新

