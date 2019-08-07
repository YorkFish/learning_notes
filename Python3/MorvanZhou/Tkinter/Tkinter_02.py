#!/usr/bin/env python3
# coding:utf-8

import tkinter as tk

window = tk.Tk()                # 窗口 object
window.title("my window")       # 标题
window.geometry("300x200")      # 窗口大小

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg="green", font=("Arial", 12), width=15, height=2)
l.pack()                        # 布局管理器，按添加顺序并排列组件
# l.place()                     # 按具体的像素点放

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("you hit me")
    else:
        on_hit = False
        var.set("")

b = tk.Button(window, text="hit me", width=15, height=2, command=hit_me)
b.pack()

window.mainloop()               # 循环刷新

