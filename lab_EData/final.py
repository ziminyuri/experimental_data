from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math



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


    def calculation1(self):
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

    def update_UI(self, array_models, k, b, alpha, beta):
        print("альфа")
        print(k)
        """
        for i in (array_models): ### Не правильно сделал массив объектов
           
            i.k = k.get()
            i.b = b.get()
            i.alpha = alpha.get()
            i.beta = beta.get()
            
            i.calculation()
        """

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

        label1 = Label(text="Коэффициенты для графиков", height=1, width=29, font='Arial 14')
        label1.place(x=1000, y=50)

        ###Ввод к
        label2 = Label(text="k", height=1, width=1, font='Arial 14')
        label2.place(x=1018, y=90)
        input_k = Entry(width=10)
        input_k.place(x=1065, y=85)

        ### Ввод b
        label3 = Label(text="b", height=1, width=1, font='Arial 14')
        label3.place(x=1018, y=120)
        input_b = Entry(width=10)
        input_b.place(x=1065, y=115)


        ### Ввод alpha
        label4 = Label(text="alpha", height=1, width=5, font='Arial 14')
        label4.place(x=1018, y=150)
        input_alpha = Entry(width=10)
        input_alpha.place(x=1065, y=145)

        ### Ввод beta
        label5 = Label(text="beta", height=1, width=4, font='Arial 14')
        label5.place(x=1018, y=180)
        input_beta = Entry(width=10)
        input_beta.place(x=1065, y=175)

        ### Ввод label's с названием функция
        label6 = Label(text="x(t) = k(x)+ b", height=1, width=15, font='Arial 18')
        label6.place(x=55, y=15)

        label7 = Label(text="x(t) = -k(x)+ b", height=1, width=15, font='Arial 18')
        label7.place(x=600, y=15)

        label8 = Label(text="x(t) = beta * E^(alpha * x)", height=1, width=25, font='Arial 18')
        label8.place(x=40, y=410)

        label9 = Label(text="x(t) = beta * E^(-alpha * x)", height=1, width=25, font='Arial 18')
        label9.place(x=580, y=410)

        b1 = Button(text="Обновить графики", command=self.update_UI(array_models, input_k, input_b, input_alpha.get(), input_beta), width="26", height="2")
        b1.place(x=1020, y=220)


def main():
    root = Tk()
    root.title("Лабораторная №1 / Методы обработки эксперементальных данных")
    root.geometry('1320x820')
    ex = Display(root)
    root.mainloop()

if __name__ == '__main__':
    main()