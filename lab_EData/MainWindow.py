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
        ChildWindow(self, self.root, self.graph)

    def check_stationarity_click_button(self):

        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                check_result = i.check_stationarity_average_value()

        if check_result == True:
            messagebox.showinfo("Проверка на стационарность: Среднее значение","График стационарен")
        else:
            messagebox.showinfo("Проверка на стационарность: Среднее значение","График не стационарен")

    def check_stationarity_dispersion_click_button(self):

        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                check_result = i.check_stationarity_dispersion1(1)

        print(check_result)
        messagebox.showinfo("Проверка на стационарность: Дисперсия", "Корень из дисперсии: " + str(check_result))

    #Проверка на стационарность
    def check_stationarity_dispersion_x_10_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                check_result = i.check_stationarity_dispersion1(10)

        print(check_result)
        messagebox.showinfo("Проверка на стационарность: Дисперсия", "Корень из дисперсии x10: " + str(check_result))

    #Среднее значение
    def average_value_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                check_result = i.average_value()

        print(check_result)
        messagebox.showinfo("Среднее значение: " + str(check_result))


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

        label1 = Label(text="Номер графика", height=1, width=14, font='Arial 14')
        label1.place(x=1120, y=150)
        self.c1 = ttk.Combobox(values=[u"1", u"2", u"3", u"4"], height=4, width = "24")
        self.c1.place(x=1120, y=180)

        b3 = Button(text="Стационарность: СЗ", command=self.check_stationarity_click_button, width="26", height="2")
        b3.place(x=1120, y=220)

        b4 = Button(text="Дисперсия", command=self.check_stationarity_dispersion_click_button, width="26", height="2")
        b4.place(x=1120, y=270)

        b5 = Button(text="Дисперсия x10", command=self.check_stationarity_dispersion_x_10_click_button, width="26", height="2")
        b5.place(x=1120, y=320)

        b6 = Button(text="Среднее значение", command=self.average_value_click_button, width="26", height="2")
        b6.place(x=1120, y=370)

    def draw_graph(self, model, chart_number):

        if chart_number == "1":
            fig = Figure(figsize=(5, 3), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.get_N()])
            ax.set_ylim([model.get_axis_y_graph_min() - model.get_argument(), model.get_axis_y_graf_max() + model.get_argument()])

            ax.plot(model.get_x(), model.get_y(), color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=5, y=35)

        if chart_number == "2":
            fig = Figure(figsize=(5, 3), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.get_N()])
            ax.set_ylim([model.get_axis_y_graph_min() - model.get_argument(), model.get_axis_y_graf_max() + model.get_argument()])
            ax.plot(model.get_x(), model.get_y(), color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=550, y=35)

        if chart_number == "3":
            fig = Figure(figsize=(5, 3), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.get_N()])
            ax.set_ylim([model.get_axis_y_graph_min() - model.get_argument(), model.get_axis_y_graf_max() + model.get_argument()])
            ax.plot(model.get_x(), model.get_y(), color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=5, y=400)

        if chart_number == "4":
            fig = Figure(figsize=(5, 3), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.get_N()])
            ax.set_ylim([model.get_axis_y_graph_min() - model.get_argument(), model.get_axis_y_graf_max() + model.get_argument()])
            ax.plot(model.get_x(), model.get_y(), color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=550, y=400)
