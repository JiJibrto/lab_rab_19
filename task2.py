#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *

# Решите задачу: напишите программу, состоящую из семи кнопок, цвета которых
# соответствуют цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен
# вставляться код цвета, а в метку – название цвета.
# button_off.pack(side=LEFT)
# root.mainloop()Коды цветов в шестнадцатеричной кодировке: #ff0000 – красный, #ff7d00 – оранжевый,
# #ffff00 – желтый, #00ff00 – зеленый, #007dff – голубой, #0000ff – синий, #7d00ff –
# фиолетовый.


class Rainbow:
    def __init__(self, master):
        self.l_1 = Label(width=20)
        self.e_1 = Entry(width=20)
        self.b_1 = Button(width=20, bg="#ff0000")
        self.b_2 = Button(width=20, bg="#ff9900")
        self.b_3 = Button(width=20, bg="#ffff00")
        self.b_4 = Button(width=20, bg="#33cc33")
        self.b_5 = Button(width=20, bg="#6699ff")
        self.b_6 = Button(width=20, bg="#0000ff")
        self.b_7 = Button(width=20, bg="#cc00cc")

        self.b_1.bind('<Button-1>', self.clr)
        self.b_2.bind('<Button-1>', self.clr)
        self.b_3.bind('<Button-1>', self.clr)
        self.b_4.bind('<Button-1>', self.clr)
        self.b_5.bind('<Button-1>', self.clr)
        self.b_6.bind('<Button-1>', self.clr)
        self.b_7.bind('<Button-1>', self.clr)

        self.l_1.pack()
        self.e_1.pack()
        self.b_1.pack()
        self.b_2.pack()
        self.b_3.pack()
        self.b_4.pack()
        self.b_5.pack()
        self.b_6.pack()
        self.b_7.pack()

    def clr(self, event):
        if event.widget['bg'] == "#ff0000":
            self.e_1.delete(0, END)
            self.l_1['text'] = "Красный"
            self.e_1.insert(0, "#ff0000")
        elif event.widget['bg'] == "#ff9900":
            self.e_1.delete(0, END)
            self.l_1['text'] = "Оранжевый"
            self.e_1.insert(0, "#ff9900")
        elif event.widget['bg'] == "#ffff00":
            self.e_1.delete(0, END)
            self.l_1['text'] = "Желтый"
            self.e_1.insert(0, "#ffff00")
        elif event.widget['bg'] == "#33cc33":
            self.e_1.delete(0, END)
            self.l_1['text'] = "Зеленый"
            self.e_1.insert(0, "#33cc33")
        elif event.widget['bg'] == "#6699ff":
            self.e_1.delete(0, END)
            self.l_1['text'] = "Голубой"
            self.e_1.insert(0, "#6699ff")
        elif event.widget['bg'] == "#0000ff":
            self.e_1.delete(0, END)
            self.l_1['text'] = "Синий"
            self.e_1.insert(0, "#0000ff")
        elif event.widget['bg'] == "#cc00cc":
            self.e_1.delete(0, END)
            self.l_1['text'] = "Филетовый"
            self.e_1.insert(0, "#cc00cc")


root = Tk()
rainbow = Rainbow(root)
root.mainloop()
