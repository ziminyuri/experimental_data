import math


# m -  количество значений
# на выходе должно быть 2m + 1
def filter_potter(m, dt, fc):
    # прямоуголник
    arg = 2 * dt * fc
    lpw = [arg]
    arg *= math.pi

    for i in range(1, m):
        append_value = (math.sin(arg * i)) / (math.pi * i)
        lpw.append(append_value)

    # трапеция
    lpw[m] /= 2

    # Сглаживающие окно Поттера P310
    d = [0.35577019, 0.24369830, 0.07211497, 0.00630165]
