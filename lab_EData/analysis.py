import math
import copy
from model import *


class Analysis:
    def __init__(self, model):

        self._model = model                 # Модель, которую анализиурем

        self._all_average_value = []        # Все средние значения
        self._average_value = 0             # Среднее значения тренда
        self._dispersion = 0                # Дисперсия
        self._standard_deviation = 0        # Стандартное отклонение
        self._asymmetry = 0                 # Асимметрия
        self._asymmetry_coefficient = 0     # Коэффициент асимметрии
        self._standard_ratio = 0            # Стандартный коэффициент

        # Параметры для гистограммы
        self._bar_graph = []            # Значения для графика гистограммы
        self._number_of_intervals = 40   # Количество интервалов для гистограмм
        self._max_bar_graph_value = 0

    def get_number_of_intervals(self):
        return self._number_of_intervals

    def get_max_bar_graph_value(self):
        return self._max_bar_graph_value

    # Рассчет среднего значения
    def average_value(self):

        average_value = 0

        for i in range(self._model.get_N()):
            average_value = average_value + self._model.get_y_i(i)

        new_average_value = average_value / self._model.get_N()

        self._average_value = new_average_value

        return new_average_value

    def check_stationarity_average_value(self):

        number_of_gaps = 10  # Количество промежутков

        gap_length = int(self._model.get_N() / number_of_gaps)  # Длина промежутка

        average_value = 0

        delta_min_max = (2 * self._model.get_axis_y_graph_max()) * 0.05

        for i in range(self._model.get_N()):
            average_value = average_value + math.fabs(self._model.get_y_i(i))
            # average_value = average_value + self._model.get_y_i(i)
            if i % gap_length == 0 and i > 0 or i == self._model.get_N() - 1:
                average_value = average_value / gap_length
                self._all_average_value.append(average_value)
                average_value = 0

        flag_stationarity = True
        for i in range(self._all_average_value.__len__() - 1):

            if math.fabs(self._all_average_value[i] - self._all_average_value[i + 1]) > delta_min_max:
                # if self._all_average_value[i] - self._all_average_value[i + 1] > delta_min_max:
                flag_stationarity = False

        return flag_stationarity

    # Рассчет дисперсии
    def dispersion(self, iteration_number):
        trend_list = []

        for i in range(iteration_number):
            self._model.calculation()
            deep_copy_y = copy.deepcopy(self._model.get_y(i))
            trend_list.append(deep_copy_y)

        average_trend_list = []

        for i in range(self._model.get_N()):
            temp_average_y = 0

            for j in range(iteration_number):
                temp_average_y = temp_average_y + trend_list[j][i]

            temp_average_y = temp_average_y / iteration_number
            average_trend_list.append(temp_average_y)

        average_value = 0
        for i in range(self._model.get_N()):
            average_value = average_value + average_trend_list[i]

        average_value = average_value / self._model.get_N()

        dispersion = 0
        for i in range(self._model.get_N()):
            dispersion = (average_trend_list[i] - average_value) * (
                    average_trend_list[i] - average_value) + dispersion

        self._dispersion = dispersion / self._model.get_N()

        return self._dispersion

    # Рассчет стандартного отклонения
    def standard_deviation(self):

        if self._dispersion == 0:  # Если не была расчитана диспресия
            self.dispersion(1)

        self._standard_deviation = math.sqrt(self._dispersion)

        return self._standard_deviation

    # Рассчет асимметрии
    def asymmetry(self):

        if self._average_value == 0:
            self.average_value()

        sum_of_values = 0

        for i in range(self._model.get_N()):
            temp_value = (self._model.get_y_i(i) - self._average_value)
            temp_value = temp_value * temp_value * temp_value
            sum_of_values = sum_of_values + temp_value

        self._asymmetry = sum_of_values / self._model.get_N()

        return self._asymmetry

    # Рассчет коэффициента асимметрии
    def asymmetry_coefficient(self):

        if self._standard_deviation == 0:
            self.standard_deviation()

        if self._asymmetry == 0:
            self.asymmetry()

        sigma3 = self._standard_deviation * self._standard_deviation * self._standard_deviation
        self._asymmetry_coefficient = self._asymmetry / sigma3

        return self._asymmetry_coefficient

    # Рассчет эксцесса
    def excess(self):

        if self._average_value == 0:
            self.average_value()

        sum_of_values = 0

        for i in range(self._model.get_N()):
            temp_value = (self._model.get_y_i(i) - self._average_value)
            temp_value = temp_value ** 4  # Возведение в степень 4
            sum_of_values = sum_of_values + temp_value

        self._excess = sum_of_values / self._model.get_N()

        return self._excess

    # Рассчет куртозис
    def kurtosis(self):

        if self._standard_deviation == 0:
            self.standard_deviation()

        if self._excess == 0:
            self.excess()

        kurtosis = self._excess / (self._standard_deviation ** 4)
        kurtosis = kurtosis - 3

        return kurtosis

    # Рассчет стандартного коэфициента
    def standard_ratio(self):

        sum_of_values = 0

        for i in range(self._model.get_N()):
            temp_value = self._model.get_y_i(i) ** 2
            sum_of_values = sum_of_values + temp_value

        self._standard_ratio = sum_of_values / self._model.get_N()

        return self._standard_ratio

    # Рассчет среднеквадратичной ошибки
    def standard_error(self):
        if self._standard_ratio == 0:
            self.standard_ratio()

        standard_error = math.sqrt(self._standard_ratio)

        return standard_error

    # Рассчет среднего абсолютного отклонения
    def mean_absolute_deviation(self):

        if self._average_value == 0:
            self.average_value()

        sum_of_values = 0

        for i in range(self._model.get_N()):
            sum_of_values = sum_of_values + math.fabs(self._model.get_y_i(i) - self._average_value)

        mean_absolute_deviation = sum_of_values / self._model.get_N()

        return mean_absolute_deviation

    # Поиск минимального Х
    def min_X(self):

        min = self._model.get_y_i(0)

        for i in range(self._model.get_N()):
            if min > self._model.get_y_i(i):
                min = self._model.get_y_i(i)

        return min

    # Поиск максимального Х
    def max_X(self):

        max = self._model.get_y(0)

        for i in range(self._model.get_N()):
            if max < self._model.get_y_i(i):
                max = self._model.get_y_i(i)

        return max

    # Гистограмма
    def bar_graph(self):

        model = Model(14)  # Модель графика гистограммы

        y_min = self._model.get_axis_y_graph_min()
        x = []

        interval_size = math.fabs(y_min) + self._model.get_axis_y_graph_max()
        interval_size = int(interval_size) / self._number_of_intervals
        temp_value_hit_count = 0
        max_bar_graph_value = 0

        for i in range(self._number_of_intervals):
            x.append(i)
            for j in range(self._model.get_N()):
                y = self._model.get_y_i(j)
                if y >= (y_min + interval_size * i):
                    if y < (y_min + interval_size * (i + 1)):
                        temp_value_hit_count = temp_value_hit_count + 1

            self._bar_graph.append(temp_value_hit_count)

            if max_bar_graph_value <= temp_value_hit_count:
                max_bar_graph_value = temp_value_hit_count

            temp_value_hit_count = 0

        model.set_N(self._number_of_intervals)
        model.set_y_all(self._bar_graph)
        model.set_x_all(x)
        model.set_axis_y_graph_min(0)
        model.set_axis_y_graph_max(max_bar_graph_value)

        return model
