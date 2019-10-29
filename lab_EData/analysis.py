import math
import copy
from model import *


class Analysis:
    def __init__(self, model):

        self.model = model                 # Модель, которую анализиурем

        self.all_average_value = []        # Все средние значения
        self.average_value = 0             # Среднее значения тренда
        self.dispersion = 0                # Дисперсия
        self.standard_deviation = 0        # Стандартное отклонение
        self.asymmetry = 0                 # Асимметрия
        self.asymmetry_coefficient = 0     # Коэффициент асимметрии
        self.standard_ratio = 0            # Стандартный коэффициент
        self.excess = 0                    # Эксцесс

        # Параметры для гистограммы
        self.bar_graph = []                # Значения для графика гистограммы
        self.number_of_intervals = 40      # Количество интервалов для гистограмм
        self.max_bar_graph_value = 0

        # Параметры для автокорреляции
        self.l = model.n - 1         # Сдвиг

    # Рассчет среднего значения
    def calculation_average_value(self):

        self.average_value = np.mean(self.model.y)

        return  self.average_value

        """
        average_value = 0

        for i in range(self.model.n):
            average_value = average_value + self.model.y[i]

        new_average_value = average_value / self.model.n

        self.average_value = new_average_value

        return new_average_value
        """

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
        model.y = np.array(self.bar_graph)
        model.x = np.array(x)
        model.s_min(0)
        model.s_max(max_bar_graph_value)

        return model

    # Взаимной корреляция
    def calculation_nested_correlation(self):

        model = Model(16)                       # Модель графика взаимной корреляция
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

        result_y_min = 0
        result_y_max = 0

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
                temp_value = (y_list_1[j] - average_value1) * (y_list_2[j+i] - average_value2)
                numerator = numerator + temp_value

            result_y = numerator / denominator

            if result_y_min > result_y:
                result_y_min = result_y

            if result_y_max < result_y:
                result_y_max = result_y

            x.append(i)
            y.append(result_y)

        model.n = self.l
        model.y = np.array(y)
        model.x = np.array(x)
        model.s_min = result_y_min
        model.s_max = result_y_max

        return model

        # Преобразование фурье
    def calculation_fourier_transform(self):

        new_model = Model(18)  # Модель графика фурье
        analyses = self.model
        x = []
        y = []

        rem = 0
        imm = 0

        n = analyses.n
        for i in range(n-1):
            for j in range(n-1):
                # xk =
                # xk = analyses.get_y_i(j)
                yn = xk * math.cos((2 * math.pi * i * j) / n)
                rem + rem + yn

                yn_1 = xk * math.sin((2 * math.pi * i * j) / n)
                imm = imm + yn_1

            rem = rem / n
            imm = imm / n

            yn = math.sqrt(rem ** 2 + imm ** 2)
            y.append(yn)
            x.append(i)
            rem = 0
            imm = 0

        new_model.x = np.array(x)
        new_model.y = np.array(y)
        new_model.n = n-1

        return new_model

    # Автокорреляция
    def calculation_autocorrelation(self):

        model = Model(15)  # Модель графика автокорреляции
        analysis_model_n = self.model.n

        if self.average_value == 0:
            self.calculation_average_value()

        x = []
        y = []

        result_y_min = 0
        result_y_max = 0

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
                y_l = self.model.y[j+i]
                temp_value = (y_i - self.average_value) * (y_l - self.average_value)
                numerator = numerator + temp_value

            result_y = numerator / denominator

            if result_y_min > result_y:
                result_y_min = result_y

            if result_y_max < result_y:
                result_y_max = result_y

            x.append(i)
            y.append(result_y)

        model.n = self.l
        model.y = np.array(y)
        model.x = np.array(x)
        model.s_min = result_y_min
        model.s_max = result_y_max

        return model

    # Антисдвиг
    def calculation_anti_shift(self):
        model = Model(23)
        model.y = np.copy(self.model.y)

        # Убираем 0 в начале графика который использовали для отображения
        for i in range(10):
            rand_value =  random.uniform(- self.model.s_without_spikes, self.model.s_without_spikes)
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
                    model.y[i] = model.y[i+1]
                else:
                    if i == analysis_model_n - 1:
                        model.y[i] = model.y[i-1]
                    else:
                        model.y[i] = (model.y[i-1] + model.y[i+1]) / 2

        model.axis_max = np.amax(model.y) * 2
        model.axis_min = np.amin(model.y) * 2

        return model

    # Антитренд методом скользящего окна
    def calculation_anti_trend(self):
        model = Model(24)
        model.y = np.copy(self.model.y)
        analysis_model_n = self.model.n

        for i in range(2):
            for j in range(analysis_model_n):
                if j == 0:
                    if model.y[j] == model.y[j+1]:
                        model.y[j] = model.y[j+1]
        ''' 
        for k in range(2):
            for i in range(analysis_model_n):
                if
        '''

        medium = int(analysis_model_n / 2)
        size_of_sliding_window  = int(analysis_model_n / 50)

        for i in range(analysis_model_n):
            sum_value_of_window = 0

            for j in range(size_of_sliding_window):

                if i < medium:
                    sum_value_of_window += model.y[i+j]
                else:
                    sum_value_of_window += model.y[i - j]

            average_value = sum_value_of_window / size_of_sliding_window
            model.y[i] = average_value

        model.axis_max = np.amax(model.y) * 2
        model.axis_min = np.amin(model.y) * 2

        return model
