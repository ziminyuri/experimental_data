from tkinter import *
from tkinter import messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from lab_EData.ChildWindow import ChildWindow
from lab_EData.analysis import Analysis
from lab_EData.model import Model


class MainWindow(Frame):
    def __init__(self, root):
        super().__init__(root)

        self.root = root
        self.graph = []
        self.analysis_model = []  # Список, где храним модели анализа

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

        button_filter = Button(text="Фильтр", command=self.click_button_filter, width="26", height="2")
        button_filter.place(x=1120, y=170)

        button_sound = Button(text="Звук", command=self.click_button_sound, width="26", height="2")
        button_sound.place(x=1120, y=220)

        self.combobox_value = []  # ComboBox графиков для анализа

    def click_button_add_model(self):
        ChildWindow(self, self.root, self.graph)

    def get_analysis(self, analysis_model):

        flag_we_have_already_analysis_model = 0
        if self.analysis_model:
            for i in self.analysis_model:
                if i.model == analysis_model:
                    analysis = i
                    flag_we_have_already_analysis_model = 1

        if flag_we_have_already_analysis_model == 0:
            analysis = Analysis(analysis_model)
            self.analysis_model.append(analysis)

        return analysis

    def check_empty_c1(self):
        if self.c1.get() == "":
            messagebox.showinfo("Ошибка", "Не указан номер графика")
            return 1
        else:
            return 0

    # Указали какому графику принадлежит график и добавили в combobox
    def set_graph(self, model, place_of_graph):
        model.graph = int(place_of_graph)

        j = 0
        for i in self.graph:
            if i.graph == int(place_of_graph):
                del self.graph[j]
            j = j + 1


    def get_model(self, number_of_trend):
        for i in self.graph:
            g = i.graph
            if g == int(number_of_trend):
                return i

    def set_combobox_value_of_graph(self, value):

        flag = 0                                # Переменная не встречается в массиве
        for i in range(self.combobox_value):

            if i == value:
                flag = 1

        if flag is 0:
            self.combobox_value.append(value)


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

        check_result = analysis.calculation_dispersion(1)
        messagebox.showinfo("Дисперсия", "Дисперсия: " + str(check_result))

    # Обработка нажатия на кнопку "Дисперсия х10"
    @staticmethod
    def dispersion_x_10_click_button(analysis):

        check_result = analysis.calculation_dispersion(10)
        messagebox.showinfo("Дисперсия", "Дисперсия x10: " + str(check_result))

    # Обработка нажатия на кнопку "Среднее значение"
    @staticmethod
    def average_value_click_button(analysis):

        check_result = analysis.calculation_average_value()
        messagebox.showinfo("Среднее значение", "Среднее значение: " + str(check_result))

    # Обработка нажатия на кнопку "Асимметрия"
    @staticmethod
    def asymmetry_click_button(analysis):

        result = analysis.calculation_asymmetry()
        messagebox.showinfo("Ассиметрия", "Ассиметрия: " + str(result))

    # Обработка нажатия на кнопку "Стандартное отклонение"
    @staticmethod
    def standard_deviation(analysis):

        result = analysis.calculation_standard_deviation()
        messagebox.showinfo("Стандартное отклонение", "Стандартное отклонение: " + str(result))

    # Обработка нажатия на кнопку "Коэффициент асимметрии"
    @staticmethod
    def asymmetry_coefficient_click_button(analysis):

        result = analysis.calculation_asymmetry_coefficient()
        messagebox.showinfo("Коэффициент асимметрии", "Коэффициент асимметрии: " + str(result))

    # Обработка нажатия на кнопку "Эксцесс"
    @staticmethod
    def excess_click_button(analysis):

        result = analysis.calculation_excess()
        messagebox.showinfo("Эксцесс", "Эксцесс: " + str(result))

    # Обработка нажатия на кнопку "Куртозис"
    @staticmethod
    def kurtosis_click_button(analysis):

        result = analysis.calculation_kurtosis()
        messagebox.showinfo("Куртозис", "Куртозис: " + str(result))

    # Обработка нажатия на кнопку "Стандартный коэфифциент"
    @staticmethod
    def standard_ratio_click_button(analysis):

        result = analysis.calculation_standard_ratio()
        messagebox.showinfo("Стандартный коэфифциент", "Стандартный коэфифциент: " + str(result))

    # Обработка нажатия на кнопку "Среднеквадратичная ошибка"
    @staticmethod
    def standard_error_click_button(analysis):

        result = analysis.calculation_standard_error()
        messagebox.showinfo("Среднеквадратичная ошибка", "Среднеквадратичная ошибка: " + str(result))

    # Обработка нажатия на кнопку "Среднее абсолютное отклонение"
    @staticmethod
    def mean_absolute_deviation_click_button(analysis):

        result = analysis.calculation_mean_absolute_deviation()
        messagebox.showinfo("Среднее абсолютное отклонение", "Среднее абсолютное отклонение: " + str(result))

    # Обработка нажатия на кнопку "Минимальный Х"
    @staticmethod
    def x_min_click_button(analysis):

        result = analysis.calculation_min_x()
        messagebox.showinfo("Минимальный Х", "Минимальный Х: " + str(result))

    # Обработка нажатия на кнопку "Максимальный Х"
    @staticmethod
    def x_max_click_button(analysis):

        result = analysis.calculation_max_x()
        messagebox.showinfo("Максимальный Х", "Максимальный Х: " + str(result))

    def click_button_add_and_close(self, window, choice_of_calculation):

        if self.check_empty_c1():
            return

        analysis_model = self.get_model(self.c1.get())
        analysis = self.get_analysis(analysis_model)

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

        if self.check_empty_c1():
            return

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        model = analysis.calculation_bar_graph()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()

    def click_button_autocorrelation(self, window):

        if self.check_empty_c1():
            return

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        model = analysis.calculation_autocorrelation()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()

    def click_button_nested_correlation(self, window):

        if self.check_empty_c1():
            return

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        model = analysis.calculation_nested_correlation()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()

    def click_button_fourier_transform(self, window):

        if self.check_empty_c1():
            return

        analysis_model = self.get_model(self.c1.get())

        if self.input_delta_t.get():
            delta_t = float(self.input_delta_t.get())
        else:
            delta_t = 0.001

        analysis = Analysis(analysis_model, delta_t)

        model = analysis.calculation_fourier_transform()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        # model.normalization()

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()

    # Нажатие на кнопку антисдвиг
    def click_button_anti_shift(self, window):

        if self.check_empty_c1():
            return

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        model = analysis.calculation_anti_shift()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        # model.normalization()

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()

    # Нажатие на кнопку антиспайк
    def click_button_anti_spike(self, window):

        if self.check_empty_c1():
            return

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        model = analysis.calculation_anti_spike()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        # model.normalization()

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()

    # Нажатие на кнопку антитренд
    def click_button_anti_trend(self, window):

        if self.check_empty_c1():
            return

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        model = analysis.calculation_anti_trend()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        # model.normalization()

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()

    def click_button_shift(self, window):

        if self.check_empty_c1():
            return

        analysis_model = self.get_model(self.c1.get())
        analysis = Analysis(analysis_model)

        model = analysis.calculation_fourier_transform()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        model.normalization()

        self.graph.append(model)
        self.draw_graph(model)

        window.destroy()

    # Выполнение процесса фильтрация
    def filtration(self, subWindow):
        choice_of_filtration = self.combobox_type_filter.get()

        if choice_of_filtration == "Низких частот":
            model = Model(30)

        if choice_of_filtration == "Высоких частот":
            model = Model(31)

        if choice_of_filtration == "Полосовой":
            model = Model(32)

        if choice_of_filtration == "Режекторный":
            model = Model(33)

        model.calculation()
        model.normalisation_axis()

        place_graph = int(self.combobox_place_graph.get())
        self.set_graph(model, place_graph)

        self.draw_graph(model)

        subWindow.destroy()

    def sound(self, subWindow):
        model = Model(34)

        if self.input_const_sound.get() == "":
            const = 1
        else:
            const = float(self.input_const_sound.get())

        model.c = const

        model.calculation()
        model.normalisation_axis()

        place_graph = int(self.combobox_place_graph.get())
        self.set_graph(model, place_graph)

        self.draw_graph(model)

        subWindow.destroy()


    # Нажатие на клавишу "Вычисления"
    def click_button_calculation1(self):
        a = Toplevel()
        a.title('Вычисления')
        a.geometry('900x500')

        label1 = Label(a, text="Номер графика для анализа", height=1, width=25, font='Arial 14')
        label1.place(x=10, y=10)
        self.c1 = ttk.Combobox(a, values=self.combobox_value, height=4, width="24")
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

        # Ввод дельта t
        label_delta_t = Label(a, text="delta T", height=2, width=7, font='Arial 14')
        label_delta_t.place(x=295, y=190)
        self.input_delta_t = Entry(a, width=6)
        self.input_delta_t.place(x=300, y=215)

        button_fourier_transform = Button(a, text="Преобразование фурье",
                                          command=lambda: self.click_button_fourier_transform(a),
                                          width="18", height="2")
        button_fourier_transform.place(x=370, y=210)

        button_anti_shift = Button(a, text="Антисдвиг",
                                   command=lambda: self.click_button_anti_shift(a),
                                   width="26", height="2")
        button_anti_shift.place(x=600, y=70)

        button_anti_spike = Button(a, text="Антиспайк",
                                   command=lambda: self.click_button_anti_spike(a),
                                   width="26", height="2")
        button_anti_spike.place(x=600, y=110)

        button_anti_trend = Button(a, text="Антитренд",
                                   command=lambda: self.click_button_anti_trend(a),
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

    # Нажатие на клавишу "Фильтр" в главном окне
    def click_button_filter(self):
        a = Toplevel()
        a.title('Фильтр')
        a.geometry('600x300')

        label1 = Label(a, text="Номер графика для фильтрации", height=1, width=28, font='Arial 14')
        label1.place(x=10, y=10)
        self.c1 = ttk.Combobox(a, values=self.combobox_value, height=4, width="28")
        self.c1.place(x=10, y=30)

        label2 = Label(a, text="Место для вывода результата", height=1, width=28, font='Arial 14')
        label2.place(x=300, y=10)
        self.combobox_place_graph = ttk.Combobox(a, values=[u"1", u"2", u"3", u"4"], height=4, width="28")
        self.combobox_place_graph.place(x=300, y=30)

        label3 = Label(a, text="Тип фильтра", height=1, width=28, font='Arial 14')
        label3.place(x=300, y=70)
        self.combobox_type_filter = ttk.Combobox(a, values=[u"Низких частот", u"Высоких частот", u"Полосовой",
                                                            u"Режекторный"], height=4, width="28")
        self.combobox_type_filter.place(x=300, y=100)

        # Ввод дельта t
        label_delta_t = Label(a, text="delta T", height=2, width=7, font='Arial 14')
        label_delta_t.place(x=10, y=70)
        self.input_delta_t = Entry(a, width=28)
        self.input_delta_t.place(x=10, y=100)

        # Ввод m
        label_m = Label(a, text="m", height=2, width=1, font='Arial 14')
        label_m.place(x=10, y=130)
        self.input_m = Entry(a, width=28)
        self.input_m.place(x=10, y=160)

        # Ввод fc
        label_fc = Label(a, text="fc", height=2, width=2, font='Arial 14')
        label_fc.place(x=10, y=190)
        self.input_fc = Entry(a, width=28)
        self.input_fc.place(x=10, y=220)

        b1 = Button(a, text="Выполнить",
                    command=lambda: self.filtration(a), width="14", height="2")
        b1.place(x=300, y=250)
        b2 = Button(a, text="Закрыть", command=lambda: self.click_button_close(a), width="14", height="2")
        b2.place(x=450, y=250)

        a.grab_set()  # Перехватывает все события происходящие в приложении
        a.focus_set()  # Захватывает и удерживает фокус

    # Нажатие на клавишу "Звук" в главном окне
    def click_button_sound(self):
        a = Toplevel()
        a.title('Звук')
        a.geometry('600x300')

        label2 = Label(a, text="Место для вывода результата", height=1, width=28, font='Arial 14')
        label2.place(x=10, y=10)
        self.combobox_place_graph = ttk.Combobox(a, values=[u"1", u"2", u"3", u"4"], height=4, width="28")
        self.combobox_place_graph.place(x=10, y=30)

        # Ввод константы
        label_const= Label(a, text="Констанста", height=2, width=7, font='Arial 14')
        label_const.place(x=10, y=70)
        self.input_const_sound = Entry(a, width=28)
        self.input_const_sound.place(x=10, y=100)

        b1 = Button(a, text="Выполнить", command=lambda: self.sound(a), width="14", height="2")
        b1.place(x=300, y=250)
        b2 = Button(a, text="Закрыть", command=lambda: self.click_button_close(a), width="14", height="2")
        b2.place(x=450, y=250)

        a.grab_set()  # Перехватывает все события происходящие в приложении
        a.focus_set()  # Захватывает и удерживает фокус

    def draw_graph(self, model):

        chart_number = str(model.graph)
        # x = model.display_n
        # y_min = model.axis_min
        # y_max = model.axis_max

        x_list = model.x
        y_list = model.y

        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        # ax.set_xlim([0, x])
        # ax.set_ylim([y_min, y_max])

        ax.plot(x_list, y_list, color='red', label='Линия 1')

        canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        canvas.draw()

        if chart_number == "1":
            canvas.get_tk_widget().place(x=5, y=35)

        if chart_number == "2":
            canvas.get_tk_widget().place(x=550, y=35)

        if chart_number == "3":
            canvas.get_tk_widget().place(x=5, y=400)

        if chart_number == "4":
            canvas.get_tk_widget().place(x=550, y=400)
