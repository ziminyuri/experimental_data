from PyQt5 import QtCore, QtWidgets
from forms.py_forms.add_graph import Ui_add_graph
from forms.py_forms.add_sound_window import Ui_add_sound
from forms.py_forms.statistics_window import Ui_statistics
from forms.py_forms.filter_window import Ui_filter_window
from forms.py_forms.deconvolution_window import Ui_deconvolution_window
from PyQt5.QtGui import QPixmap


class Ui_MainWindow:
    def __init__(self, MainWindow):
        self.image_path = ''

        self.main_window = MainWindow

        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.main_window.setCentralWidget(self.centralwidget)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 511, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

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
        self.action_2.triggered.connect(self.open_image_window)
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

        self.image_label = QtWidgets.QLabel(self.main_window)
        path = "/Users/zimin/Documents/Github/experimental_data/lab_EData/input files/lab3/image2.jpg"
        pixmap = QPixmap(path)
        self.image_label.setPixmap(pixmap)
        self.gridLayout.addWidget(self.image_label,1, 0, 1, 1)
        # self.main_window.resize(pixmap.width(), pixmap.height())

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
