import random
import struct
import time

from filter import *


class Trend:
    def __init__(self):
        self.k = 0.1
        self.b = 4
        self.beta = 20
        self.alpha = 0.05

        self.n = 1000  # Количество точек по оси Х

        self.x = np.arange(0, self.n)
        self.y = np.zeros(self.n)  # Сгенерировали матрицу из нулей

        self.axis_y_delta = 10  # Небходимо для самого графика, например:у_min= -(delta+ self.axisy_graph_max)
        self.argument = (
            0  # Константа на сколько поднять/опустить точки на аномальном участке
        )

        # Гармоничекое процесс
        self.a_0 = 100  # А0
        self.f_0 = 11  # 11; 110; 250; 510
        self.delta_t = 0.001
        self.c = 0  # Константа

        self.piecewise_function = int(self.n / 3)

        # Фильтр
        self.m = 32
        self.fc_1 = 120
        self.fc_2 = 140
        self.dt = 0.001

    # Генерируем рандомно спайки
    def generating_random_spikes(self, min, max):
        self.argument = max * 2

        number_spikes = int(self.n * 0.01)

        for i in range(number_spikes):
            rand_index_array = random.randint(0, self.n - 1)
            rand_value = random.uniform(min, min)

            if rand_value > 0:
                rand_value += self.argument

            else:
                rand_value -= self.argument

            self.y[rand_index_array] = rand_value

    # Генерируем спайки
    def generating_spikes(self, max):
        number_of_spike = 5

        gap = int(self.n / number_of_spike)

        i = 0
        while i < self.n:
            self.y[i] = max
            i += gap

    # Гененрируем кастомный рандом
    def generating_custom_random(self):
        temp_y = []
        for i in range(self.n):
            try:
                temp_string_time = str(time.time())
                reverse_temp_string_time = temp_string_time[::-1]
                new_value = float(reverse_temp_string_time[0])
                new_value = new_value / 10

                temp_string_time_for_even = str(time.time())
                reverse_temp_string_time_for_even = temp_string_time_for_even[::-1]
                new_value_for_even = int(reverse_temp_string_time_for_even[0])
                new_value_for_even = new_value_for_even % 2

                if new_value_for_even == 1:
                    new_value = -new_value

                temp_y.append(new_value)

            except:
                temp_y.append(0)

            self.y = np.array(temp_y)

    # Генерируем кусочную функцию
    def generating_piecewise_function(self, min, max):
        y = []
        for i in range(self.n):
            try:
                if i < self.piecewise_function:
                    yn = -self.k * i + self.b

                if i < self.piecewise_function * 2:
                    if i >= self.piecewise_function:
                        yn = random.uniform(min, max)

                if i >= self.piecewise_function * 2:
                    yn = self.k * i + self.b

                y.append(yn)

            except:
                y.append(0)

        self.y = np.array(y)

    # Генерируем значение встроенным рандомом
    def generating_trend_random(self, min, max):
        self.y = np.random.uniform(min, max, self.n)

    # Генерация тренда прямой линии
    def generating_trend_line(self):
        self.y = self.k * self.x + self.b

    # Генерация тренда экспоненты
    def generating_exhibitor(self):
        temp_y = []
        for i in range(self.n):
            try:
                yn = self.beta * math.exp((self.alpha * i))
                temp_y.append(yn)

            except:
                temp_y.append(0)

        self.y = np.array(temp_y)

    # Генерация графика гармонического процесса
    def generating_harmonic_process(self):
        temp = []

        # self.delta_t = 0.002
        for i in range(self.n):
            yn = self.a_0 * math.sin(2 * math.pi * self.f_0 * i * self.delta_t)
            temp.append(yn)

        self.y = np.array(temp)

    # Гененрируем тренд из файла
    def generating_trend_from_file(self):

        filename = "/Users/zimin/Documents/Github/experimental_data/lab_EData/input files/input.dat"

        f = open(filename, "rb")
        data = f.read(4)

        y_list = []
        while data:
            temp_tuple = struct.unpack("<f", data)
            temp_value = temp_tuple[0]
            y_list.append(temp_value)
            data = f.read(4)

        self.y = np.array(y_list)

    # Гененрируем тренд из файла для экзамена
    def generating_trend_from_file_exam(self):

        filename = "/Users/zimin/Documents/Github/experimental_data/lab_EData/input files/v1u7.dat"

        f = open(filename, "rb")
        data = f.read(4)

        y_list = []
        while data:
            temp_tuple = struct.unpack("<f", data)
            temp_value = temp_tuple[0]
            y_list.append(temp_value)
            data = f.read(4)

        self.y = np.array(y_list)

    # Генерируем тренд фильтра низких частот
    def generation_trend_filter_potter(self):
        lpw = filter_potter(self.m, self.dt, self.fc_1)

        self.n = self.m
        self.x = np.arange(0, self.n * 2 + 1)
        self.y = lpw
        self.display_n = self.n * 2 + 1

    # Генерируем тренд фильтра высоких частот
    def generating_trend_high_potter(self):
        hpf = high_potter_filter(self.m, self.dt, self.fc_1)

        self.n = self.m
        self.x = np.arange(0, self.n * 2 + 1)
        self.y = hpf
        self.display_n = self.n * 2 + 1

    # Генерируем тренд фильтра полосового
    def generating_trend_bandpass_filter(self):
        bpf = bandpass_filter(self.m, self.dt, self.fc_1, self.fc_2)

        self.n = self.m
        self.x = np.arange(0, self.n * 2 + 1)
        self.y = bpf
        self.display_n = self.n * 2 + 1

    # Генерируем тренд фильтра режекторного
    def generating_trend_notch_filter(self):
        bsf = notch_filter(self.m, self.dt, self.fc_1, self.fc_2)

        self.n = self.m
        self.x = np.arange(0, self.n * 2 + 1)
        self.y = bsf
        self.display_n = self.n * 2 + 1
