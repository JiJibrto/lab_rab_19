# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

# напишите простейший калькулятор, состоящий из двух текстовых полей,
# куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/".
# Результат вычисления должен отображаться в метке.
# Если арифметическое действие выполнить невозможно
# (например, если были введены буквы, а не числа),
# то в метке должно появляться слово "ошибка".

class Calk:
    def __init__(self, master, func):
        self.ent_1 = Entry(master, width=20)
        self.ent_2 = Entry(master, width=20)
        self.but_sum = Button(master, text='+',)
        self.but_dif = Button(master, text='-')
        self.but_mul = Button(master, text='*')
        self.but_div = Button(master, text='/')

root = Tk()



ent.pack()
but.pack()
lab.pack()
root.mainloop()


