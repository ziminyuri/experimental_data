from tkinter import messagebox


# Обработка нажатия на кнопку "Стационарность: СЗ"
def check_stationarity_click_button(analysis):
    check_result = analysis.check_stationarity_average_value()

    if check_result:
        messagebox.showinfo(
            "Проверка на стационарность: Среднее значение", "График стационарен"
        )
    else:
        messagebox.showinfo(
            "Проверка на стационарность: Среднее значение", "График не стационарен"
        )


# Обработка нажатия на кнопку "Диспресия"
def dispersion_click_button(analysis):
    check_result = analysis.calculation_dispersion(1)
    messagebox.showinfo("Дисперсия", "Дисперсия: " + str(check_result))


# Обработка нажатия на кнопку "Дисперсия х10"
def dispersion_x_10_click_button(analysis):
    check_result = analysis.calculation_dispersion(10)
    messagebox.showinfo("Дисперсия", "Дисперсия x10: " + str(check_result))


# Обработка нажатия на кнопку "Среднее значение"
def average_value_click_button(analysis):
    check_result = analysis.calculation_average_value()
    messagebox.showinfo("Среднее значение", "Среднее значение: " + str(check_result))


# Обработка нажатия на кнопку "Асимметрия"
def asymmetry_click_button(analysis):
    result = analysis.calculation_asymmetry()
    messagebox.showinfo("Ассиметрия", "Ассиметрия: " + str(result))


# Обработка нажатия на кнопку "Стандартное отклонение"
def standard_deviation(analysis):
    result = analysis.calculation_standard_deviation()
    messagebox.showinfo(
        "Стандартное отклонение", "Стандартное отклонение: " + str(result)
    )


# Обработка нажатия на кнопку "Коэффициент асимметрии"
def asymmetry_coefficient_click_button(analysis):
    result = analysis.calculation_asymmetry_coefficient()
    messagebox.showinfo(
        "Коэффициент асимметрии", "Коэффициент асимметрии: " + str(result)
    )


# Обработка нажатия на кнопку "Эксцесс"
def excess_click_button(analysis):
    result = analysis.calculation_excess()
    messagebox.showinfo("Эксцесс", "Эксцесс: " + str(result))


# Обработка нажатия на кнопку "Куртозис"
def kurtosis_click_button(analysis):
    result = analysis.calculation_kurtosis()
    messagebox.showinfo("Куртозис", "Куртозис: " + str(result))


# Обработка нажатия на кнопку "Стандартный коэфифциент"
def standard_ratio_click_button(analysis):
    result = analysis.calculation_standard_ratio()
    messagebox.showinfo(
        "Стандартный коэфифциент", "Стандартный коэфифциент: " + str(result)
    )


# Обработка нажатия на кнопку "Среднеквадратичная ошибка"
def standard_error_click_button(analysis):
    result = analysis.calculation_standard_error()
    messagebox.showinfo(
        "Среднеквадратичная ошибка", "Среднеквадратичная ошибка: " + str(result)
    )


# Обработка нажатия на кнопку "Среднее абсолютное отклонение"
def mean_absolute_deviation_click_button(analysis):
    result = analysis.calculation_mean_absolute_deviation()
    messagebox.showinfo(
        "Среднее абсолютное отклонение", "Среднее абсолютное отклонение: " + str(result)
    )


# Обработка нажатия на кнопку "Минимальный Х"
def x_min_click_button(analysis):
    result = analysis.calculation_min_x()
    messagebox.showinfo("Минимальный Х", "Минимальный Х: " + str(result))


# Обработка нажатия на кнопку "Максимальный Х"
def x_max_click_button(analysis):
    result = analysis.calculation_max_x()
    messagebox.showinfo("Максимальный Х", "Максимальный Х: " + str(result))
