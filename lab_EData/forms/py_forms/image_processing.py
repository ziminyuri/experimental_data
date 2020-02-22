from PyQt5 import QtCore, QtWidgets
from Image import MyImage


class image_processing_window(object):
    def __init__(self, main_window: object, image_for_processing: object):
        self.image = image_for_processing
        main_window.setObjectName("MainWindow")
        main_window.resize(853, 521)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 831, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 2, 1, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 3, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 380, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.triggered.connect(self.processing)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 380, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.triggered.connect(self.close_window)
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def processing(self) -> None:
        if self.radioButton.isChecked():
            try:
                smoothing_factor = float(self.lineEdit.text())
                self.image.smoothing("nearest", smoothing_factor)

            except:
                pass

        if self.radioButton_2.isChecked():
            try:
                smoothing_factor = float(self.lineEdit.text())
                self.image.smoothing("bilinear", smoothing_factor)

            except:
                pass

        if self.radioButton_3.isChecked():
            self.image.image_processing("negative")

        if self.radioButton_4.isChecked():
            self.image.image_processing("gamma")

        if self.radioButton_5.isChecked():
            self.image.image_processing("logarithmic")

    def close_window(self) -> None:
        pass

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Обработка изображения"))
        self.label_2.setText(_translate("MainWindow", "Коэфициент"))
        self.radioButton_4.setText(_translate("MainWindow", "Гамма коррекция"))
        self.radioButton_5.setText(_translate("MainWindow", "Логорифмическое"))
        self.radioButton.setText(_translate("MainWindow", "Ближайший сосед"))
        self.radioButton_2.setText(_translate("MainWindow", "Билинейное"))
        self.radioButton_3.setText(_translate("MainWindow", "Негатив"))
        self.label.setText(_translate("MainWindow", "Сглаживание"))
        self.pushButton.setText(_translate("MainWindow", "Применить"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))
