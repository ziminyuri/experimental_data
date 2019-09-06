import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk

root = Tk.Tk()
root.wm_title("Embedding in TK")


f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0, 3.0, 0.01)
s = sin(2*pi*t)

#a.plot(t, s)
#a.set_title('Tk embedding')
#a.set_xlabel('X axis label')
#a.set_ylabel('Y label')

f1 = Figure(figsize=(8, 10), dpi=100)
"""

a1 = f.add_subplot(111)
t1 = arange(0.0, 3.0, 0.01)
s1 = sin(5*pi*t)

a1.plot(t1, s1)
a1.set_title('новый график')
a1.set_xlabel('инксы')
a1.set_ylabel('игкрики')
"""


# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
#canvas = FigureCanvasTkAgg(f1, master=root)

canvas.draw()
#canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

#canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
canvas.pack(side = LEFT , padx = 10, pady = 10)

Tk.mainloop()