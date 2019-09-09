from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt

from display import *

def main():
    root = Tk()
    root.title("Лабораторная №1 / Методы обработки эксперементальных данных")
    root.geometry('1320x820')
    ex = Display(root)

    root.mainloop()

if __name__ == '__main__':
    main()