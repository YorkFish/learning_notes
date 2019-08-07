#!/usr/bin/env python3
# coding:utf-8

import tkinter as tk

window = tk.Tk()                        # 窗口 object
window.title("my window")               # 标题
window.geometry("300x200")              # 窗口大小

l = tk.Label(window, bg="yellow", 
            width=20, text="empty")     # width 是字符串的最大宽度
l.pack()

def print_selection(v):
    l.config(text="you have selected" + v)

s = tk.Scale(window, label="try me", from_=5, to=11, orient=tk.HORIZONTAL, 
            length=200, showvalue=0, tickinterval=2, resolution=0.01, 
            command=print_selection)    # from_ 是起始值，to 是最终值，HORIZONTAL 是设置拖拽条（滚动条）方向为横向
                                        # length 是拖拽条的长度，showvalue 是设置是否拖拽条上方显示数值 1：显示 0：不显示，
                                        # tickinterval 是间隔，resolution 是精度
s.pack()

window.mainloop()                       # 循环刷新

