from PyQt5 import QtCore, QtGui, QtWidgets

from Image import MyImage as Image
from model import Model

from setting import *

class image_processing_window(object):
    def __init__(self, main_window: object, graphWidget):
        self.image = main_window.image
        self.processing_image_window = main_window.processing_image_window
        self.processing_image_window.setObjectName("MainWindow")
        self.processing_image_window.resize(804, 441)
        self.processing_image_window.setStyleSheet("background-color: #263238")
        self.main_window = main_window
        self.graphWidget = graphWidget

        self.is_image = False

        self.centralwidget = QtWidgets.QWidget(self.processing_image_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_5.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_5, 9, 0, 1, 1)

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_3.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.line_3, 10, 0, 1, 4)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.processing)
        self.pushButton.setStyleSheet("color: #EEEEEE; background-color: #546E7A;")
        self.gridLayout.addWidget(self.pushButton, 22, 2, 1, 1)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 2)

        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_7.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_7, 1, 2, 1, 2)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 5, 1)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_3, 11, 0, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: #546E7A")
        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 1)

        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 14, 1, 4, 1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 7, 1, 3, 1)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["1", "2", "3", "4", "5", "6"])
        self.comboBox.setStyleSheet("color: #EEEEEE; background-color: #546E7A")
        self.gridLayout.addWidget(self.comboBox, 16, 2, 1, 1)

        self.comboBox_place_to_show_plot = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_place_to_show_plot.setObjectName("comboBox_place_to_show_plot")
        self.comboBox_place_to_show_plot.addItems(["1", "2", "3", "4", "5", "6"])
        self.comboBox_place_to_show_plot.setStyleSheet("color: #EEEEEE; background-color: #546E7A")
        self.gridLayout.addWidget(self.comboBox_place_to_show_plot, 16, 4, 1, 1)

        self.checkBox_show_plot = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_show_plot.setObjectName("checkBox_3")
        self.checkBox_show_plot.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.checkBox_show_plot, 14, 4, 1, 1)

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
        self.pushButton_2.setStyleSheet("color: #EEEEEE; background-color: #546E7A")
        self.gridLayout.addWidget(self.pushButton_2, 22, 4, 1, 1)

        self.checkBox_normalisation = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_normalisation.setObjectName("checkBox")
        self.checkBox_normalisation.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.checkBox_normalisation, 17, 4, 1, 1)

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_4, 8, 0, 1, 1)

        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_6.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_6, 0, 2, 1, 2)

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_3, 7, 0, 1, 1)

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_2, 2, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_4, 14, 0, 1, 1)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setStyleSheet("background-color: #546E7A")
        combo_list:list = GET_LIST_ANALYSIS()
        self.comboBox_2.addItems(combo_list)
        self.gridLayout.addWidget(self.comboBox_2, 15, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_3, 15, 2, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 2, 2, 1, 2)

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.checkBox_2, 14, 2, 1, 1)

        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 14, 3, 4, 1)

        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_8.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_8, 4, 2, 1, 1)

        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 4, 3, 7, 1)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_6, 4, 4, 1, 1)

        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.checkBox_4, 5, 4, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-color: #546E7A")
        self.gridLayout.addWidget(self.lineEdit_2, 6, 4, 1, 1)

        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_5.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.checkBox_5, 7, 4, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        self.processing_image_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.processing_image_window)
        self.statusbar.setObjectName("statusbar")
        self.processing_image_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.processing_image_window)
        QtCore.QMetaObject.connectSlotsByName(self.processing_image_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Коэфициент"))
        self.radioButton_5.setText(_translate("MainWindow", "Логорифмическое"))
        self.pushButton.setText(_translate("MainWindow", "Применить"))
        self.radioButton.setText(_translate("MainWindow", "Ближайший сосед"))
        self.radioButton_4.setText(_translate("MainWindow", "Гамма коррекция"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))
        self.radioButton_3.setText(_translate("MainWindow", "Негатив"))
        self.radioButton_2.setText(_translate("MainWindow", "Билинейное"))
        self.label_4.setText(_translate("MainWindow", "Данные для обработки"))
        self.label.setText(_translate("MainWindow", "Сглаживание"))
        self.label_3.setText(_translate("MainWindow", "Позиция вывода после обработки"))
        self.radioButton_6.setText(_translate("MainWindow", "Гистограмма"))
        self.radioButton_7.setText(
            _translate("MainWindow", "Кумулятивная функция распределения")
        )
        self.checkBox_normalisation.setText(_translate("MainWindow", "Нормализовать"))
        self.checkBox_2.setText(
            _translate("MainWindow", "Показать обработанное изображение")
        )
        self.checkBox_show_plot.setText(_translate("MainWindow", "Показать график"))
        self.radioButton_8.setText(_translate("MainWindow", "Нулевая строка"))
        self.label_6.setText(_translate("MainWindow", "Шум"))
        self.checkBox_4.setText(_translate("MainWindow", "Гаусса"))
        self.checkBox_5.setText(_translate("MainWindow", "Соль и перец"))

    def processing(self) -> None:

        show_image: bool = self.checkBox_2.isChecked()
        show_plot: bool = self.checkBox_show_plot.isChecked()

        place_to_show_image: int = int(self.comboBox.currentText())
        place_to_show_plot: int = int(self.comboBox_place_to_show_plot.currentText())

        # Ближайший сосед
        if self.radioButton.isChecked():
            try:
                smoothing_factor = float(self.lineEdit.text())
                self.image.smoothing("nearest", smoothing_factor, show_image, place_to_show_image)
                self.is_image = True

            except:
                pass

        # Билинейное
        elif self.radioButton_2.isChecked():
            try:
                smoothing_factor = float(self.lineEdit.text())
                self.image.smoothing("bilinear", smoothing_factor, show_image, place_to_show_image)
                self.is_image = True

            except:
                pass

        # Негатив
        elif self.radioButton_3.isChecked():
            self.image.image_processing("negative", show_image, place_to_show_image)
            self.is_image = True

        # Гамма коррекция
        elif self.radioButton_4.isChecked():
            self.image.image_processing("gamma", show_image, place_to_show_image)
            self.is_image = True

        # Логорифмическое
        elif self.radioButton_5.isChecked():
            self.image.image_processing("logarithmic", show_image, place_to_show_image)
            self.is_image = True

        # Гисторграмма
        elif self.radioButton_6.isChecked():
            model = self.image.bar_chart()

            if show_plot:
                self.main_window.show_graph(model, place_to_show_plot)

            self.close_window()

        # Кумулятивная функция распределения
        elif self.radioButton_7.isChecked():
            normalisation = self.checkBox_normalisation.isChecked()
            model = self.image.cdf_function(normalisation)

            if show_plot:
                self.main_window.show_graph(model, place_to_show_plot)

            self.image.image_processing("cdf", show_image, place_to_show_image)

        # Спектр фурье изображения
        elif self.radioButton_8.isChecked():
            if place_to_show_plot == 1:
                self.image.zero_row(self.main_window.graphWidget_1, show_plot)

            elif place_to_show_plot == 2:
                self.image.zero_row(self.main_window.graphWidget_2, show_plot)

            elif place_to_show_plot == 3:
                self.image.zero_row(self.main_window.graphWidget_3, show_plot)

            elif place_to_show_plot == 4:
                self.image.zero_row(self.main_window.graphWidget_4, show_plot)

            elif place_to_show_plot == 5:
                self.image.zero_row(self.main_window.graphWidget_5, show_plot)

            elif place_to_show_plot == 6:
                self.image.zero_row(self.main_window.graphWidget_6, show_plot)



        # Шум: Соль и Перец
        if self.checkBox_5.isChecked():
            try:
                factor = float(self.lineEdit_2.text())
                self.image.noise("sold_peper", show_image, place_to_show_image, factor)
            except:
                self.image.noise("sold_peper", show_image, place_to_show_image)

        # Гаусса
        if self.checkBox_4.isChecked():
            try:
                factor = float(self.lineEdit_2.text())
                self.image.noise("gaussian", show_image, place_to_show_image, factor)
            except:
                self.image.noise("gaussian", show_image, place_to_show_image)

        self.close_window()

    def close_window(self) -> None:
        self.processing_image_window.close()
