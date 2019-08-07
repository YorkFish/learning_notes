#!/usr/bin/env python3
# coding:utf-8

import tkinter as tk

window = tk.Tk()                # 窗口 object
window.title("my window")       # 标题
window.geometry("300x200")      # 窗口大小

canvas = tk.Canvas(window, bg="blue", width=250, height=150)

image_file = tk.PhotoImage(file="ins.gif")
image = canvas.create_image(0, 0, anchor="nw", image=image_file)

x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)               # 画线
oval = canvas.create_oval(x0, y0, x1, y1, fill="red")   # 画圆
arc = canvas.create_arc(x0+50, y0+50, x1+50, y1+50, 
                        start=30, extent=120)           # 画扇形
rect = canvas.create_rectangle(100, 30, 130, 60)        # 画方框，左上、右下两点

canvas.pack()

def moveit():
    canvas.move(rect, 0, 2)     # 横坐标移动 0 个单位，纵坐标移动 2 个单位

b = tk.Button(window, text="move", command=moveit).pack()

window.mainloop()               # 循环刷新

