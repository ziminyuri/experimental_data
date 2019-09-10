from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from model import *

class Display():
    def __init__(self, root):

        self.root = root
        self.root.title("Лабораторная №1 / Методы обработки эксперементальных данных")
        self.root.geometry('1400x820')
        self.initUI()


    def draw_graph(self, model):

        if model.option == 1:
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, 100])
            ax.set_ylim([0, 100])
            ax.plot(model.x, model.y, color='red', label='Линия 1')

            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=10)

        if model.option == 2:

            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.n])
            ax.set_ylim([model.axis_y_min, model.axis_y_max])
            ax.plot(model.x, model.y, color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=550, y=10)

            """
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, 100])
            ax.set_ylim([0, 100])
            ax.plot(model.x, model.y, color='red', label='Линия 1')

            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=550, y=10)
            """


        if model.option == 3:
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.n])
            ax.set_ylim([model.axis_y_min, model.axis_y_max])
            ax.plot(model.x, model.y, color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=400)

            """
            
            Здесь рабочая гипербола
            
            
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            #ax.set_xlim([0, 10])
            #ax.set_ylim([0, 100])
            ax.plot(model.x, model.y, color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=400)
            """


        if model.option == 4:

            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.n])
            ax.set_ylim([model.axis_y_min, model.axis_y_max])
            ax.plot(model.x, model.y, color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=550, y=400)

            """
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([-10, 10])
            ax.set_ylim([0, 100])
            ax.plot(model.x, model.y, color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=550, y=400)
            """


    def update_UI(self, models):
        print("альфа")

        for obj in models:
            obj.k = float(self.k.get())
            obj.b = float(self.b.get())
            obj.beta = float(self.beta.get())
            obj.alpha = float(self.alpha.get())
            obj.calculation()
            self.draw_graph(obj)



    def initUI(self):
        canvas = Canvas(self.root)
        array_models = []

        model1 = Model(1)
        array_models.append(model1)
        model1.calculation()
        self.draw_graph(model1)

        model2 = Model(2)
        array_models.append(model2)
        model2.calculation()
        self.draw_graph(model2)


        model3 = Model(3)
        array_models.append(model3)
        model3.calculation()
        self.draw_graph(model3)


        model4 = Model(4)
        array_models.append(model4)
        model4.calculation()
        self.draw_graph(model4)


        label1 = Label(text="Коэффициенты для графиков", height=1, width=29, font='Arial 14')
        label1.place(x=1100, y=50)

        ###Ввод к
        label2 = Label(text="k", height=1, width=1, font='Arial 14')
        label2.place(x=1118, y=90)
        input_k = Entry(width=10)
        input_k.place(x=1165, y=85)
        self.k = input_k

        ### Ввод b
        label3 = Label(text="b", height=1, width=1, font='Arial 14')
        label3.place(x=1118, y=120)
        input_b = Entry(width=10)
        input_b.place(x=1165, y=115)
        self.b = input_b

        ### Ввод alpha
        label4 = Label(text="alpha", height=1, width=5, font='Arial 14')
        label4.place(x=1118, y=150)
        input_alpha = Entry(width=10)
        input_alpha.place(x=1165, y=145)
        self.alpha = input_alpha

        ### Ввод beta
        label5 = Label(text="beta", height=1, width=4, font='Arial 14')
        label5.place(x=1118, y=180)
        input_beta = Entry(width=10)
        input_beta.place(x=1165, y=175)
        self.beta = input_beta

        ### Ввод N - количество записей
        label5 = Label(text="beta", height=1, width=4, font='Arial 14')
        label5.place(x=1118, y=180)
        input_beta = Entry(width=10)
        input_beta.place(x=1165, y=175)
        self.beta = input_beta

        ### Ввод 
        label5 = Label(text="beta", height=1, width=4, font='Arial 14')
        label5.place(x=1118, y=180)
        input_beta = Entry(width=10)
        input_beta.place(x=1165, y=175)
        self.beta = input_beta

        ### Ввод beta
        label5 = Label(text="beta", height=1, width=4, font='Arial 14')
        label5.place(x=1118, y=180)
        input_beta = Entry(width=10)
        input_beta.place(x=1165, y=175)
        self.beta = input_beta

        ### Ввод label's с названием функция
        label6 = Label(text="x(t) = k(x)+ b", height=1, width=15, font='Arial 18')
        label6.place(x=55, y=15)

        label7 = Label(text="x(t) = -k(x)+ b", height=1, width=15, font='Arial 18')
        label7.place(x=600, y=15)

        label8 = Label(text="x(t) = beta * E^(alpha * x)", height=1, width=25, font='Arial 18')
        label8.place(x=40, y=410)

        label9 = Label(text="x(t) = beta * E^(-alpha * x)", height=1, width=25, font='Arial 18')
        label9.place(x=580, y=410)

        b1 = Button(text="Обновить графики", command=lambda: self.update_UI(array_models), width="26", height="2")
        b1.place(x=1120, y=220)

