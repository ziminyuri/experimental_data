import statistics
from tkinter import *
from tkinter import Menu
from tkinter import filedialog as fd
from tkinter import messagebox, ttk

import pyglet
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from analysis import Analysis
from ChildWindow import ChildWindow
from Image import MyImage as Image
from model import Model


class MainWindow(Frame):
    def __init__(self, root):
        super().__init__(root)

        self.root = root
        self.analysis_model = []  # Список, где храним модели анализа

        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar)
        file_menu.add_command(label="Добавить график", command=self.button_add_graph)
        file_menu.add_command(
            label="Открыть изображение", command=self.button_open_image
        )
        file_menu.add_command(
            label="Открыть звуковой файл", command=self.button_open_sound
        )
        file_menu.add_command(label="Выход", command=self.button_exit)
        menubar.add_cascade(label="Файл", menu=file_menu)

        processing_menu = Menu(menubar)
        processing_menu.add_command(label="Статистики", command=self.button_statistics)
        processing_menu.add_command(label="Фильтры", command=self.button_filter)
        processing_menu.add_command(
            label="Деконволюция", command=self.button_deconvolution
        )
        menubar.add_cascade(label="Обработка", menu=processing_menu)

        """
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
        """

        self.combobox_graph_list = []  # ComboBox графиков для анализа
        self.graph_list = []  # Список объектов модели
        self.analysis_model_list = []  # Список объектов объектов класса Analysis
        self.combobox_analysis_model_list = []  # ComboBox с моделями анализа

    # Меню
    # Файл
    # Добавить график
    def button_add_graph(self):
        ChildWindow(self, self.root)

    # Отркыть изображение
    def button_open_image(self):
        file_name = fd.askopenfilename(
            filetypes=(("JPG files", "*.jpg"), ("All files", "*.*"))
        )
        image = Image(file_name)
        image = image.open()
        self.draw_image(image)

    # Открыть звуковой файл
    def button_open_sound(self):
        a = Toplevel()
        a.title("Звук")
        a.geometry("600x300")

        label_combobox_place_graph = Label(
            a, text="Место для вывода результата", height=1, width=27, font="Arial 14"
        )
        label_combobox_place_graph.place(x=10, y=10)
        self.combobox_place_graph = ttk.Combobox(
            a, values=[u"1", u"2", u"3", u"4"], height=4, width="28"
        )
        self.combobox_place_graph.place(x=10, y=30)

        # Ввод константы
        label_const = Label(a, text="Констанста", height=1, width=10, font="Arial 14")
        label_const.place(x=300, y=10)
        self.input_const_sound = Entry(a, width=28)
        self.input_const_sound.place(x=300, y=30)

        label_combobox_type_of_sound = Label(
            a, text="Выберите звуковой файл", height=1, width=27, font="Arial 14"
        )
        label_combobox_type_of_sound.place(x=10, y=70)
        self.combobox_type_of_sound = ttk.Combobox(
            a, values=[u"ma.wav", u"my_voice.wav"], height=4, width="28"
        )
        self.combobox_type_of_sound.place(x=10, y=100)

        b1 = Button(
            a, text="Выполнить", command=lambda: self.sound(a), width="14", height="2"
        )
        b1.place(x=300, y=250)
        b2 = Button(
            a,
            text="Закрыть",
            command=lambda: self.click_button_close(a),
            width="14",
            height="2",
        )
        b2.place(x=450, y=250)

        a.grab_set()  # Перехватывает все события происходящие в приложении
        a.focus_set()  # Захватывает и удерживает фокус

    # Выход
    def button_exit(self):
        self.quit()

    # Обработка
    # Статистики
    def button_statistics(self):
        a = Toplevel()
        a.title("Вычисления")
        a.geometry("900x500")

        label_combobox_graph = Label(
            a, text="Номер графика для анализа", height=1, width=25, font="Arial 14"
        )
        label_combobox_graph.place(x=10, y=10)
        self.combobox_graph = ttk.Combobox(
            a, values=self.combobox_graph_list, height=4, width="24"
        )
        self.combobox_graph.place(x=10, y=30)

        label2 = Label(
            a, text="Место для вывода анализа", height=1, width=24, font="Arial 14"
        )
        label2.place(x=300, y=10)
        self.c2 = ttk.Combobox(a, values=[u"1", u"2", u"3", u"4"], height=4, width="24")
        self.c2.place(x=300, y=30)

        button_bar_graph = Button(
            a,
            text="Гистограмма",
            command=lambda: self.click_button_bar_graph(a),
            width="26",
            height="2",
        )
        button_bar_graph.place(x=300, y=70)

        button_autocorrelation = Button(
            a,
            text="Автокорелляция",
            command=lambda: self.click_button_autocorrelation(a),
            width="26",
            height="2",
        )
        button_autocorrelation.place(x=300, y=110)

        button_nested_correlation = Button(
            a,
            text="Взаимная корелляция",
            command=lambda: self.click_button_nested_correlation(a),
            width="26",
            height="2",
        )
        button_nested_correlation.place(x=300, y=150)

        # Ввод дельта t
        label_delta_t = Label(a, text="delta T", height=2, width=7, font="Arial 14")
        label_delta_t.place(x=295, y=190)
        self.input_delta_t = Entry(a, width=6)
        self.input_delta_t.place(x=300, y=215)

        button_fourier_transform = Button(
            a,
            text="Преобразование фурье",
            command=lambda: self.click_button_fourier_transform(a),
            width="18",
            height="2",
        )
        button_fourier_transform.place(x=370, y=210)

        button_spectrum = Button(
            a,
            text="Спектр",
            command=lambda: self.click_button_spectrum(a),
            width="26",
            height="2",
        )
        button_spectrum.place(x=300, y=270)

        button_bpf = Button(
            a,
            text="БПФ",
            command=lambda: self.click_button_bpf(a),
            width="26",
            height="2",
        )
        button_bpf.place(x=300, y=330)

        button_anti_shift = Button(
            a,
            text="Антисдвиг",
            command=lambda: self.click_button_anti_shift(a),
            width="26",
            height="2",
        )
        button_anti_shift.place(x=600, y=70)

        button_anti_spike = Button(
            a,
            text="Антиспайк",
            command=lambda: self.click_button_anti_spike(a),
            width="26",
            height="2",
        )
        button_anti_spike.place(x=600, y=110)

        button_anti_trend = Button(
            a,
            text="Антитренд",
            command=lambda: self.click_button_anti_trend(a),
            width="26",
            height="2",
        )
        button_anti_trend.place(x=600, y=150)

        button_anti_trend = Button(
            a,
            text="Антитренд + антиспайк",
            command=lambda: self.click_button_anti_trend_anti_spike(a),
            width="26",
            height="2",
        )
        button_anti_trend.place(x=600, y=190)

        choice_of_calculation = IntVar()
        choice_of_calculation.set(0)
        stationarity = Radiobutton(
            a, text="Стационарность: СЗ", variable=choice_of_calculation, value=1
        )
        average_value = Radiobutton(
            a, text="Среднее значение", variable=choice_of_calculation, value=2
        )
        dispersion = Radiobutton(
            a, text="Дисперсия", variable=choice_of_calculation, value=3
        )
        dispersion_x_10 = Radiobutton(
            a, text="Дисперсия x10", variable=choice_of_calculation, value=4
        )
        standard_deviation = Radiobutton(
            a, text="Стандартное отклоение", variable=choice_of_calculation, value=5
        )
        asymmetry = Radiobutton(
            a, text="Асимметрия", variable=choice_of_calculation, value=6
        )
        asymmetry_coefficient = Radiobutton(
            a, text="Коэффициент асимметрии", variable=choice_of_calculation, value=7
        )
        excess = Radiobutton(a, text="Эксцесс", variable=choice_of_calculation, value=8)
        kurtosis = Radiobutton(
            a, text="Куртозис", variable=choice_of_calculation, value=9
        )
        standard_ratio = Radiobutton(
            a, text="Стандартный коэфифциент", variable=choice_of_calculation, value=10
        )
        mean_absolute_deviation = Radiobutton(
            a,
            text="Среднее абсолютное отклонение",
            variable=choice_of_calculation,
            value=11,
        )
        x_min = Radiobutton(
            a, text="Минимальный Х", variable=choice_of_calculation, value=12
        )
        x_max = Radiobutton(
            a, text="Максимальный Х", variable=choice_of_calculation, value=13
        )

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

        b1 = Button(
            a,
            text="Вычислить",
            command=lambda: self.click_button_add_and_close(
                a, choice_of_calculation.get()
            ),
            width="15",
            height="2",
        )
        b1.place(x=600, y=450)
        b2 = Button(
            a,
            text="Закрыть",
            command=lambda: self.click_button_close(a),
            width="15",
            height="2",
        )
        b2.place(x=750, y=450)

        a.grab_set()  # Перехватывает все события происходящие в приложении
        a.focus_set()  # Захватывает и удерживает фокус

    # Фильтры
    def button_filter(self):
        a = Toplevel()
        a.title("Фильтр")
        a.geometry("600x300")

        label_combobox_graph = Label(
            a, text="Номер графика для фильтрации", height=1, width=28, font="Arial 14"
        )
        label_combobox_graph.place(x=10, y=10)
        self.combobox_graph = ttk.Combobox(
            a, values=self.combobox_graph_list, height=4, width="28"
        )
        self.combobox_graph.place(x=10, y=30)

        label2 = Label(
            a, text="Место для вывода результата", height=1, width=28, font="Arial 14"
        )
        label2.place(x=300, y=10)
        self.combobox_place_graph = ttk.Combobox(
            a, values=[u"1", u"2", u"3", u"4"], height=4, width="28"
        )
        self.combobox_place_graph.place(x=300, y=30)

        label3 = Label(a, text="Тип фильтра", height=1, width=28, font="Arial 14")
        label3.place(x=300, y=70)
        self.combobox_type_filter = ttk.Combobox(
            a,
            values=[u"Низких частот", u"Высоких частот", u"Полосовой", u"Режекторный"],
            height=4,
            width="28",
        )
        self.combobox_type_filter.place(x=300, y=100)

        # Ввод дельта t
        label_delta_t = Label(a, text="delta T", height=2, width=7, font="Arial 14")
        label_delta_t.place(x=10, y=70)
        self.input_delta_t = Entry(a, width=28)
        self.input_delta_t.place(x=10, y=100)

        # Ввод m
        label_m = Label(a, text="m", height=2, width=1, font="Arial 14")
        label_m.place(x=10, y=130)
        self.input_m = Entry(a, width=28)
        self.input_m.place(x=10, y=160)

        # Ввод fc
        label_fc = Label(a, text="fc", height=2, width=2, font="Arial 14")
        label_fc.place(x=10, y=190)
        self.input_fc = Entry(a, width=28)
        self.input_fc.place(x=10, y=220)

        b3 = Button(
            a,
            text="Добавить график фильтра",
            command=lambda: self.click_button_add_graph_filtr(a),
            width="30",
            height="2",
        )
        b3.place(x=300, y=150)

        b1 = Button(
            a,
            text="Выполнить",
            command=lambda: self.filtration(a),
            width="14",
            height="2",
        )
        b1.place(x=300, y=250)
        b2 = Button(
            a,
            text="Закрыть",
            command=lambda: self.click_button_close(a),
            width="14",
            height="2",
        )
        b2.place(x=450, y=250)

        a.grab_set()  # Перехватывает все события происходящие в приложении
        a.focus_set()  # Захватывает и удерживает фокус

    # Деконволюция
    def button_deconvolution(self):
        a = Toplevel()
        a.title("Деконволюция")
        a.geometry("1200x340")

        # Построение графика
        label_build_graph = Label(
            a, text="Построение графика", height=1, width=18, font="Arial 18"
        )
        label_build_graph.place(x=2, y=10)
        label_combobox_type_of_function = Label(
            a, text="Выберите функция", height=1, width=16, font="Arial 14"
        )
        label_combobox_type_of_function.place(x=10, y=40)
        self.combobox_type_of_function = ttk.Combobox(
            a,
            values=[u"Input:кардиограмма", u"Output:кардиограмма"],
            height=2,
            width="28",
        )
        self.combobox_type_of_function.place(x=10, y=60)

        # Построение спектра
        label_spectrum = Label(
            a, text="Построение спектра", height=1, width=18, font="Arial 18"
        )
        label_spectrum.place(x=300, y=10)
        label_combobox_graph = Label(
            a, text="Номер графика для спектра", height=1, width=25, font="Arial 14"
        )
        label_combobox_graph.place(x=300, y=40)
        self.combobox_graph = ttk.Combobox(
            a, values=self.combobox_graph_list, height=4, width="28"
        )
        self.combobox_graph.place(x=300, y=60)

        # Деконволюция
        label_deconvolution = Label(
            a, text="Деконволюция", height=1, width=12, font="Arial 18"
        )
        label_deconvolution.place(x=600, y=10)
        label_model_1 = Label(a, text="Модель №1", height=1, width=9, font="Arial 14")
        label_model_1.place(x=600, y=40)
        self.combobox_analysis_model_1 = ttk.Combobox(
            a,
            values=[u"Input:кардиограмма", u"Output:кардиограмма"],
            height=4,
            width="28",
        )
        self.combobox_analysis_model_1.place(x=600, y=60)
        label_model_2 = Label(a, text="Модель №2", height=1, width=9, font="Arial 14")
        label_model_2.place(x=600, y=100)
        self.combobox_analysis_model_2 = ttk.Combobox(
            a,
            values=[u"Input:кардиограмма", u"Output:кардиограмма"],
            height=4,
            width="28",
        )
        self.combobox_analysis_model_2.place(x=600, y=120)

        # Область запроса результата
        label_result = Label(
            a, text="Запрос результата", height=1, width=17, font="Arial 18"
        )
        label_result.place(x=900, y=10)
        label_combobox_place_graph = Label(
            a, text="Место для вывода результата", height=1, width=27, font="Arial 14"
        )
        label_combobox_place_graph.place(x=900, y=40)
        self.combobox_place_graph = ttk.Combobox(
            a, values=[u"1", u"2", u"3", u"4"], height=4, width="28"
        )
        self.combobox_place_graph.place(x=900, y=60)
        b1 = Button(
            a,
            text="Построить",
            command=lambda: self.task_build(a),
            width="30",
            height="2",
        )
        b1.place(x=900, y=120)

        b2 = Button(
            a,
            text="Спектр",
            command=lambda: self.task_spectrum(a),
            width="30",
            height="2",
        )
        b2.place(x=900, y=170)

        b3 = Button(
            a,
            text="Деконволюция",
            command=lambda: self.task_reverse(a),
            width="30",
            height="2",
        )
        b3.place(x=900, y=220)

        b4 = Button(
            a,
            text="Закрыть",
            command=lambda: self.click_button_close(a),
            width="30",
            height="2",
        )
        b4.place(x=900, y=270)

    # Добавление в комбобокс построенных графиков и в список объектов моделей
    def append_graph_to_list_and_combobox(self, model):
        flag = 0

        for i in self.combobox_graph_list:
            if i == str(model.graph) and flag == 0:
                flag = 1

        if flag == 0:
            self.combobox_graph_list.append(str(model.graph))
            self.combobox_graph_list.sort()

        for i in self.graph_list:
            if i.graph == model.graph:
                i = model
                return

        self.graph_list.append(model)

    # Возвращаем объект модели из списка
    def get_model(self):
        for i in self.graph_list:
            if i.graph == int(self.combobox_graph.get()):
                return i

    def check_empty_combobox_graph(self):
        if self.combobox_graph.get() == "":
            messagebox.showinfo("Ошибка", "Не указан номер графика")
            return 1
        else:
            return 0

    # Закрепляем место вывода за определенным графиком
    @staticmethod
    def set_graph(model, place):
        model.graph = int(place)

    # Получаем объект класса Analysis, если его нет, то инициализируем такой объект
    def get_analysis(self, analyzed_model):
        for i in self.analysis_model_list:
            if i.model == analyzed_model:
                return i

        analysis_model = Analysis(analyzed_model)
        self.analysis_model_list.append(analysis_model)
        return analysis_model

    # Обработка нажатия на кнопку "Вычислить" в окне Вычисления
    def click_button_add_and_close(self, window, choice_of_calculation):

        if self.check_empty_combobox_graph():
            return

        analyzed_model = self.get_model()
        analysis_model = self.get_analysis(analyzed_model)

        if choice_of_calculation == 1:
            statistics.check_stationarity_click_button(analysis_model)

        if choice_of_calculation == 2:
            statistics.average_value_click_button(analysis_model)

        if choice_of_calculation == 3:
            statistics.dispersion_click_button(analysis_model)

        if choice_of_calculation == 4:
            statistics.dispersion_x_10_click_button(analysis_model)

        if choice_of_calculation == 5:
            statistics.standard_deviation(analysis_model)

        if choice_of_calculation == 6:
            statistics.asymmetry_click_button(analysis_model)

        if choice_of_calculation == 7:
            statistics.asymmetry_coefficient_click_button(analysis_model)

        if choice_of_calculation == 8:
            statistics.excess_click_button(analysis_model)

        if choice_of_calculation == 9:
            statistics.kurtosis_click_button(analysis_model)

        if choice_of_calculation == 10:
            statistics.standard_ratio_click_button(analysis_model)

        if choice_of_calculation == 11:
            statistics.mean_absolute_deviation_click_button(analysis_model)

        if choice_of_calculation == 12:
            statistics.x_min_click_button(analysis_model)

        if choice_of_calculation == 13:
            statistics.x_max_click_button(analysis_model)

        window.destroy()

    # Обрабатывает событие закрытия окна
    @staticmethod
    def click_button_close(window):
        window.destroy()

    def click_button_bar_graph(self, window):

        if self.check_empty_combobox_graph():
            return

        analysis_model = self.get_model()
        analysis = Analysis(analysis_model)

        model = analysis.calculation_bar_graph()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        # self.graph_array.append(model)
        self.draw_graph(model)

        window.destroy()

    def click_button_autocorrelation(self, window):

        if self.check_empty_combobox_graph():
            return

        analysis_model = self.get_model()
        analysis = Analysis(analysis_model)

        model = analysis.calculation_autocorrelation()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        # self.graph_array.append(model)
        self.append_graph_to_list_and_combobox(model)
        self.draw_graph(model)

        window.destroy()

    def click_button_nested_correlation(self, window):

        if self.check_empty_combobox_graph():
            return

        analysis_model = self.get_model()
        analysis = Analysis(analysis_model)

        model = analysis.calculation_nested_correlation()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        # self.graph_array.append(model)
        self.draw_graph(model)

        window.destroy()

    def click_button_fourier_transform(self, window):

        if self.check_empty_combobox_graph():
            return

        analysis_model = self.get_model()

        if self.input_delta_t.get():
            delta_t = float(self.input_delta_t.get())
        else:
            delta_t = 0.001

        analysis = Analysis(analysis_model)
        analysis.set_delta_t(delta_t)
        model = analysis.calculation_fourier_transform()

        n = model.n
        model.display_n = int(n / 2)
        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        # model.normalization()

        # self.graph_array.append(model)
        self.draw_graph(model)

        window.destroy()

    # Обработка нажатия по кнопке спектр - Рассчет преобразования фурье через библиотеки Python (для звука)
    def click_button_spectrum(self, window):
        if self.check_empty_combobox_graph():
            return

        analysis_model = self.get_model()
        analysis = Analysis(analysis_model)
        model = analysis.calculation_spectrum()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        self.draw_graph(model)

        window.destroy()

    # Обработка нажатия по кнопке БПФ - Рассчет быстрого преобразования фурье через библиотеки Python (для всех
    # остальных случаев)
    def click_button_bpf(self, window):
        if self.check_empty_combobox_graph():
            return

        analysis_model = self.get_model()
        analysis = Analysis(analysis_model)
        model = analysis.spectrum()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        self.draw_graph(model)
        window.destroy()

    # Нажатие на кнопку антисдвиг
    def click_button_anti_shift(self, window):

        if self.check_empty_combobox_graph():
            return

        analysis_model = self.get_model()
        analysis = Analysis(analysis_model)

        model = analysis.calculation_anti_shift()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        # model.normalization()

        # self.graph_array.append(model)
        self.draw_graph(model)

        window.destroy()

    # Нажатие на кнопку антиспайк
    def click_button_anti_spike(self, window):

        if self.check_empty_combobox_graph():
            return

        analysis_model = self.get_model()
        analysis = Analysis(analysis_model)

        model = analysis.calculation_anti_spike()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        # model.normalization()

        # self.graph_array.append(model)
        self.draw_graph(model)

        window.destroy()

    # Нажатие на кнопку антитренд
    def click_button_anti_trend(self, window):

        if self.check_empty_combobox_graph():
            return

        analysis_model = self.get_model()
        analysis = Analysis(analysis_model)

        model = analysis.calculation_anti_trend()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        # model.normalization()

        # self.graph_array.append(model)
        self.draw_graph(model)

        window.destroy()

    def click_button_shift(self, window):

        if self.check_empty_combobox_graph():
            return

        analysis_model = self.get_model()
        analysis = Analysis(analysis_model)

        model = analysis.calculation_fourier_transform()

        place_of_graph = self.c2.get()
        self.set_graph(model, place_of_graph)

        model.normalization()

        # self.graph_array.append(model)
        self.draw_graph(model)

        window.destroy()

    def click_button_anti_trend_anti_spike(self, window):
        if self.check_empty_combobox_graph():
            return

        analysis_model = self.get_model()
        analysis = Analysis(analysis_model)

        model = analysis.calculation_anti_trend()
        analysis_2 = Analysis(model)
        model.s_without_spikes_min = -300
        model.s_without_spikes_max = 500
        model_2 = analysis_2.calculation_anti_spike_exam()

        place_of_graph = self.c2.get()
        self.set_graph(model_2, place_of_graph)
        self.append_graph_to_list_and_combobox(model_2)

        # model.normalization()

        # self.graph_array.append(model)
        self.draw_graph(model_2)

        window.destroy()

    # Выполнение процесса фильтрация
    def filtration(self, subWindow):
        model = Model(36)
        graph_for_filtration = self.get_model()

        if self.combobox_type_filter.get() == "Низких частот":
            choice_of_filter = 1

        if self.combobox_type_filter.get() == "Высоких частот":
            choice_of_filter = 2

        if self.combobox_type_filter.get() == "Полосовой":
            choice_of_filter = 3

        if self.combobox_type_filter.get() == "Режекторный":
            choice_of_filter = 4

        model.filtration(graph_for_filtration, choice_of_filter)
        model.normalisation_axis()

        place_graph = int(self.combobox_place_graph.get())
        self.set_graph(model, place_graph)
        self.append_graph_to_list_and_combobox(
            model
        )  # Добавили модель в комбобокс для анализа
        self.draw_graph(model)

        subWindow.destroy()

    # Обработка нажатия на кнопку "Добавить график фильтра"
    def click_button_add_graph_filtr(self, subWindow):

        if self.combobox_type_filter.get() == "Низких частот":
            model = Model(30)

        if self.combobox_type_filter.get() == "Высоких частот":
            model = Model(31)

        if self.combobox_type_filter.get() == "Полосовой":
            model = Model(32)

        if self.combobox_type_filter.get() == "Режекторный":
            model = Model(33)

        model.calculation()
        model.normalisation_axis()

        place_graph = int(self.combobox_place_graph.get())
        self.set_graph(model, place_graph)
        self.append_graph_to_list_and_combobox(
            model
        )  # Добавили модель в комбобокс для анализа
        self.draw_graph(model)

        subWindow.destroy()

    # Нажатие на кнопку "Выполнить" в окне Звук
    def sound(self, subWindow):

        if self.combobox_type_of_sound.get() == "ma.wav":
            model = Model(34)

        if self.combobox_type_of_sound.get() == "my_voice.wav":
            model = Model(35)

        if self.input_const_sound.get() == "":
            const = 1
        else:
            const = float(self.input_const_sound.get())

        model.c = const

        model.calculation()
        model.normalisation_axis()

        place_graph = int(self.combobox_place_graph.get())
        self.set_graph(model, place_graph)

        self.append_graph_to_list_and_combobox(
            model
        )  # Добавили модель в комбобокс для анализа
        self.draw_graph(model)
        self.add_button_play(model)

        subWindow.destroy()

    @staticmethod
    def play(model):
        """
        music = pyglet.resource.media(model.name_of_wav_file)
        music.play()

        pyglet.app.run()
        """
        pyglet.options["audio"] = ("openal", "pulse", "directsound", "silent")
        source = pyglet.media.StaticSource(pyglet.media.load(model.name_of_wav_file))

        player = pyglet.media.Player()
        player.queue(source)
        player.EOS_LOOP = "loop"
        player.play()

        pyglet.app.run()

        event_loop = pyglet.app.EventLoop()

    # Выводим спектры из окна "Деконволюция"
    def task_spectrum(self, window):

        analysis_model = self.get_model()
        analysis = Analysis(analysis_model)

        model = analysis.calculation_fourier_transform()

        place_of_graph = self.combobox_place_graph.get()
        self.set_graph(model, place_of_graph)

        model.normalization()

        # self.graph_array.append(model)
        self.draw_graph(model)

        window.destroy()

    # Выводим графики функции по нажатию на клавишу "Построить" из окна "Деконволюция"
    def task_build(self, window):
        type_of_function = self.combobox_type_of_function.get()
        if type_of_function == "Input:кардиограмма":
            model = Model(37)

        elif type_of_function == "Output:кардиограмма":
            model = Model(29)

        model.calculation()

        model.normalisation_axis()

        place_graph = int(self.combobox_place_graph.get())
        self.set_graph(model, place_graph)

        self.append_graph_to_list_and_combobox(
            model
        )  # Добавили модель в комбобокс для анализа
        self.draw_graph(model)

        window.destroy()

    # Вычисляем новый график
    def task_reverse(self, windows):

        windows.destroy()

    def draw_image(self, image):
        panel = Label(self.root, image=image)
        panel.place(x=10, y=10)

    def draw_graph(self, model):

        chart_number = str(model.graph)

        # y_min = model.axis_min
        # y_max = model.axis_max

        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)

        if model.flag_checking_display_x == 1:
            x_list = model.display_x
            y_list = model.display_y
            # x_max = np.amax(x_list)
            # ax.set_xlim([0, x_max])
        else:
            x_list = model.x
            y_list = model.y

        if model.flag_checking_display_n == 1:
            x = model.display_n
            ax.set_xlim([0, x])
        # ax.set_ylim([y_min, y_max])

        ax.plot(x_list, y_list, color="red", label="Линия 1")

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

    def add_button_play(self, model):
        chart_number = str(model.graph)

        if chart_number == "1":
            self.button_play_sound = Button(
                text="Воспроизведение",
                command=lambda: self.play(model),
                width="14",
                height="2",
            )
            self.button_play_sound.place(x=330, y=20)

        if chart_number == "2":
            self.button_play_sound = Button(
                text="Воспроизведение",
                command=lambda: self.play(model),
                width="14",
                height="2",
            )
            self.button_play_sound.place(x=870, y=20)

        if chart_number == "3":
            self.button_play_sound = Button(
                text="Воспроизведение",
                command=lambda: self.play(model),
                width="14",
                height="2",
            )
            self.button_play_sound.place(x=330, y=390)

        if chart_number == "4":
            b1 = Button(
                text="Воспроизведение",
                command=lambda: self.play(model),
                width="14",
                height="2",
            )
            b1.place(x=870, y=390)
