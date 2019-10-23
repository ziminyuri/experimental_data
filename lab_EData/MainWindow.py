from tkinter import *
from ChildWindow import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from analysis import *


class MainWindow(Frame):
    def __init__(self, root):
        super().__init__(root)

        self.root = root
        self.graph = []

        self.init_main_window()

        self._combobox_value = []  # ComboBox графиков для анализа

    def set_combobox_value(self, value):
        self._combobox_value.append(value)

    def click_button_add_model(self):

        ChildWindow(self, self.root, self.graph)

    # Обработка нажатия на кнопку "Стационарность: СЗ"
    @staticmethod
    def check_stationarity_click_button(analysis):

        check_result = analysis.check_stationarity_average_value()

        if check_result:
            messagebox.showinfo("Проверка на стационарность: Среднее значение", "График стационарен")
        else:
            messagebox.showinfo("Проверка на стационарность: Среднее значение", "График не стационарен")

    # Обработка нажатия на кнопку "Диспресия"
    @staticmethod
    def dispersion_click_button(analysis):

        check_result = analysis.dispersion(1)
        messagebox.showinfo("Дисперсия", "Дисперсия: " + str(check_result))

    # Обработка нажатия на кнопку "Дисперсия х10"
    @staticmethod
    def dispersion_x_10_click_button(analysis):

        check_result = analysis.dispersion(10)
        messagebox.showinfo("Дисперсия", "Дисперсия x10: " + str(check_result))

    # Обработка нажатия на кнопку "Среднее значение"
    @staticmethod
    def average_value_click_button(analysis):

        check_result = analysis.average_value()
        messagebox.showinfo("Среднее значение", "Среднее значение: " + str(check_result))

    # Обработка нажатия на кнопку "Асимметрия"
    @staticmethod
    def asymmetry_click_button(analysis):

        result = analysis.asymmetry()
        messagebox.showinfo("Ассиметрия", "Ассиметрия: " + str(result))

    # Обработка нажатия на кнопку "Стандартное отклонение"
    @staticmethod
    def standard_deviation(analysis):

        result = analysis.standard_deviation()
        messagebox.showinfo("Стандартное отклонение", "Стандартное отклонение: " + str(result))

    # Обработка нажатия на кнопку "Коэффициент асимметрии"
    @staticmethod
    def asymmetry_coefficient_click_button(analysis):

        result = analysis.asymmetry_coefficient()
        messagebox.showinfo("Коэффициент асимметрии", "Коэффициент асимметрии: " + str(result))

    # Обработка нажатия на кнопку "Эксцесс"
    @staticmethod
    def excess_click_button(analysis):

        result = analysis.excess()
        messagebox.showinfo("Эксцесс", "Эксцесс: " + str(result))

    # Обработка нажатия на кнопку "Куртозис"
    @staticmethod
    def kurtosis_click_button(analysis):

        result = analysis.kurtosis()
        messagebox.showinfo("Куртозис", "Куртозис: " + str(result))

    # Обработка нажатия на кнопку "Стандартный коэфифциент"
    @staticmethod
    def standard_ratio_click_button(analysis):

        result = analysis.standard_ratio()
        messagebox.showinfo("Стандартный коэфифциент", "Стандартный коэфифциент: " + str(result))

    # Обработка нажатия на кнопку "Среднеквадратичная ошибка"
    @staticmethod
    def standard_error_click_button(analysis):

        result = analysis.standard_error()
        messagebox.showinfo("Среднеквадратичная ошибка", "Среднеквадратичная ошибка: " + str(result))

    # Обработка нажатия на кнопку "Среднее абсолютное отклонение"
    @staticmethod
    def mean_absolute_deviation_click_button(analysis):

        result = analysis.mean_absolute_deviation()
        messagebox.showinfo("Среднее абсолютное отклонение", "Среднее абсолютное отклонение: " + str(result))

    # Обработка нажатия на кнопку "Минимальный Х"
    @staticmethod
    def x_min_click_button(analysis):

        result = analysis.min_X()
        messagebox.showinfo("Минимальный Х", "Минимальный Х: " + str(result))

    # Обработка нажатия на кнопку "Максимальный Х"
    @staticmethod
    def x_max_click_button(analysis):

        result = analysis.max_X()
        messagebox.showinfo("Максимальный Х", "Максимальный Х: " + str(result))

    def click_button_add_and_close(self, window, choice_of_calculation):

        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика")
            pass

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        if choice_of_calculation == 1:
            self.check_stationarity_click_button(analysis)

        if choice_of_calculation == 2:
            self.average_value_click_button(analysis)

        if choice_of_calculation == 3:
            self.dispersion_click_button(analysis)

        if choice_of_calculation == 4:
            self.dispersion_x_10_click_button(analysis)

        if choice_of_calculation == 5:
            self.standard_deviation(analysis)

        if choice_of_calculation == 6:
            self.asymmetry_click_button(analysis)

        if choice_of_calculation == 7:
            self.asymmetry_coefficient_click_button(analysis)

        if choice_of_calculation == 8:
            self.excess_click_button(analysis)

        if choice_of_calculation == 9:
            self.kurtosis_click_button(analysis)

        if choice_of_calculation == 10:
            self.standard_ratio_click_button(analysis)

        if choice_of_calculation == 11:
            self.mean_absolute_deviation_click_button(analysis)

        if choice_of_calculation == 12:
            self.x_min_click_button(analysis)

        if choice_of_calculation == 13:
            self.x_max_click_button(analysis)

        window.destroy()

    @staticmethod
    def click_button_close(window):
        window.destroy()

    def click_button_bar_graph(self, window):

        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика")
            pass

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        model = analysis.bar_graph()
        model.set_graph(int(self.c2.get()))  # Указали какому графику принадлежит график

        j = 0
        for i in self.graph:
            if i.get_graph() == int(self.c2.get()):
                del self.graph[j]
            j = j + 1

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()

    def click_button_autocorrelation(self, window):

        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика")
            pass

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        model = analysis.autocorrelation()
        model.set_graph(int(self.c2.get()))  # Указали какому графику принадлежит график

        j = 0
        for i in self.graph:
            if i.get_graph() == int(self.c2.get()):
                del self.graph[j]
            j = j + 1

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()

    def click_button_nested_correlation(self, window):

        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика")
            pass

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        model = analysis.nested_correlation()
        model.set_graph(int(self.c2.get()))  # Указали какому графику принадлежит график

        j = 0
        for i in self.graph:
            if i.get_graph() == int(self.c2.get()):
                del self.graph[j]
            j = j + 1

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()

    def click_button_fourier_transform(self, window):

        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика")
            pass

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        model = analysis.fourier_transform()
        model.set_graph(int(self.c2.get()))  # Указали какому графику принадлежит график

        j = 0
        for i in self.graph:
            if i.get_graph() == int(self.c2.get()):
                del self.graph[j]
            j = j + 1

        model.normalization()

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()


    def click_button_shift(self, window):

        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика")
            pass

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        model = analysis.fourier_transform()
        model.set_graph(int(self.c2.get()))  # Указали какому графику принадлежит график

        j = 0
        for i in self.graph:
            if i.get_graph() == int(self.c2.get()):
                del self.graph[j]
            j = j + 1

        model.normalization()

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()

    # Нажатие на клавишу "Вычисления"
    def click_button_calculation1(self):
        a = Toplevel()
        a.title('Вычисления')
        a.geometry('900x500')

        label1 = Label(a, text="Номер графика для анализа", height=1, width=25, font='Arial 14')
        label1.place(x=10, y=10)
        self.c1 = ttk.Combobox(a, values=self._combobox_value, height=4, width="24")
        self.c1.place(x=10, y=30)

        label2 = Label(a, text="Место для вывода анализа", height=1, width=24, font='Arial 14')
        label2.place(x=300, y=10)
        self.c2 = ttk.Combobox(a, values=[u"1", u"2", u"3", u"4"], height=4, width="24")
        self.c2.place(x=300, y=30)

        button_bar_graph = Button(a, text="Гистограмма", command=lambda: self.click_button_bar_graph(a),
                                  width="26", height="2")
        button_bar_graph.place(x=300, y=70)

        button_autocorrelation = Button(a, text="Автокорелляция", command=lambda: self.click_button_autocorrelation(a),
                                        width="26", height="2")
        button_autocorrelation.place(x=300, y=110)

        button_nested_correlation = Button(a, text="Взаимная корелляция",
                                           command=lambda: self.click_button_nested_correlation(a),
                                           width="26", height="2")
        button_nested_correlation.place(x=300, y=150)

        button_fourier_transform = Button(a, text="Преобразование фурье",
                                           command=lambda: self.click_button_fourier_transform(a),
                                           width="26", height="2")
        button_fourier_transform.place(x=300, y=190)

        button_anti_shift = Button(a, text="Антисдвиг",
                                          command=lambda: self.click_button_fourier_transform(a),
                                          width="26", height="2")
        button_anti_shift.place(x=600, y=70)

        button_anti_spike = Button(a, text="Антиспайк",
                                          command=lambda: self.click_button_fourier_transform(a),
                                          width="26", height="2")
        button_anti_spike.place(x=600, y=110)

        button_anti_trend = Button(a, text="Антитренд",
                                   command=lambda: self.click_button_fourier_transform(a),
                                   width="26", height="2")
        button_anti_trend.place(x=600, y=150)

        choice_of_calculation = IntVar()
        choice_of_calculation.set(0)
        stationarity = Radiobutton(a, text='Стационарность: СЗ', variable=choice_of_calculation, value=1)
        average_value = Radiobutton(a, text='Среднее значение', variable=choice_of_calculation, value=2)
        dispersion = Radiobutton(a, text='Дисперсия', variable=choice_of_calculation, value=3)
        dispersion_x_10 = Radiobutton(a, text='Дисперсия x10', variable=choice_of_calculation, value=4)
        standard_deviation = Radiobutton(a, text='Стандартное отклоение', variable=choice_of_calculation, value=5)
        asymmetry = Radiobutton(a, text='Асимметрия', variable=choice_of_calculation, value=6)
        asymmetry_coefficient = Radiobutton(a, text='Коэффициент асимметрии', variable=choice_of_calculation, value=7)
        excess = Radiobutton(a, text='Эксцесс', variable=choice_of_calculation, value=8)
        kurtosis = Radiobutton(a, text='Куртозис', variable=choice_of_calculation, value=9)
        standard_ratio = Radiobutton(a, text='Стандартный коэфифциент', variable=choice_of_calculation, value=10)
        mean_absolute_deviation = Radiobutton(a, text='Среднее абсолютное отклонение', variable=choice_of_calculation,
                                              value=11)
        x_min = Radiobutton(a, text='Минимальный Х', variable=choice_of_calculation, value=12)
        x_max = Radiobutton(a, text='Максимальный Х', variable=choice_of_calculation, value=13)

        stationarity.place(x=10, y=60)
        average_value.place(x=10, y=80)
        dispersion.place(x=10, y=100)
        dispersion_x_10.place(x=10, y=120)
        standard_deviation.place(x=10, y=140)
        asymmetry.place(x=10, y=160)
        asymmetry_coefficient.place(x=10, y=180)
        excess.place(x=10, y=200)
        kurtosis.place(x=10, y=220)
        standard_ratio.place(x=10, y=240)
        mean_absolute_deviation.place(x=10, y=260)
        x_min.place(x=10, y=280)
        x_max.place(x=10, y=300)

        b1 = Button(a, text="Вычислить",
                    command=lambda: self.click_button_add_and_close(a, choice_of_calculation.get()),
                    width="15", height="2")
        b1.place(x=600, y=450)
        b2 = Button(a, text="Закрыть", command=self.click_button_close, width="15", height="2")
        b2.place(x=750, y=450)

        a.grab_set()  # Перехватывает все события происходящие в приложении
        a.focus_set()  # Захватывает и удерживает фокус

    def get_model(self, number_of_trend):
        for i in self.graph:
            g = i.get_graph()
            if g == int(number_of_trend):
                return i

    def init_main_window(self):
        label1 = Label(text="График №1", height=1, width=15, font='Arial 18')
        label1.place(x=165, y=5)

        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_xlim([0, 1000])
        ax.set_ylim([-100, 100])
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=5, y=35)

        label2 = Label(text="График №2", height=1, width=15, font='Arial 18')
        label2.place(x=700, y=5)
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=35)

        label3 = Label(text="График №3", height=1, width=15, font='Arial 18')
        label3.place(x=165, y=360)
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=5, y=400)

        label4 = Label(text="График №4", height=1, width=15, font='Arial 18')
        label4.place(x=700, y=360)
        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=400)

        b2 = Button(text="Добавить", command=self.click_button_add_model, width="26", height="2")
        b2.place(x=1120, y=70)

        b3 = Button(text="Вычисления", command=self.click_button_calculation1, width="26", height="2")
        b3.place(x=1120, y=120)

    def draw_graph(self, model):

        chart_number = str(model.get_graph())
        x = model.get_N()
        y_min = model.get_axis_y_graph_min()
        y_max = model.get_axis_y_graph_max()

        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_xlim([0, x])
        ax.set_ylim([y_min - model.get_argument(), y_max + model.get_argument()])

        ax.plot(model.get_x(), model.get_y(), color='red', label='Линия 1')

        if chart_number == "1":
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=5, y=35)

        if chart_number == "2":
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=550, y=35)

        if chart_number == "3":
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=5, y=400)

        if chart_number == "4":
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=550, y=400)
