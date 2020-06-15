from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from setting import *
from image import smoothing, histogram_equalization


class HistogramEqualizationWindow(object):
    def __init__(self, main_window: object):
        self.main_window = main_window
        self.histogram_equalization_window = main_window.histogram_equalization_window
        self.histogram_equalization_window.setObjectName("MainWindow")
        self.histogram_equalization_window.resize(498, 249)
        self.centralwidget = QtWidgets.QWidget(self.histogram_equalization_window)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 171, 20))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 190, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.histogram_equalization_click)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 190, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 100, 201, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 331, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 131, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 160, 231, 32))
        self.comboBox.setObjectName("comboBox")
        comboBox_list: list = GET_LIST_ANALYSIS()
        self.comboBox.addItems(comboBox_list)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(260, 160, 231, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["1", "2", "3", "4", "5", "6"])
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 211, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 140, 281, 16))
        self.label_3.setObjectName("label_3")
        self.histogram_equalization_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.histogram_equalization_window)
        self.statusbar.setObjectName("statusbar")
        self.histogram_equalization_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.histogram_equalization_window)
        QtCore.QMetaObject.connectSlotsByName(self.histogram_equalization_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Эквализация гистограммы"))
        self.checkBox.setText(_translate("MainWindow", "Изменить размеры"))
        self.pushButton.setText(_translate("MainWindow", "Выполнить"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))
        self.checkBox_2.setText(_translate("MainWindow", "Эквализация гистограммы"))
        self.label.setText(_translate("MainWindow", "Новая ширина"))
        self.label_2.setText(_translate("MainWindow", "Позиция исходного изображения"))
        self.label_3.setText(_translate("MainWindow", "Позиция выходного изображения"))

    def histogram_equalization_click(self):
        resize_flag: bool = self.checkBox.isChecked()
        equalization_flag: bool = self.checkBox_2.isChecked()

        place_image: int = int(self.comboBox.currentText())
        place_to_show_image: int = int(self.comboBox_2.currentText())

        try:
            img_path = POSITION_FOR_ANALYSIS.get(place_image)
        except:
            QMessageBox.about(self, "Title", "Message")

        if resize_flag:
            # Resize Билинейное
            try:
                new_width = int(self.lineEdit.text())
                smoothing(img_path, "bilinear", place=place_to_show_image, new_width=new_width, resize_from_width=True)
            except:
                pass

        elif equalization_flag:
            try:
                histogram_equalization(img_path, place=place_to_show_image)
            except:
                pass

        self.main_window.show_img(place_to_show_image)

    def close_window(self):
        self.histogram_equalization_window.close()
