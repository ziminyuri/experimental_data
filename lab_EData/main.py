from tkinter import *

from PyQt5 import QtWidgets

from forms.py_forms.mainwindow import Ui_mainwindow
from tkinter_ui.MainWindow import MainWindow


def tkinter_main():
    root = Tk()
    app = MainWindow(root)
    app.pack()
    root.title("Лабораторная №1 / Методы обработки эксперементальных данных")
    root.geometry("1400x820")
    root.resizable(False, False)
    root.mainloop()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_mainwindow(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    # tkinter_main()
