from tkinter import *
import tkinter.ttk as ttk
from model import *
from tkinter import messagebox

class ChildWindow(Toplevel):
    def __init__(self, main_window, root, graph_array):
        super().__init__(root)
        self.root = root
        self.graph_array = graph_array

        self.main = main_window
        self.init_child_window()



    def set_defual_values_for_model(self, model):

        if self.input_k.get() != "":
            try:
                k = float(self.input_k.get())
                model.set_k(k)
            except:
                messagebox.showerror("Ошибка", "k должно быть вещественнным")
                return

        if self.input_b.get() != "":
            try:
                b = float(self.input_b.get())
                model.set_b(b)
            except:
                messagebox.showerror("Ошибка", "b должно быть вещественнным")
                return

        if self.input_alpha.get() != "":
            try:
                alpha = float(self.input_alpha.get())
                model.set_alpha(alpha)
            except:
                messagebox.showerror("Ошибка", "alpha должно быть вещественнным")
                return

        if self.input_beta.get() != "":
            try:
                beta = float(self.input_beta.get())
                model.set_beta(beta)
            except:
                messagebox.showerror("Ошибка", "beta должно быть вещественнным")
                return

        if self.input_N.get() != "":
            try:
                N = int(self.input_N.get())
                model.set_N(N)
            except:
                messagebox.showerror("Ошибка", "Количество записей должно быть целочисленным")
                return

        if self.input_n.get() != "":
            try:
                n = int(self.input_n.get())
                model.set_n(n)
            except:
                messagebox.showerror("Ошибка", "Начало промежутка должно быть целочисленным")
                return

        if self.input_m.get() != "":
            try:
                m = int(self.input_m.get())
                model.set_m(m)
            except:
                messagebox.showerror("Ошибка", "Окончание промежутка должно быть целочисленным")
                return

        if self.input_S_min.get() != "":
            try:
                min = int(self.input_S_min.get())
                model.set_axis_y_graph_min(min)
            except:
                messagebox.showerror("Ошибка", "Минимальное значение ф-ии должно быть целочисленным")
                return

        if self.input_S_max.get() != "":
            try:
                max = int(self.input_S_max.get())
                model.set_axis_y_graf_max(max)
            except:
                messagebox.showerror("Ошибка", "Максимальное значение ф-ии должно быть целочисленным")
                return

        #Указали какому графику принадлежит график
        model.set_graph(int(self.c1.get()))

    def add_model(self, model):

        j = 0
        for i in (self.graph_array):
            if i.get_graph() == int(self.c1.get()):
                del self.graph_array[j]
            j= j + 1

        self.graph_array.append(model)

    def click_button_add_and_close(self):

        if self.c1.get() == "":
            messagebox.showinfo("Не указан номер графика")
            pass

        model1 = Model(1)

        if self.c2.get() == "y(x)=kx+b":
            model1 = Model(1)

        if self.c2.get() == "y(x)=-kx+b":
            model1 = Model(2)

        if self.c2.get() == "y(x) = beta * exp^(alpha * i)":
            model1 = Model(3)

        if self.c2.get() == "y(x) = beta * exp^(alpha * -i)":
            model1 = Model(4)

        if self.c2.get() == "Встроенный рандом":
            model1 = Model(5)

        if self.c2.get() == "Кастомный рандом":
            model1 = Model(6)

        if self.c2.get() == "Аномальные участки":
            model1 = Model(7)

        if self.c2.get() == "Значения за областью":
            model1 = Model(8)

        if self.c2.get() == "Адитивная модель №1":
            model1 = Model(9)

        if self.c2.get() == "Адитивная модель №2":
            model1 = Model(10)

        if self.c2.get() == "Мультипликативная модель №1":
            model1 = Model(11)

        if self.c2.get() == "Мультипликативная модель №2":
            model1 = Model(12)

        self.set_defual_values_for_model(model1)
        model1.calculation()
        model1.normalization()

        self.add_model(model1)
        self.main.draw_graph(model1, self.c1.get())

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
                                         u"Аномальные участки", u"Значения за областью", u"Адитивная модель №1",
                                        u"Адитивная модель №2", u"Мультипликативная модель №1", u"Мультипликативная модель №2"],
                               height=12)

        self.c2.place(x=10, y=80)

        ### Ввод k
        label2 = Label(self, text="k", height=1, width=1, font='Arial 14')
        label2.place(x=300, y=10)
        self.input_k = Entry(self, width=15)
        self.input_k.place(x=300, y=30)

        ### Ввод b
        label3 = Label(self, text="b", height=1, width=1, font='Arial 14')
        label3.place(x=300, y=60)
        self.input_b = Entry(self,width=15)
        self.input_b.place(x=300, y=80)

        ### Ввод alpha
        label4 = Label(self,text="alpha", height=1, width=5, font='Arial 14')
        label4.place(x=300, y=110)
        self.input_alpha = Entry(self,width=15)
        self.input_alpha.place(x=300, y=130)

        ### Ввод beta
        label5 = Label(self,text="beta", height=1, width=4, font='Arial 14')
        label5.place(x=300, y=160)
        self.input_beta = Entry(self,width=22)
        self.input_beta.place(x=300, y=180)

        ### Ввод N - Количество записей
        label6 = Label(self,text="Количество записей", height=1, width=17, font='Arial 14')
        label6.place(x=10, y=210)
        self.input_N = Entry(self,width=22)
        self.input_N.place(x=10, y=230)

        ### Ввод n - Начало промежутка
        label7 = Label(self,text="Начало промежутка", height=1, width=17, font='Arial 14')
        label7.place(x=10, y=260)
        self.input_n = Entry(self,width=22)
        self.input_n.place(x=10, y=280)

        ### Ввод m - Конец промежутка
        label8 = Label(self,text="Окончание промежутка", height=1, width=20, font='Arial 14')
        label8.place(x=10, y=310)
        self.input_m = Entry(self,width=22)
        self.input_m.place(x=10, y=330)

        ### Ввод -S - Минимальное значение функции
        label9 = Label(self,text="Минимальное значение ф-ии", height=1, width=24, font='Arial 14')
        label9.place(x=10, y=110)
        self.input_S_min = Entry(self,width=22)
        self.input_S_min.place(x=10, y=130)

        ### Ввод S - Максимальное значение функции
        label10 = Label(self,text="Максимальное значение ф-ии", height=1, width=25, font='Arial 14')
        label10.place(x=10, y=160)
        self.input_S_max = Entry(self,width=22)
        self.input_S_max.place(x=10, y=180)


        b1 = Button(self, text="Добавить", command=self.click_button_add_and_close, width="15", height="2")
        b1.place(x=300, y=350)
        b2= Button(self, text="Закрыть", command=self.click_button_close, width="15", height="2")
        b2.place(x=450, y=350)

        self.grab_set()       #Перехватывает все события происходящие в приложении
        self.focus_set()      #Захватывает и удерживает фокус



