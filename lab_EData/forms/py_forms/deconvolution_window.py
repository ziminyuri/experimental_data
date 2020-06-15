from PyQt5 import QtCore, QtWidgets

from image import deconvolution_img
from model import Model
from model import deconvolution as model_deconvolution
from setting import POSITION_FOR_ANALYSIS, GET_LIST_ANALYSIS


class UiDeconvolutionWindow(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.deconvolution_window = main_window.deconvolution_window
        self.deconvolution_window.setObjectName("MainWindow")
        self.deconvolution_window.resize(378, 322)
        self.centralwidget = QtWidgets.QWidget(self.deconvolution_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 361, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 9, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        ls = ['Тренд сердцебиения', 'Тренд функции для IMG']
        self.comboBox_4.addItems(ls)
        self.gridLayout.addWidget(self.comboBox_4, 3, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 10, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        comboBox_list: list = GET_LIST_ANALYSIS()
        self.comboBox_3.addItems(comboBox_list)
        self.gridLayout.addWidget(self.comboBox_3, 1, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItems(["1", "2", "3", "4", "5", "6"])
        self.gridLayout.addWidget(self.comboBox_5, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.deconvlution)
        self.gridLayout.addWidget(self.pushButton, 11, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 12, 0, 1, 1)
        self.deconvolution_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.deconvolution_window)
        self.statusbar.setObjectName("statusbar")
        self.deconvolution_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.deconvolution_window)
        QtCore.QMetaObject.connectSlotsByName(self.deconvolution_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Деконволюция"))
        self.checkBox.setText(_translate("MainWindow", "Изображение"))
        self.label_6.setText(_translate("MainWindow", "Позиция графика"))
        self.checkBox_2.setText(_translate("MainWindow", "Подавить шумы"))
        self.pushButton.setText(_translate("MainWindow", "Деконволюция"))
        self.label_7.setText(_translate("MainWindow", "Тренд "))
        self.label_9.setText(_translate("MainWindow", "Место для вывода результата"))
        self.pushButton_2.setText(_translate("MainWindow", "Вывести тренд"))

    def deconvlution(self):
        position_to_analysis: int = int(self.comboBox_3.currentText())
        place_to_show: int = int(self.comboBox_5.currentText())
        deconvoltion_func: str = self.comboBox_4.currentText()

        if self.checkBox.isChecked():   # is img
            img_path: str = POSITION_FOR_ANALYSIS.get(position_to_analysis)

            if self.checkBox_2.isChecked():     # has noise
                deconvolution_img(img_path, place_to_show, deconvoltion_func, noise=True)
            else:
                deconvolution_img(img_path, place_to_show, deconvoltion_func)

            self.main_window.show_img(place_to_show)
            self.deconvolution_window.close()

        else:
            model = POSITION_FOR_ANALYSIS.get(position_to_analysis)

            model_func = Model(deconvoltion_func)
            model_func.calculation()

            result_model = model_deconvolution(model, model_func)

            POSITION_FOR_ANALYSIS[place_to_show] = result_model
            self.main_window.show_graph(result_model, place_to_show)
            self.deconvolution_window.close()
