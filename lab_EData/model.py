from trend import Trend
from filter import *
from sound import Sound


def sum_trend(trend_1, trend_2):
    trend = Trend()
    trend.y = trend_1.y + trend_2.y
    trend.x = trend_1.x

    return trend


def multi(trend_1, trend_2):
    trend = Trend()
    trend.y = trend_1.y * trend_2.y
    trend.x = trend_1.x

    return trend


def convolution(trend_1, trend_2):
    trend = Trend()

    n = len(trend_1.y)
    m = len(trend_2.y)

    y = []
    for i in range(n):
        y_k = 0
        for j in range(m):
            coefficient_x = i - j
            if coefficient_x >= 0:
                y_m = trend_1.y[coefficient_x] * trend_2.y[j]
            else:
                # y_m = trend_2.y[j]
                y_m = 0
            y_k += y_m

        y.append(y_k)

    trend.y = np.array(y)
    trend.x = trend_1.x

    return trend


class Model:
    def __init__(self, option):
        self.n = 1000  # Количество точек по оси Х
        self.display_n = self.n
        self.flag_checking_display_n = 0    # Флаг использования dislpay_n при отрисовки графика

        self.x = np.arange(0, self.n)
        self.y = np.zeros(self.n)  # Сгенерировали матрицу из нулей

        self.option = option  # Тип функции
        self.graph = 0        # Номер места где расположен график
        self.flag_normalisation = 1  # Флаг, что необходима нормализация

        self.s_max = 100  # Максимальное значение функции
        self.s_min = - self.s_max  # Минимальное значение ф-ии

        self.axis_max = 100
        self.axis_min = -100

        self.axis_y_delta = 10  # Небходимо для самого графика, например:у_min= -(delta+ self.axisy_graph_max)
        self.argument = 0  # Константа на сколько поднять/опустить точки на аномальном участке

        # Гармоничекое процесс
        self.c = 0  # Константа

    # Нормализация осей
    def normalisation_axis(self):
        max_y = np.amax(self.y)
        min_y = np.amin(self.y)

        self.axis_min = min_y * 1.2
        self.axis_max = max_y * 1.2

    # Нормализация
    def normalization(self):

        if self.flag_normalisation == 0:
            return

        self.y = np.array(self.y)

        x_max = np.amax(self.y)
        x_min = np.amin(self.y)
        c = x_max - x_min

        self.y = ((((self.y - x_min) / c) - 0.5) * 2 * self.s_max)

    def shift(self, trend):
        trend.y = trend.y + self.argument

        for i in range(10):
            trend.y[i] = 0

        return trend

    def calculation(self):

        # y(x)=kx+b
        if self.option == 1:
            trend = Trend()
            trend.generating_trend_line()

            self.y = trend.y

        # y(x)=-kx+b
        if self.option == 2:
            trend = Trend()
            trend.generating_trend_line()
            trend.y = np.flip(trend.y)

            self.y = trend.y

        # y(x) = beta * exp^(alpha * i)
        if self.option == 3:
            trend = Trend()
            trend.generating_exhibitor()

            self.y = trend.y

        # y(x) = beta * exp^(alpha * -i)
        if self.option == 4:
            trend = Trend()
            trend.generating_exhibitor()
            trend.y = np.flip(trend.y)

            self.y = trend.y

        # Встроенный рандом
        if self.option == 5:
            trend = Trend()
            trend.generating_trend_random(self.s_min, self.s_max)

            self.y = trend.y

        # Кастомный рандом
        if self.option == 6:
            trend = Trend()
            trend.generating_custom_random()

            self.y = trend.y

        # Рандом + сдвиг
        if self.option == 7:
            trend1 = Trend()
            trend1.generating_trend_random(self.s_min, self.s_max)

            trend = self.shift(trend1)

            self.y = trend.y

            # Указали, что не требуется нормализация
            self.flag_normalisation = 0

        # Значения за областью
        if self.option == 8:
            trend1 = Trend()
            trend1.generating_random_spikes(self.s_min, self.s_max)

            self.y = trend1.y

            # Указали, что не требуется нормализация
            self.flag_normalisation = 0

        # Адитивная модель №1
        if self.option == 9:
            trend1 = Trend()
            trend1.generating_trend_line()
            trend1.y = np.flip(trend1.y)

            trend2 = Trend()
            trend2.generating_trend_random(self.s_min, self.s_max)

            trend = sum_trend(trend1, trend2)

            self.y = trend.y

        # Адитивная модель №2
        if self.option == 10:
            trend1 = Trend()
            trend1.generating_trend_line()

            trend2 = Trend()
            trend2.generating_trend_random(self.s_min, self.s_max)

            trend = sum_trend(trend1, trend2)

            self.y = trend.y

        # Мультипликативная модель №1
        if self.option == 11:
            trend1 = Trend()
            trend1.generating_trend_line()
            trend1.y = np.flip(trend1.y)

            trend2 = Trend()
            trend2.generating_trend_random(self.s_min, self.s_max)

            trend = multi(trend1, trend2)

            self.y = trend.y

        # Мультипликативная модель №2
        if self.option == 12:
            trend1 = Trend()
            trend1.generating_trend_line()

            trend2 = Trend()
            trend2.generating_trend_random(self.s_min, self.s_max)

            trend = multi(trend1, trend2)

            self.y = trend.y

        # График кусочной функции
        if self.option == 13:
            trend = Trend()
            trend.generating_piecewise_function(self.s_min, self.s_max)

            self.y = trend.y

        # График гармонический процесс
        if self.option == 17:
            trend = Trend()
            trend.generating_harmonic_process()

            if self.c != 0:
                self.y = self.y + self.c

            else:
                self.y = trend.y

            self.flag_normalisation = 0
            self.normalisation_axis()

        # График полигармонического процесса
        # x(t) = x1(t) + x2(t) = x3(t)
        # xi(t) = Ai * sin(2piFit)
        # A1 = 25       f1 = 11
        # A2 = 35       f2 = 41
        # A3 = 30       f3 = 141

        if self.option == 19:
            trend1 = Trend()
            trend2 = Trend()
            trend3 = Trend()

            trend1.a_0 = 25
            trend1.f_0 = 11
            trend1.generating_harmonic_process()

            trend2.a_0 = 35
            trend2.f_0 = 41
            trend2.generating_harmonic_process()

            trend3.a_0 = 30
            trend3.f_0 = 141
            trend3.generating_harmonic_process()

            trend4 = sum_trend(trend1, trend2)
            trend = sum_trend(trend4, trend3)

            self.y = trend.y

        # График Рандом + спайки
        if self.option == 20:
            trend_1 = Trend()
            trend_1.generating_trend_random(self.s_min, self.s_max)

            trend_2 = Trend()
            trend_2.generating_random_spikes(self.s_min, self.s_max)

            trend = sum_trend(trend_1, trend_2)

            self.y = trend.y

            self.flag_normalisation = 0
            self.axis_max = np.amax(self.y) * 1.2
            self.axis_min = np.amin(self.y) * 1.2

        # График Гармонический процесс + trend
        if self.option == 25:
            trend_1 = Trend()
            trend_2 = Trend()

            trend_1.generating_harmonic_process()
            trend_2.generating_trend_line()
            trend = sum_trend(trend_1, trend_2)

            self.y = trend.y

        # График Гармонический процесс + спайки
        if self.option == 26:
            trend_1 = Trend()
            trend_2 = Trend()

            trend_1.generating_harmonic_process()
            trend_2.generating_random_spikes(self.s_min, self.s_max)

            trend = sum_trend(trend_1, trend_2)

            self.y = trend.y

            self.flag_normalisation = 0
            self.normalisation_axis()

        # График ГП(гармонический процесс) + спайки + рандом + trend
        if self.option == 27:
            trend_1 = Trend()
            trend_2 = Trend()
            trend_3 = Trend()
            trend_4 = Trend()

            trend_1.generating_harmonic_process()
            trend_2.generating_random_spikes(self.s_min, self.s_max)
            trend_3.generating_trend_random(self.s_min, self.s_max)
            trend_4.generating_trend_line()

            trend = (trend_1, trend_2)
            trend = (trend, trend_3)
            trend = (trend, trend_4)

            self.y = trend.y

            self.flag_normalisation = 0
            self.normalisation_axis()

        # График из файла
        if self.option == 28:
            trend = Trend()
            trend.generating_trend_from_file()

            self.y = trend.y

            self.flag_normalisation = 0
            self.normalisation_axis()

        # График ГП + экспонента
        if self.option == 29:
            self.n = 200
            self.x = np.arange(0, self.n)
            # self.delta_t = 0.005
            # self.display_n = self.n
            self.s_max = 1

            trend_1 = Trend()
            trend_1.n = self.n
            trend_1.x = self.x
            trend_1.delta_t = 0.005
            trend_1.generating_harmonic_process()

            trend_2 = Trend()
            trend_2.n = self.n
            trend_2.x = self.x
            trend_2.generating_exhibitor()

            # Получили тренд сердцебиения
            trend = multi(trend_1, trend_2)
            # self.y = trend.y
            # self.normalization()
            # trend.y = self.y

            self.n = 1000
            trend_3 = Trend()
            trend_3.generating_spikes(100)

            trend = convolution(trend_3, trend)

            self.y = trend.y
            self.x = trend.x
            self.s_max = 100
            self.s_min = - self.s_max

        # Реализация фильтров
        # Низких частот
        if self.option == 30:
            m = 32
            dt = 0.001
            fc = 100
            lpw = filter_potter(m, dt, fc)

            self.n = m
            self.x = np.arange(0, self.n * 2 + 1)
            self.y = lpw
            self.display_n = self.n * 2 + 1

        # Фильтр высоких частот
        if self.option == 31:
            m = 32
            dt = 0.001
            fc = 100

            hpf = high_potter_filter(m, dt, fc)

            self.n = m
            self.x = np.arange(0, self.n * 2 + 1)
            self.y = hpf
            self.display_n = self.n * 2 + 1

        # Звук ma.wav
        if self.option == 34:
            self.name_of_wav_file = "input files/custom.wav"
            sound_trend = Sound(self.name_of_wav_file)

            self.x = sound_trend.x
            self.y = sound_trend.y * self.c
            self.rate = sound_trend.rate

            self.n = len(self.x)
            self.flag_checking_display_n = 1

        # Звук my_voice.wav
        if self.option == 35:
            self.name_of_wav_file = "input files/my_voice.wav"
            sound_trend = Sound(self.name_of_wav_file)

            self.x = sound_trend.x
            self.y = sound_trend.y * self.c
            self.rate = sound_trend.rate

            self.n = len(self.x)
            self.flag_checking_display_n = 1
