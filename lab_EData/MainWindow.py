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

    def click_button_add_model(self):

        ChildWindow(self, self.root, self.graph)

    # Обработка нажатия на кнопку "Стационарность: СЗ"
    def check_stationarity_click_button(self):

        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика","Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                check_result = i.check_stationarity_average_value()

        if check_result == True:
            messagebox.showinfo("Проверка на стационарность: Среднее значение","График стационарен")
        else:
            messagebox.showinfo("Проверка на стационарность: Среднее значение","График не стационарен")

    # Обработка нажатия на кнопку "Диспресия"
    def dispersion_click_button(self):

        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика","Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                check_result = i.dispersion(1)

        messagebox.showinfo("Дисперсия", "Дисперсия: " + str(check_result))

        self._b7['state'] = 'normal'  # Активирование кнопки "Стандартное отклонение"

    # Обработка нажатия на кнопку "Дисперсия х10"
    def dispersion_x_10_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика","Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                check_result = i.dispersion(10)

        messagebox.showinfo("Дисперсия", "Дисперсия x10: " + str(check_result))

        self._b7['state'] = 'normal'  # Активирование кнопки "Стандартное отклонение"

    # Обработка нажатия на кнопку "Среднее значение"
    def average_value_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика","Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                check_result = i.average_value()

        messagebox.showinfo("Среднее значение", "Среднее значение: " + str(check_result))

        self._button_asymmetry['state'] = 'normal'  # Активирование кнопки "Асимметрия"
        self._button_excess['state'] = 'normal'     # Активирование кнопки "Эксцесс"

    # Обработка нажатия на кнопку "Асимметрия"
    def asymmetry_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика","Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                result = i.asymmetry()

                check_button_asymmetry_coefficient = i.check_asymmetry_and_standard_deviation()
                if check_button_asymmetry_coefficient == True:
                    self._button_asymmetry_coefficient[
                        'state'] = 'normal'                    # Активирование кнопки "Коэффициент асимметрии"

                check_button_kurtosis = i.check_excess_and_standard_deviation()
                if check_button_kurtosis == True:
                    self._button_kurtosis['state'] = 'normal'  # Активирование кнопки "Куртозиса"

        messagebox.showinfo("Ассиметрия", "Ассиметрия: " + str(result))

    # Обработка нажатия на кнопку "Стандартное отклонение"
    def standard_deviation(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика","Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                result = i.standard_deviation()

                check_button_asymmetry_coefficient = i.check_asymmetry_and_standard_deviation()
                if check_button_asymmetry_coefficient == True:
                    self._button_asymmetry_coefficient[
                        'state'] = 'normal'  # Активирование кнопки "Коэффициент асимметрии"

                check_button_kurtosis = i.check_excess_and_standard_deviation()
                if check_button_kurtosis == True:
                    self._button_kurtosis['state'] = 'normal'  # Активирование кнопки "Куртозиса"

        messagebox.showinfo("Стандартное отклонение", "Стандартное отклонение: " + str(result))

    # Обработка нажатия на кнопку "Коэффициент асимметрии"
    def asymmetry_coefficient_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика", "Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                result = i.asymmetry_coefficient()

        messagebox.showinfo("Коэффициент асимметрии", "Коэффициент асимметрии: " + str(result))

    # Обработка нажатия на кнопку "Эксцесс"
    def excess_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика", "Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                result = i.excess()

        messagebox.showinfo("Эксцесс", "Эксцесс: " + str(result))

    # Обработка нажатия на кнопку "Куртозис"
    def kurtosis_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика", "Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                result = i.kurtosis()

        messagebox.showinfo("Куртозис", "Куртозис: " + str(result))

    # Обработка нажатия на кнопку "Стандартный коэфифциент"
    def standard_ratio_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика", "Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                result = i.kurtosis()

        messagebox.showinfo("Стандартный коэфифциент", "Стандартный коэфифциент: " + str(result))

    # Обработка нажатия на кнопку "Среднеквадратичная ошибка"
    def standard_error_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика", "Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                result = i.kurtosis()

        messagebox.showinfo("Среднеквадратичная ошибка", "Среднеквадратичная ошибка: " + str(result))

    # Обработка нажатия на кнопку "Среднее абсолютное отклонение"
    def mean_absolute_deviation_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика", "Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                result = i.kurtosis()

        messagebox.showinfo("Среднее абсолютное отклонение", "Среднее абсолютное отклонение: " + str(result))

    # Обработка нажатия на кнопку "Минимальный Х"
    def x_min_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика", "Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                result = i.kurtosis()

        messagebox.showinfo("Минимальный Х", "Минимальный Х: " + str(result))

    # Обработка нажатия на кнопку "Максимальный Х"
    def x_max_click_button(self):
        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика", "Не указан номер графика")
            pass

        for i in (self.graph):
            if i.get_graph() == int(self.c1.get()):
                result = i.kurtosis()

        messagebox.showinfo("Максимальный Х", "Максимальный Х: " + str(result))

    def click_button_add_and_close(self, window, choice_of_calculation):


        if choice_of_calculation == 1:
            self.check_stationarity_click_button()

        if choice_of_calculation == 2:
            self.average_value_click_button()

        if choice_of_calculation == 3:
            self.dispersion_click_button()

        if choice_of_calculation == 4:
            self.dispersion_x_10_click_button()

        if choice_of_calculation == 5:
            self.standard_deviation()

        if choice_of_calculation == 6:
            self.asymmetry_click_button()

        if choice_of_calculation == 7:
            self.asymmetry_coefficient_click_button()

        if choice_of_calculation == 8:
            self.excess_click_button()

        if choice_of_calculation == 9:
            self.kurtosis_click_button()

        if choice_of_calculation == 10:
            self.asymmetry_click_button()

        if choice_of_calculation == 11:
            self.asymmetry_click_button()

        window.destroy()

    def click_button_close(self, window):
        window.destroy()

    def click_button_calculation1(self):
        a = Toplevel()
        a.title('Вычисления')
        a.geometry('600x400')
        label1 = Label(a, text="Номер графика", height=1, width=14, font='Arial 14')
        label1.place(x=10, y=10)
        self.c1 = ttk.Combobox(a, values=[u"1", u"2", u"3", u"4"], height=4, width="24")
        self.c1.place(x=10, y=30)

        choice_of_calculation = BooleanVar()
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
        b1.place(x=300, y=350)
        b2 = Button(a, text="Закрыть", command=self.click_button_close, width="15", height="2")
        b2.place(x=450, y=350)

        """
        button_stationarity = Button(a, text="Стационарность: СЗ", command=self.check_stationarity_click_button, width="26",
                          height="2",state=DISABLED)
        button_stationarity.place(x=10, y=60)

        b4 = Button(a, text="Среднее значение", command=self.average_value_click_button, width="26", height="2",
                          state=DISABLED)
        b4.place(x=10, y=270)

        b5 = Button(a, text="Дисперсия", command=self.dispersion_click_button, width="26", height="2",
                          state=DISABLED)
        b5.place(x=10, y=320)

        b6 = Button(a, text="Дисперсия x10", command=self.dispersion_x_10_click_button, width="26",
                          height="2", state=DISABLED)
        b6.place(x=10, y=370)

        b7 = Button(a, text="Стандартное отклоение", command=self.standard_deviation, width="26",
                          height="2", state=DISABLED)
        b7.place(x=10, y=420)

        button_asymmetry = Button(a, text="Асимметрия", command=self.asymmetry_click_button, width="26", height="2",
                                        state=DISABLED)
        button_asymmetry.place(x=10, y=470)

        button_asymmetry_coefficient = Button(a, text="Коэффициент асимметрии",
                                                    command=self.asymmetry_coefficient_click_button,
                                                    width="26", height="2", state=DISABLED)
        button_asymmetry_coefficient.place(x=10, y=520)

        button_excess = Button(a, text="Эксцесс", command=self.excess_click_button, width="26", height="2",
                                     state=DISABLED)
        button_excess.place(x=10, y=570)

        button_kurtosis = Button(a, text="Куртозис", command=self.kurtosis_click_button, width="26", height="2",
                                       state=DISABLED)
        button_kurtosis.place(x=10, y=620)

        standard_ratio = Button(a, text="Стандартный коэфифциент", command=self.kurtosis_click_button,
                                      width="26", height="2", state=DISABLED)
        standard_ratio.place(x=10, y=670)

        standard_error = Button(a, text="Среднеквадратичная ошибка", command=self.kurtosis_click_button, width="26",
                                      height="2", state=DISABLED)
        standard_error.place(x=10, y=720)

        mean_absolute_deviation = Button(text="Среднее абсолютное отклонение",
                                               command=self.kurtosis_click_button, width="26", height="2",
                                               state=DISABLED)
        mean_absolute_deviation.place(x=10, y=770)

        x_min = Button(text="Минимальный Х", command=self.kurtosis_click_button, width="26",
                             height="2", state=DISABLED)
        x_min.place(x=10, y=820)

        """

        a.grab_set()  # Перехватывает все события происходящие в приложении
        a.focus_set()  # Захватывает и удерживает фокус

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

        b2 = Button(text="Добавить", command=self.click_button_add_model, width="26", height="2")
        b2.place(x=1120, y=70)

        b3 = Button(text="Вычисления", command=self.click_button_calculation1, width="26", height="2")
        b3.place(x=1120, y=120)

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
