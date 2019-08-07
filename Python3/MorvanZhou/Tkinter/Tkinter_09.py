#!/usr/bin/env python3
# coding:utf-8

import tkinter as tk

window = tk.Tk()                # 窗口 object
window.title("my window")       # 标题
window.geometry("300x200")      # 窗口大小

l = tk.Label(window, text="", bg="yellow")
l.pack() 

counter = 0
def do_job():
    global counter
    l.config(text="do " + str(counter))                         # + 不要改成 ,
    counter += 1

menubar = tk.Menu(window)                                       # 菜单栏
filemenu = tk.Menu(menubar, tearoff=0)                          # 下拉菜单；0 表示不可分，1 表示可分

menubar.add_cascade(label="File", menu=filemenu)                # 加入 File 栏目
filemenu.add_command(label="New", command=do_job)
filemenu.add_command(label="Open", command=do_job)
filemenu.add_command(label="Save", command=do_job)

filemenu.add_separator()                                        # 分离
filemenu.add_command(label="Exit", command=window.quit)         # 退出

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)                # 加入 Edit 栏目
editmenu.add_command(label="Cut", command=do_job)
editmenu.add_command(label="Copy", command=do_job)
editmenu.add_command(label="Paste", command=do_job)

submenu = tk.Menu(filemenu)
editmenu.add_cascade(label="Import", menu=submenu, underline=0) # 加入 Edit 栏目
submenu.add_command(label="submenu1", command=do_job)
submenu.add_command(label="submenu2", command=do_job)

window.config(menu=menubar)     # 显示出来

window.mainloop()               # 循环刷新

