from tkinter import *
import tkinter.ttk as ttk
from model import *

class ChildWindow(Toplevel):
    def __init__(self, main_window, root):
        super().__init__(root)
        self.root = root
        self.main = main_window
        self.init_child_window()


    def click_button_add_and_close(self):

        if self.c2.get() == "y(x)=kx+b":
            model1 = Model(1)
            model1.calculation()
            self.main.draw_graph(model1)

        if self.c2.get() == "y(x)=-kx+b":
            model1 = Model(2)
            model1.calculation()
            self.main.draw_graph(model1)

        if self.c2.get() == "y(x) = beta * exp^(alpha * i)":
            model1 = Model(3)
            model1.calculation()
            self.main.draw_graph(model1)

        if self.c2.get() == "y(x) = beta * exp^(alpha * -i)":
            model1 = Model(4)
            model1.calculation()
            self.main.draw_graph(model1)

        if self.c2.get() == "Встроенный рандом":
            model1 = Model(5)
            model1.calculation()
            self.main.draw_graph(model1)

        if self.c2.get() == "Кастомный рандом":
            model1 = Model(6)
            model1.calculation()
            self.main.draw_graph(model1)

        if self.c2.get() == "Аномальные участки":
            model1 = Model(7)
            model1.calculation()
            self.main.draw_graph(model1)

        if self.c2.get() == "Значения за областью":
            model1 = Model(8)
            model1.calculation()
            self.main.draw_graph(model1)

        self.destroy()

    def click_button_close(self):
        self.destroy()

    def init_child_window(self):
        self.title('Добавить новый график')
        self.geometry('600x400')
        self.resizable(False,False)   #Нельзя изменить размер окна


        label1 = Label(self, text="Номер графика", height=1, width=14, font='Arial 14')
        label1.place(x=10, y=10)
        self.c1 = ttk.Combobox(self, values = [u"1",u"2",u"3",u"4"],height=4)
        self.c1.place(x=10, y=30)

        label2 = Label(self, text="График функции", height=1, width=14, font='Arial 14')
        label2.place(x=10, y=60)
        self.c2 = ttk.Combobox(self, values = [u"y(x)=kx+b",u"y(x)=-kx+b",u"y(x) = beta * exp^(alpha * i)",
                                         u"y(x) = beta * exp^(alpha * -i)", u"Встроенный рандом",u"Кастомный рандом",
                                         u"Аномальные участки", u"Значения за областью"],height=8)
        self.c2.place(x=10, y=80)

        ### Ввод k
        label2 = Label(self, text="k", height=1, width=1, font='Arial 14')
        label2.place(x=300, y=10)
        input_k = Entry(self, width=15)
        input_k.place(x=300, y=30)

        ### Ввод b
        label3 = Label(self, text="b", height=1, width=1, font='Arial 14')
        label3.place(x=300, y=60)
        input_b = Entry(self,width=15)
        input_b.place(x=300, y=80)

        ### Ввод alpha
        label4 = Label(self,text="alpha", height=1, width=5, font='Arial 14')
        label4.place(x=300, y=110)
        input_alpha = Entry(self,width=15)
        input_alpha.place(x=300, y=130)

        ### Ввод beta
        label5 = Label(self,text="beta", height=1, width=4, font='Arial 14')
        label5.place(x=300, y=160)
        input_beta = Entry(self,width=22)
        input_beta.place(x=300, y=180)

        ### Ввод N - Количество записей
        label6 = Label(self,text="Количество записей", height=1, width=17, font='Arial 14')
        label6.place(x=10, y=210)
        input_N = Entry(self,width=22)
        input_N.place(x=10, y=230)

        ### Ввод n - Начало промежутка
        label7 = Label(self,text="Начало промежутка", height=1, width=17, font='Arial 14')
        label7.place(x=10, y=260)
        input_n = Entry(self,width=22)
        input_n.place(x=10, y=280)

        ### Ввод m - Конец промежутка
        label8 = Label(self,text="Окончание промежутка", height=1, width=20, font='Arial 14')
        label8.place(x=10, y=310)
        input_m = Entry(self,width=22)
        input_m.place(x=10, y=330)

        ### Ввод -S - Минимальное значение функции
        label9 = Label(self,text="Минимальное значение ф-ии", height=1, width=24, font='Arial 14')
        label9.place(x=10, y=110)
        input_S_min = Entry(self,width=22)
        input_S_min.place(x=10, y=130)

        ### Ввод S - Максимальное значение функции
        label10 = Label(self,text="Максимальное значение ф-ии", height=1, width=25, font='Arial 14')
        label10.place(x=10, y=160)
        input_S_max = Entry(self,width=22)
        input_S_max.place(x=10, y=180)


        b1 = Button(self, text="Добавить", command=self.click_button_add_and_close, width="15", height="2")
        b1.place(x=300, y=350)
        b2= Button(self, text="Закрыть", command=self.click_button_close, width="15", height="2")
        b2.place(x=450, y=350)

        self.grab_set()       #Перехватывает все события происходящие в приложении
        self.focus_set()      #Захватывает и удерживает фокус



