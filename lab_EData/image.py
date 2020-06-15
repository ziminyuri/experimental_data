import array
import math
import os
import random

import imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from PyQt5 import QtWidgets
from scipy import ndimage, misc

from analysis.fourier_transform import (direct_fourier_transform, division,
                                        inverse_fourier_transform)
from model import Model, convolution_img
from normalisation.img import normalisation_arr_to_pixel
from setting import *

import cv2 as opencv
import matplotlib.pyplot as plt
import skimage.measure as measure
import skimage.feature as feature
from skimage import img_as_ubyte, color
import pandas as pd


def binary_to_array(path, size_binary):
    if size_binary == 2:
        count: int = int(os.stat(path).st_size / 2)
    elif size_binary == 4:
        count: int = int(os.stat(path).st_size / 4)

    with open(path, 'rb') as fp:
        if size_binary == 2:
            binary16 = array.array("h")
        elif size_binary == 4:
            binary16 = array.array("f")

        binary16.fromfile(fp, count)

    binary_array: np.ndarray = np.array(binary16.tolist())

    return binary_array


def binary_to_jpg(path, size_binary, width, height, place_to_save=1, save_path=False, normalisation=False):
    binary_array: np.ndarray = binary_to_array(path, size_binary)
    binary_array_min = np.amin(binary_array)
    img = Image.new('RGB', (width, height), color='red')
    pil_draw = ImageDraw.Draw(img)

    if normalisation:
        binary_array_max = np.amax(binary_array)
        b_len = len(binary_array)
        for i in range(b_len):
            binary_array[i] = binary_array[i] / binary_array_max * 255

    pixel: int = 0
    for i in range(height):
        for j in range(width):
            if normalisation == False:
                pixel_value = int(binary_array[pixel] - binary_array_min)
            else:
                pixel_value = int(binary_array[pixel])

            pil_draw.point((j, i), (pixel_value, pixel_value, pixel_value))
            pixel += 1

    if save_path is False:
        save_img(img, place_to_save)
    else:
        save_img(img, place_to_save, path=path)


def open_img(main_window) -> None:
    path, _ = QtWidgets.QFileDialog.getOpenFileName(main_window.main_window, "Open Image", ".",
                                                    "Image Files (*.png *.jpg *.bmp *.xcr *.dat *.bin)")
    flag_xcr: int = path.find('.xcr')
    flag_dat: int = path.find('.dat')
    flag_bin: int = path.find('.bin')

    if path and flag_xcr == -1 and flag_dat == -1 and flag_bin == -1:
        pil_img = Image.open(path)
        save_img(pil_img)

    elif path and flag_xcr != -1:
        binary_to_jpg(path, 2, 400, 300)

    elif path and flag_dat != -1:
        binary_to_jpg(path, 4, 259, 185, save_path=True)

    elif path and flag_bin != -1:
        # binary_to_jpg(path, 2, 512, 512, normalisation=True)
        binary_to_jpg(path, 2, 256, 256, normalisation=True)


def save_img(pillow_img=None, place_to_show: int = 1, path=None) -> None:
    if place_to_show == 1:
        path_save = PATH_IMG_TEMP_1

    elif place_to_show == 2:
        path_save = PATH_IMG_TEMP_2

    elif place_to_show == 3:
        path_save = PATH_IMG_TEMP_3

    elif place_to_show == 4:
        path_save = PATH_IMG_TEMP_4

    elif place_to_show == 5:
        path_save = PATH_IMG_TEMP_5

    elif place_to_show == 6:
        path_save = PATH_IMG_TEMP_6

    pillow_img.save(path_save)

    if path is not None:
        POSITION_FOR_ANALYSIS[place_to_show] = path
    else:
        POSITION_FOR_ANALYSIS[place_to_show] = path_save


def img_row(path: str, number_row: int = 0, binary: bool = False) -> object:
    if not binary:
        pil_img = Image.open(path)
        width = pil_img.size[0]
        pix = pil_img.load()
        matrix = []

        for i in range(width):
            try:
                pixel = pix[i, number_row][0]
            except:
                pixel = pix[i, number_row]
            matrix.append(pixel)

    else:
        arr = binary_to_array(path, 4)
        arr = arr.reshape((185, 259))
        matrix = arr[number_row]

    model = Model("Cтрока №" + str(number_row))
    model.n = len(matrix)
    model.x = np.arange(model.n)
    model.y = np.array(matrix)

    return model


def derivative(path: str, number_row: int = 0, binary: bool = False) -> object:
    row_model = img_row(path, number_row, binary)
    y = np.gradient(row_model.y)
    n = len(row_model.y)
    x = np.arange(n)

    model = Model("Производная строки №" + str(number_row))
    model.y = y
    model.x = x
    model.n = n

    return model


# Переместил старую версию в image_archive.py
def noise(type_of_noise, place_to_show_image, path_img: str, factor=0.3) -> None:
    if type_of_noise == "gaussian":
        img = opencv.imread(path_img, opencv.IMREAD_GRAYSCALE)
        mean = 0
        std_dev = 255 / 2 * factor
        rows, cols = img.shape
        gauss = np.random.normal(mean, std_dev, (rows, cols)).reshape(rows, cols)
        new_img = (img + gauss).astype('uint8')
        temporary_path = 'input files/img/temp/noise.jpg'
        imageio.imsave(temporary_path, new_img)

        pillow_img = Image.open(temporary_path)
        save_img(pillow_img, place_to_show_image)

    else:
        img = opencv.imread(path_img, opencv.IMREAD_GRAYSCALE)
        for pixel in np.nditer(img, op_flags=['readwrite']):
            if random.random() < factor:
                salt_or_pepper = random.choice([0, 255])
                pixel[...] = salt_or_pepper

        temporary_path = 'input files/img/temp/noise.jpg'
        imageio.imsave(temporary_path, img)

        pillow_img = Image.open(temporary_path)
        save_img(pillow_img, place_to_show_image)


def negative(red: int, green: int, blue: int):
    return 255 - red, 255 - green, 255 - blue


def negative_gray(pixel: int) -> int:
    return 255 - pixel


def gamma_correction(red: int, green: int, blue: int, c: int):
    # c = 20
    gamma = 0.3
    new_red = int(c * math.pow(red, gamma))
    new_green = int(c * math.pow(green, gamma))
    new_blue = int(c * math.pow(blue, gamma))

    if new_red > 255:
        new_red = 255

    if new_green > 255:
        new_green = 255

    if new_blue > 255:
        new_blue = 255

    return new_red, new_green, new_blue


def gamma_correction_gray(pixel: int, c: int) -> int:
    # c = 20
    gamma = 0.3
    new_pixel = int(c * math.pow(pixel, gamma))

    if new_pixel > 255:
        new_pixel = 255

    return new_pixel


def logarithmic(red: int, green: int, blue: int, c: int):
    # c = 60
    new_red = int(c * math.log10(red + 1))
    new_green = int(c * math.log10(green + 1))
    new_blue = int(c * math.log10(blue + 1))

    if new_red > 255:
        new_red = 255

    if new_green > 255:
        new_green = 255

    if new_blue > 255:
        new_blue = 255

    return new_red, new_green, new_blue


def logarithmic_gray(pixel: int, c: int) -> int:
    # c = 60
    new_pixel = int(c * math.log10(pixel + 1))

    if new_pixel > 255:
        new_pixel = 255

    return new_pixel


def cdf(red: int, green: int, blue: int, model: object):
    red = int(model.y[red])
    green = int(model.y[green])
    blue = int(model.y[blue])

    return red, green, blue


def cdf_gray(pixel: int, model: object) -> int:
    pixel = int(model.y[pixel])

    return pixel


def image_processing(type_processing: str, path: str, place_to_show_image: int = 1, coefficient: int = 60) -> None:
    pil_img = Image.open(path)
    pil_draw = ImageDraw.Draw(pil_img)
    width = pil_img.size[0]
    height = pil_img.size[1]
    pix = pil_img.load()

    if type_processing == "cdf":
        model_cdf = cdf_function(path)

    for i in range(width):
        for j in range(height):
            try:
                r = pix[i, j][0]
                g = pix[i, j][1]
                b = pix[i, j][2]

                if type_processing == "negative":
                    red, green, blue = negative(r, g, b)

                elif type_processing == "gamma":
                    red, green, blue = gamma_correction(r, g, b, coefficient)

                elif type_processing == "logarithmic":
                    red, green, blue = logarithmic(r, g, b, coefficient)

                elif type_processing == "cdf":
                    red, green, blue = cdf(r, g, b, model_cdf)

                else:
                    red = 0
                    green = 0
                    blue = 0

                pil_draw.point((i, j), (red, green, blue))

            except:
                pixel = pix[i, j]

                if type_processing == "negative":
                    pixel = negative_gray(pixel)

                elif type_processing == "gamma":
                    pixel = gamma_correction_gray(pixel, coefficient)

                elif type_processing == "logarithmic":
                    pixel = logarithmic_gray(pixel, coefficient)

                elif type_processing == "cdf":
                    pixel = cdf_gray(pixel, model_cdf)

                else:
                    pixel = 0

                pil_draw.point((i, j), pixel)

    save_img(pil_img, place_to_show_image)


def bar_chart(path) -> object:
    bar_chart_y: np.ndarray = np.zeros(256)
    pil_img = Image.open(path)
    width: int = pil_img.size[0]
    height: int = pil_img.size[1]
    pix = pil_img.load()
    for i in range(width):
        for j in range(height):

            try:
                r = pix[i, j][0]
                g = pix[i, j][1]
                b = pix[i, j][2]

                pixel_value: int = int((r + g + b) / 3)
            except:
                pixel_value: int = pix[i, j]

            bar_chart_y_value: int = bar_chart_y[pixel_value] + 1
            bar_chart_y[pixel_value] = bar_chart_y_value

    model = Model("Гистограма изображения")
    model.y = bar_chart_y
    model.x = np.arange(0, 256)

    return model


# Кумулятивная функция распределения
def cdf_function(path: str, normalisation: bool = False) -> object:
    model_bar_chart = bar_chart(path)
    cdf_x: np.ndarray = np.arange(0, 256)
    cdf_y: np.ndarray = np.zeros(256)

    cdf_y[0] = model_bar_chart.y[0]
    for i in range(1, model_bar_chart.x.size):
        cdf_y[i] = model_bar_chart.y[i] + cdf_y[i - 1]

    if normalisation is True:
        cdf_max: int = np.amax(cdf_y)
        for i in range(0, cdf_x.size):
            cdf_y[i] = int(cdf_y[i] / cdf_max * 256)

    model = Model("Кумулятивная функция распределения")
    model.y = cdf_y
    model.x = cdf_x

    return model


def filtration(path: str, my_filter: object, place_to_show: int = 1):
    pil_img = Image.open(path)
    pil_draw = ImageDraw.Draw(pil_img)
    width = pil_img.size[0]
    height = pil_img.size[1]
    pix = pil_img.load()
    matrix = np.zeros((width, height))

    for i in range(width):
        for j in range(height):

            try:
                red = pix[i, j][0]
            except:
                red = pix[i, j]

            matrix[i][j] = red

    transpose_matrix = np.transpose(matrix)
    m = []
    for row in transpose_matrix:
        convolution_row = convolution_img(row, my_filter.y)
        m.append(convolution_row)

    s = np.array(m)
    matrix = np.transpose(s)

    normalisation = False
    if normalisation is True:
        pix_max: int = np.amax(matrix)
        for i in range(width):
            for j in range(height):
                matrix[i][j] = int(matrix[i][j] / pix_max * 255)

    for i in range(width):
        for j in range(height):

            try:
                red = int(matrix[i][j])
                green = int(matrix[i][j])
                blue = int(matrix[i][j])

                pil_draw.point((i, j), (red, green, blue))

            except:
                pixel = int(matrix[i][j])
                pil_draw.point((i, j), pixel)

    save_img(pil_img, place_to_show)


def smoothing(path: str, type_smoothing: str, factor: float = 0.5, place: int = 1,
              new_width: int = 500, resize_from_width: bool = False) -> None:
    pil_img = Image.open(path)
    width = pil_img.size[0]
    height = pil_img.size[1]

    if resize_from_width:
        factor = new_width / width
        new_width = int(width * factor)
        new_height = int(height * factor)
    else:
        new_width = int(width * factor)
        new_height = int(height * factor)

    if type_smoothing == "nearest":
        p = pil_img.resize((new_width, new_height), Image.NEAREST)
        pil_img = p

    elif type_smoothing == "bilinear":
        p = pil_img.resize((new_width, new_height), Image.BILINEAR)
        pil_img = p

    save_img(pil_img, place)


def arithmetic_filter_img(path: str, place_to_save: int, n_of_maska: int) -> None:
    pillow_img = Image.open(path)
    pil_draw = ImageDraw.Draw(pillow_img)
    width: int = pillow_img.size[0]
    height: int = pillow_img.size[1]
    pix = pillow_img.load()
    for j in range(height):
        for i in range(width):
            all_value_pixel: int = 0
            pixel_quantity: int = 0
            loop: int = 0
            average: int = 0
            while loop < 2:

                for k in range(j, j + n_of_maska):
                    if k == height:
                        break
                    for s in range(i, i + n_of_maska):
                        if s == width:
                            break

                        if loop == 0:
                            pixel = pix[s, k]
                            all_value_pixel += pixel
                            pixel_quantity += 1

                        else:
                            pil_draw.point((s, k), average)

                if pixel_quantity == 0:
                    break

                average = int(all_value_pixel / pixel_quantity)
                loop += 1

    save_img(pillow_img, place_to_save)


def median_img(path: str, place_to_save: int, n_of_maska: int) -> None:
    pillow_img = Image.open(path)
    image_after_filter = pillow_img.filter(ImageFilter.MedianFilter(n_of_maska))
    save_img(image_after_filter, place_to_save)


def deconvolution_img(path: str, place_to_save: int, func: str, noise=False) -> None:
    path_func: str = 'input files/deconvoltion_img/kernL64_f4.dat'
    path_func_array: np.ndarray = binary_to_array(path_func, 4)

    path_array: np.ndarray = binary_to_array(path, 4)

    width: int = 259
    height: int = 185

    width_func: int = 64
    kernel_list: list = path_func_array.tolist()

    for i in range(width - width_func):
        kernel_list.append(0)

    kernel_np_array: np.ndarray = np.array(kernel_list)
    func_model_real_part, func_model_im_part = direct_fourier_transform(kernel_np_array)

    path_array: np.ndarray = path_array.reshape(height, width)

    result_arr: np.ndarray = np.zeros((height, width))

    rows, cols = path_array.shape

    for i in range(rows):
        y: np.ndarray = path_array[i]
        model_real_part, model_im_part = direct_fourier_transform(y)
        decon_model_real_part, decon_model_im_part = division(model_real_part, model_im_part, func_model_real_part,
                                                              func_model_im_part, noise=noise)

        result_arr[i] = inverse_fourier_transform(decon_model_real_part, decon_model_im_part)

    result_arr: np.ndarray = normalisation_arr_to_pixel(result_arr)
    img: Image = Image.new('RGB', (width, height), color='red')
    pil_draw: ImageDraw = ImageDraw.Draw(img)

    for j in range(height):
        for i in range(width):
            pixel_v: int = int(result_arr[j][i])
            pil_draw.point((i, j), (pixel_v, pixel_v, pixel_v))

    save_img(img, place_to_save)


# Пороговое преобразование
def threshold_conversion(path: str, place_to_save: int, threshold_value: int = 100, return_img: bool = False):
    img = opencv.imread(path, opencv.IMREAD_GRAYSCALE)

    img_after_threshold = opencv.threshold(img, threshold_value, 255, opencv.THRESH_BINARY)

    # Пороговое преобразование в тех же оттенках
    # img_after_threshold = opencv.threshold(img, 100, 255, opencv.THRESH_TRUNC)

    if return_img is False:
        temporary_path = 'input files/img/temp/threshold_conversion.jpg'
        imageio.imsave(temporary_path, img_after_threshold[1])

        pillow_img = Image.open(temporary_path)
        save_img(pillow_img, place_to_save)
        return

    else:
        return img_after_threshold[1]


# Окунтуривание методом градиента
def gradient(path: str, place_to_save: int) -> None:
    pass


# Окунтуривание методом Собеля
def sobeling(path: str, place_to_save: int) -> None:
    im = imageio.imread(path)
    im = im.astype('int32')
    dx = ndimage.sobel(im, 0)  # horizontal derivative
    dy = ndimage.sobel(im, 1)  # vertical derivative
    mag = np.hypot(dx, dy)  # magnitude
    mag *= 255.0 / np.max(mag)  # normalize (Q&D)

    temporary_path = 'input files/img/temp/sobel.jpg'
    imageio.imsave(temporary_path, mag)

    pillow_img = Image.open(temporary_path)
    save_img(pillow_img, place_to_save)


# Окунтуривание оператором Лапласа
def laplacian(path: str, place_to_save: int) -> None:
    src = opencv.imread(path, opencv.IMREAD_COLOR)  # Load an image
    src_gray = opencv.cvtColor(src, opencv.COLOR_BGR2GRAY)
    ddepth = opencv.CV_16S
    kernel_size = 3
    dst = opencv.Laplacian(src_gray, ddepth, ksize=kernel_size)
    temporary_path = 'input files/img/temp/laplacian.jpg'
    abs_dst = opencv.convertScaleAbs(dst)
    imageio.imsave(temporary_path, abs_dst)

    pillow_img = Image.open(temporary_path)
    save_img(pillow_img, place_to_save)


# Эрозия
def erosion(path: str, place_to_save: int,  threshold_value: int = 100, return_img: bool = False):
    size = 3
    img_after_threshold = threshold_conversion(path, place_to_save, return_img=True, threshold_value=threshold_value)

    kernel = opencv.getStructuringElement(opencv.MORPH_RECT, (size, size))
    img_after_erosion = opencv.erode(img_after_threshold, kernel)

    if return_img is False:
        result_img = img_after_threshold - img_after_erosion

        temporary_path = 'input files/img/temp/erosion.jpg'
        # imageio.imsave(temporary_path, img_after_erosion)
        imageio.imsave(temporary_path, result_img)

        pillow_img = Image.open(temporary_path)
        save_img(pillow_img, place_to_save)
        return

    else:
        return img_after_erosion


# Диалатация
def dialatization(path: str, place_to_save: int,  threshold_value: int = 100) -> None:
    size = 3
    img_after_threshold = threshold_conversion(path, place_to_save, return_img=True, threshold_value=threshold_value)

    kernel = opencv.getStructuringElement(opencv.MORPH_RECT, (size, size))
    img_after_dialatization = opencv.dilate(img_after_threshold, kernel)
    img_after_erosion = erosion(path, place_to_save, return_img=True, threshold_value=threshold_value)

    # result_img = img_after_dialatization - img_after_threshold
    result_img = img_after_dialatization - img_after_erosion

    temporary_path = 'input files/img/temp/dialatization.jpg'
    # imageio.imsave(temporary_path, img_after_dialatization)
    imageio.imsave(temporary_path, result_img)

    pillow_img = Image.open(temporary_path)
    save_img(pillow_img, place_to_save)


# create our cumulative sum function
def cumsum(a):
    c = a
    a = iter(a)
    b = [next(a)]
    for i in a:
        v = b[-1]
        b.append(b[-1] + i)
    return np.array(b)


# create our own histogram function
def get_histogram(image, bins):
    # array with size of bins, set to zeros
    histogram = np.zeros(bins)

    # loop through pixels and sum up counts of pixels
    for pixel in image:
        histogram[pixel] += 1

    # return our final result
    return histogram


def img_to_np_array(path: str) -> np.ndarray:
    array = []
    pil_img = Image.open(path)
    width: int = pil_img.size[0]
    height: int = pil_img.size[1]
    pix = pil_img.load()
    for i in range(width):
        for j in range(height):

            try:
                r = pix[i, j][0]
                g = pix[i, j][1]
                b = pix[i, j][2]

                pixel_value: int = int((r + g + b) / 3)
            except:
                pixel_value: int = pix[i, j]

            array.append(pixel_value)

    array = np.array(array)
    return array


# Эквализация гистограммы
def histogram_equalization(path: str, place: int = 1) -> None:
    img = Image.open(path)

    # convert image into a numpy array
    img = np.asarray(img)

    # put pixels in a 1D array by flattening out img array
    flat = img.flatten()

    # show the histogram
    # plt.hist(flat, bins=50)
    hist = get_histogram(flat, 256)

    # execute the fn
    cs = cumsum(hist)

    # display the result
    plt.plot(cs)
    plt.show()

    # re-normalize cumsum values to be between 0-255

    # numerator & denomenator
    nj = (cs - cs.min()) * 255
    N = cs.max() - cs.min()

    # re-normalize the cdf
    cs = nj / N

    # cast it back to uint8 since we can't use floating point values in images
    cs = cs.astype('uint8')

    # get the value from cumulative sum for every index in flat, and set that as img_new
    img_new = cs[flat]

    # we see a much more evenly distributed histogram
    plt.hist(img_new, bins=50)

    # put array back into original shape since we flattened it
    img_new = np.reshape(img_new, img.shape)

    # set up side-by-side image display
    # fig = plt.figure()
    # fig.set_figheight(15)
    # fig.set_figwidth(15)

    # fig.add_subplot(1, 2, 1)
    #plt.imshow(img)

    # display the new image
    # fig.add_subplot(1, 2, 2)
    # plt.imshow(img_new)

    temporary_path = 'input files/img/temp/equalization.jpg'
    imageio.imsave(temporary_path, img_new)

    pillow_img = Image.open(temporary_path)
    save_img(pillow_img, place)

    plt.show(block=True)


def stones(path: str, place: int = 1) -> None:
    fn = path  # путь к файлу с картинкой
    img = opencv.imread(fn)
    gray_image = opencv.cvtColor(img, opencv.COLOR_BGR2GRAY)
    edges = feature.canny(gray_image, sigma=1.1)
    label_image = measure.label(edges)
    image_copy = gray_image.copy()
    for region in measure.regionprops(label_image):
        minr, minc, maxr, maxc = region.bbox
        image_copy[minr:maxr, (minc, maxc)] = 255
        image_copy[(minr, maxr), minc:maxc] = 255

    edges = color.gray2rgb(img_as_ubyte(image_copy))

    temporary_path = 'input files/img/temp/stones.jpg'
    imageio.imsave(temporary_path, edges)

    pillow_img = Image.open(temporary_path)
    save_img(pillow_img, place)
