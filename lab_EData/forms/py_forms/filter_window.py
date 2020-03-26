from PyQt5 import QtCore, QtWidgets

from model import Model
from trend import Trend
from setting import *
from Image import filtration


class Ui_filter_window(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.filter_window = main_window.filter_window
        # self.image = main_window.image
        self.filter_window.setObjectName("MainWindow")
        self.filter_window.resize(523, 461)
        self.centralwidget = QtWidgets.QWidget(self.filter_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.close_window)
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 3, 1, 1)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 9, 0, 1, 1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 7, 0, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        comboBox_values: list = ['1', '2', '3', '4', '5', '6']
        self.comboBox_2.addItems(comboBox_values)
        self.gridLayout.addWidget(self.comboBox_2, 12, 0, 1, 1)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 10, 0, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        comboBox_list: list = GET_LIST_ANALYSIS()
        self.comboBox.addItems(comboBox_list)
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 11, 0, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 5, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        type_values: list = ['Низких частот', 'Высоких частот', 'Полосовой', 'Режекторный']
        self.comboBox_3.addItems(type_values)
        self.gridLayout.addWidget(self.comboBox_3, 1, 2, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_filter_graph)
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 2, 1, 1)

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 5, 2, 1, 1)

        self.radioButton_image = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_image.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_image, 6, 2, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 2, 1, 1)

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 7, 2, 1, 1)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 13, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.filtration)
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.filter_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.filter_window)
        self.statusbar.setObjectName("statusbar")
        self.filter_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.filter_window)
        QtCore.QMetaObject.connectSlotsByName(self.filter_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фильтры"))
        self.pushButton_3.setText(_translate("MainWindow", "Закрыть"))
        self.label.setText(_translate("MainWindow", "Позиция для фильтрации"))
        self.label_7.setText(_translate("MainWindow", "fc 2"))
        self.label_2.setText(_translate("MainWindow", "delta t"))
        self.label_5.setText(_translate("MainWindow", "Место для вывода результата"))
        self.label_4.setText(_translate("MainWindow", "fc 1"))
        self.label_3.setText(_translate("MainWindow", "m"))
        self.label_6.setText(_translate("MainWindow", "Тип фильтра"))
        self.pushButton.setText(_translate("MainWindow", "Добавить график фильтра"))
        self.radioButton.setText(_translate("MainWindow", "График"))
        self.radioButton_image.setText(_translate("MainWindow", "Изображение"))
        self.label_8.setText(_translate("MainWindow", "Объект фильтрации"))
        self.pushButton_2.setText(_translate("MainWindow", "Выполнить фильтрацию"))

    def filtration(self):
        if self.radioButton_image.isChecked():

            filter_trend = Trend()
            type_of_filter = self.comboBox_3.currentText()

            m = self.lineEdit_2.text()
            delta_t = self.lineEdit.text()
            fc_1 = self.lineEdit_3.text()
            fc_2 = self.lineEdit_4.text()
            error_dialog = QtWidgets.QErrorMessage()

            if m != '':
                try:
                    m = int(m)
                    filter_trend.m = m

                except:
                    error_dialog.showMessage('Значение m должны быть целочисленными. Использовано значение m по '
                                             'умолчанию')

            if delta_t != '':
                try:
                    delta_t = float(delta_t)
                    filter_trend.delta_t = delta_t

                except:
                    error_dialog.showMessage('Значение delta t должны быть вещественными. Использовано значение delta t по '
                                             'умолчанию')

            if fc_1 != '':
                try:
                    fc_1 = int(fc_1)
                    filter_trend.fc_1 = fc_1

                except:
                    error_dialog.showMessage('Значение fc_1 должны быть целочисленными. Использовано значение fc_1 по '
                                             'умолчанию')

            if fc_2 != '':
                try:
                    fc_2 = int(fc_2)
                    filter_trend.fc_2 = fc_2

                except:
                    error_dialog.showMessage('Значение fc_2 должны быть целочисленными. Использовано значение fc_2 по '
                                             'умолчанию')

            if type_of_filter == 'Низких частот':
                filter_trend.generation_trend_filter_potter()

            elif type_of_filter == 'Высоких частот':
                filter_trend.generating_trend_high_potter()

            elif type_of_filter == 'Полосовой':
                filter_trend.generating_trend_bandpass_filter()

            elif type_of_filter == 'Режекторный':
                filter_trend.generating_trend_notch_filter()

            place_to_show_image: int = int(self.comboBox_2.currentText())

            try:
                position_img: int = int(self.comboBox.currentText())
                img_path = POSITION_FOR_ANALYSIS.get(position_img)
            except:
                error_dialog.showMessage('Не найдено изображение для фильтрации')
                return

            filtration(img_path, filter_trend, place_to_show_image)
            self.main_window.show_img(place_to_show_image)

        self.close_window()

    def add_filter_graph(self):
        place_to_show: int = int(self.comboBox_2.currentText())
        name_of_graph: str = self.comboBox_3.currentText()
        model = Model(name_of_graph)
        model.calculation()

        POSITION_FOR_ANALYSIS[place_to_show] = model
        self.main_window.show_graph(model, place_to_show)

        self.close_window()

    def close_window(self):
        self.filter_window.close()
