from tkinter import *
from MainWindow import MainWindow


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.py_forms.mainwindow import Ui_MainWindow



def main():
    root = Tk()
    app = MainWindow(root)
    app.pack()
    root.title("Лабораторная №1 / Методы обработки эксперементальных данных")
    root.geometry('1400x820')
    root.resizable(False, False)
    root.mainloop()


def pyqt5():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    # pyqt5()
