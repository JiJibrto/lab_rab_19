# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

# напишите простейший калькулятор, состоящий из двух текстовых полей,
# куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/".
# Результат вычисления должен отображаться в метке.
# Если арифметическое действие выполнить невозможно
# (например, если были введены буквы, а не числа),
# то в метке должно появляться слово "ошибка".


class Calc:

    def __init__(self, master):
        self.ent_top = LabelFrame(master, text="Первое число")
        self.ent_bot = LabelFrame(master, text="Второе число")
        self.res_lab = LabelFrame(master, text="Результат")
        self.b_top = Frame(master)
        self.b_bot = Frame(master)
        self.res = Label(self.res_lab, width=20, text="")
        self.ent_1 = Entry(self.ent_top, width=20)
        self.ent_2 = Entry(self.ent_bot, width=20)
        self.but_sum = Button(self.b_top, text='+', width=10, height=5)
        self.but_dif = Button(self.b_top, text='-', width=10, height=5)
        self.but_mul = Button(self.b_bot, text='*', width=10, height=5)
        self.but_div = Button(self.b_bot, text='/', width=10, height=5)

        self.but_sum.bind('<Button-1>', self.sum)
        self.but_dif.bind('<Button-1>', self.dif)
        self.but_mul.bind('<Button-1>', self.mul)
        self.but_div.bind('<Button-1>', self.div)

        self.ent_top.pack()
        self.ent_bot.pack()
        self.res_lab.pack()
        self.res.pack()
        self.ent_1.pack()
        self.ent_2.pack()
        self.b_top.pack()
        self.b_bot.pack()
        self.but_sum.pack(side=LEFT)
        self.but_dif.pack(side=LEFT)
        self.but_mul.pack(side=LEFT)
        self.but_div.pack(side=LEFT)

        self.x_1 = 0
        self.x_2 = 0
        self.res_num = 0

    def sum(self, event):
        try:
            self.x_1 = self.ent_1.get()
            self.x_2 = self.ent_2.get()
            self.res_num = float(self.x_1) + float(self.x_2)
            self.res['text'] = self.res_num
        except:
            self.res['text'] = "Error!"

    def dif(self, event):
        try:
            self.x_1 = self.ent_1.get()
            self.x_2 = self.ent_2.get()
            self.res_num = float(self.x_1) - float(self.x_2)
            self.res['text'] = self.res_num
        except:
            self.res['text'] = "Error!"

    def mul(self, event):
        try:
            self.x_1 = self.ent_1.get()
            self.x_2 = self.ent_2.get()
            self.res_num = float(self.x_1) * float(self.x_2)
            self.res['text'] = self.res_num
        except:
            self.res['text'] = "Error!"

    def div(self, event):
        try:
            self.x_1 = self.ent_1.get()
            self.x_2 = self.ent_2.get()
            self.res_num = float(self.x_1) / float(self.x_2)
            self.res['text'] = self.res_num
        except:
            self.res['text'] = "Error!"


root = Tk()
main_calc = Calc(root)
root.mainloop()
