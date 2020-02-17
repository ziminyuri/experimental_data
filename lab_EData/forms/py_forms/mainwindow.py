# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/qt_forms/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from forms.py_forms.add_graph import Ui_add_graph
from forms.py_forms.add_sound_window import Ui_add_sound
from forms.py_forms.statistics_window import Ui_statistics
from forms.py_forms.filter_window import Ui_filter_window
from forms.py_forms.deconvolution_window import Ui_deconvolution_window


class Ui_MainWindow(object):
    # Открыть окно добавления графика
    def open_add_graph_window(self):
        self.add_graph_window = QtWidgets.QMainWindow()
        self.add_graph_ui = Ui_add_graph()
        self.add_graph_ui.setupUi(self.add_graph_window)
        self.add_graph_window.show()

    # Открыть окно добавления звукового файла
    def open_add_sound_window(self):
        self.add_sound_window = QtWidgets.QMainWindow()
        self.add_sound_ui = Ui_add_sound()
        self.add_sound_ui.setupUi(self.add_sound_window)
        self.add_sound_window.show()

    # Открыть окно рассчета статистик
    def open_statistics_window(self):
        self.statistics_window = QtWidgets.QMainWindow()
        self.statistics_ui = Ui_statistics()
        self.statistics_ui.setupUi(self.statistics_window)
        self.statistics_window.show()

    # Открыть окно фильтров
    def open_filter_window(self):
        self.filter_window = QtWidgets.QMainWindow()
        self.filter_ui = Ui_filter_window()
        self.filter_ui.setupUi(self.filter_window)
        self.filter_window.show()

    # Открыть окно деконволюций
    def open_deconvolution_window(self):
        self.deconvolution_window = QtWidgets.QMainWindow()
        self.deconvolution_ui = Ui_deconvolution_window()
        self.deconvolution_ui.setupUi(self.deconvolution_window)
        self.deconvolution_window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action.triggered.connect(self.open_add_graph_window)
        self.action.setShortcut('Ctrl+N')
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_3.triggered.connect(self.open_add_sound_window)
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_6.triggered.connect(self.open_statistics_window)
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_7.triggered.connect(self.open_filter_window)
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_8.triggered.connect(self.open_deconvolution_window)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)
        self.menu_2.addAction(self.action_8)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Обработка и анализ данных"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Обработка"))
        self.action.setText(_translate("MainWindow", "Добавить график"))
        self.action_2.setText(_translate("MainWindow", "Открыть изображение"))
        self.action_3.setText(_translate("MainWindow", "Открыть звуковой файл"))
        self.action_5.setText(_translate("MainWindow", "Выход"))
        self.action_6.setText(_translate("MainWindow", "Статистики"))
        self.action_7.setText(_translate("MainWindow", "Фильтр"))
        self.action_8.setText(_translate("MainWindow", "Деконволюция"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
