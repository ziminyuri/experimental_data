import tkinter as tk
from tkinter import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


Data1 = {'Country': ['US', 'CA', 'GER', 'UK', 'FR'],
         'GDP_Per_Capita': [45000, 42000, 52000, 49000, 47000]
         }

df1 = DataFrame(Data1, columns=['Country', 'GDP_Per_Capita'])
df1 = df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum()

Data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
         'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
         }

df2 = DataFrame(Data2, columns=['Year', 'Unemployment_Rate'])
df2 = df2[['Year', 'Unemployment_Rate']].groupby('Year').sum()

Data3 = {'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
         'Stock_Index_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
         }

df3 = DataFrame(Data3, columns=['Interest_Rate', 'Stock_Index_Price'])


root = tk.Tk()
root.title("Графика / Лабораторная №5")
root.geometry('1320x820')
canvas = Canvas(root,width=1100,height=700)
canvas.pack(side = LEFT , padx = 10, pady = 10)


figure1 = plt.Figure(figsize=(5, 4), dpi=100)
ax1 = figure1.add_subplot(111)
line1 = FigureCanvasTkAgg(figure1, root)
line1.get_tk_widget().place(x = 20, y = 20)
df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
ax1.set_title('Year Vs. Unemployment Rate')

figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().place(x = 550, y = 20)
df1.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')


figure3 = plt.Figure(figsize=(5, 4), dpi=100)
ax3 = figure3.add_subplot(111)
line3 = FigureCanvasTkAgg(figure3, root)
line3.get_tk_widget().place(x = 20, y = 400)
df1.plot(kind='line', legend=True, ax=ax3, color='r', marker='o', fontsize=10)
ax3.set_title('Year Vs. Unemployment Rate')


figure4 = plt.Figure(figsize=(5, 4), dpi=100)
ax4 = figure4.add_subplot(111)
line4 = FigureCanvasTkAgg(figure4, root)
line4.get_tk_widget().place(x = 550, y = 400)
df1.plot(kind='line', legend=True, ax=ax4, color='r', marker='o', fontsize=10)
ax4.set_title('Year Vs. Unemployment Rate')


root.mainloop()