import copy
import math
from random import random

import numpy as np
from numpy.fft import fft, rfft, rfftfreq

from model import Model


# Деление двух спектров (действительных и комплексных чисел)
def spectral_division(analysis_model_1, analysis_model_2):
    pass

class Analysis:
    def __init__(self, model):

        self.model = model  # Модель, которую анализиурем

        self.all_average_value = []     # Все средние значения
        self.average_value = 0          # Среднее значения тренда
        self.dispersion = 0    # Дисперсия
        self.standard_deviation = 0  # Стандартное отклонение
        self.asymmetry = 0  # Асимметрия
        self.asymmetry_coefficient = 0  # Коэффициент асимметрии
        self.standard_ratio = 0  # Стандартный коэффициент
        self.excess = 0  # Эксцесс

        # Параметры для гистограммы
        self.bar_graph = []  # Значения для графика гистограммы
        self.number_of_intervals = 40  # Количество интервалов для гистограмм
        self.max_bar_graph_value = 0

        # Параметры для автокорреляции
        self.l = model.n - 1  # Сдвиг

        # Параментр для Преобразования Фурье (Спектр)
        self.delta_t = 0.01

    # Устанавилваем delta t
    def set_delta_t(self, delta_t):
        self.delta_t = delta_t

    # Рассчет среднего значения
    def calculation_average_value(self):

        self.average_value = np.mean(self.model.y)

        return self.average_value

    def check_stationarity_average_value(self):

        number_of_gaps = 10  # Количество промежутков

        gap_length = int(self.model.n / number_of_gaps)  # Длина промежутка

        average_value = 0

        delta_min_max = (2 * self.model.s_max) * 0.05

        for i in range(self.model.n):
            average_value = average_value + math.fabs(self.model.y[i])
            if i % gap_length == 0 and i > 0 or i == self.model.n - 1:
                average_value = average_value / gap_length
                self.all_average_value.append(average_value)
                average_value = 0

        flag_stationarity = True
        for i in range(self.all_average_value.__len__() - 1):

            if math.fabs(self.all_average_value[i] - self.all_average_value[i + 1]) > delta_min_max:
                flag_stationarity = False

        return flag_stationarity

    # Рассчет дисперсии
    def calculation_dispersion(self, iteration_number):

        if iteration_number <= 0:
            return

        trend_list = np.copy(self.model.y)

        for i in range(iteration_number - 1):
            self.model.calculation()
            deep_copy_y = np.copy(self.model.y)
            trend_list += deep_copy_y

        trend_list = trend_list / iteration_number

        average_value = np.mean(trend_list)

        dispersion = 0
        for i in range(self.model.n):
            dispersion += (trend_list[i] - average_value) * (trend_list[i] - average_value)

        self.dispersion = dispersion / self.model.n

        return self.dispersion

    # Рассчет стандартного отклонения
    def calculation_standard_deviation(self):

        if self.dispersion == 0:  # Если не была расчитана диспресия
            self.calculation_dispersion(1)

        self.standard_deviation = math.sqrt(self.dispersion)

        return self.standard_deviation

    # Рассчет асимметрии
    def calculation_asymmetry(self):

        if self.average_value == 0:
            self.calculation_average_value()

        sum_of_values = 0

        for i in range(self.model.n):
            temp_value = (self.model.y[i] - self.average_value)
            temp_value = temp_value * temp_value * temp_value
            sum_of_values = sum_of_values + temp_value

        self.asymmetry = sum_of_values / self.model.n

        return self.asymmetry

    # Рассчет коэффициента асимметрии
    def calculation_asymmetry_coefficient(self):

        if self.standard_deviation == 0:
            self.calculation_standard_deviation()

        if self.asymmetry == 0:
            self.calculation_asymmetry()

        sigma3 = self.standard_deviation * self.standard_deviation * self.standard_deviation
        self.asymmetry_coefficient = self.asymmetry / sigma3

        return self.asymmetry_coefficient

    # Рассчет эксцесса
    def calculation_excess(self):

        if self.average_value == 0:
            self.calculation_average_value()

        sum_of_values = 0

        for i in range(self.model.n):
            temp_value = (self.model.y[i] - self.average_value)
            temp_value = temp_value ** 4  # Возведение в степень 4
            sum_of_values = sum_of_values + temp_value

        self.excess = sum_of_values / self.model.n

        return self.excess

    # Рассчет куртозис
    def calculation_kurtosis(self):

        if self.standard_deviation == 0:
            self.calculation_standard_deviation()

        if self.excess == 0:
            self.calculation_excess()

        kurtosis = self.excess / self.standard_deviation ** 4
        kurtosis = kurtosis - 3

        return kurtosis

    # Рассчет стандартного коэфициента
    def calculation_standard_ratio(self):

        sum_of_values = 0

        for i in range(self.model.n):
            temp_value = self.model.y[i] ** 2
            sum_of_values = sum_of_values + temp_value

        self.standard_ratio = sum_of_values / self.model.n

        return self.standard_ratio

    # Рассчет среднеквадратичной ошибки
    def calculation_standard_error(self):
        if self.standard_ratio == 0:
            self.calculation_standard_ratio()

        standard_error = math.sqrt(self.standard_ratio)

        return standard_error

    # Рассчет среднего абсолютного отклонения
    def calculation_mean_absolute_deviation(self):

        if self.average_value == 0:
            self.calculation_average_value()

        sum_of_values = 0

        for i in range(self.model.n):
            sum_of_values = sum_of_values + math.fabs(self.model.y[i] - self.average_value)

        mean_absolute_deviation = sum_of_values / self.model.n

        return mean_absolute_deviation

    # Поиск минимального Х
    def calculation_min_x(self):
        x = np.amin(self.model.y)
        return x

    # Поиск максимального Х
    def calculation_max_x(self):
        x = np.amax(self.model.y)
        return x

    # Гистограмма
    def calculation_bar_graph(self):

        model = Model(14)  # Модель графика гистограммы

        y_min = self.model.s_min
        x = []

        interval_size = math.fabs(y_min) + self.model.s_max
        interval_size = int(interval_size) / self.number_of_intervals
        temp_value_hit_count = 0
        max_bar_graph_value = 0

        for i in range(self.number_of_intervals):
            x.append(i)
            for j in range(self.model.n):
                y = self.model.y[j]
                if y >= (y_min + interval_size * i):
                    if y < (y_min + interval_size * (i + 1)):
                        temp_value_hit_count = temp_value_hit_count + 1

            self.bar_graph.append(temp_value_hit_count)

            if max_bar_graph_value <= temp_value_hit_count:
                max_bar_graph_value = temp_value_hit_count

            temp_value_hit_count = 0

        model.n = self.number_of_intervals
        model.display_n = model.n
        model.y = np.array(self.bar_graph)
        model.x = np.array(x)
        model.s_min = 0
        model.s_max = max_bar_graph_value

        return model

    # Взаимной корреляция
    def calculation_nested_correlation(self):

        model = Model(16)  # Модель графика взаимной корреляция
        analysis_model_n = self.model.n

        y_list_1 = copy.deepcopy(self.model.y)
        self.calculation_average_value()
        average_value1 = self.average_value

        self.model.calculation()
        y_list_2 = copy.deepcopy(self.model.y)
        self.calculation_average_value()
        average_value2 = self.average_value

        x = []
        y = []

        # Знаменатель
        sum_1 = 0
        sum_2 = 0

        for j in range(analysis_model_n - 1):
            temp_value_1 = (y_list_1[j] - average_value1)
            temp_value_1 = temp_value_1 ** 2
            sum_1 = sum_1 + temp_value_1

            temp_value_2 = (y_list_2[j] - average_value2)
            temp_value_2 = temp_value_2 ** 2
            sum_2 = sum_2 + temp_value_2

        denominator = sum_1 * sum_2
        denominator = math.sqrt(denominator)

        for i in range(self.l):

            numerator = 0

            for j in range(analysis_model_n - i - 1):
                temp_value = (y_list_1[j] - average_value1) * (y_list_2[j + i] - average_value2)
                numerator = numerator + temp_value

            result_y = numerator / denominator

            x.append(i)
            y.append(result_y)

        model.n = self.l
        model.y = np.array(y)
        model.x = np.array(x)

        model.axis_max = np.amax(model.y)
        model.axis_min = np.amin(model.y)

        return model

        # Преобразование фурье

    # Преобразование Фурье (Спектр) - Custom
    def calculation_fourier_transform(self):

        new_model = Model(18)  # Модель графика фурье
        analyses = self.model
        x = []
        y = []

        # Создаем списки для операции деконволюции
        self.spectrum_real_part_list = []         # Список с действительной частью
        self.spectrum_imaginary_part_list = []    # Список с мнимой частью

        rem = 0
        imm = 0

        n = analyses.n
        for i in range(n - 1):
            for j in range(n - 1):
                xk = analyses.y[j]
                # xk = analyses.get_y_i(j)
                yn = xk * math.cos((2 * math.pi * i * j) / n)
                rem + rem + yn

                yn_1 = xk * math.sin((2 * math.pi * i * j) / n)
                imm = imm + yn_1

            rem = rem / n
            imm = imm / n

            self.spectrum_real_part_list.append(rem)
            self.spectrum_imaginary_part_list.append(imm)

            yn = math.sqrt(rem ** 2 + imm ** 2)
            y.append(yn)
            x.append(i)
            rem = 0
            imm = 0

        delta_f = 1 / (self.model.n * self.delta_t)

        end = 0
        for i in x:
            x[i] = x[i] * delta_f
            end += 1

        new_model.x = np.array(x)
        new_model.y = np.array(y)
        new_model.n = new_model.x[end - 1]

        new_model.display_n = new_model.n / 2

        new_model.axis_max = np.amax(new_model.y) * 2
        new_model.axis_min = np.amin(new_model.y) * 2

        new_model.flag_checking_display_n = 1

        return new_model

    # Обратное преобразование фурье для операции Деконволюции
    def inverse_fourier_transform(self):
        pass

    # Операция деконволюции
    def deconvolution(self):
        pass

    # Преобразование фурье (Спектр) - Стандартные библиотеки Python для звука
    def calculation_spectrum(self):
        new_model = Model(18)  # Модель графика фурье
        spectrum = rfft(self.model.y)

        n = self.model.n
        new_model.x = rfftfreq(n, 1./self.model.rate)
        new_model.y = np.abs(spectrum/n)

        return new_model

    # Быстрое Преобразование фурье (Спектр) - Стандартные библиотеки Python для остальных случаев
    def calculation_bpf(self):
        new_model = Model(18)  # Модель графика фурье
        spectrum = rfft(self.model.y)

        new_model.y = abs(spectrum)
        new_model.n = len(spectrum)
        new_model.display_n = new_model.n
        new_model.x = np.arange(0, new_model.n)
        return new_model

    # Спектр фильтров
    def spectrum(self):
        new_model = Model(18)  # Модель графика фурье
        number_of_points = int(len(self.model.y))
        delta_freq_1 = 1 / (2 * self.model.dt)
        delta_freq_2 = int(number_of_points / 2)
        delta_freq = delta_freq_1 / delta_freq_2
        # delta_freq = (1 / (2 * self.model.dt)) / (number_of_points / 2)

        result_y = []
        result_x = []

        for i in range(number_of_points):
            real_part = 0
            imaginary_part = 0

            for j in range(number_of_points):
                real_part += self.model.y[j] * math.cos(2 * math.pi * i * j / number_of_points)
                imaginary_part += self.model.y[j] * math.sin(2 * math.pi * i * j / number_of_points)

            real_part /= number_of_points
            imaginary_part /= number_of_points

            result_x.append(i * delta_freq)
            value_y = math.sqrt(math.pow(real_part, 2) + math.pow(imaginary_part, 2))
            result_y.append(value_y)

        for i in range(number_of_points):
            result_y[i] *= number_of_points

        new_model.x = np.array(result_x)
        new_model.y = np.array(result_y)

        display_n = int( len(new_model.x) / 2)
        new_model.display_x = new_model.x[:display_n]
        new_model.display_y = new_model.y[:display_n]
        new_model.flag_checking_display_x = 1

        return new_model

    # Автокорреляция
    def calculation_autocorrelation(self):

        model = Model(15)  # Модель графика автокорреляции
        analysis_model_n = self.model.n

        if self.average_value == 0:
            self.calculation_average_value()

        x = []
        y = []

        # Считаем знаменатель
        denominator = 0
        for j in range(analysis_model_n - 1):
            y_i = self.model.y[j]
            temp_value = (y_i - self.average_value)
            temp_value = temp_value ** 2
            denominator = denominator + temp_value

        # Считаем числитель
        for i in range(self.l):

            numerator = 0

            for j in range(analysis_model_n - i - 1):
                y_i = self.model.y[j]
                y_l = self.model.y[j + i]
                temp_value = (y_i - self.average_value) * (y_l - self.average_value)
                numerator = numerator + temp_value

            result_y = numerator / denominator

            x.append(i)
            y.append(result_y)

        model.n = self.l
        model.y = np.array(y)
        model.x = np.array(x)

        model.axis_max = np.amax(model.y)
        model.axis_min = np.amin(model.y)

        return model

    # Антисдвиг
    def calculation_anti_shift(self):
        model = Model(23)
        model.y = np.copy(self.model.y)

        # Убираем 0 в начале графика который использовали для отображения
        for i in range(10):
            rand_value = random.uniform(- self.model.s_without_spikes, self.model.s_without_spikes)
            model.y[i] = rand_value + self.model.argument

        average_value = np.mean(model.y)
        model.y = model.y - average_value

        model.axis_max = np.amax(model.y) * 2
        model.axis_min = np.amin(model.y) * 2

        return model

    # Антиспайк
    def calculation_anti_spike(self):
        model = Model(22)
        analysis_model_n = self.model.n
        model.y = np.copy(self.model.y)

        spike_min = self.model.s_without_spikes
        for i in range(analysis_model_n):
            yn = math.fabs(model.y[i])
            if yn > spike_min:
                if i == 0:
                    model.y[i] = model.y[i + 1]
                else:
                    if i == analysis_model_n - 1:
                        model.y[i] = model.y[i - 1]
                    else:
                        model.y[i] = (model.y[i - 1] + model.y[i + 1]) / 2

        model.axis_max = np.amax(model.y) * 2
        model.axis_min = np.amin(model.y) * 2

        return model

    def calculation_anti_spike_exam(self):
        model = Model(22)
        analysis_model_n = self.model.n
        model.y = np.copy(self.model.y)

        spike_min = self.model.s_without_spikes_min
        spike_max = self.model.s_without_spikes_max

        for i in range(analysis_model_n):
            #yn = math.fabs(model.y[i])
            yn = model.y[i]
            if yn < spike_min:
                if i == 0:
                    model.y[i] = model.y[i + 1]
                else:
                    if i == analysis_model_n - 1:
                        model.y[i] = model.y[i - 1]
                    else:
                        model.y[i] = (model.y[i - 1] + model.y[i + 1]) / 2

            if yn > spike_max:
                if i == 0:
                    model.y[i] = model.y[i + 1]
                else:
                    if i == analysis_model_n - 1:
                        model.y[i] = model.y[i - 1]
                    else:
                        model.y[i] = (model.y[i - 1] + model.y[i + 1]) / 2

        model.axis_max = np.amax(model.y) * 2
        model.axis_min = np.amin(model.y) * 2

        return model

    # Антитренд методом скользящего окна
    def calculation_anti_trend(self):
        model = Model(24)
        size_of_window = 100
        analysis_model_n = self.model.n
        sum_value_of_window = 0
        model.y = np.copy(self.model.y)

        for i in range(analysis_model_n - size_of_window):
            for j in range(size_of_window):
                sum_value_of_window += model.y[i + j]

            average = sum_value_of_window / size_of_window
            model.y[i] = average
            sum_value_of_window = 0

        for i in range(analysis_model_n - size_of_window, analysis_model_n):
            for j in range(size_of_window):
                sum_value_of_window += model.y[i - j]

            average = sum_value_of_window / size_of_window
            model.y[i] = average
            sum_value_of_window = 0

        model.y = self.model.y - model.y

        model.axis_max = np.amax(model.y) * 1.2
        model.axis_min = np.amin(model.y) * 1.2

        return model
