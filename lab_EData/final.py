from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math


def colculation()

class Model():
    def __init__(self, option):
        self.k = 5
        self.b = 10
        self.beta = 15
        self.alpha = 20
        self.y = []
        self.option = option

        self.x = []
        for i in range(1000):
            self.x.append(i)

    def calculation(self):
        if(self.option == 1):
            x_max = 1000

            for i in range(x_max):
                yn = self.k * i + self.b
                self.y.append(yn)

        if (self.option == 2):
            x_max = 1000

            for i in range(x_max):
                yn = -self.k * i + self.b
                self.y.append(yn)

        if (self.option == 3):   ### Проблемы с экспонентой
            x_max = 1000

            for i in range(x_max):
                try:
                    #yn = self.beta * math.exp((self.alpha * i))
                    yn = math.exp(i)
                    self.y.append(yn)
                except:
                    self.y.append(0)

        if (self.option == 4):
            x_max = 1000

            for i in range(x_max):
                yn = self.beta * math.exp(self.alpha * -i)
                self.y.append(yn)


class Display(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def update_UI(self, array_models):
        for i in range(array_models):
            i.calculation()   ### Не правильно сделал массив объектов

    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        array_models = []

        model1 = Model(1)
        array_models.append(model1)
        model1.calculation()


        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(model1.x, model1.y, color='red', label='Линия 1')
        canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=10, y=10)

        model2 = Model(2)
        array_models.append(model2)
        model2.calculation()

        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(model2.x, model2.y, color='red', label='Линия 1')
        canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=10)

        model3 = Model(1)
        array_models.append(model3)
        model3.calculation()

        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(model3.x, model3.y, color='red', label='Линия 1')
        canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=10, y=400)

        model4 = Model(2)
        array_models.append(model4)
        model4.calculation()

        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(model4.x, model4.y, color='red', label='Линия 1')
        canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=400)

        b1 = Button(text="Обновить графики", command=self.update_UI(array_models), width="26", height="2")
        b1.place(x=1020, y=11)


def main():
    root = Tk()
    root.title("Лабораторная №1 / Методы обработки эксперементальных данных")
    root.geometry('1320x820')
    ex = Display(root)
    root.mainloop()

if __name__ == '__main__':
    main()