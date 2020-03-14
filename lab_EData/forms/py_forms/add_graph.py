# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/qt_forms/add_graph.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


# Окно: Добавить новый график
class Ui_add_graph(object):
    def __init__(self, add_graph):
        self.add_grpah_window = add_graph
        add_graph.setObjectName("add_graph")
        add_graph.resize(613, 437)
        add_graph.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(add_graph)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 360, 131, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 541, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 4, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 7, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 4, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 5, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["1", "2", "3", "4"])
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 8, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 4, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 9, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 3, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(
            [
                "y(x)=kx+b",
                "y(x)=-kx+b",
                "y(x) = beta * exp^(alpha * i)",
                "y(x) = beta * exp^(alpha * -i)",
                "Встроенный рандом",
                "Кастомный рандом",
                "Значения за областью",
                "Адитивная модель №1",
                "Адитивная модель №2",
                "Мультипликативная модель №1",
                "Мультипликативная модель №2",
                "Кусочная функция",
                "Гармоническое процесс",
                "Полигармоническое процесс",
                "Рандом + сдвиг",
                "Рандом + спайки",
                "ГП + trend",
                "ГП + спайки",
                "ГП + спайки + рандом + trend",
                "Загрузить из файла",
                "ГП + exp",
                "Экзамен",
            ]
        )
        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 5, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 9, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 4, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 11, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 360, 131, 32))
        self.pushButton.setObjectName("pushButton")
        add_graph.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(add_graph)
        self.statusbar.setObjectName("statusbar")
        add_graph.setStatusBar(self.statusbar)

        self.retranslateUi(add_graph)
        QtCore.QMetaObject.connectSlotsByName(add_graph)

    def retranslateUi(self, add_graph):
        _translate = QtCore.QCoreApplication.translate
        add_graph.setWindowTitle(_translate("add_graph", "Добавить график"))
        self.pushButton_2.setText(_translate("add_graph", "Закрыть"))
        self.label_9.setText(_translate("add_graph", "alpha"))
        self.label_10.setText(_translate("add_graph", "beta"))
        self.label_7.setText(_translate("add_graph", "k"))
        self.label_2.setText(_translate("add_graph", "График функции"))
        self.label_5.setText(_translate("add_graph", "Количество записей"))
        self.label_11.setText(_translate("add_graph", "fo"))
        self.label_4.setText(_translate("add_graph", "Максимальное значение ф-ии"))
        self.label_6.setText(_translate("add_graph", "Константа"))
        self.label_3.setText(_translate("add_graph", "Минимальное значение ф-ии"))
        self.label.setText(_translate("add_graph", "Место вывода графика"))
        self.label_8.setText(_translate("add_graph", "b"))
        self.pushButton.setText(_translate("add_graph", "Добавить"))

    def close_window(self):
        self.add_grpah_window.close()
