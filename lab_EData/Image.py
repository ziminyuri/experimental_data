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
        self.place_to_show = main_window.label_model_1

        self.bar_chart_y = np.zeros(255)
        self.bar_chart_x = np.arange(0, 255)

    def open(self) -> None:
        self.path, _ = QtWidgets.QFileDialog.getOpenFileName(self.main_window,
                                                             "Open Image", ".", "Image Files (*.png *.jpg *.bmp)")
        if self.path:
            self.image = QPixmap(self.path)
            self.place_to_show.setPixmap(self.image)

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

    def update(self) -> None:
        self.image = QPixmap("temp.jpg")
        self.place_to_show.setPixmap(self.image)

    def image_processing(self, type_processing: str) -> None:
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

                else:
                    red = 0
                    green = 0
                    blue = 0

                pil_draw.point((i, j), (red, green, blue))

        pil_img.save("temp.jpg")
        self.update()

    def bar_chart(self, graphWidget):
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

        graphWidget.plot(self.bar_chart_x, self.bar_chart_y, pen='#AB47BC')



    """
    @staticmethod
    def bar_chart_pyqt() -> None:
        global p_img
        width = p_img.size[0]
        height = p_img.size[1]
        rgb_im = p_img.convert('RGB')
        pix = rgb_im.load()

        for i in range(width):
            for j in range(height):
                r = pix[i, j][0]
                g = pix[i, j][1]
                b = pix[i, j][2]

                average_value: int = int((r + g + b) / 3)
                bar_chart_value = bar_chart_y[average_value] + 1
                bar_chart_y[average_value] = bar_chart_value

        plt.plot(bar_chart_x, bar_chart_y)
        plt.show()
"""


