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

        self.n = 1000                         # Количество точек по оси Х

        self.x = np.arange(0, self.n)
        self.y = np.zeros(self.n)           # Сгенерировали матрицу из нулей

        self.option = option                # Тип функции
        self.graph = 0                      # Номер графика
        self.flag_normalisation = 1         # Флаг, что необходима нормализация

        self.s = 100                    # Максимальное значение функции
        self.axis_y_delta = 10          # Небходимо для самого графика, например:у_min= -(delta+ self.axisy_graph_max)
        self.argument = 0   # Константа на сколько поднять/опустить точки на аномальном участке

        # Гармоничекое процесс
        self.a_0 = 100  # А0
        self.f_0 = 11  # 11; 110; 250; 510
        self.delta_t = 0.001

        self.piecewise_function = int(self.n / 3)

    # Генерируем единственное значение спайки
    def generating_spikes(self):

        rand_value = random.randint(0, 99)

        if rand_value == 3:
            return self.generating_trend_random()

        else:
            return 0

    # Генерируем значение встроенным рандомом
    def generating_trend_random(self):

        random_trend = np.random.uniform(-self.s, self.s, self.n)
        return random_trend

    def normalization(self):

        if self.flag_normalisation == 0:
            return

        self.y = np.array(self.y)

        x_max = np.amax(self.y)
        x_min = np.amin(self.y)
        c = x_max - x_min

        self.y = ((((self.y - x_min) / c) - 0.5) * 2 * self.s)

    def calculation(self):

        # y(x)=kx+b
        if self.option == 1:
            self.y = self.k * self.x + self.b

        # y(x)=-kx+b
        if self.option == 2:
            self.y = - self.k * self.x + self.b

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

            self.argument = self.s * 1000

            self.y = self.generating_trend_random()
            self.y = self.y + self.argument
            self.s = self.argument

        # Значения за областью
        if self.option == 8:

            # Указали, что не требуется нормализация
            self.flag_normalisation = 0

            self.argument = self.s * 2

            for i in range(self.n):
                value = self.generating_spikes()
                if value < 0:
                    value -= self.argument

                if value > 0:
                    value += self.argument

                self.y.append(value)

            self.s = self.argument * 1.1

        # Адитивная модель №1
        if self.option == 9:

            for i in range(self.n):
                try:
                    yn = random.uniform(- self.s, self.s)

                    yn_1 = -self.k * i + self.b

                    yn = yn + yn_1

                    self.y.append(yn)
                except:
                    self.y.append(0)

        # Адитивная модель №2
        if self.option == 10:

            for i in range(self.n):
                try:
                    yn = random.uniform(- self.s, self.s)

                    yn_1 = self.k * i + self.b

                    yn = yn + yn_1

                    self.y.append(yn)
                except:
                    self.y.append(0)

        # Мультипликативная модель №1
        if self.option == 11:

            for i in range(self.n):
                try:
                    yn = random.uniform(- self.s, self.s)

                    yn_1 = -self.k * i + self.b

                    yn = yn * yn_1

                    self.y.append(yn)
                except:
                    self.y.append(0)

            np.flip(self.y)

        # Мультипликативная модель №2
        if self.option == 12:

            for i in range(self.n):
                try:
                    yn = random.uniform(- self.s, self.s)

                    yn_1 = self.k * i + self.b

                    yn = yn * yn_1

                    self.y.append(yn)
                except:
                    self.y.append(0)

        # График кусочной функции
        if self.option == 13:

            for i in range(self.n):
                try:
                    if i < self.piecewise_function:
                        yn = -self.k * i + self.b

                    if i < self.piecewise_function * 2:
                        if i >= self.piecewise_function:
                            yn = random.uniform(- self.s, self.s)

                    if i >= self.piecewise_function * 2:
                        yn = self.k * i + self.b

                    self.y.append(yn)

                except:
                    self.y.append(0)

        # График гармонический процесс
        if self.option == 17:
            for i in range(self.n):
                yn = self.a_0 * math.sin(2 * math.pi * self.f_0 * i * self.delta_t)
                self.y.append(yn)

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

            for i in range(self.n):
                yn1 = a1 * math.sin(2 * math.pi * f1 * i)
                yn2 = a2 * math.sin(2 * math.pi * f2 * i)
                yn3 = a3 * math.sin(2 * math.pi * f3 * i)
                yn = yn1 + yn2 + yn3
                self.y.append(yn)

        # График Рандом + спайки
        if self.option == 20:

            for i in range(self.n):
                random_value = self.generating_trend_random()
                spike = self.generating_spikes()

                value = random_value + spike
                self.y.append(value)

        # График Рандом + спайки + trend
        if self.option == 21:
            for i in range(self.n):
                yn = self.a_0 * math.sin(2 * math.pi * self.f_0 * i * self.delta_t)
                self.y.append(yn)
