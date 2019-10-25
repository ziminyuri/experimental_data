import math
import random
import time
import numpy as np


class Model:
    def __init__(self, option):
        self.k = 0.1
        self.b = 4
        self.beta = 20
        self.alpha = 0.05

        self.n = 1000                           # Количество точек по оси Х

        self.x = np.arange(0, self.n)
        self.y = np.zeros(self.n)               # Сгенерировали матрицу из нулей

        self.option = option                    # Тип функции
        self.graph = 0                          # Номер графика
        self.flag_normalisation = 1             # Флаг, что необходима нормализация

        self.s_max = 100                        # Максимальное значение функции
        self.s_min = - self.s_max               # Минимальное значение ф-ии
        self.s_without_spikes = self.s_max      # Значение функции без спаек
        self.axis_max = self.s_max * 1.2
        self.axis_min = self.s_min * 1.2

        self.axis_y_delta = 10          # Небходимо для самого графика, например:у_min= -(delta+ self.axisy_graph_max)
        self.argument = 0               # Константа на сколько поднять/опустить точки на аномальном участке

        # Гармоничекое процесс
        self.a_0 = 100  # А0
        self.f_0 = 11  # 11; 110; 250; 510
        self.delta_t = 0.001

        self.piecewise_function = int(self.n / 3)

    # Генерируем спайки
    def generating_spikes(self):
        self.argument = self.s_max * 2
        temp = np.zeros(self.n)

        number_spikes = int(self.n * 0.01)

        for i in range(number_spikes):
            rand_index_array = random.randint(0, self.n-1)
            rand_value = random.uniform(self.s_min, self.s_max)

            if rand_value > 0:
                rand_value += self.argument

            else:
                rand_value -= self.argument

            temp[rand_index_array] = rand_value

        self.s_max = self.argument * 1.1
        return temp

    # Генерируем значение встроенным рандомом
    def generating_trend_random(self):

        random_trend = np.random.uniform(self.s_min, self.s_max, self.n)
        return random_trend

    # Генерация тренда прямой линии
    def generating_trend_line(self):
        temp = self.k * self.x + self.b

        return temp

    def normalization(self):

        if self.flag_normalisation == 0:
            return

        self.y = np.array(self.y)

        x_max = np.amax(self.y)
        x_min = np.amin(self.y)
        c = x_max - x_min

        self.y = ((((self.y - x_min) / c) - 0.5) * 2 * self.s_max)

    def calculation(self):

        # y(x)=kx+b
        if self.option == 1:
            self.y = self.generating_trend_line()

        # y(x)=-kx+b
        if self.option == 2:
            self.y = self.generating_trend_line()
            self.y = np.flip(self.y)

        # y(x) = beta * exp^(alpha * i)
        if self.option == 3:

            temp_y = []
            for i in range(self.n):
                try:
                    yn = self.beta * math.exp((self.alpha * i))
                    temp_y.append(yn)

                except:
                    temp_y.append(0)

            self.y = np.array(temp_y)

        # y(x) = beta * exp^(alpha * -i)
        if self.option == 4:

            temp_y = []
            for i in range(self.n):
                try:
                    yn = self.beta * math.exp((self.alpha * -i))
                    temp_y.append(yn)

                except:
                    temp_y.append(0)

            self.y = np.array(temp_y)

        # Встроенный рандом
        if self.option == 5:
            self.y = self.generating_trend_random()

        # Кастомный рандом
        if self.option == 6:

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
                        new_value = - new_value

                    temp_y.append(new_value)

                except:
                    temp_y.append(0)

            self.y = np.array(temp_y)

        # Рандом + сдвиг
        if self.option == 7:

            # Указали, что не требуется нормализация
            self.flag_normalisation = 0

            self.argument = self.s_max * 100

            self.y = self.generating_trend_random()
            self.y = self.y + self.argument

            for i in range(10):
                self.y[i] = 0

            self.s_max = self.argument
            self.axis_max = self.s_max * 1.1
            self.axis_min = 0

        # Значения за областью
        if self.option == 8:

            # Указали, что не требуется нормализация
            self.flag_normalisation = 0
            self.y = self.generating_spikes()

        # Адитивная модель №1
        if self.option == 9:

            trend_1 = self.generating_trend_line()
            trend_1 = np.flip(trend_1)

            trend_2 = self.generating_trend_random()

            self.y = trend_1 + trend_2

        # Адитивная модель №2
        if self.option == 10:

            trend_1 = self.generating_trend_line()
            trend_2 = self.generating_trend_random()

            self.y = trend_1 + trend_2

        # Мультипликативная модель №1
        if self.option == 11:
            trend_1 = self.generating_trend_line()
            trend_1 = np.flip(trend_1)

            trend_2 = self.generating_trend_random()

            self.y = trend_1 * trend_2

        # Мультипликативная модель №2
        if self.option == 12:

            trend_1 = self.generating_trend_line()
            trend_2 = self.generating_trend_random()

            self.y = trend_1 * trend_2

        # График кусочной функции
        if self.option == 13:

            for i in range(self.n):
                try:
                    if i < self.piecewise_function:
                        yn = -self.k * i + self.b

                    if i < self.piecewise_function * 2:
                        if i >= self.piecewise_function:
                            yn = random.uniform(self.s_min, self.s_max)

                    if i >= self.piecewise_function * 2:
                        yn = self.k * i + self.b

                    self.y.append(yn)

                except:
                    self.y.append(0)

        # График гармонический процесс
        if self.option == 17:

            temp = []
            for i in range(self.n):
                yn = self.a_0 * math.sin(2 * math.pi * self.f_0 * i * self.delta_t)
                temp.append(yn)

            self.y = np.array(temp)

        # График полигармонического процесса
        # x(t) = x1(t) + x2(t) = x3(t)
        # xi(t) = Ai * sin(2piFit)
        # A1 = 25       f1 = 11
        # A2 = 35       f2 = 41
        # A3 = 30       f3 = 141
        if self.option == 19:
            a1 = 25
            a2 = 35
            a3 = 30

            f1 = 11
            f2 = 41
            f3 = 141

            temp = []
            for i in range(self.n):
                yn1 = a1 * math.sin(2 * math.pi * f1 * i)
                yn2 = a2 * math.sin(2 * math.pi * f2 * i)
                yn3 = a3 * math.sin(2 * math.pi * f3 * i)
                yn = yn1 + yn2 + yn3
                temp.append(yn)

            self.y = np.array(temp)

        # График Рандом + спайки
        if self.option == 20:
            trend_1 = self.generating_trend_random()
            trend_2 = self.generating_spikes()

            self.y = trend_1 + trend_2

            self.flag_normalisation = 0
            self.axis_max = np.amax(self.y) * 1.2
            self.axis_min = np.amin(self.y) * 1.2

        # График Рандом + спайки + trend
        if self.option == 21:
            trend_1 = self.generating_trend_random()
            trend_2 = self.generating_trend_line()
            trend_3 = self.generating_spikes()

            self.y = trend_1 + trend_2 + trend_3

            self.flag_normalisation = 0
            self.axis_max = np.amax(self.y) * 1.2
            self.axis_min = np.amin(self.y) * 1.2