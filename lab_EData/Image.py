import math
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg

from PIL import Image, ImageDraw
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap


class MyImage:
    def __init__(self, main_window):
        self.main_window = main_window.main_window
        self.path = None
        self.image = None

        self.place_to_show_1 = main_window.label_model_1
        self.place_to_show_2 = main_window.label_model_2
        self.place_to_show_3 = main_window.label_model_3
        self.place_to_show_4 = main_window.label_model_4
        self.place_to_show_5 = main_window.label_model_5
        self.place_to_show_6 = main_window.label_model_6

        self.bar_chart_y = np.zeros(255)
        self.bar_chart_x = np.arange(0, 255)

        self.cdf_x = self.bar_chart_x.copy()
        self.cdf_y = np.zeros(255)

    def open(self) -> None:
        self.path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.main_window, "Open Image", ".", "Image Files (*.png *.jpg *.bmp)"
        )
        if self.path:
            self.image = QPixmap(self.path)
            self.place_to_show_1.setPixmap(self.image)

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

    def update(self, place_to_show: int = 1) -> None:
        self.image = QPixmap("temp.jpg")

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

    def image_processing(self, type_processing: str, show_image: bool = False, place_to_show_image: int = 1) -> None:
        self.image.save("temp.jpg")
        pil_img = Image.open("temp.jpg")
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

        pil_img.save("temp.jpg")

        if show_image:
            self.update(place_to_show_image)

    def bar_chart(self, graphWidget, plot: bool = True) -> None:
        self.bar_chart_y = np.zeros(255)
        self.image.save("temp.jpg")
        pil_img = Image.open("temp.jpg")
        width = pil_img.size[0]
        height = pil_img.size[1]
        pix = pil_img.load()
        for i in range(width):
            for j in range(height):
                r = pix[i, j][0]
                g = pix[i, j][1]
                b = pix[i, j][2]

                pixel_value = int((r + g + b) / 3)
                bar_chart_y_value = self.bar_chart_y[pixel_value] + 1
                self.bar_chart_y[pixel_value] = bar_chart_y_value

        if plot:
            pen = pg.mkPen(color="#AB47BC", width=5)
            graphWidget.plot(self.bar_chart_x, self.bar_chart_y, pen=pen)

    # Кумулятивная функция распределения
    def cdf_function(
        self, graphWidget, plot: bool = True, normalisation: bool = False
    ) -> None:
        self.bar_chart(graphWidget, False)

        self.cdf_y[0] = self.bar_chart_y[0]
        for i in range(1, self.bar_chart_x.size):
            self.cdf_y[i] = self.bar_chart_y[i] + self.cdf_y[i - 1]

        if normalisation is False:
            if plot:
                pen = pg.mkPen(color="#AB47BC", width=5)
                graphWidget.plot(self.cdf_x, self.cdf_y, pen=pen)

        else:
            cdf_max: int = np.amax(self.cdf_y)
            for i in range(0, self.cdf_x.size):
                self.cdf_y[i] = int(self.cdf_y[i] / cdf_max * 255)

            if plot:
                pen = pg.mkPen(color="#AB47BC", width=5)
                graphWidget.plot(self.cdf_x, self.cdf_y, pen=pen)
