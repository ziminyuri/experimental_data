import math
import numpy as np


# m -  количество значений
# на выходе должно быть 2m + 1
# Фильтр низких частот
def filter_potter(m, dt, fc):
    # прямоуголник
    arg = 2 * dt * fc
    lpw = [arg]
    arg *= math.pi

    for i in range(1, m + 1):
        append_value = (math.sin(arg * i)) / (math.pi * i)
        lpw.append(append_value)

    # трапеция
    lpw[m] /= 2

    # Сглаживающие окно Поттера P310
    d = [0.35577019, 0.24369830, 0.07211497, 0.00630165]

    sum_g = lpw[0]

    for i in range(1, m + 1):
        summ = d[0]
        arg = (math.pi * i) / m
        for k in range(1, 4):
            summ += 2 * d[k] * math.cos(arg * k)
        lpw[i] *= summ
        sum_g += 2 * lpw[i]

    # нормализация
    for i in range(m + 1):
        lpw[i] /= sum_g

    lpw_2 = lpw.copy()
    lpw_2.reverse()

    for i in range(1, len(lpw)):
        lpw_2.append(lpw[i])

    lpw = np.array(lpw_2)

    return lpw


# Фильтр высоких частот
def high_potter_filter(m, dt, fc):
    low_potter_filter = filter_potter(m, dt, fc)

    high_potter_filter_graph = []
    n = 2 * m + 1

    for i in range(n):
        if i == m:
            high_potter_filter_graph.append(1 - low_potter_filter[i])
        else:
            high_potter_filter_graph.append(-low_potter_filter[i])

    return high_potter_filter_graph


# Полосовой фильтр
def bandpass_filter(m, dt, fc_1, fc_2):
    bandpass_filter_graph = []

    low_potter_filter_1 = filter_potter(m, dt, fc_1)
    low_potter_filter_2 = filter_potter(m, dt, fc_2)

    n = 2 * m + 1
    for i in range(n):
        value = low_potter_filter_2[i] - low_potter_filter_1[i]
        bandpass_filter_graph.append(value)

    return bandpass_filter_graph


# Режекторный фильтр
def notch_filter(m, dt, fc_1, fc_2):
    notch_filter_graph = []

    if (fc_2 > fc_1):
        low_potter_filter_1 = filter_potter(m, dt, fc_1)
        low_potter_filter_2 = filter_potter(m, dt, fc_2)
    else:
        low_potter_filter_1 = filter_potter(m, dt, fc_2)
        low_potter_filter_2 = filter_potter(m, dt, fc_1)

    n = 2 * m + 1
    for i in range(n):
        if i == m:
            value = 1 + low_potter_filter_1[i] - low_potter_filter_2[i]
            notch_filter_graph.append(value)
        else:
            value = low_potter_filter_1[i] - low_potter_filter_2[i]
            notch_filter_graph.append(value)

    return notch_filter_graph
