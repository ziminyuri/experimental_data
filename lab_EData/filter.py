import math
import numpy as np

# m -  количество значений
# на выходе должно быть 2m + 1
def filter_potter(m, dt, fc):
    # прямоуголник
    arg = 2 * dt * fc
    lpw = [arg]
    arg *= math.pi

    for i in range(1, m+1):
        append_value = (math.sin(arg * i)) / (math.pi * i)
        lpw.append(append_value)

    # трапеция
    lpw[m] /= 2

    # Сглаживающие окно Поттера P310
    d = [0.35577019, 0.24369830, 0.07211497, 0.00630165]

    sum_g = lpw[0]

    for i in range(1, m+1):
        summ = d[0]
        arg = math.pi * i / m
        for k in range(1, 3):
            summ += 2 * d[k] * math.cos(arg * k)
        lpw[i] *= summ
        sum_g += 2 * lpw[i]

    # нормализация
    for i in range(m+1):
        lpw[i] /= sum_g

    #lpw_1 = np.array(lpw)
    lpw_2 = lpw.copy()
    lpw_2.reverse()

    for i in range(1, len(lpw)):
        lpw_2.append(lpw[i])

    lpw = np.array(lpw_2)
    print('fdsaf')

    return lpw

    #final = lpw_2.copy()
    #final = np.append(lpw_1)
    #return final
