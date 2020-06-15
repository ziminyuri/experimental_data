from PyQt5 import QtCore, QtWidgets

from analysis.analysis import Analysis
from setting import *


class Ui_statistics(object):
    def __init__(self, MainWindow):
        self.main_window = MainWindow
        self.statistics_window = MainWindow.statistics_window
        self.statistics_window.setObjectName("MainWindow")
        self.statistics_window.resize(800, 539)
        self.centralwidget = QtWidgets.QWidget(self.statistics_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 771, 456))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_10 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_10.setObjectName("radioButton_10")
        self.gridLayout.addWidget(self.radioButton_10, 11, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 8, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.radioButton_13 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_13.setObjectName("radioButton_13")
        self.gridLayout.addWidget(self.radioButton_13, 14, 0, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout.addWidget(self.radioButton_8, 9, 0, 1, 1)
        self.radioButton_12 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_12.setObjectName("radioButton_12")
        self.gridLayout.addWidget(self.radioButton_12, 13, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 5, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 3, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 1)
        self.radioButton_11 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_11.setObjectName("radioButton_11")
        self.gridLayout.addWidget(self.radioButton_11, 12, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 9, 1, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 4, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.spectrum)
        self.gridLayout.addWidget(self.pushButton_6, 11, 1, 1, 1)
        self.radioButton_9 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.gridLayout.addWidget(self.radioButton_9, 10, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        comboBox_values: list = GET_LIST_ANALYSIS()
        self.comboBox.addItems(comboBox_values)
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.autocorrelation)
        self.gridLayout.addWidget(self.pushButton_3, 4, 1, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout.addWidget(self.radioButton_7, 8, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 5, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.fast_fourier_transform)
        self.gridLayout.addWidget(self.pushButton_7, 12, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["1", "2", "3", "4", "5", "6"])
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 7, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 3, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 4, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 5, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 6, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 470, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(670, 470, 112, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.close_window)
        self.statistics_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.statistics_window)
        self.statusbar.setObjectName("statusbar")
        self.statistics_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.statistics_window)
        QtCore.QMetaObject.connectSlotsByName(self.statistics_window)

    def close_window(self):
        self.statistics_window.close()

    def update(self):
        comboBox_values: list = GET_LIST_ANALYSIS()
        self.comboBox.addItems(comboBox_values)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.statistics_window.setWindowTitle(_translate("MainWindow", "Статистики"))
        self.radioButton_10.setText(_translate("MainWindow", "Стандартный коэфициент"))
        self.label.setText(_translate("MainWindow", "График для анализа"))
        self.radioButton_13.setText(_translate("MainWindow", "Максимальный Х"))
        self.radioButton_8.setText(_translate("MainWindow", "Эксцесс"))
        self.radioButton_12.setText(_translate("MainWindow", "Минимальный Х"))
        self.pushButton_4.setText(_translate("MainWindow", "Взаимная корреляция"))
        self.radioButton_2.setText(_translate("MainWindow", "Среднее значение"))
        self.radioButton_5.setText(_translate("MainWindow", "Стандартное отклонение"))
        self.label_3.setText(_translate("MainWindow", "delta t"))
        self.radioButton_11.setText(
            _translate("MainWindow", "Среднее абсолютное отклонение")
        )
        self.radioButton.setText(_translate("MainWindow", "Стационарность: СЗ"))
        self.pushButton_5.setText(_translate("MainWindow", "Преобразование Фурье"))
        self.radioButton_3.setText(_translate("MainWindow", "Дисперссия"))
        self.pushButton_6.setText(_translate("MainWindow", "Спектр"))
        self.radioButton_9.setText(_translate("MainWindow", "Куртозис"))
        self.pushButton_3.setText(_translate("MainWindow", "Автокорреляция"))
        self.radioButton_7.setText(_translate("MainWindow", "Коэфициент асимметрии"))
        self.radioButton_4.setText(_translate("MainWindow", "Дисперсия х10"))
        self.pushButton_2.setText(_translate("MainWindow", "Гистограмма"))
        self.pushButton_7.setText(
            _translate("MainWindow", "Быстрое преобразование Фурье")
        )
        self.label_2.setText(_translate("MainWindow", "Место для вывода анализа"))
        self.radioButton_6.setText(_translate("MainWindow", "Асимметрия"))
        self.pushButton_9.setText(_translate("MainWindow", "Антисдвиг"))
        self.pushButton_10.setText(_translate("MainWindow", "Антиспайк"))
        self.pushButton_11.setText(_translate("MainWindow", "Антитренд"))
        self.pushButton_12.setText(_translate("MainWindow", "Антитренд + антиспайк"))
        self.pushButton.setText(_translate("MainWindow", "Вычислить"))
        self.pushButton_8.setText(_translate("MainWindow", "Закрыть"))

    def fast_fourier_transform(self):
        position_to_analysis = int(self.comboBox.currentText())
        model_for_analysis = POSITION_FOR_ANALYSIS.get(position_to_analysis)

        analysis = Analysis(model_for_analysis)
        model = analysis.spectrum()

        place_to_show = int(self.comboBox_2.currentText())
        POSITION_FOR_ANALYSIS[place_to_show] = model
        self.main_window.show_graph(model, place_to_show, normalisation=True)
        self.close_window()

    def autocorrelation(self):
        position_to_analysis = int(self.comboBox.currentText())
        model_for_analysis = POSITION_FOR_ANALYSIS.get(position_to_analysis)

        analysis = Analysis(model_for_analysis)

        model = analysis.calculation_autocorrelation()

        place_to_show = int(self.comboBox_2.currentText())
        POSITION_FOR_ANALYSIS[place_to_show] = model

        self.main_window.show_graph(model, place_to_show, normalisation=False)
        self.close_window()

    def spectrum(self):
        position_to_analysis = int(self.comboBox.currentText())
        model_for_analysis = POSITION_FOR_ANALYSIS.get(position_to_analysis)

        analysis = Analysis(model_for_analysis)
        delta_t = 0.001

        # if self.input_delta_t.get():
          #   delta_t = float(self.input_delta_t.get())
        # else:
          #  delta_t = 0.001

        analysis.set_delta_t(delta_t)
        model = analysis.calculation_fourier_transform()

        n = model.n
        model.display_n = int(n / 2)
        model.x = model.x[:model.display_n]
        model.y = model.y[:model.display_n]

        place_to_show = int(self.comboBox_2.currentText())
        POSITION_FOR_ANALYSIS[place_to_show] = model

        self.main_window.show_graph(model, place_to_show, normalisation=True)
        self.close_window()
