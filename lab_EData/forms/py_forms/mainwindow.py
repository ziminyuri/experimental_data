import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap

from forms.py_forms.add_graph import Ui_add_graph
from forms.py_forms.add_sound_window import Ui_add_sound
from forms.py_forms.deconvolution_window import Ui_deconvolution_window
from forms.py_forms.filter_window import Ui_filter_window
from forms.py_forms.image_processing import image_processing_window
from forms.py_forms.statistics_window import Ui_statistics
from image import open_img

from setting import *


class Ui_mainwindow(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.setObjectName("mainwindow")
        self.main_window.resize(1500, 900)
        self.main_window.setStyleSheet("background-color: #263238")

        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.label_for_model_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_model_3.setAutoFillBackground(False)
        self.label_for_model_3.setObjectName("label_for_model_3")
        self.label_for_model_3.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_for_model_3, 0, 1, 1, 1)

        self.label_for_model_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_model_5.setObjectName("label_for_model_5")
        self.label_for_model_5.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_for_model_5, 0, 2, 1, 1)

        self.label_for_model_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_model_1.setAutoFillBackground(False)
        self.label_for_model_1.setObjectName("label_for_model_1")
        self.label_for_model_1.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_for_model_1, 0, 0, 1, 1)

        self.label_for_model_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_model_6.setObjectName("label_for_model_6")
        self.label_for_model_6.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_for_model_6, 2, 2, 1, 1)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 353, 432))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_model_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_model_1.setObjectName("label_model_1")

        self.graphWidget_1 = pg.PlotWidget(self.scrollAreaWidgetContents)
        self.graphWidget_1.hide()
        self.graphWidget_1.setBackground("#37474F")
        self.horizontalLayout.addWidget(self.graphWidget_1)

        self.horizontalLayout.addWidget(self.label_model_1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.scrollArea_5 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 253, 236))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_model_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_model_4.setObjectName("label_model_4")
        self.graphWidget_4 = pg.PlotWidget(self.scrollAreaWidgetContents)
        self.graphWidget_4.hide()
        self.graphWidget_4.setBackground("#37474F")
        self.gridLayout_6.addWidget(self.label_model_4, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.graphWidget_4, 0, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout.addWidget(self.scrollArea_5, 3, 1, 1, 1)

        self.label_for_model_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_model_2.setObjectName("label_for_model_2")
        self.label_for_model_2.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_for_model_2, 2, 0, 1, 1)

        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 253, 236))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.label_model_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_model_3.setObjectName("label_model_3")
        self.graphWidget_3 = pg.PlotWidget(self.scrollAreaWidgetContents)
        self.graphWidget_3.hide()
        self.graphWidget_3.setBackground("#37474F")
        self.gridLayout_3.addWidget(self.graphWidget_3, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.label_model_3, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_2, 1, 1, 1, 1)

        self.scrollArea_6 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 254, 236))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_model_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_model_6.setObjectName("label_model_6")
        self.graphWidget_6 = pg.PlotWidget(self.scrollAreaWidgetContents)
        self.graphWidget_6.hide()
        self.graphWidget_6.setBackground("#37474F")
        self.gridLayout_7.addWidget(self.label_model_6, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.graphWidget_6, 0, 0, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_7)
        self.gridLayout.addWidget(self.scrollArea_6, 3, 2, 1, 1)

        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 254, 236))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_model_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_model_5.setObjectName("label_model_5")
        self.graphWidget_5 = pg.PlotWidget(self.scrollAreaWidgetContents)
        self.graphWidget_5.hide()
        self.graphWidget_5.setBackground("#37474F")
        self.gridLayout_2.addWidget(self.label_model_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.graphWidget_5, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout.addWidget(self.scrollArea_3, 1, 2, 1, 1)

        self.label_for_model_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_model_4.setObjectName("label_for_model_4")
        self.label_for_model_4.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_for_model_4, 2, 1, 1, 1)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")

        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 254, 236))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_model_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_model_2.setObjectName("label_model_2")

        self.graphWidget_2 = pg.PlotWidget(self.scrollAreaWidgetContents_5)
        self.graphWidget_2.hide()
        self.graphWidget_2.setBackground("#37474F")
        self.gridLayout_5.addWidget(self.label_model_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.graphWidget_2, 0, 0, 1, 1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout.addWidget(self.scrollArea_4, 3, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        self.main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.main_window)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)


        # Инициализируем окна
        self.add_graph_window = QtWidgets.QMainWindow()
        self.add_graph_ui = Ui_add_graph(self)

        self.add_sound_window = QtWidgets.QMainWindow()
        self.add_sound_ui = Ui_add_sound()

        self.statistics_window = QtWidgets.QMainWindow()

        self.filter_window = QtWidgets.QMainWindow()

        self.deconvolution_window = QtWidgets.QMainWindow()
        self.deconvolution_ui = Ui_deconvolution_window()

        self.processing_image_window = QtWidgets.QMainWindow()

        self.action_add_graph = QtWidgets.QAction(self.main_window)
        self.action_add_graph.setObjectName("action_add_graph")
        self.action_add_graph.setShortcut('Ctrl+N')
        self.action_add_graph.triggered.connect(self.open_add_graph_window)

        self.action_open_image = QtWidgets.QAction(self.main_window)
        self.action_open_image.setObjectName("action_open_image")
        self.action_open_image.setShortcut('Ctrl+I')
        self.action_open_image.triggered.connect(self.open_image_window)

        self.action_open_sound = QtWidgets.QAction(self.main_window)
        self.action_open_sound.setObjectName("action_open_sound")
        self.action_open_sound.setShortcut('Ctrl+S')
        self.action_open_sound.triggered.connect(self.open_add_sound_window)

        self.action_close = QtWidgets.QAction(self.main_window)
        self.action_close.setShortcut('Ctrl+Q')
        self.action_close.setObjectName("action_close")

        self.action_statistics = QtWidgets.QAction(self.main_window)
        self.action_statistics.setObjectName("action_statistics")
        self.action_statistics.setShortcut('Ctrl+L')
        self.action_statistics.triggered.connect(self.open_statistics_window)

        self.action_filter = QtWidgets.QAction(self.main_window)
        self.action_filter.setObjectName("action_filter")
        self.action_filter.setShortcut('Ctrl+F')
        self.action_filter.triggered.connect(self.open_filter_window)

        self.action_deconvolution = QtWidgets.QAction(self.main_window)
        self.action_deconvolution.setObjectName("action_deconvolution")

        self.action_processing_image = QtWidgets.QAction(self.main_window)
        self.action_processing_image.setObjectName("action_processing_image")
        self.action_processing_image.setShortcut('Ctrl+P')
        self.action_processing_image.triggered.connect(
            self.open_processing_image_window
        )

        self.menu.addAction(self.action_add_graph)
        self.menu.addAction(self.action_open_image)
        self.menu.addAction(self.action_open_sound)
        self.menu.addSeparator()
        self.menu.addAction(self.action_close)
        self.menu_2.addAction(self.action_statistics)
        self.menu_2.addAction(self.action_filter)
        self.menu_2.addAction(self.action_deconvolution)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_processing_image)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def open_add_graph_window(self) -> None:
        self.add_graph_window.show()

    def open_image_window(self) -> None:
        self.graphWidget_1.hide()
        self.label_model_1.show()
        open_img(self)
        self.show_img(1)

    def open_add_sound_window(self) -> None:
        self.add_sound_ui.setupUi(self.add_sound_window)
        self.add_sound_window.show()

    def open_statistics_window(self) -> None:
        self.statistics_ui = Ui_statistics(self)
        self.statistics_window.show()

    def open_filter_window(self) -> None:
        self.filter_ui = Ui_filter_window(self)
        self.filter_window.show()

    def open_deconvolution_window(self) -> None:
        self.deconvolution_ui.setupUi(self.deconvolution_window)
        self.deconvolution_window.show()

    def open_processing_image_window(self) -> None:
        self.image_processing_ui = image_processing_window(self)
        self.processing_image_window.show()

    def show_graph(self, graph, place: int, normalisation: bool = False) -> None:
        pen = pg.mkPen(color="#AB47BC", width=1)
        x = graph.x
        y = graph.y

        if normalisation is True:
            len_graph = len(graph.x)
            new_n = int(len_graph / 2)
            x = graph.x[:new_n]
            y = graph.y[:new_n]

        if place == 1:
            self.graphWidget_1.clear()
            try:
                self.legend_1.scene().removeItem(self.legend_1)
            except:
                pass

            self.legend_1 = self.graphWidget_1.addLegend()
            self.graphWidget_1.plot(x, y, pen=pen, name=graph.option)
            self.label_model_1.hide()
            self.graphWidget_1.show()

        elif place == 2:
            self.graphWidget_2.clear()
            try:
                self.legend_2.scene().removeItem(self.legend_1)
            except:
                pass

            self.legend_2 = self.graphWidget_2.addLegend()
            self.graphWidget_2.plot(x, y, pen=pen, name=graph.option)
            self.label_model_2.hide()
            self.graphWidget_2.show()

        elif place == 3:
            self.graphWidget_3.clear()
            try:
                self.legend_3.scene().removeItem(self.legend_3)
            except:
                pass

            self.legend_3 = self.graphWidget_3.addLegend()
            self.graphWidget_3.plot(x, y, pen=pen, name=graph.option)
            self.label_model_3.hide()
            self.graphWidget_3.show()

        elif place == 4:
            self.graphWidget_4.clear()
            try:
                self.legend_4.scene().removeItem(self.legend_4)
            except:
                pass

            self.legend_4 = self.graphWidget_4.addLegend()
            self.graphWidget_4.plot(x, y, pen=pen, name=graph.option)
            self.label_model_4.hide()
            self.graphWidget_4.show()

        elif place == 5:
            self.graphWidget_5.clear()
            try:
                self.legend_5.scene().removeItem(self.legend_5)
            except:
                pass

            self.legend_5 = self.graphWidget_5.addLegend()
            self.graphWidget_5.plot(x, y, pen=pen, name=graph.option)
            self.label_model_5.hide()
            self.graphWidget_5.show()

        elif place == 6:
            self.graphWidget_6.clear()
            try:
                self.legend_6.scene().removeItem(self.legend_6)
            except:
                pass

            self.legend_6 = self.graphWidget_6.addLegend()
            self.graphWidget_6.plot(x, y, pen=pen, name=graph.option)
            self.label_model_6.hide()
            self.graphWidget_6.show()

    def show_img(self, place):
        if place == 1:
            self.graphWidget_1.hide()
            self.label_model_1.show()
            image = QPixmap(PATH_IMG_TEMP_1)
            self.label_model_1.setPixmap(image)

        elif place == 2:
            self.graphWidget_2.hide()
            self.label_model_2.show()
            image = QPixmap(PATH_IMG_TEMP_2)
            self.label_model_2.setPixmap(image)

        elif place == 3:
            self.graphWidget_3.hide()
            self.label_model_3.show()
            image = QPixmap(PATH_IMG_TEMP_3)
            self.label_model_3.setPixmap(image)

        elif place == 4:
            self.graphWidget_4.hide()
            self.label_model_4.show()
            image = QPixmap(PATH_IMG_TEMP_4)
            self.label_model_4.setPixmap(image)

        elif place == 5:
            self.graphWidget_5.hide()
            self.label_model_5.show()
            image = QPixmap(PATH_IMG_TEMP_5)
            self.label_model_5.setPixmap(image)

        elif place == 6:
            self.graphWidget_6.hide()
            self.label_model_6.show()
            image = QPixmap(PATH_IMG_TEMP_6)
            self.label_model_6.setPixmap(image)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(
            _translate("mainwindow", "Обработка и анализ данных")
        )

        self.label_for_model_1.setText(_translate("mainwindow", "Позиция №1"))
        self.label_for_model_2.setText(_translate("mainwindow", "Позиция №2"))
        self.label_for_model_3.setText(_translate("mainwindow", "Позиция №3"))
        self.label_for_model_4.setText(_translate("mainwindow", "Позиция №4"))
        self.label_for_model_5.setText(_translate("mainwindow", "Позиция №5"))
        self.label_for_model_6.setText(_translate("mainwindow", "Позиция №6"))

        self.label_model_1.setText(_translate("mainwindow", ""))
        self.label_model_2.setText(_translate("mainwindow", ""))
        self.label_model_3.setText(_translate("mainwindow", ""))
        self.label_model_4.setText(_translate("mainwindow", ""))
        self.label_model_5.setText(_translate("mainwindow", ""))
        self.label_model_6.setText(_translate("mainwindow", ""))

        self.menu.setTitle(_translate("mainwindow", "Файл"))
        self.menu_2.setTitle(_translate("mainwindow", "Обработка"))
        self.action_add_graph.setText(_translate("mainwindow", "Добавить график"))
        self.action_open_image.setText(_translate("mainwindow", "Открыть изображение"))
        self.action_open_sound.setText(
            _translate("mainwindow", "Открыть звуковой файл")
        )
        self.action_close.setText(_translate("mainwindow", "Выход"))
        self.action_statistics.setText(_translate("mainwindow", "Статистики"))
        self.action_filter.setText(_translate("mainwindow", "Фильтр"))
        self.action_deconvolution.setText(_translate("mainwindow", "Деконволюция"))
        self.action_processing_image.setText(_translate("mainwindow", "Изображения..."))
