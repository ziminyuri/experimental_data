from tkinter import *
from ChildWindow import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class MainWindow(Frame):
    def __init__(self,root):
        super().__init__(root)

        self.root = root
        self.graph = []

        self.init_main_window()

    def click_button_add(self):
        ChildWindow(self, self.root)

    def init_main_window(self):
        label1 = Label(text="График №1", height=1, width=15, font='Arial 18')
        label1.place(x=165, y=5)

        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_xlim([0, 1000])
        ax.set_ylim([-100,100])
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=5, y=35)

        label2 = Label(text="График №2", height=1, width=15, font='Arial 18')
        label2.place(x=700, y=5)

        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_xlim([0, 1000])
        ax.set_ylim([-100, 100])
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=35)

        label3 = Label(text="График №3", height=1, width=15, font='Arial 18')
        label3.place(x=165, y=360)

        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_xlim([0, 1000])
        ax.set_ylim([-100, 100])
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=5, y=400)

        label4 = Label(text="График №4", height=1, width=15, font='Arial 18')
        label4.place(x=700, y=360)

        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_xlim([0, 1000])
        ax.set_ylim([-100, 100])
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=400)

        b2 = Button(text="Добавить", command=self.click_button_add, width="26", height="2")
        b2.place(x=1120, y=70)

        b3 = Button(text="Проверить на стационарность", command=self.click_button_add, width="26", height="2")
        b3.place(x=1120, y=120)

    def draw_graph(self, model):

        if model.option == 1:
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.N])
            ax.set_ylim([model.axis_y_graph_min - model.argument, model.axis_y_graf_max + model.argument])
            ax.plot(model.x, model.y, color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=10)

            """
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, 100])
            ax.set_ylim([0, 100])
            ax.plot(model.x, model.y, color='red', label='Линия 1')

            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=10)

            """

        if model.option == 2:
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.N])
            ax.set_ylim([model.axis_y_graph_min - model.argument, model.axis_y_graf_max + model.argument])
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
            ax.set_xlim([0, model.N])
            ax.set_ylim([model.axis_y_graph_min - model.argument, model.axis_y_graf_max + model.argument])
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
            ax.set_xlim([0, model.N])
            ax.set_ylim([model.axis_y_graph_min - model.argument, model.axis_y_graf_max + model.argument])
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
