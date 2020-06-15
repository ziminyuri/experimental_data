from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from setting import *
from image import img_row, derivative, noise, image_processing, smoothing, bar_chart, cdf_function
from image import threshold_conversion, gradient, sobeling, laplacian, erosion, dialatization, stones


class ImageProcessingWindow(object):
    def __init__(self, main_window: object):
        self.main_window = main_window
        self.processing_image_window = main_window.processing_image_window
        self.processing_image_window.setObjectName("MainWindow")
        self.processing_image_window.resize(804, 490)
        self.processing_image_window.setStyleSheet("background-color: #263238")

        self.centralwidget = QtWidgets.QWidget(self.processing_image_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_7.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_7, 2, 2, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("color: #EEEEEE; background-color: #546E7A;")
        self.pushButton.clicked.connect(self.processing)
        self.gridLayout.addWidget(self.pushButton, 25, 2, 1, 1)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 1, 5, 1)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.checkBox, 20, 4, 1, 1)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setStyleSheet("color: #EEEEEE; background-color: #546E7A")
        comboBox_list: list = GET_LIST_ANALYSIS()
        self.comboBox_2.addItems(comboBox_list)
        self.gridLayout.addWidget(self.comboBox_2, 18, 0, 1, 1)

        self.radioButton_15 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_15.setObjectName("radioButton_15")
        self.radioButton_15.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_15, 11, 4, 1, 1)

        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 17, 3, 4, 1)

        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 6, 4, 1, 1)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("background-color: #546E7A; color: #EEEEEE;")
        self.gridLayout.addWidget(self.lineEdit_3, 7, 2, 1, 1)

        self.checkBox_show_plot = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_show_plot.setObjectName("checkBox_3")
        self.checkBox_show_plot.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.checkBox_show_plot, 17, 4, 1, 1)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 0, 1, 2)

        self.radioButton_13 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_13.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_13, 9, 4, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_3, 18, 2, 1, 1)

        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_5.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.checkBox_5, 5, 4, 1, 1)

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.checkBox_2, 17, 2, 1, 1)

        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_9.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_9, 5, 2, 1, 1)

        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_10.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_10, 12, 4, 1, 1)

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_3, 9, 0, 1, 1)

        self.comboBox_place_to_show_plot = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_place_to_show_plot.setObjectName("comboBox_place_to_show_plot")
        self.comboBox_place_to_show_plot.setStyleSheet("color: #EEEEEE; background-color: #546E7A")
        self.comboBox_place_to_show_plot.addItems(["1", "2", "3", "4", "5", "6"])
        self.gridLayout.addWidget(self.comboBox_place_to_show_plot, 19, 4, 1, 1)

        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_5.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_5, 11, 0, 1, 1)

        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_11.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_11, 8, 4, 1, 1)

        self.radioButton_14 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_14.setObjectName("radioButton_14")
        self.radioButton_14.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_14, 10, 4, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
        self.pushButton_2.setStyleSheet("color: #EEEEEE; background-color: #546E7A;")
        self.gridLayout.addWidget(self.pushButton_2, 25, 4, 1, 1)

        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_8.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_8, 4, 2, 1, 1)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_9, 7, 4, 1, 1)

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_4, 10, 0, 1, 1)

        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 17, 1, 4, 1)

        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_12.setObjectName("radioButton_12")
        self.radioButton_12.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_12, 10, 2, 1, 1)

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_10, 11, 2, 1, 1)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet("background-color: #546E7A; color: #EEEEEE;")
        self.gridLayout.addWidget(self.lineEdit_4, 12, 2, 1, 1)

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 14, 0, 1, 5)

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_8, 2, 4, 1, 1)

        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_6.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_6, 1, 2, 1, 1)

        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_6.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.checkBox_6, 8, 2, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_7, 6, 2, 1, 1)

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_2, 3, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_5, 18, 4, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.addItems(["1", "2", "3", "4", "5", "6"])
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("color: #EEEEEE; background-color: #546E7A")
        self.gridLayout.addWidget(self.comboBox, 19, 2, 1, 1)

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 7, 1, 7, 1)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_4, 17, 0, 1, 1)

        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 3, 2, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: #546E7A; color: #EEEEEE;")
        self.gridLayout.addWidget(self.lineEdit, 5, 0, 1, 1)

        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.checkBox_4, 4, 4, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-color: #546E7A; color: #EEEEEE;")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 4, 1, 1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)

        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 1, 3, 13, 1)

        self.radioButton_16 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_16.setObjectName("radioButton_16")
        self.radioButton_16.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton_16, 13, 4, 1, 1)

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_11, 12, 0, 1, 1)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setStyleSheet("background-color: #546E7A; color: #EEEEEE;")
        self.gridLayout.addWidget(self.lineEdit_5, 13, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        self.processing_image_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.processing_image_window)
        self.statusbar.setObjectName("statusbar")
        self.processing_image_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.processing_image_window)
        QtCore.QMetaObject.connectSlotsByName(self.processing_image_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Обработка  изображения"))
        self.radioButton_7.setText(_translate("MainWindow", "Кумулятивная функция распределения"))
        self.pushButton.setText(_translate("MainWindow", "Применить"))
        self.checkBox.setText(_translate("MainWindow", "Нормализовать"))
        self.radioButton_15.setText(_translate("MainWindow", "Диалатация"))
        self.checkBox_show_plot.setText(_translate("MainWindow", "Показать график"))
        self.radioButton_13.setText(_translate("MainWindow", "Окунтуривание градиентом"))
        self.label_3.setText(_translate("MainWindow", "Позиция вывода изображение после обработки"))
        self.checkBox_5.setText(_translate("MainWindow", "Соль и перец"))
        self.checkBox_2.setText(_translate("MainWindow", "Показать обработанное изображение"))
        self.radioButton_9.setText(_translate("MainWindow", "Производная cтроки"))
        self.radioButton_10.setText(_translate("MainWindow", "Окунтуривание методом Собеля"))
        self.radioButton_3.setText(_translate("MainWindow", "Негатив"))
        self.radioButton_5.setText(_translate("MainWindow", "Логорифмическое"))
        self.radioButton_11.setText(_translate("MainWindow", "Окунтуривание оператором Лапласа"))
        self.radioButton_14.setText(_translate("MainWindow", "Эрозия"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))
        self.radioButton_8.setText(_translate("MainWindow", "Cтрока"))
        self.label_9.setText(_translate("MainWindow", "Сегментация"))
        self.radioButton_4.setText(_translate("MainWindow", "Гамма коррекция"))
        self.radioButton_12.setText(_translate("MainWindow", "Пороговое преобразование"))
        self.radioButton.setText(_translate("MainWindow", "Ближайший сосед"))
        self.label_8.setText(_translate("MainWindow", "Процент шума"))
        self.radioButton_6.setText(_translate("MainWindow", "Гистограмма"))
        self.checkBox_6.setText(_translate("MainWindow", "Бинарное изображение"))
        self.label_7.setText(_translate("MainWindow", "Номер строки"))
        self.radioButton_2.setText(_translate("MainWindow", "Билинейное"))
        self.label_2.setText(_translate("MainWindow", "Коэфициент"))
        self.label_5.setText(_translate("MainWindow", "Позиция вывода графика"))
        self.label_4.setText(_translate("MainWindow", "Данные для обработки"))
        self.checkBox_4.setText(_translate("MainWindow", "Гаусса"))
        self.label.setText(_translate("MainWindow", "Сглаживание"))
        self.label_6.setText(_translate("MainWindow", "Шум"))
        self.label_10.setText(_translate("MainWindow", "Значение порога"))
        self.radioButton_16.setText(_translate("MainWindow", "Камни"))
        self.label_11.setText(_translate("MainWindow", "Коэффициент"))

    def processing(self) -> None:

        show_image: bool = self.checkBox_2.isChecked()
        show_plot: bool = self.checkBox_show_plot.isChecked()

        place_to_show_image: int = int(self.comboBox.currentText())
        place_to_show_plot: int = int(self.comboBox_place_to_show_plot.currentText())

        try:
            position_img: int = int(self.comboBox_2.currentText())
            img_path = POSITION_FOR_ANALYSIS.get(position_img)
        except:
            QMessageBox.about(self, "Title", "Message")

        # Ближайший сосед
        if self.radioButton.isChecked():
            try:
                smoothing_factor = float(self.lineEdit.text())
                smoothing(img_path, "nearest", factor=smoothing_factor, place=place_to_show_image)
            except:
                pass

        # Билинейное
        elif self.radioButton_2.isChecked():
            try:
                smoothing_factor = float(self.lineEdit.text())
                smoothing(img_path, "bilinear", place=place_to_show_image, factor=smoothing_factor)
            except:
                pass

        # Негатив
        elif self.radioButton_3.isChecked():
            image_processing("negative", img_path, place_to_show_image)

        # Гамма коррекция
        elif self.radioButton_4.isChecked():
            k = self.lineEdit_5.text()
            if k == '':
                image_processing("gamma", img_path, place_to_show_image)
            else:
                image_processing("gamma", img_path, place_to_show_image, coefficient=int(k))

        # Логорифмическое
        elif self.radioButton_5.isChecked():
            k = self.lineEdit_5.text()
            if k == '':
                image_processing("logarithmic", img_path, place_to_show_image)
            else:
                image_processing("logarithmic", img_path, place_to_show_image, coefficient=int(k))

        # Гисторграмма
        elif self.radioButton_6.isChecked():
            model = bar_chart(img_path)

        # Кумулятивная функция распределения
        elif self.radioButton_7.isChecked():
            normalisation = self.checkBox_normalisation.isChecked()
            model = cdf_function(img_path, normalisation)
            image_processing("cdf", img_path, place_to_show_image)

        # График строки
        elif self.radioButton_8.isChecked():
            if self.checkBox_6.isChecked():  # бинарное
                number_row: int = int(self.lineEdit_3.text())
                model = img_row(img_path, number_row, binary=True)
            else:
                number_row:int = int(self.lineEdit_3.text())
                model = img_row(img_path, number_row)

        # Производная строки
        elif self.radioButton_9.isChecked():
            if self.checkBox_6.isChecked():     # бинарное
                number_row: int = int(self.lineEdit_3.text())
                model = derivative(img_path, number_row, binary=True)
            else:
                number_row: int = int(self.lineEdit_3.text())
                model = derivative(img_path, number_row)

        # Пороговое преобразование
        elif self.radioButton_12.isChecked():
            try:
                factor = int(self.lineEdit_4.text())
                threshold_conversion(img_path, place_to_show_image, threshold_value=factor)
            except:
                threshold_conversion(img_path, place_to_show_image)


        # Окунтуривание оператором Собеля
        elif self.radioButton_10.isChecked():
            sobeling(img_path, place_to_show_image)

        # Окунтуривание оператором Лапласа
        elif self.radioButton_11.isChecked():
            laplacian(img_path, place_to_show_image)

        # Эрозия
        elif self.radioButton_14.isChecked():
            try:
                factor = int(self.lineEdit_4.text())
                erosion(img_path, place_to_show_image, threshold_value=factor)
            except:
                erosion(img_path, place_to_show_image)

        # Диалатация
        elif self.radioButton_15.isChecked():
            try:
                factor = int(self.lineEdit_4.text())
                dialatization(img_path, place_to_show_image, threshold_value=factor)
            except:
                dialatization(img_path, place_to_show_image)

        #Камни
        elif self.radioButton_16.isChecked():
            stones(img_path, place_to_show_image)

        # Шум: Соль и Перец
        if self.checkBox_5.isChecked():
            try:
                factor = float(self.lineEdit_2.text())
                noise("sold_peper", place_to_show_image, img_path, factor)
            except:
                noise("sold_peper", place_to_show_image, img_path)

        # Гаусса
        if self.checkBox_4.isChecked():
            try:
                factor = float(self.lineEdit_2.text())
                noise("gaussian", place_to_show_image, img_path, factor)
            except:
                noise("gaussian", place_to_show_image, img_path)

        if show_image:
            self.main_window.show_img(place_to_show_image)

        if show_plot:
            self.main_window.show_graph(model, place_to_show_plot)
            POSITION_FOR_ANALYSIS[place_to_show_plot] = model

        self.close_window()

    def close_window(self) -> None:
        self.processing_image_window.close()