#!/usr/bin/env python3
# coding:utf-8

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()                # 窗口 object
window.title("my window")       # 标题
window.geometry("300x200")      # 窗口大小

def hit_me():
    # tk.messagebox.showinfo(title="Hi", message="hahaha")                  # 信息符号，伴随声音 1
    # tk.messagebox.showwarning(title="Hi", message="nonono")               # 警告符号，伴随声音 1
    # tk.messagebox.showerror(title="Hi", message="No!! never")             # 错误符号，伴随声音 2
    # print(tk.messagebox.askquestion(title="Hi", message="lalala"))        # return "yes", "no"
    # print(tk.messagebox.askyesno(title="Hi", message="yes or no"))        # return Ture, False
    print(tk.messagebox.askretrycancel(title="Hi", message="yes or no"))    # return Ture, False; no adktrycancel; 警告符号，伴随声音 1
    # print(tk.messagebox.askokcancel(title="Hi", message="yes or no"))     # return Ture, False

tk.Button(window, text="hit me", command=hit_me).pack()

window.mainloop()               # 循环刷新

