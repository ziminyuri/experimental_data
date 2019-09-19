from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from model import *
from tkinter import messagebox
from ChildWindow import *

class Display(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main_window()

        self.root = root
        self.root.title("Лабораторная №1 / Методы обработки эксперементальных данных")
        self.root.geometry('1400x820')

        self.check_k = IntVar()
        self.check_b = IntVar()
        self.check_alpha = IntVar()
        self.check_beta = IntVar()
        self.check_N = IntVar()
        self.check_n = IntVar()
        self.check_m = IntVar()
        self.check_s_min = IntVar()
        self.check_s_max = IntVar()

        self.initUI()

    def init_main_window(self):
        ChildWindow()

    def draw_graph(self, model):

        if model.option == 1:

            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.N])
            ax.set_ylim([model.axis_y_graph_min - model.argument, model.axis_y_graf_max + model.argument])
            ax.plot(model.x, model.y, color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=10)

            """
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, 100])
            ax.set_ylim([0, 100])
            ax.plot(model.x, model.y, color='red', label='Линия 1')

            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=10)
            
            """

        if model.option == 2:

            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.N])
            ax.set_ylim([model.axis_y_graph_min - model.argument, model.axis_y_graf_max + model.argument])
            ax.plot(model.x, model.y, color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=550, y=10)

            """
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, 100])
            ax.set_ylim([0, 100])
            ax.plot(model.x, model.y, color='red', label='Линия 1')

            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=550, y=10)
            """


        if model.option == 3:
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.N])
            ax.set_ylim([model.axis_y_graph_min - model.argument, model.axis_y_graf_max + model.argument])
            ax.plot(model.x, model.y, color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=400)

            """
            
            Здесь рабочая гипербола
            
            
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            #ax.set_xlim([0, 10])
            #ax.set_ylim([0, 100])
            ax.plot(model.x, model.y, color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=400)
            """


        if model.option == 4:

            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([0, model.N])
            ax.set_ylim([model.axis_y_graph_min - model.argument, model.axis_y_graf_max + model.argument])
            ax.plot(model.x, model.y, color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=550, y=400)

            """
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.set_xlim([-10, 10])
            ax.set_ylim([0, 100])
            ax.plot(model.x, model.y, color='red', label='Линия 1')
            canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=550, y=400)
            """


    def update_UI(self, models):
        print("альфа")

        for obj in models:

            obj.k = float(self.k.get())
            obj.b = float(self.b.get())
            obj.beta = float(self.beta.get())
            obj.alpha = float(self.alpha.get())
            obj.calculation()
            self.draw_graph(obj)

    #Нажатие на клавишу проверка на стационарность
    def click_button_stationarity(self, models):

        for obj in models:
            flag_stationarity_UI = obj.check_stationarity()

            message = ""

            j = 1
            for i in obj.all_average_value:
                message = message + "Среднее значение №:" + str(j)+ " = " + str(i) + "\n"
                j = j+ 1


            if flag_stationarity_UI == True:
                messagebox.showinfo("Проверка на стационарность", message + "\nГрафик №:"+ str(obj.option) +" стационарен")

            else:
                messagebox.showinfo("Проверка на стационарность", "График №:"+ str(obj.option) +" не стационарен")

    def click_button_add(self):
        a = Toplevel()
        a.geometry('200x150')
        a['bg'] = 'grey'
        a.overrideredirect(True)
        Label(a, text="About this").pack(expand=1)
        a.after(5000, lambda: a.destroy())

    def initUI(self):
        canvas = Canvas(self.root)
        array_models = []



        model1 = Model(1)
        array_models.append(model1)
        model1.calculation()
        self.draw_graph(model1)
        """
        model2 = Model(2)
        array_models.append(model2)
        model2.calculation()
        self.draw_graph(model2)


        model3 = Model(3)
        array_models.append(model3)
        model3.calculation()
        self.draw_graph(model3)


        model4 = Model(4)
        array_models.append(model4)
        model4.calculation()
        self.draw_graph(model4)

        """


        label1 = Label(text="Коэффициенты для графиков", height=1, width=29, font='Arial 14')
        label1.place(x=1100, y=50)

        ###Ввод к
        label2 = Label(text="k", height=1, width=1, font='Arial 14')
        label2.place(x=1018, y=90)
        input_k = Entry(width=10)
        input_k.place(x=1260, y=85)
        self.k = input_k

        check_k_button = Checkbutton(variable=self.check_k, onvalue=1, offvalue=0)
        check_k_button.place(x=1367, y=89)

        ### Ввод b
        label3 = Label(text="b", height=1, width=1, font='Arial 14')
        label3.place(x=1018, y=120)
        input_b = Entry(width=10)
        input_b.place(x=1260, y=115)
        self.b = input_b

        check_b_button = Checkbutton(variable=self.check_b, onvalue=1, offvalue=0)
        check_b_button.place(x=1367, y=119)

        ### Ввод alpha
        label4 = Label(text="alpha", height=1, width=5, font='Arial 14')
        label4.place(x=1018, y=150)
        input_alpha = Entry(width=10)
        input_alpha.place(x=1260, y=145)
        self.alpha = input_alpha

        check_alpha_button = Checkbutton(variable=self.check_alpha, onvalue=1, offvalue=0)
        check_alpha_button.place(x=1367, y=149)

        ### Ввод beta
        label5 = Label(text="beta", height=1, width=4, font='Arial 14')
        label5.place(x=1018, y=180)
        input_beta = Entry(width=10)
        input_beta.place(x=1260, y=175)
        self.beta = input_beta

        check_beta_button = Checkbutton(variable=self.check_beta, onvalue=1, offvalue=0)
        check_beta_button.place(x=1367, y=179)

        ### Ввод N - Количество записей
        label6 = Label(text="Количество записей", height=1, width=17, font='Arial 14')
        label6.place(x=1018, y=210)
        input_N = Entry(width=10)
        input_N.place(x=1260, y=205)
        self.N = input_N


        check_N_button = Checkbutton(variable=self.check_N, onvalue=1, offvalue=0)
        check_N_button.place(x=1367, y=209)

        ### Ввод n - Начало промежутка
        label7 = Label(text="Начало промежутка", height=1, width=17, font='Arial 14')
        label7.place(x=1018, y=240)
        input_n = Entry(width=10)
        input_n.place(x=1260, y=235)
        self.n = input_n


        check_n_button = Checkbutton(variable=self.check_n, onvalue=1, offvalue=0)
        check_n_button.place(x=1367, y=239)

        ### Ввод m - Конец промежутка
        label8 = Label(text="Окончание промежутка", height=1, width=20, font='Arial 14')
        label8.place(x=1018, y=270)
        input_m = Entry(width=10)
        input_m.place(x=1260, y=265)
        self.m = input_m


        check_m_button = Checkbutton(variable=self.check_m, onvalue=1, offvalue=0)
        check_m_button.place(x=1367, y=269)

        ### Ввод -S - Минимальное значение функции
        label9 = Label(text="Минимальное значение функции", height=1, width=28, font='Arial 14')
        label9.place(x=1018, y=300)
        input_S_min = Entry(width=10)
        input_S_min.place(x=1260, y=295)
        self.axis_y_graph_min = input_S_min

        check_s_min_button = Checkbutton(variable=self.check_s_min, onvalue=1, offvalue=0)
        check_s_min_button.place(x=1367, y=299)

        ### Ввод S - Максимальное значение функции
        label10 = Label(text="Максимальное значение функции", height=1, width=29, font='Arial 14')
        label10.place(x=1018, y=330)
        input_S_max = Entry(width=10)
        input_S_max.place(x=1260, y=325)
        self.axis_y_graph_max = input_S_max


        check_s_max_button = Checkbutton(variable=self.check_s_max, onvalue=1, offvalue=0)
        check_s_max_button.place(x=1367, y=329)

        ### Ввод label's с названием функция
        #label6 = Label(text="x(t) = k(x)+ b", height=1, width=15, font='Arial 18')
        label6 = Label(text="График №1", height=1, width=15, font='Arial 18')
        label6.place(x=55, y=15)

        #label7 = Label(text="x(t) = -k(x)+ b", height=1, width=15, font='Arial 18')
        label7 = Label(text="График №2", height=1, width=15, font='Arial 18')
        label7.place(x=600, y=15)

        #label8 = Label(text="x(t) = beta * E^(alpha * x)", height=1, width=25, font='Arial 18')
        label8 = Label(text="График №3", height=1, width=25, font='Arial 18')
        label8.place(x=40, y=410)

        #label9 = Label(text="x(t) = beta * E^(-alpha * x)", height=1, width=25, font='Arial 18')
        label9 = Label(text="График №4", height=1, width=25, font='Arial 18')
        label9.place(x=580, y=410)

        b1 = Button(text="Обновить графики", command=lambda: self.update_UI(array_models), width="26", height="2")
        b1.place(x=1120, y=370)

        b2 = Button(text="Проверить на стационарность", command=lambda: self.click_button_stationarity(array_models), width="26", height="2")
        b2.place(x=1120, y=410)

        b2 = Button(text="Добавить", command=lambda: self.click_button_add,width="26", height="2")
        b2.place(x=1120, y=450)

