import numpy as np
import math


def direct_fourier_transform(y):
    n: int = len(y)

    real_part_y: np.ndarray = np.zeros(n)
    im_part_y: np.ndarray = np.zeros(n)

    for i in range(n):
        sum_real_part: int = 0
        sum_im_part: int = 0

        for j in range(n):
            angle = (2 * math.pi * i * j) / n
            sum_real_part += y[j] * math.cos(angle)
            sum_im_part += y[j] * math.sin(angle)

        real_part_y[i] = sum_real_part / n
        im_part_y[i] = sum_im_part / n
    return real_part_y, im_part_y


def division(real_part_1, im_part_1, real_part_2, im_part_2, noise=False):
    if noise:
        # k: float = 0.00001
        # k: float = 0.0001
        k: float = 0.0005

        divider: np.ndarray = real_part_2 ** 2 + im_part_2 ** 2 + k
        real_part_3, im_part_3 = real_part_2 / divider, -im_part_2 / divider
        real_part: np.ndarray = real_part_1 * real_part_3 - im_part_1 * im_part_3
        im_part: np.ndarray = real_part_1 * im_part_3 + real_part_3 * im_part_1

    else:
        real_part: np.ndarray = (real_part_1 * real_part_2 + im_part_1 * im_part_2) / (real_part_2 ** 2 + im_part_2 ** 2)
        im_part: np.ndarray = (im_part_1 * real_part_2 - real_part_1 * im_part_2) / (real_part_2 ** 2 + im_part_2 ** 2)

    return real_part, im_part


def inverse_fourier_transform(real_part: np.ndarray, im_part: np.ndarray):
    n: int = len(real_part)
    result: np.ndarray = np.zeros(n)
    for i in range(n):
        sum_r = 0
        for j in range(n):
            angle = (2 * math.pi * i * j) / n
            sum_r += real_part[j] * math.cos(angle) + im_part[j] * math.sin(angle)
        result[i] = sum_r

    return result