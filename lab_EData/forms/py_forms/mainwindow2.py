from PyQt5 import QtCore, QtGui, QtWidgets
from forms.py_forms.add_graph import Ui_add_graph
from forms.py_forms.add_sound_window import Ui_add_sound
from forms.py_forms.statistics_window import Ui_statistics
from forms.py_forms.filter_window import Ui_filter_window
from forms.py_forms.deconvolution_window import Ui_deconvolution_window
from forms.py_forms.image_processing1 import image_processing_window
from Image import MyImage


class Ui_mainwindow(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.setObjectName("mainwindow")
        self.main_window.resize(800, 600)
        self.main_window.setStyleSheet("background-color: #263238")

        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_for_model_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_model_3.setObjectName("label_for_model_3")
        self.gridLayout.addWidget(self.label_for_model_3, 0, 1, 1, 1)
        self.label_for_model_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_model_5.setObjectName("label_for_model_5")
        self.gridLayout.addWidget(self.label_for_model_5, 0, 2, 1, 1)
        self.label_for_model_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_model_1.setAutoFillBackground(False)
        self.label_for_model_1.setObjectName("label_for_model_1")
        self.gridLayout.addWidget(self.label_for_model_1, 0, 0, 1, 1)
        self.label_for_model_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_model_6.setObjectName("label_for_model_6")
        self.gridLayout.addWidget(self.label_for_model_6, 2, 2, 1, 1)
        self.label_model_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_model_1.setObjectName("label_model_1")
        self.gridLayout.addWidget(self.label_model_1, 1, 0, 1, 1)
        self.label_model_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_model_4.setObjectName("label_model_4")
        self.gridLayout.addWidget(self.label_model_4, 3, 1, 1, 1)
        self.label_for_model_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_model_2.setObjectName("label_for_model_2")
        self.gridLayout.addWidget(self.label_for_model_2, 2, 0, 1, 1)
        self.label_model_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_model_3.setObjectName("label_model_3")
        self.gridLayout.addWidget(self.label_model_3, 1, 1, 1, 1)
        self.label_model_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_model_6.setObjectName("label_model_6")
        self.gridLayout.addWidget(self.label_model_6, 3, 2, 1, 1)
        self.label_model_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_model_5.setObjectName("label_model_5")
        self.gridLayout.addWidget(self.label_model_5, 1, 2, 1, 1)
        self.label_for_model_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_model_4.setObjectName("label_for_model_4")
        self.gridLayout.addWidget(self.label_for_model_4, 2, 1, 1, 1)
        self.label_model_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_model_2.setObjectName("label_model_2")
        self.gridLayout.addWidget(self.label_model_2, 3, 0, 1, 1)
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

        self.action_add_graph = QtWidgets.QAction(self.main_window)
        self.action_add_graph.setObjectName("action_add_graph")
        self.action_add_graph.triggered.connect(self.open_add_graph_window)

        self.action_open_image = QtWidgets.QAction(self.main_window)
        self.action_open_image.setObjectName("action_open_image")
        self.action_open_image.triggered.connect(self.open_image_window)

        self.action_open_sound = QtWidgets.QAction(self.main_window)
        self.action_open_sound.setObjectName("action_open_sound")
        self.action_open_sound.triggered.connect(self.open_add_sound_window)

        self.action_close = QtWidgets.QAction(self.main_window)
        self.action_close.setObjectName("action_close")

        self.action_statistics = QtWidgets.QAction(self.main_window)
        self.action_statistics.setObjectName("action_statistics")

        self.action_filter = QtWidgets.QAction(self.main_window)
        self.action_filter.setObjectName("action_filter")

        self.action_deconvolution = QtWidgets.QAction(self.main_window)
        self.action_deconvolution.setObjectName("action_deconvolution")

        self.action_processing_image = QtWidgets.QAction(self.main_window)
        self.action_processing_image.setObjectName("action_processing_image")
        self.action_processing_image.triggered.connect(self.open_processing_image_window)

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

    def open_add_graph_window(self):
        self.add_graph_window = QtWidgets.QMainWindow()
        self.add_graph_ui = Ui_add_graph(self.add_graph_window)
        self.add_graph_window.show()

    def open_image_window(self) -> None:
        self.image = MyImage(self)
        self.image.open()

    def open_add_sound_window(self):
        self.add_sound_window = QtWidgets.QMainWindow()
        self.add_sound_ui = Ui_add_sound()
        self.add_sound_ui.setupUi(self.add_sound_window)
        self.add_sound_window.show()

    def open_statistics_window(self):
        self.statistics_window = QtWidgets.QMainWindow()
        self.statistics_ui = Ui_statistics()
        self.statistics_ui.setupUi(self.statistics_window)
        self.statistics_window.show()

    def open_filter_window(self):
        self.filter_window = QtWidgets.QMainWindow()
        self.filter_ui = Ui_filter_window()
        self.filter_ui.setupUi(self.filter_window)
        self.filter_window.show()

    def open_deconvolution_window(self):
        self.deconvolution_window = QtWidgets.QMainWindow()
        self.deconvolution_ui = Ui_deconvolution_window()
        self.deconvolution_ui.setupUi(self.deconvolution_window)
        self.deconvolution_window.show()

    def open_processing_image_window(self):
        self.processing_image_window = QtWidgets.QMainWindow()
        self.processing_image_ui = image_processing_window(self.processing_image_window, self.image)
        self.processing_image_window.show()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("mainwindow", "Обработка и анализ данных"))
        self.label_for_model_3.setText(_translate("mainwindow", ""))
        self.label_for_model_5.setText(_translate("mainwindow", ""))
        self.label_for_model_1.setText(_translate("mainwindow", ""))
        self.label_for_model_6.setText(_translate("mainwindow", ""))
        self.label_model_1.setText(_translate("mainwindow", ""))
        self.label_model_4.setText(_translate("mainwindow", ""))
        self.label_for_model_2.setText(_translate("mainwindow", ""))
        self.label_model_3.setText(_translate("mainwindow", ""))
        self.label_model_6.setText(_translate("mainwindow", ""))
        self.label_model_5.setText(_translate("mainwindow", ""))
        self.label_for_model_4.setText(_translate("mainwindow", ""))
        self.label_model_2.setText(_translate("mainwindow", ""))
        self.menu.setTitle(_translate("mainwindow", "Файл"))
        self.menu_2.setTitle(_translate("mainwindow", "Обработка"))
        self.action_add_graph.setText(_translate("mainwindow", "Добавить график"))
        self.action_open_image.setText(_translate("mainwindow", "Открыть изображение"))
        self.action_open_sound.setText(_translate("mainwindow", "Открыть звуковой файл"))
        self.action_close.setText(_translate("mainwindow", "Выход"))
        self.action_statistics.setText(_translate("mainwindow", "Статистики"))
        self.action_filter.setText(_translate("mainwindow", "Фильтр"))
        self.action_deconvolution.setText(_translate("mainwindow", "Деконволюция"))
        self.action_processing_image.setText(_translate("mainwindow", "Изображения..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
