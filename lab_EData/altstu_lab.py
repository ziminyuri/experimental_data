import random
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageTk

path = "/Users/zimin/Documents/Github/experimental_data/lab_EData/input files/grace.jpg"
p_img = Image.open(path)

def sgla1():
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

def figuru():
    global p_img
    draw = ImageDraw.Draw(p_img)

    number_of_dots = scale1.get()

    chb = var1.get() # 1 включен режим чб 0 выключен
    color_list = []
    if chb == 1:
        color_list = ['black', 'white']
    else:
        color_list = ['blue', 'red', 'black', 'white', 'green', 'gray']



    for n in range(number_of_dots):
        ellipsex = random.randrange(1, 600, 1)
        ellipsey = random.randrange(1, 400, 1)
        length_ellipse = random.randrange(10, 300, 5)
        ellipseXYrandom = random.randrange(0, 2, 1)
        wight_ellipse = random.randrange(1, 20, 1)
        if ellipseXYrandom == 0:
            draw.ellipse((ellipsex, ellipsey, ellipsex + (20 * wight_ellipse), ellipsey + length_ellipse),
                         outline=random.choice(color_list))
        else:
            draw.ellipse((ellipsex, ellipsey, ellipsex + length_ellipse, ellipsey + (20 * wight_ellipse)),
                         outline=random.choice(color_list))

    number_of_lines = scale2.get()
    for n in range(number_of_lines):
        linex = random.randrange(1, 600, 1)
        liney = random.randrange(1, 400, 1)
        length_line = random.randrange(10, 300, 5)
        lineXYrandom = random.randrange(0, 2, 1)
        if lineXYrandom == 0:
            draw.line((linex, liney, linex, liney+length_line), fill=random.choice(color_list),width=1)
        else:
            draw.line((linex, liney, linex + length_line, liney), fill=random.choice(color_list), width=1)

    number_of_ellipses = scale3.get()
    for n in range(number_of_ellipses):
        ellipsex = random.randrange(1, 600, 1)
        ellipsey = random.randrange(1, 400, 1)
        length_ellipse = random.randrange(10, 300, 5)
        ellipseXYrandom = random.randrange(0, 2, 1)
        wight_ellipse = random.randrange(1, 20, 1)
        if ellipseXYrandom == 0:
            draw.ellipse((ellipsex, ellipsey, ellipsex + (20 * wight_ellipse), ellipsey + length_ellipse),
                         fill=random.choice(color_list))
        else:
            draw.ellipse((ellipsex, ellipsey, ellipsex + length_ellipse, ellipsey + (20 * wight_ellipse)),
                         fill=random.choice(color_list))

    img2 = ImageTk.PhotoImage(p_img)
    p_img.save("temp_image.jpg")
    panel.configure(image=img2)
    panel.image = img2


def rebuild_img():

    new_path = "/Users/zimin/PycharmProjects/lab7GR/temp_image.jpg"
    p_img = Image.open(new_path)
    img3 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img3)
    panel.image = img3

def sgla():
    img = cv2.imread('temp_image.jpg')
    W = img.shape[0]
    H = img.shape[1]
    factor = float(input2.get())

    newW = int(W * factor)
    newH = int(H * factor)
    newImage = np.zeros((newW, newH, 3), np.uint8)

    choice = listbox2.curselection()
    if choice == (0,):
        for row in range(newW):
            for col in range(newH):
                newImage[row, col] = img[int(row / factor), int(col / factor)]

    if choice == (1,):
        for row in range(newW):
            for col in range(newH):
                oldPix = [0, 0, 0]
                count = 0
                oldRow = int(row / factor)
                oldCol = int(col / factor)
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if 0 <= oldRow + i < W and 0 <= oldCol + j < H:
                            oldPix += img[oldRow + i, oldCol + j]
                            count += 1

                newImage[row, col] = oldPix / count

    cv2.imwrite("temp_image.jpg", newImage)

    rebuild_img()


def holst():
    new_path = "/Users/zimin/PycharmProjects/lab7GR/holst.jpg"
    global p_img, path
    path = new_path
    p_img = Image.open(path)
    p_img.save("temp_image.jpg")
    img3 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img3)
    panel.image = img3


root = tk.Tk()
root.title("Графика / Лабораторная №7")
root.geometry('1520x820')
canvas = Canvas(root,width=1300,height=700)
canvas.pack(side = LEFT , padx = 10, pady = 10)

b1 = Button(text="Открыть", command=insertText, width = "23", height = "2")
b1.place(x = 1010, y = 11)
b8 = Button(text="Сброс", command=lambda:rebuild(panel), width = "23", height = "2")
b8.place(x = 1225, y = 11)

###################    Фигуры     ####################################
label1=Label(text = "Фигуры", height=1,width=7,font='Arial 24')
label1.place(x = 1175, y = 70)

label2=Label(text = "Кольца",height=1,width=7,font='Arial 14')
label2.place(x = 1020, y = 100)
scale1 = Scale(root,orient=HORIZONTAL,length=400,from_=1,to=20,tickinterval=1,resolution=1)
scale1.place(x = 1020, y = 120)
label3=Label(text = "Линии",height=1,width=7,font='Arial 14')
label3.place(x = 1020, y = 180)
scale2 = Scale(root,orient=HORIZONTAL,length=400,from_=1,to=20,tickinterval=1,resolution=1)
scale2.place(x = 1020, y = 200)
label4=Label(text = "Круги",height=1,width=7,font='Arial 14')
label4.place(x = 1020, y = 260)
scale3 = Scale(root,orient=HORIZONTAL,length=400,from_=1,to=20,tickinterval=1,resolution=1)
scale3.place(x = 1020, y = 280)
var1=IntVar()
check1=Checkbutton(root,text=u'Черно-белые',variable=var1,onvalue=1,offvalue=0)
check1.place(x = 1020, y = 350)
b2 = Button(text="Применить", command=figuru, width = "26", height = "2")
b2.place(x = 1180, y = 350)

###################    Холст     ####################################
label_frame1 = LabelFrame(root, text='Чистый холст')
label_frame1.place(x = 1020, y = 400)
b3 = Button(label_frame1, text="Создать", command=holst, width = "45", height = "2")
b3.pack()

###################    Сглаживание     ####################################
label5=Label(text = "Сглаживание",height=1,width=10,font='Arial 24')
label5.place(x = 1170, y = 470)
listbox2=Listbox(root,height=2,width=45,selectmode=SINGLE)
list2=[u"Ближайший сосед",u"Билинейное"]
for i in list2:
    listbox2.insert(END,i)
listbox2.place(x = 1020, y = 510)

label_frame1 = LabelFrame(root, text='Коэфициент масштабирования')
label_frame1.place(x = 1180, y = 550)
input2 = Entry(label_frame1, width=25)
input2.pack()
b4 = Button(text="Применить", command=sgla1, width = "26", height = "2")
b4.place(x = 1180, y = 600)

p_img.save("temp_image.jpg")
img = ImageTk.PhotoImage(p_img)
panel = tk.Label(root, image=img)
panel.place(x = 10, y =10)

root.mainloop()
