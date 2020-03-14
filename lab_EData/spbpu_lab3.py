import math
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageTk

path = "/Users/zimin/Documents/Github/experimental_data/lab_EData/input files/lab3/image3.jpg"
p_img = Image.open(path)

bar_chart_x = np.arange(0, 255)
bar_chart_y = np.zeros(255)


def insertText() -> None:
    global file_name
    file_name = fd.askopenfilename(
        filetypes=(("JPG files", "*.jpg"), ("All files", "*.*"))
    )
    print(file_name)
    global p_img, path
    path = file_name
    p_img = Image.open(file_name)
    img2 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img2)
    panel.image = img2


def rebuild(panel) -> None:
    global p_img, path
    p_img = Image.open(path)
    img3 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img3)
    panel.image = img3


def rebuild_img() -> None:
    new_path = "temp_image.jpg"
    p_img = Image.open(new_path)
    img3 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img3)
    panel.image = img3


def negative(red: int, green: int, blue: int):
    return 255 - red, 255 - green, 255 - blue


def gamma_correction(red, green, blue):
    c = 20
    gamma = 0.3
    new_red = int(c * math.pow(red, gamma))
    new_green = int(c * math.pow(green, gamma))
    new_blue = int(c * math.pow(blue, gamma))

    if new_red > 255:
        new_red = 255

    if new_green > 255:
        new_green = 255

    if new_blue > 255:
        new_blue = 255

    return new_red, new_green, new_blue


def logarithmic(red, green, blue):
    c = 60
    new_red = int(c * math.log10(red + 1))
    new_green = int(c * math.log10(green + 1))
    new_blue = int(c * math.log10(blue + 1))

    if new_red > 255:
        new_red = 255

    if new_green > 255:
        new_green = 255

    if new_blue > 255:
        new_blue = 255

    return new_red, new_green, new_blue


def image_processing(type_processing: str) -> None:
    global p_img
    draw = ImageDraw.Draw(p_img)
    width = p_img.size[0]
    height = p_img.size[1]

    rgb_im = p_img.convert("RGB")
    pix = rgb_im.load()

    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]

            if type_processing == "negative":
                red, green, blue = negative(r, g, b)

            elif type_processing == "gamma":
                red, green, blue = gamma_correction(r, g, b)

            elif type_processing == "logarithmic":
                red, green, blue = logarithmic(r, g, b)

            else:
                red = 0
                green = 0
                blue = 0

            draw.point((i, j), (red, green, blue))

    img2 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img2)
    panel.image = img2


def bar_chart() -> None:
    global p_img
    width = p_img.size[0]
    height = p_img.size[1]
    rgb_im = p_img.convert("RGB")
    pix = rgb_im.load()

    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]

            average_value: int = int((r + g + b) / 3)
            bar_chart_value = bar_chart_y[average_value] + 1
            bar_chart_y[average_value] = bar_chart_value

    plt.plot(bar_chart_x, bar_chart_y)
    plt.show()


def histogram_equalization() -> None:
    histogram_equalization_x = bar_chart_x
    histogram_equalization_y = np.zeros(255)

    histogram_equalization_y[0] = bar_chart_y[0]
    for i in range(1, len(bar_chart_y)):
        histogram_equalization_y[i] = histogram_equalization_y[i - 1] + bar_chart_y[i]

    plt.plot(histogram_equalization_x, histogram_equalization_y)
    plt.show()


def smoothing() -> None:
    global p_img
    W, H = p_img.size
    print(W)
    factor = float(input2.get())

    newW = int(W * factor)
    newH = int(H * factor)
    print(newW)

    choice = listbox2.curselection()
    if choice == (0,):
        p = p_img.resize((newW, newH), Image.NEAREST)
        p_img = p

    if choice == (1,):
        p = p_img.resize((newW, newH), Image.BILINEAR)
        p_img = p
    img2 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img2)
    panel.image = img2


root = tk.Tk()
root.title("Графика / Лабораторная №7")
root.geometry("1520x820")
canvas = Canvas(root, width=1300, height=700)
canvas.pack(side=LEFT, padx=10, pady=10)

b1 = Button(text="Открыть", command=insertText, width="23", height="2")
b1.place(x=1010, y=11)

b2 = Button(
    text="Негатив", command=lambda: image_processing("negative"), width="23", height="2"
)
b2.place(x=1010, y=100)
b3 = Button(
    text="Гамма-коррекция",
    command=lambda: image_processing("gamma"),
    width="23",
    height="2",
)
b3.place(x=1010, y=150)
b5 = Button(
    text="Логарифмическая",
    command=lambda: image_processing("logarithmic"),
    width="23",
    height="2",
)
b5.place(x=1010, y=200)

b4 = Button(text="Гистограмма", command=lambda: bar_chart(), width="23", height="2")
b4.place(x=1010, y=300)

b6 = Button(
    text="Эквализация гистограммы", command=lambda: bar_chart(), width="23", height="2"
)
b6.place(x=1010, y=350)

listbox2 = Listbox(root, height=2, width=45, selectmode=SINGLE)
list2 = [u"Ближайший сосед", u"Билинейное"]
for i in list2:
    listbox2.insert(END, i)
listbox2.place(x=1020, y=510)

label_frame1 = LabelFrame(root, text="Коэфициент масштабирования")
label_frame1.place(x=1180, y=550)
input2 = Entry(label_frame1, width=25)
input2.pack()
b4 = Button(text="Применить", command=smoothing, width="26", height="2")
b4.place(x=1180, y=600)


b8 = Button(text="Сброс", command=lambda: rebuild(panel), width="23", height="2")
b8.place(x=1225, y=11)

p_img.save("temp_image.jpg")
img = ImageTk.PhotoImage(p_img)
panel = tk.Label(root, image=img)
panel.place(x=10, y=10)

root.mainloop()
