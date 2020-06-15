import numpy as np


def normalisation_arr_to_pixel(arr):
    arr_max = np.amax(arr)
    arr_min = np.amin(arr)

    c = arr_max - arr_min

    result = ((arr - arr_min) / c) * 255

    return result
