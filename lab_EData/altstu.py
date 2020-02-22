import random
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

import cv2
import numpy
import scipy
from PIL import Image, ImageDraw, ImageFilter, ImageTk
from scipy import ndimage
from scipy.ndimage.filters import gaussian_filter

path = "/Users/zimin/Documents/Github/experimental_data/lab_EData/input files/grace.jpg"
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


def shum():
    global p_img
    draw = ImageDraw.Draw(p_img)

    number_of_dots = scale1.get()

    chb = var1.get() # 1 включен режим чб 0 выключен
    if chb == 1:
        color_list = ['black', 'white']
    else:
        color_list = ['blue', 'red', 'black', 'white', 'green', 'gray']

    for n in range (number_of_dots):
        dotx = random.randrange(1, 1000, 1)
        doty = random.randrange(1, 665, 1)
        draw.line((dotx, doty, dotx+1, doty+1), fill=random.choice(color_list),width=1)

    number_of_lines = scale2.get()
    for n in range(number_of_lines):
        linex = random.randrange(1, 1000, 1)
        liney = random.randrange(1, 665, 1)
        length_line = random.randrange(10, 300, 5)
        lineXYrandom = random.randrange(0, 2, 1)
        if lineXYrandom == 0:
            draw.line((linex, liney, linex, liney+length_line), fill=random.choice(color_list),width=1)
        else:
            draw.line((linex, liney, linex + length_line, liney), fill=random.choice(color_list), width=1)

    number_of_ellipses = scale3.get()
    for n in range(number_of_ellipses):
        ellipsex = random.randrange(1, 1000, 1)
        ellipsey = random.randrange(1, 665, 1)
        length_ellipse = random.randrange(10, 300, 5)
        ellipseXYrandom = random.randrange(0, 2, 1)
        wight_ellipse = random.randrange(1, 20, 1)
        if ellipseXYrandom == 0:
            draw.ellipse((ellipsex, ellipsey, ellipsex+(20 * wight_ellipse), ellipsey+length_ellipse), outline=random.choice(color_list))
        else:
            draw.ellipse((ellipsex, ellipsey, ellipsex + length_ellipse, ellipsey+(20*wight_ellipse)), outline=random.choice(color_list))

    img2 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img2)
    panel.image = img2


def kontur():
    global p_img
    draw = ImageDraw.Draw(p_img)
    width = p_img.size[0]
    height = p_img.size[1]
    pix = p_img.load()

    for i in range(width):
        for j in range(height):
            Yp = int(round(pix[i, j][0] * 0.299 + pix[i, j][1] * 0.5876 + pix[i, j][2] * 0.114))
            draw.point((i, j), (Yp, Yp, Yp))

    p_img_copy = p_img
    draw = ImageDraw.Draw(p_img_copy)
    width = p_img_copy.size[0]
    height = p_img_copy.size[1]
    pix = p_img_copy.load()

    i=1
    j=1
    print(width)
    print(height)
    for i in range(1, width-1):
        for j in range(1,height-1):
            #print("i=")
            #print(i)
            #print("j=")
            #print(j)
            P = pix[i-1, j-1][0]
            P1 = 2 * pix[i-1, j][0]
            P2 = pix[i-1, j + 1][0] - 1
            P3 = pix[i + 1, j-1][0] - 1
            P4 = 2 * pix[i + 1, j][0] - 2
            P5 = pix[i + 1, j + 1][0] - 1
            P7 = (P + P1 + P2 - P3 - P4 - P5)
            P6 = abs(P + P1 + P2 - P3 - P4 - P5) + abs(P + P1 + P2 - P3 - P4 - P5)
            if (P6 < 0):
                P6 = 0
            if (P6 >255):
                P6 = 255
            draw.point((i, j), (P6, P6, P6))
            #print(P)


    img2 = ImageTk.PhotoImage(p_img_copy)
    panel.configure(image=img2)
    panel.image = img2

def kontur1():
    im = scipy.misc.imread(path)
    im = im.astype('int32')
    dx = ndimage.sobel(im, 0)  # horizontal derivative
    dy = ndimage.sobel(im, 1)  # vertical derivative
    mag = numpy.hypot(dx, dy)  # magnitude
    mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
    scipy.misc.imsave("/Users/zimin/PycharmProjects/lab6GR/sb.jpg", mag)
    path1 = "/Users/zimin/PycharmProjects/lab6GR/sb.jpg"
    p_img = Image.open(path1)
    img2 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img2)
    panel.image = img2



def ser():
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
            S = (r + g + b) // 3
            draw.point((i, j), (S, S, S))
    img2 = ImageTk.PhotoImage(p_img)
    panel.configure(image=img2)
    panel.image = img2

def count_vector(c):
    count = 0
    for num in c:
            count += 1
    #if(count != 9):
        #print("ЧТО-то")
    return  count
def filter1():
    global p_img
    choice = listbox2.curselection()
    n_of_maska = int(input1.get())
    if n_of_maska%2 == 0:
        n_of_maska = n_of_maska+1

    m_of_maska = input2.get()

    if choice == (0,):
        im1 = p_img.filter(ImageFilter.MedianFilter(n_of_maska))
        img2 = ImageTk.PhotoImage(im1)
        panel.configure(image=img2)
        panel.image = img2
    if choice == (1,):
        sigma = int(input3.get())
        im1 = p_img.filter(ImageFilter.GaussianBlur(sigma))
        img2 = ImageTk.PhotoImage(im1)
        panel.configure(image=img2)
        panel.image = img2


def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = []
    data_final = numpy.zeros((len(data),len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final



def filter():
    global p_img
    draw = ImageDraw.Draw(p_img)
    n_of_maska = input1.get()
    m_of_maska = input2.get()
    choice = listbox2.curselection()
    width = p_img.size[0]
    height = p_img.size[1]
    pix = p_img.load()
    print(pix[0,0])


    ############## Медианный фильтр ###################

    if choice == (0,):
        p = int(n_of_maska)
        q = int(m_of_maska)
        p= round(p/2)
        q = round(q/2)
        #print(q)
        r1 = -p
        r2 = -q
        c = p ** q
        cc = int(round(c / 2))
        count =0
        for i in range(width):
            for j in range(height):
                colors = []
                for r1 in range(p+1):
                    for r2 in range(q+1):
                        valid_y = j + r1
                        if (valid_y < 0 or valid_y >= height):
                            valid_y -= 2 * r1

                        valid_x = i + r2
                        if (valid_x < 0 or valid_x >= width):
                            valid_x -= 2 * r2

                        colors.append(pix[valid_x,valid_y])


                colors.sort()

                if(c % 2 == 1):
                    f = 1
                else:
                    f = 0

                if(f == 1):
                    r = colors[cc][0]
                    g = colors[cc][1]
                    b = colors[cc][2]
                    draw.point((i, j), (r,g,b))

                else:
                    pix1 = colors[cc-1]
                    pix2 = colors[cc]
                    r = int(round((pix1[0] + pix2[0])/2))
                    #print(r)
                    g = int(round((pix1[1] + pix2[1])/2))
                    #print(g)
                    b = int(round((pix1[2] + pix2[2])/2))
                    #print (b)
                    draw.point((i, j), (r,g,b))
                colors.clear()
        img2 = ImageTk.PhotoImage(p_img)
        panel.configure(image=img2)
        panel.image = img2

    ##############  Фильтр Гаусса ###################
    if choice == (1,):
        #p = int(n_of_maska)
        #q = int(m_of_maska)
        #p = round(p / 2)
        #q = round(q / 2)
        #sigma = int(input2.get())
        #denom = 2 * sigma * sigma
        im = cv2.imread(path)
        blurred = gaussian_filter(im, sigma=1)
        scipy.misc.imsave("/Users/zimin/PycharmProjects/lab6GR/sb.jpg", blurred)
        path1 = "/Users/zimin/PycharmProjects/lab6GR/sb.jpg"
        p_img = Image.open(path1)
        img2 = ImageTk.PhotoImage(p_img)
        panel.configure(image=img2)
        panel.image = img2










root = tk.Tk()
root.title("Графика / Лабораторная №6")
root.geometry('1520x820')
canvas = Canvas(root,width=1300,height=700)
canvas.pack(side = LEFT , padx = 10, pady = 10)

b1 = Button(text="Открыть", command=insertText, width = "23", height = "2")
b1.place(x = 1010, y = 11)
b8 = Button(text="Сброс", command=lambda:rebuild(panel), width = "23", height = "2")
b8.place(x = 1225, y = 11)

###################    ШУМЫ     ####################################
label1=Label(text = "Шумы", height=1,width=7,font='Arial 24')
label1.place(x = 1175, y = 70)

label2=Label(text = "Точки",height=1,width=7,font='Arial 14')
label2.place(x = 1020, y = 100)
scale1 = Scale(root,orient=HORIZONTAL,length=400,from_=200,to=2000,tickinterval=200,resolution=200)
scale1.place(x = 1020, y = 120)
label3=Label(text = "Линии",height=1,width=7,font='Arial 14')
label3.place(x = 1020, y = 180)
scale2 = Scale(root,orient=HORIZONTAL,length=400,from_=1,to=20,tickinterval=1,resolution=1)
scale2.place(x = 1020, y = 200)
label4=Label(text = "Эллипсы",height=1,width=7,font='Arial 14')
label4.place(x = 1020, y = 260)
scale3 = Scale(root,orient=HORIZONTAL,length=400,from_=1,to=20,tickinterval=1,resolution=1)
scale3.place(x = 1020, y = 280)
var1=IntVar()
check1=Checkbutton(root,text=u'Черно-белые',variable=var1,onvalue=1,offvalue=0)
check1.place(x = 1020, y = 350)
b2 = Button(text="Применить", command=shum, width = "26", height = "2")
b2.place(x = 1180, y = 350)

###################    Эффекты     ####################################
label_frame1 = LabelFrame(root, text='Эффекты')
label_frame1.place(x = 1020, y = 400)
b3 = Button(label_frame1, text="Окунтуривание", command=kontur1, width = "45", height = "2")
b3.pack()

###################    Фильтры     ####################################
label5=Label(text = "Фильтр",height=1,width=10,font='Arial 24')
label5.place(x = 1170, y = 470)
listbox2=Listbox(root,height=2,width=45,selectmode=SINGLE)
list2=[u"Медианный",u"Гаусса"]
for i in list2:
    listbox2.insert(END,i)
listbox2.place(x = 1020, y = 510)
label6=Label(text = "Маска",height=1,width=7,font='Arial 14')
label6.place(x = 1020, y = 550)
input1 = Entry(width=3)
input1.place(x = 1020, y = 570)
label7=Label(text = "X", height=1,width=1,font='Arial 14')
label7.place(x = 1060, y = 570)
input2 = Entry(width=3)
input2.place(x = 1080, y = 570)

label6=Label(text = "σ",height=1,width=7,font='Arial 14')
label6.place(x = 1120, y = 550)
input3 = Entry(width=3)
input3.place(x = 1140, y = 570)
b4 = Button(text="Применить", command=filter1, width = "26", height = "2")
b4.place(x = 1180, y = 600)

img = ImageTk.PhotoImage(p_img)
panel = tk.Label(root, image=img)
panel.place(x = 10, y =10)

root.mainloop()
