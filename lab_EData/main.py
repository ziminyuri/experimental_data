from tkinter import *

from PyQt5 import QtWidgets

from forms.py_forms.mainwindow import Ui_mainwindow
from MainWindow import MainWindow

_GRAPH: list = [None, None, None, None, None, None]
# _GRAPH: list = [0, 0, 0, 0, 0, 0]
_IMG: list = [0, 0, 0, 0, 0, 0]
# _IMG: list = [None, None, None, None, None, None]


def get_GRAPH():
    return _GRAPH


def get_IMG():
    return _IMG


def main():
    root = Tk()
    app = MainWindow(root)
    app.pack()
    root.title("Лабораторная №1 / Методы обработки эксперементальных данных")
    root.geometry("1400x820")
    root.resizable(False, False)
    root.mainloop()


def pyqt5():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_mainwindow(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # main()
    pyqt5()
