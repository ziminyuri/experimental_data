import math
import random
import time
import copy

class Model():
    def __init__(self, option):
        self._k = 0.1
        self._b = 5
        self._beta = 2
        self._alpha = 0.5
        self._y = []

        self._option = option #Тип функции
        self._graph = 0 #Номер графика

        self._x = []

        self._axis_y_graph_min = -100    #Минимальное значение функции
        self._axis_y_graf_max = 100      #Максимальное значение функции
        self._axis_y_delta = 10         #Небходимо для самого графика, например: у_min = -(delta + self.axis_y_graf_max)

        self._N = 1000    #Количество точек по оси Х
        self._n = 10     #Начало аномального отрезка
        self._m = 40     #Окончание аномального отрезка
        self._argument = 100  #Константа на сколько поднять/опустить точки на аномальном участке

        self._all_average_value = []   #Средние значения

        for i in range(self._N):
            self._x.append(i)

    def set_k(self,k):
        self._k = k

    def set_b(self,b):
        self._b = b

    def set_beta(self,beta):
        self._beta = beta

    def set_alpha(self,alpha):
        self._alpha = alpha

    def set_axis_y_graph_min(self,axis_y_graph_min):
        self._axis_y_graph_min = axis_y_graph_min

    def get_axis_y_graph_min(self):
        return self._axis_y_graph_min

    def set_axis_y_graf_max(self,axis_y_graf_max):
        self._axis_y_graf_max = axis_y_graf_max

    def get_axis_y_graf_max(self):
        return self._axis_y_graf_max

    def set_n(self,n):
        self._n = n

    def set_m(self,m):
        self._m = m

    def set_N(self,N):
        self._N = N

    def get_N(self):
        return self._N

    def get_argument(self):
        return self._argument

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_graph(self, number):
        self._graph = number

    def get_graph(self):
        return self._graph

    def normalization(self):
        x_max = self._y[0]
        x_min = self._y[0]
        for i in range(self._N):
            if self._y[i]>x_max:
                x_max = self._y[i]

            if self._y[i] <x_min:
                x_min = self._y[i]

        temp_y = copy.deepcopy(self._y)
        self._y.clear()
        for i in range(self._N):
            a = temp_y[i]
            b = a - x_min
            c = x_max - x_min
            d = b / c
            e = d - 0.5
            f = e * 2 * self._axis_y_graf_max
            self._y.append(f)

    def check_stationarity(self):

        number_of_gaps = 10 #Количество промежутков

        gap_length = int(self._N / number_of_gaps)      #Длина промежутка

        average_value = 0

        delta_min_max = (2 * self._axis_y_graf_max) * 0.05

        for i in range(self._N):
            average_value = average_value + self._y[i]
            if i % gap_length == 0:
                average_value = average_value / gap_length
                self._all_average_value.append(average_value)
                average_value = 0

        flag_stationarity = True
        for i in range(self._all_average_value.__len__() - 1):
            if self._all_average_value[i] - self._all_average_value[i+1] > delta_min_max:
                flag_stationarity = False

        return flag_stationarity


    def calculation(self):

        self._y[:] = []

        # y(x)=kx+b
        if (self._option == 1):
            for i in range(self._N):
                yn = self._k * i + self._b
                self._y.append(yn)

        # y(x)=-kx+b
        if (self._option == 2):
            for i in range(self._N):
                yn = -self._k * i + self._b
                self._y.append(yn)

        # y(x) = beta * exp^(alpha * i)
        if (self._option == 3):
            for i in range(self._N):
                try:
                    yn = self._beta * math.exp((self._alpha * i))
                    # yn = 2 * math.exp(i)
                    self._y.append(yn)
                except:
                    self._y.append(0)

        # y(x) = beta * exp^(alpha * -i)
        if (self._option == 4):
            for i in range(self._N):
                try:
                    yn = self._beta * math.exp((self._alpha * -i))
                    # yn = 2 * math.exp(i)
                    self._y.append(yn)
                except:
                    self._y.append(0)

        #Встроенный рандом
        if(self._option == 5):
            for i in range(self._N):
                try:
                    yn = random.uniform(self._axis_y_graph_min, self._axis_y_graf_max)
                    self._y.append(yn)
                except:
                    self._y.append(0)

        #Кастомный рандом
        if (self._option == 6):
            for i in range(self._N):
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

        # Аномальные участки
        if (self._option == 7):
            for i in range(self._N):
                if (i >= self._n) and (i <= self._m):
                    try:
                        yn = random.uniform(self._axis_y_graph_min + self._argument,
                                            self._axis_y_graf_max + self._argument)
                        self._y.append(yn)
                    except:
                        self._y.append(0)
                else:
                    try:
                        yn = random.uniform(self._axis_y_graph_min, self._axis_y_graf_max)
                        self._y.append(yn)
                    except:
                        self._y.append(0)

        # Значения за областью
        if (self._option == 8):

            for i in range(self._N):
                try:
                    temp_string_time = str(time.time())
                    reverse_temp_string_time = temp_string_time[::-1]
                    new_value = int(reverse_temp_string_time[0])

                    temp_string_time_for_even = str(time.time())
                    reverse_temp_string_time_for_even = temp_string_time_for_even[::-1]
                    new_value_for_even = int(reverse_temp_string_time_for_even[0])
                    new_value_for_even = new_value_for_even % 2

                    new_value_choice = new_value

                    if new_value_choice == 5:
                        temp_string_time_spikes = str(time.time())
                        reverse_temp_string_time_spikes = temp_string_time_spikes[::-1]
                        new_value = int(reverse_temp_string_time_spikes[0])
                    else:
                        new_value = 0

                    if new_value_for_even == 1:
                        new_value = - new_value

                    self._y.append(new_value)

                except:
                    self._y.append(0)

        # Адитивная модель №1
        if(self._option == 9):
            for i in range(self._N):
                try:
                    yn = random.uniform(self._axis_y_graph_min, self._axis_y_graf_max)

                    yn_1 = -self._k * i + self._b

                    yn = yn + yn_1

                    self._y.append(yn)
                except:
                    self._y.append(0)

        # Адитивная модель №2
        if (self._option == 10):
            for i in range(self._N):
                try:
                    yn = random.uniform(self._axis_y_graph_min, self._axis_y_graf_max)

                    yn_1 = self._k * i + self._b

                    yn = yn + yn_1

                    self._y.append(yn)
                except:
                    self._y.append(0)

        # Мультипликативная модель №1
        if (self._option == 11):
            for i in range(self._N):
                try:
                    yn = random.uniform(self._axis_y_graph_min, self._axis_y_graf_max)

                    yn_1 = -self._k * i + self._b

                    yn = yn * yn_1

                    self._y.append(yn)
                except:
                    self._y.append(0)

        # Мультипликативная модель №2
        if (self._option == 12):
            for i in range(self._N):
                try:
                    yn = random.uniform(self._axis_y_graph_min, self._axis_y_graf_max)

                    yn_1 = self._k * i + self._b

                    yn = yn * yn_1

                    self._y.append(yn)
                except:
                    self._y.append(0)





            

            


