import math
import random
import time
import copy
import numpy as np

class Model:
    def __init__(self, option):
        self._k = 0.1
        self._b = 4
        self._beta = 20
        self._alpha = 0.05

        self._n = 10  # Количество точек по оси Х

        self._x = np.arange(0, self._n)
        self._y = np.zeros(self._n)

        self._option = option  # Тип функции
        self._graph = 0  # Номер графика
        self._flag_normalisation = 1  # Флаг, что необходима нормализация

        self._s = 100  # Максимальное значение функции
        self._axis_y_delta = 10  # Небходимо для самого графика, например:у_min= -(delta+ self.axis_y_graph_max)
        self._argument = self._s * 0.10  # Константа на сколько поднять/опустить точки на аномальном участке

        # Гармоничекое процесс
        self._a_0 = 100  # А0
        self._f_0 = 11  # 11; 110; 250; 510
        self._delta_t = 0.001

        self._piecewise_function = int(self._n / 3)

    def set_k(self, k):
        self._k = k

    def set_b(self, b):
        self._b = b

    # Меняем частоту
    def set_f_0(self, f):
        self._f_0 = f

    def set_argument(self, a):
        self._argument = a

    def set_beta(self, beta):
        self._beta = beta

    def set_alpha(self, alpha):
        self._alpha = alpha

    def get_axis_y_graph_min(self):
        return - self._s

    def set_axis_y_graph_max(self, axis_y_graph_max):
        self._s = axis_y_graph_max

    def get_axis_y_graph_max(self):
        return self._s

    def set_n(self, n):
        self._n = n

    def get_n(self):
        return self._n

    def get_argument(self):
        return self._argument

    def get_x(self):
        return self._x

    def set_x_all(self, x_all):
        self._x = copy.deepcopy(x_all)

    def get_y_i(self, i):
        return self._y[i]

    def get_y(self):
        return self._y

    def set_y_all(self, y_all):
        self._y = copy.deepcopy(y_all)

    def set_graph(self, number):
        self._graph = number

    def get_graph(self):
        return self._graph

    # Генерируем единственное значение спайки
    def generating_spikes(self):

        rand_value = random.randint(0, 99)

        if rand_value == 3:
            return self.generating_trend_random()

        else:
            return 0

    # Генерируем значение встроенным рандомом
    def generating_trend_random(self):
        y = np.random.uniform(-self._s, self._s, self._n)
        return y

    def normalization(self):

        if self._flag_normalisation == 0:
            return

        self._y = np.array(self._y)

        x_max = np.amax(self._y)
        x_min = np.amin(self._y)
        c = x_max - x_min

        self._y = ((((self._y - x_min) / c) - 0.5) * 2 * self._s)

    def calculation(self):

        self._y = []

        # y(x)=kx+b
        if self._option == 1:

            for i in range(self._n):
                yn = self._k * i + self._b
                self._y.append(yn)

        # y(x)=-kx+b
        if self._option == 2:

            for i in range(self._n):
                yn = -self._k * i + self._b
                self._y.append(yn)

        # y(x) = beta * exp^(alpha * i)
        if self._option == 3:

            for i in range(self._n):
                try:
                    yn = self._beta * math.exp((self._alpha * i))
                    # yn = 2 * math.exp(i)
                    self._y.append(yn)

                except:
                    self._y.append(0)

        # y(x) = beta * exp^(alpha * -i)
        if self._option == 4:

            for i in range(self._n):
                try:
                    yn = self._beta * math.exp((self._alpha * -i))
                    self._y.append(yn)

                except:
                    self._y.append(0)

        # Встроенный рандом
        if self._option == 5:

            for i in range(self._n):
                value = self.generating_trend_random()
                self._y.append(value)

        # Кастомный рандом
        if self._option == 6:

            for i in range(self._n):
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

                    self._y.append(new_value)

                except:
                    self._y.append(0)


        # Рандом + сдвиг
        if self._option == 7:

            # Указали, что не требуется нормализация
            self._flag_normalisation = 0

            self._argument = self._s * 1000

            for i in range(self._n):
                value = self.generating_trend_random()
                value += self._argument
                self._y.append(value)

            for i in range(5):
                self._y[i] = 0

            self._s = self._argument * 1.05

        # Значения за областью
        if self._option == 8:

            # Указали, что не требуется нормализация
            self._flag_normalisation = 0

            self._argument = self._s * 2

            for i in range(self._n):
                value = self.generating_spikes()
                if value < 0:
                    value -= self._argument

                if value > 0:
                    value += self._argument

                self._y.append(value)

            self._s = self._argument * 1.1

        # Адитивная модель №1
        if self._option == 9:

            for i in range(self._n):
                try:
                    yn = random.uniform(- self._s, self._s)

                    yn_1 = -self._k * i + self._b

                    yn = yn + yn_1

                    self._y.append(yn)
                except:
                    self._y.append(0)

        # Адитивная модель №2
        if self._option == 10:

            for i in range(self._n):
                try:
                    yn = random.uniform(- self._s, self._s)

                    yn_1 = self._k * i + self._b

                    yn = yn + yn_1

                    self._y.append(yn)
                except:
                    self._y.append(0)

        # Мультипликативная модель №1
        if self._option == 11:

            for i in range(self._n):
                try:
                    yn = random.uniform(- self._s, self._s)

                    yn_1 = -self._k * i + self._b

                    yn = yn * yn_1

                    self._y.append(yn)
                except:
                    self._y.append(0)

            np.flip(self._y)

        # Мультипликативная модель №2
        if self._option == 12:

            for i in range(self._n):
                try:
                    yn = random.uniform(- self._s, self._s)

                    yn_1 = self._k * i + self._b

                    yn = yn * yn_1

                    self._y.append(yn)
                except:
                    self._y.append(0)

        # График кусочной функции
        if self._option == 13:

            for i in range(self._n):
                try:
                    if i < self._piecewise_function:
                        yn = -self._k * i + self._b

                    if i < self._piecewise_function * 2:
                        if i >= self._piecewise_function:
                            yn = random.uniform(- self._s, self._s)

                    if i >= self._piecewise_function * 2:
                        yn = self._k * i + self._b

                    self._y.append(yn)

                except:
                    self._y.append(0)

        # График гармонический процесс
        if self._option == 17:
            for i in range(self._n):
                yn = self._a_0 * math.sin(2 * math.pi * self._f_0 * i * self._delta_t)
                self._y.append(yn)

        # График полигармонического процесса
        # x(t) = x1(t) + x2(t) = x3(t)
        # xi(t) = Ai * sin(2piFit)
        # A1 = 25       f1 = 11
        # A2 = 35       f2 = 41
        # A3 = 30       f3 = 141
        if self._option == 19:
            a1 = 25
            a2 = 35
            a3 = 30

            f1 = 11
            f2 = 41
            f3 = 141

            for i in range(self._n):
                yn1 = a1 * math.sin(2 * math.pi * f1 * i)
                yn2 = a2 * math.sin(2 * math.pi * f2 * i)
                yn3 = a3 * math.sin(2 * math.pi * f3 * i)
                yn = yn1 + yn2 + yn3
                self._y.append(yn)

        # График Рандом + спайки
        if self._option == 20:

            for i in range(self._n):
                random_value = self.generating_trend_random()
                spike = self.generating_spikes()

                value = random_value + spike
                self._y.append(value)

        # График Рандом + спайки + trend
        if self._option == 21:
            for i in range(self._n):
                yn = self._a_0 * math.sin(2 * math.pi * self._f_0 * i * self._delta_t)
                self._y.append(yn)
