# негатив
# гамма коррекция
# логарифмическая

from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
from PIL import ImageTk, Image, ImageDraw
import math

path = "/Users/zimin/Documents/Github/experimental_data/lab_EData/input files/lab3/image1.jpg"
p_img = Image.open(path)


def insertText():
    global file_name
    file_name = fd.askopenfilename(filetypes=(("JPG files", "*.jpg"),
                                                ("All files", "*.*")))
    print(file_name)
    global p_img, path
    path = file_name
    p_img= Image.open(file_name)
    img2 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img2)
    panel.image = img2


def rebuild(panel):
    global p_img,path
    p_img = Image.open(path)
    img3 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img3)
    panel.image = img3


def rebuild_img():

    new_path = "/Users/zimin/PycharmProjects/lab7GR/temp_image.jpg"
    p_img = Image.open(new_path)
    img3 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img3)
    panel.image = img3

# Негатив
def negative():
    global p_img
    draw = ImageDraw.Draw(p_img)
    width = p_img.size[0]
    height = p_img.size[1]
    pix = p_img.load()
    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            draw.point((i, j), (255 - r, 255 - g, 255 - b))

    img2 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img2)
    panel.image = img2


# Гамма коррекция
def gamma_correction():
    global p_img
    draw = ImageDraw.Draw(p_img)
    width = p_img.size[0]
    height = p_img.size[1]
    pix = p_img.load()
    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]

            c = 1
            gamma = 1.5
            new_r = int(c * math.pow(r, gamma))
            new_g = int(c * math.pow(g, gamma))
            new_b = int(c * math.pow(b, gamma))

            if new_r > 255:
                new_r = 255

            if new_g > 255:
                new_g = 255

            if new_b > 255:
                new_b = 255

            draw.point((i, j), (new_r, new_g, new_b))

    img2 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img2)
    panel.image = img2

def logarithmic():
    global p_img
    draw = ImageDraw.Draw(p_img)
    width = p_img.size[0]
    height = p_img.size[1]
    pix = p_img.load()
    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]

            c = 60
            new_r = int(c * math.log10(r + 1))
            new_g = int(c * math.log10(g + 1))
            new_b = int(c * math.log10(b + 1))

            if new_r > 255:
                new_r = 255

            if new_g > 255:
                new_g = 255

            if new_b > 255:
                new_b = 255

            draw.point((i, j), (new_r, new_g, new_b))

    img2 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img2)
    panel.image = img2

root = tk.Tk()
root.title("Графика / Лабораторная №7")
root.geometry('1520x820')
canvas = Canvas(root,width=1300,height=700)
canvas.pack(side = LEFT , padx = 10, pady = 10)

b1 = Button(text="Открыть", command=insertText, width = "23", height = "2")
b1.place(x=1010, y=11)

b2 = Button(text="Негатив", command=negative, width = "23", height = "2")
b2.place(x=1010, y=100)
b3 = Button(text="Гамма-коррекция", command=gamma_correction, width = "23", height = "2")
b3.place(x=1010, y=150)
b4 = Button(text="Логарифмическая", command=logarithmic, width = "23", height = "2")
b4.place(x=1010, y=200)

b8 = Button(text="Сброс", command=lambda:rebuild(panel), width = "23", height = "2")
b8.place(x=1225, y=11)



p_img.save("temp_image.jpg")
img = ImageTk.PhotoImage(p_img)
panel = tk.Label(root, image=img)
panel.place(x = 10, y =10)

root.mainloop()