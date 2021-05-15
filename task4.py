#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *

# напишите программу, состоящую из однострочного и многострочного
# текстовых полей и двух кнопок "Открыть" и "Сохранить". При клике на первую должен
# открываться на чтение файл, чье имя указано в поле класса Entry , а содержимое файла
# должно загружаться в поле типа Text .
# При клике на вторую кнопку текст, введенный пользователем в экземпляр Text , должен
# сохраняться в файле под именем, которое пользователь указал в однострочном текстовом
# поле.


class Main_prog:
    def __init__(self, master):
        self.header = LabelFrame(master, text="Menu")
        self.ent_1 = Entry(self.header, width=77)
        self.tex_1 = Text(master)
        self.but_1 = Button(self.header, width=10, text="OPEN")
        self.but_2 = Button(self.header, width=10, text="SAVE")

        self.but_1.config(command=self.openfile)
        self.but_2.config(command=self.savefile)

        self.header.pack(pady=10)
        self.ent_1.pack(side=LEFT, padx=1, pady=1)
        self.tex_1.pack()
        self.but_1.pack(side=LEFT, padx=1, pady=1)
        self.but_2.pack(side=LEFT, padx=1, pady=1)

        self.filename = ""
        self.temp = ""

    def openfile(self):
        try:
            self.filename = self.ent_1.get()
            with open(self.filename, 'r') as s:
                self.tex_1.insert(0.0, s.read())
        except:
            self.ent_1.delete(0, END)
            self.ent_1.insert(0, 'Error!')

    def savefile(self):
            self.temp = self.tex_1.get(0.0, 'end')
            self.filename = self.ent_1.get()
            with open(self.filename, 'w') as f:
                f.write(self.temp)


root = Tk()
setuper = Main_prog(root)
root.mainloop()
