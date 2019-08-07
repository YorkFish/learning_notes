#!/usr/bin/env python3
# coding:utf-8

import tkinter as tk

window = tk.Tk()                # 窗口 object
window.title("my window")       # 标题
window.geometry("300x200")      # 窗口大小

# e = tk.Entry(window, show='*')# show='*' 为隐藏
# e = tk.Entry(window, show='1')# show='1' “恶搞”
e = tk.Entry(window, show=None) # show=None 为显示
e.pack()

def insert_point():
    var = e.get()
    t.insert("insert", var)     # "insert" 指在光标后添加

def insert_end():
    var = e.get()
    # t.insert("end", var)      # "end" 指添加至末尾
    t.insert(1.1, var)          # 1.1 指第一行第一列

b1 = tk.Button(window, text="insert point", width=15, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text="insert end", width=15, height=2, command=insert_end)
b2.pack()

t = tk.Text(window, height=2)   # 定义文本框位两行
t.pack()

window.mainloop()               # 循环刷新

