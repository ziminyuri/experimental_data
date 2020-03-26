import numpy as np

from sound import Sound
from trend import Trend


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


def convolution_img(img: np.ndarray, my_filter: np.ndarray) -> np.ndarray:
    n: int = len(img)
    m: int = len(my_filter)

    y: list = []
    for i in range(n):
        y_k: int = 0
        for j in range(m):
            coefficient_x: int = i - j
            if coefficient_x >= 0:
                y_m = img[coefficient_x] * my_filter[j]
            else:
                y_m = 0
            y_k += y_m

        y.append(y_k)

    img_after_filtration = np.array(y)
    return img_after_filtration


class Model:
    def __init__(self, option, m=32, fc_1=60, fc_2=80, delta_t=0.001):
        self.n = 1000  # Количество точек по оси Х
        self.display_n = self.n
        self.flag_checking_display_n = 0  # Флаг использования dislpay_n при отрисовки графика

        self.x = np.arange(0, self.n)
        self.y = np.zeros(self.n)  # Сгенерировали матрицу из нулей
        self.flag_checking_display_x = 0  # Флаг использования половины self.x

        self.option: str = option  # Тип функции
        self.graph = 0  # Номер места где расположен график
        self.flag_normalisation = 1  # Флаг, что необходима нормализация

        self.s_max = 100  # Максимальное значение функции
        self.s_min = -self.s_max  # Минимальное значение ф-ии

        self.axis_max = 100
        self.axis_min = -100

        self.axis_y_delta = 10  # Небходимо для самого графика, например:у_min= -(delta+ self.axisy_graph_max)
        self.argument = (
            0  # Константа на сколько поднять/опустить точки на аномальном участке
        )

        # Гармоничекое процесс
        self.c = 0  # Константа

        # Фильтр
        self.m = m
        self.fc_1 = fc_1
        self.fc_2 = fc_2
        self.dt = delta_t

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

        self.y = (((self.y - x_min) / c) - 0.5) * 2 * self.s_max

    def shift(self, trend):
        trend.y = trend.y + self.argument

        for i in range(10):
            trend.y[i] = 0

        return trend

    def calculation(self):

        if self.option == 'y(x)=kx+b':
            trend = Trend()
            trend.generating_trend_line()

            self.y = trend.y

        if self.option == 'y(x)=-kx+b':
            trend = Trend()
            trend.generating_trend_line()
            trend.y = np.flip(trend.y)

            self.y = trend.y

        if self.option == 'y(x) = beta * exp^(alpha * i)':
            trend = Trend()
            trend.generating_exhibitor()

            self.y = trend.y

        if self.option == 'y(x) = beta * exp^(alpha * -i)':
            trend = Trend()
            trend.generating_exhibitor()
            trend.y = np.flip(trend.y)

            self.y = trend.y

        if self.option == 'Встроенный рандом':
            trend = Trend()
            trend.generating_trend_random(self.s_min, self.s_max)

            self.y = trend.y

        if self.option == 'Кастомный рандом':
            trend = Trend()
            trend.generating_custom_random()

            self.y = trend.y

        if self.option == 'Рандом + сдвиг':
            trend1 = Trend()
            trend1.generating_trend_random(self.s_min, self.s_max)

            trend = self.shift(trend1)

            self.y = trend.y

            # Указали, что не требуется нормализация
            self.flag_normalisation = 0

        if self.option == 'Значения за областью':
            trend1 = Trend()
            trend1.generating_random_spikes(self.s_min, self.s_max)

            self.y = trend1.y

            # Указали, что не требуется нормализация
            self.flag_normalisation = 0

        if self.option == 'Адитивная модель №1':
            trend1 = Trend()
            trend1.generating_trend_line()
            trend1.y = np.flip(trend1.y)

            trend2 = Trend()
            trend2.generating_trend_random(self.s_min, self.s_max)

            trend = sum_trend(trend1, trend2)

            self.y = trend.y

        if self.option == 'Адитивная модель №2':
            trend1 = Trend()
            trend1.generating_trend_line()

            trend2 = Trend()
            trend2.generating_trend_random(self.s_min, self.s_max)

            trend = sum_trend(trend1, trend2)

            self.y = trend.y

        if self.option == 'Мультипликативная модель №1':
            trend1 = Trend()
            trend1.generating_trend_line()
            trend1.y = np.flip(trend1.y)

            trend2 = Trend()
            trend2.generating_trend_random(self.s_min, self.s_max)

            trend = multi(trend1, trend2)

            self.y = trend.y

        if self.option == 'Мультипликативная модель №2':
            trend1 = Trend()
            trend1.generating_trend_line()

            trend2 = Trend()
            trend2.generating_trend_random(self.s_min, self.s_max)

            trend = multi(trend1, trend2)

            self.y = trend.y

        if self.option == 'График кусочной функции':
            trend = Trend()
            trend.generating_piecewise_function(self.s_min, self.s_max)

            self.y = trend.y

        if self.option == 'Гармоническое процесс':
            trend = Trend()
            trend.generating_harmonic_process()

            if self.c != 0:
                self.y = self.y + self.c

            else:
                self.y = trend.y

            self.flag_normalisation = 0
            self.normalisation_axis()

        # x(t) = x1(t) + x2(t) = x3(t)
        # xi(t) = Ai * sin(2piFit)
        # A1 = 25       f1 = 11
        # A2 = 35       f2 = 41
        # A3 = 30       f3 = 141

        if self.option == 'Полигармоническое процесс':
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

        if self.option == 'Рандом + спайки':
            trend_1 = Trend()
            trend_1.generating_trend_random(self.s_min, self.s_max)

            trend_2 = Trend()
            trend_2.generating_random_spikes(self.s_min, self.s_max)

            trend = sum_trend(trend_1, trend_2)

            self.y = trend.y

            self.flag_normalisation = 0
            self.axis_max = np.amax(self.y) * 1.2
            self.axis_min = np.amin(self.y) * 1.2

        if self.option == 'ГП + trend':
            trend_1 = Trend()
            trend_2 = Trend()

            trend_1.generating_harmonic_process()
            trend_2.generating_trend_line()
            trend = sum_trend(trend_1, trend_2)

            self.y = trend.y

        if self.option == 'ГП + спайки':
            trend_1 = Trend()
            trend_2 = Trend()

            trend_1.generating_harmonic_process()
            trend_2.generating_random_spikes(self.s_min, self.s_max)

            trend = sum_trend(trend_1, trend_2)

            self.y = trend.y

            self.flag_normalisation = 0
            self.normalisation_axis()

        if self.option == 'ГП + спайки + рандом + trend':
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

        if self.option == 'Загрузить из файла':
            trend = Trend()
            trend.generating_trend_from_file()

            self.y = trend.y

            self.flag_normalisation = 0
            self.normalisation_axis()

        # кардиограма
        if self.option == 'ГП + exp':
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
            self.s_min = -self.s_max

        # Реализация фильтров
        if self.option == 'Низких частот':
            trend = Trend()
            trend.generation_trend_filter_potter(self.m, self.dt, self.fc_1)

            self.y = trend.y
            self.x = trend.x
            self.n = trend.n
            self.display_n = trend.display_n
            self.dt = trend.dt

        if self.option == 'Высоких частот':
            trend = Trend()
            trend.generating_trend_high_potter(self.m, self.dt, self.fc_1)

            self.y = trend.y
            self.x = trend.x
            self.n = trend.n
            self.display_n = trend.display_n
            self.dt = trend.dt

        if self.option == 'Полосовой':
            trend = Trend()
            trend.generating_trend_bandpass_filter(self.m, self.dt, self.fc_1, self.fc_2)

            self.y = trend.y
            self.x = trend.x
            self.n = trend.n
            self.display_n = trend.display_n
            self.dt = trend.dt

        if self.option == 'Режекторный':
            trend = Trend()
            trend.generating_trend_notch_filter(self.m, self.dt, self.fc_1, self.fc_2)

            self.y = trend.y
            self.x = trend.x
            self.n = trend.n
            self.display_n = trend.display_n
            self.dt = trend.dt

        if self.option == 'Звук ma.wav':
            self.name_of_wav_file = "input files/custom.wav"
            sound_trend = Sound(self.name_of_wav_file)

            self.x = sound_trend.x
            self.y = sound_trend.y * self.c
            self.rate = sound_trend.rate

            self.n = len(self.x)
            self.flag_checking_display_n = 1

        if self.option == 'Звук my_voice.wav':
            self.name_of_wav_file = "input files/my_voice.wav"
            sound_trend = Sound(self.name_of_wav_file)

            self.x = sound_trend.x
            self.y = sound_trend.y * self.c
            self.rate = sound_trend.rate

            self.n = len(self.x)
            self.flag_checking_display_n = 1

        if self.option == 'Экзамен':
            trend = Trend()
            trend.generating_trend_from_file_exam()

            self.y = trend.y

            self.flag_normalisation = 0
            self.normalisation_axis()

        # Модель Input: кардиограма, заполненная нулями с 200 до 1000
        if self.option == 'кардиограма':
            self.n = 200
            self.x = np.arange(0, self.n)
            self.s_max = 1

            trend_1 = Trend()
            trend_1.n = self.n
            trend_1.x = self.x
            trend_1.delta_t = 0.005
            trend_1.generating_harmonic_process()

            trend_2_n = 800
            trend_2_y = np.zeros(trend_2_n)

            self.n = 1000
            self.x = np.arange(0, self.n)
            self.y = np.concatenate([trend_1.y, trend_2_y])

            print(self.y)
            self.s_max = 100
            self.s_min = -self.s_max

    # Метод получения модели после фильтрации
    def filtration(self, model_for_filtration, choice_filter):
        trend_filter = Trend()  # Тренд фильтра

        # Фильтр низких частот
        if choice_filter == 1:
            trend_filter.generation_trend_filter_potter()

        # Фильтр высоких частот
        if choice_filter == 2:
            trend_filter.generating_trend_high_potter()

        # Фильтр полосовой
        if choice_filter == 3:
            trend_filter.generating_trend_bandpass_filter()

        # Фильтр режекторный
        if choice_filter == 4:
            trend_filter.generating_trend_notch_filter()

        # Тренд существущей модели
        trend_model = Trend()
        trend_model.x = model_for_filtration.x
        trend_model.y = model_for_filtration.y
        trend_model.n = model_for_filtration.n

        trend = convolution(trend_model, trend_filter)
        self.x = trend.x
        self.y = trend.y
