#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *

# Напишите программу, в которой имеется несколько объединенных в группу радиокнопок,
# индикатор которых выключен ( indicatoron=0 ). Если какая-нибудь кнопка включается, то в
# метке должна отображаться соответствующая ей информация. Обычных кнопок в окне быть
# не должно.


class Main_prog:
    def __init__(self, master):
        self.var = StringVar()
        self.body_left = LabelFrame(master, text="Гитарист")
        self.body_right = LabelFrame(master, text="Гитара")
        self.rad_1 = Radiobutton(self.body_left, text="Хендрикс", indicatoron=0,
                                 width=15, height=3,
                                 variable=self.var, value="FenderDuo-Sonic 59'", command=self.select)
        self.rad_2 = Radiobutton(self.body_left, text="Уайлд", indicatoron=0,
                                 width=15, height=3,
                                 variable=self.var, value="Gibson Les Paul Bullseye", command=self.select)
        self.rad_3 = Radiobutton(self.body_left, text="Кучер", indicatoron=0,
                                 width=15, height=3,
                                 variable=self.var, value="Custom something...", command=self.select)
        self.lab_1 = Label(self.body_right, bg="white", width=20, height=6)

        self.body_left.pack(side=LEFT)
        self.body_right.pack(side=LEFT)
        self.rad_1.pack()
        self.rad_2.pack()
        self.rad_3.pack()
        self.lab_1.pack()

    def select(self):
        temp = str(self.var.get())
        self.lab_1.config(text=temp)

root = Tk()
main_prog = Main_prog(root)
root.mainloop()



