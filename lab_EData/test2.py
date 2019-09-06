import matplotlib as mpl
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

root = tk.Tk()
root.title("Графика / Лабораторная №5")
root.geometry('1320x820')

k = -5
b = 20
x_max = 1000
y_max = 1000

x = []
y = []

for i in range(x_max):
    yn = k * i + b
    x.append(i)
    y.append(yn)

fig = Figure(figsize=(5, 4), dpi=100)
fig.add_subplot(111).plot(x, y, color='red', label='Линия 1')
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().place(x = 10, y = 10)

root.mainloop()