from PyQt5 import QtCore, QtGui, QtWidgets
from Image import MyImage as Image


class image_processing_window(object):
    def __init__(self,  main_window: object, graphWidget):
        self.image = main_window.image
        self.processing_image_window = main_window.processing_image_window
        self.processing_image_window.setObjectName("MainWindow")
        self.processing_image_window.resize(828, 478)
        self.processing_image_window.setStyleSheet("background-color: #263238")
        self.main_window = main_window
        self.graphWidget = graphWidget

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
        self.pushButton.setStyleSheet("color: #EEEEEE;"
                                      "background-color: #546E7A;")
        self.gridLayout.addWidget(self.pushButton, 14, 2, 1, 1)

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
        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 1)

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
        self.comboBox.addItems(["1", "2", "3", "4"])
        self.comboBox.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.comboBox, 12, 0, 1, 1)

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
        self.pushButton_2.setStyleSheet("color: #EEEEEE; "
                                        "background-color: #546E7A")
        self.gridLayout.addWidget(self.pushButton_2, 14, 3, 1, 1)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.checkBox, 11, 2, 1, 2)

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

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: #EEEEEE")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 2, 2, 1, 2)

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
        self.label.setText(_translate("MainWindow", "Сглаживание"))
        self.label_3.setText(_translate("MainWindow", "Позиция вывода графика"))
        self.radioButton_6.setText(_translate("MainWindow", "Гистограмма"))
        self.radioButton_7.setText(_translate("MainWindow", "Кумулятивная функция распределения"))
        self.checkBox.setText(_translate("MainWindow", "Нормализовать"))

    def processing(self) -> None:

        # Ближайший сосед
        if self.radioButton.isChecked():
            try:
                smoothing_factor = float(self.lineEdit.text())
                self.image.smoothing("nearest", smoothing_factor)

            except:
                pass

        # Билинейное
        elif self.radioButton_2.isChecked():
            try:
                smoothing_factor = float(self.lineEdit.text())
                self.image.smoothing("bilinear", smoothing_factor)

            except:
                pass

        # Негатив
        elif self.radioButton_3.isChecked():
            self.image.image_processing("negative")

        # Гамма коррекция
        elif self.radioButton_4.isChecked():
            self.image.image_processing("gamma")

        # Логорифмическое
        elif self.radioButton_5.isChecked():
            self.image.image_processing("logarithmic")

        # Гисторграмма
        elif self.radioButton_6.isChecked():
            self.image.bar_chart(self.graphWidget)
            self.graphWidget.show()
            self.close_window()

        # Кумулятивная функция распределения
        elif self.radioButton_7.isChecked():
            if self.checkBox.isChecked():
                self.image.cdf_function(self.graphWidget, normalisation=True)
            else:
                self.image.cdf_function(self.graphWidget, normalisation=False)
            self.graphWidget.show()

            self.image.image_processing("cdf")

        self.close_window()

    def close_window(self) -> None:
        self.processing_image_window.close()