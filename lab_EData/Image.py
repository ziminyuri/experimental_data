import math
import array
import os
import random

import numpy as np
from PIL import Image, ImageDraw
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from model_1 import Model
import pyqtgraph as pg
from model_1 import convolution_img
import cv2
from skimage.util import random_noise

import matplotlib.pyplot as plt


class MyImage:
    def __init__(self, main_window):
        self.main_window = main_window.main_window
        self.path = None
        self.image = None
        self.image_path_default: str = "temp.jpg"

        self.place_to_show_1 = main_window.label_model_1
        self.place_to_show_2 = main_window.label_model_2
        self.place_to_show_3 = main_window.label_model_3
        self.place_to_show_4 = main_window.label_model_4
        self.place_to_show_5 = main_window.label_model_5
        self.place_to_show_6 = main_window.label_model_6

        self.bar_chart_y: np.ndarray = np.zeros(255)
        self.bar_chart_x: np.ndarray = np.arange(0, 256)

        self.cdf_x: np.ndarray = self.bar_chart_x.copy()
        self.cdf_y: np.ndarray = np.zeros(256)

    def open(self) -> None:
        self.path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.main_window, "Open Image", ".", "Image Files (*.png *.jpg *.bmp *.xcr)"
        )
        flag_xcr: int = self.path.find('xcr')

        if self.path and flag_xcr == -1:
            self.image = QPixmap(self.path)
            self.place_to_show_1.setPixmap(self.image)

        elif self.path and flag_xcr != -1:
            count: int = int(os.stat(self.path).st_size / 2)
            with open(self.path, 'rb') as fp:
                binary16 = array.array("h")
                binary16.fromfile(fp, count)

            binary_array: np.ndarray = np.array(binary16.tolist())
            binary_array_min = np.amin(binary_array)

            width: int = 400
            height: int = 300
            img = Image.new('RGB', (width, height), color='red')
            pil_draw = ImageDraw.Draw(img)

            pixel: int = 0
            for i in range(height):
                for j in range(width):

                    pixel_value = int(binary_array[pixel] - binary_array_min)
                    pil_draw.point((j, i), (pixel_value, pixel_value, pixel_value))
                    pixel += 1

            img.save(self.image_path_default)
            self.update(1)

    def update(self, place_to_show: int = 1) -> None:
        self.image = QPixmap(self.image_path_default)

        if place_to_show == 1:
            self.place_to_show_1.setPixmap(self.image)

        elif place_to_show == 2:
            self.place_to_show_2.setPixmap(self.image)

        elif place_to_show == 3:
            self.place_to_show_3.setPixmap(self.image)

        elif place_to_show == 4:
            self.place_to_show_4.setPixmap(self.image)

        elif place_to_show == 5:
            self.place_to_show_5.setPixmap(self.image)

        elif place_to_show == 6:
            self.place_to_show_6.setPixmap(self.image)

    def smoothing(self, type_smoothing: str, factor: float, show_image: bool = False, place_to_show_image: int = 1) \
            -> None:
        self.image.save(self.image_path_default)
        pil_img = Image.open(self.image_path_default)
        width = pil_img.size[0]
        height = pil_img.size[1]

        new_width = int(width * factor)
        new_height = int(height * factor)

        if type_smoothing == "nearest":
            p = pil_img.resize((new_width, new_height), Image.NEAREST)
            pil_img = p

        elif type_smoothing == "bilinear":
            p = pil_img.resize((new_width, new_height), Image.BILINEAR)
            pil_img = p

        pil_img.save(self.image_path_default)

        if show_image:
            self.update(place_to_show_image)

    @staticmethod
    def negative(red: int, green: int, blue: int):
        return 255 - red, 255 - green, 255 - blue

    @staticmethod
    def gamma_correction(red: int, green: int, blue: int):
        c = 20
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

    @staticmethod
    def logarithmic(red: int, green: int, blue: int):
        c = 60
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

    def cdf(self, red: int, green: int, blue: int):
        red = int(self.cdf_y[red])
        green = int(self.cdf_y[green])
        blue = int(self.cdf_y[blue])

        return red, green, blue

    def image_processing(self, type_processing: str, show_image: bool = False, place_to_show_image: int = 1) -> None:
        self.image.save(self.image_path_default)
        pil_img = Image.open(self.image_path_default)
        pil_draw = ImageDraw.Draw(pil_img)
        width = pil_img.size[0]
        height = pil_img.size[1]
        pix = pil_img.load()
        for i in range(width):
            for j in range(height):
                r = pix[i, j][0]
                g = pix[i, j][1]
                b = pix[i, j][2]

                if type_processing == "negative":
                    red, green, blue = self.negative(r, g, b)

                elif type_processing == "gamma":
                    red, green, blue = self.gamma_correction(r, g, b)

                elif type_processing == "logarithmic":
                    red, green, blue = self.logarithmic(r, g, b)

                elif type_processing == "cdf":
                    red, green, blue = self.cdf(r, g, b)

                else:
                    red = 0
                    green = 0
                    blue = 0

                pil_draw.point((i, j), (red, green, blue))

        pil_img.save(self.image_path_default)

        if show_image:
            self.update(place_to_show_image)

    def bar_chart(self) -> object:
        self.bar_chart_y: np.ndarray = np.zeros(256)
        self.image.save(self.image_path_default)
        pil_img = Image.open(self.image_path_default)
        width: int = pil_img.size[0]
        height: int = pil_img.size[1]
        pix = pil_img.load()
        for i in range(width):
            for j in range(height):
                r = pix[i, j][0]
                g = pix[i, j][1]
                b = pix[i, j][2]

                pixel_value: int = int((r + g + b) / 3)
                bar_chart_y_value: int = self.bar_chart_y[pixel_value] + 1
                self.bar_chart_y[pixel_value] = bar_chart_y_value

        model = Model("Гистограма изображения")
        model.y = self.bar_chart_y
        model.x = self.bar_chart_x

        return model

    # Кумулятивная функция распределения
    def cdf_function(self, normalisation: bool = False) -> object:
        self.bar_chart()

        self.cdf_y[0] = self.bar_chart_y[0]
        for i in range(1, self.bar_chart_x.size):
            self.cdf_y[i] = self.bar_chart_y[i] + self.cdf_y[i - 1]

        if normalisation is True:
            cdf_max: int = np.amax(self.cdf_y)
            for i in range(0, self.cdf_x.size):
                self.cdf_y[i] = int(self.cdf_y[i] / cdf_max * 255)

        model = Model("Кумулятивная функция распределения")
        model.y = self.cdf_y
        model.x = self.cdf_x

        return model

    # Cпектр Фурье изображения
    def fft(self, graphWidget, show_plot):
        self.image.save(self.image_path_default)
        pil_img = Image.open(self.image_path_default)
        width = pil_img.size[0]
        height = pil_img.size[1]
        pix = pil_img.load()
        matrix = np.zeros((width, height))
        pen = pg.mkPen(color="#AB47BC", width=1)
        legend: str = 'Спектр Фурье изображения'

        if show_plot:
            graphWidget.show()
            graphWidget.addLegend()

        for i in range(width):
            for j in range(height):
                red = pix[i, j][0]
                matrix[i][j] = red

            new_image = np.gradient(matrix[i - 1, :])
            new_image_1 = np.gradient(matrix[i, :])
            Rxy = np.correlate(new_image, new_image_1, mode='full')

            fft = np.fft.rfft(Rxy)
            axis_shift = np.linspace(0, 255, len(fft))

            if i == 0:
                graphWidget.plot(x=axis_shift, y=abs(fft), pen=pen, name=legend)
            else:
                graphWidget.plot(x=axis_shift, y=abs(fft), pen=pen)

    def filtration(self, my_filter: object):
        self.image.save(self.image_path_default)
        pil_img = Image.open(self.image_path_default)
        pil_draw = ImageDraw.Draw(pil_img)
        width = pil_img.size[0]
        height = pil_img.size[1]
        pix = pil_img.load()
        matrix = np.zeros((width, height))

        for i in range(width):
            for j in range(height):
                red = pix[i, j][0]
                matrix[i][j] = red

            convolution_row = convolution_img(matrix[i], my_filter.y)
            matrix[i] = convolution_row

        normalisation = True
        if normalisation is True:
            pix_max: int = np.amax(matrix)
            for i in range(width):
                for j in range(height):
                    matrix[i][j] = int(matrix[i][j] / pix_max * 255)

        for i in range(width):
            for j in range(height):
                red = int(matrix[i][j])
                green = int(matrix[i][j])
                blue = int(matrix[i][j])

                pil_draw.point((i, j), (red, green, blue))

        pil_img.save("filtration.jpg")

    def noise(self, type_of_noise, show_image, place_to_show_image, factor=0.01):
        if type_of_noise == "sold_peper":
            self.image.save(self.image_path_default)
            pil_img = Image.open(self.image_path_default)
            pil_draw = ImageDraw.Draw(pil_img)
            width = pil_img.size[0]
            height = pil_img.size[1]
            percentage_noise = int(width * height * factor)
            for i in range (percentage_noise):
                x = random.randrange(1, width, 1)
                y = random.randrange(1, height, 1)
                choice = random.randint(1, 2)
                if choice == 1:
                    red = 0
                    green = 0
                    blue = 0

                else:
                    red = 255
                    green = 255
                    blue = 255

                pil_draw.point((x, y), (red, green, blue))

            pil_img.save(self.image_path_default)

        elif type_of_noise == "gaussian":
            self.image.save(self.image_path_default)
            image = cv2.imread(self.image_path_default)
            gauss = random_noise(image, mode='gaussian', seed=None, clip=True, var=factor)
            plt.imsave(self.image_path_default, gauss)

        if show_image:
            self.update(place_to_show_image)














