import math
import random
import time

class Model():
    def __init__(self, option):
        self.k = 5
        self.b = 10
        self.beta = 2
        self.alpha = 0.5
        self.y = []

        self.option = option #Тип функции

        self.x = []

        self.axis_y_graph_min = -100    #Минимальное значение функции
        self.axis_y_graf_max = 100      #Максимальное значение функции
        self.axis_y_delta = 10         #Небходимо для самого графика, например: у_min = -(delta + self.axis_y_graf_max)

        self.N = 100    #Количество точек по оси Х
        self.n = 10     #Начало аномального отрезка
        self.m = 40     #Окончание аномального отрезка
        self.argument = 10  #Константа на сколько поднять/опустить точки на аномальном участке

        self.all_average_value = []   #Средние значения

        for i in range(self.N):
            self.x.append(i)


    def check_stationarity(self):

        number_of_gaps = 10 #Количество промежутков

        gap_length = int(self.N / number_of_gaps)      #Длина промежутка

        average_value = 0

        delta_min_max = (- self.axis_y_graph_min + self.axis_y_graf_max) * 0.05

        for i in range(self.N):
            average_value = average_value + self.y[i]
            if i % gap_length == 0:
                average_value = average_value / gap_length
                self.all_average_value.append(average_value)
                average_value = 0

        flag_stationarity = True
        for i in range(self.all_average_value.__len__() - 1):
            if self.all_average_value[i] - self.all_average_value[i+1] > delta_min_max:
                flag_stationarity = False

        print(self.all_average_value)

        return flag_stationarity


    def calculation(self):

        self.y[:] = []

        if(self.option == 1):
            for i in range(self.N):
                if (i >= self.n) and (i <= self.m):
                    try:
                        yn = random.uniform(self.axis_y_graph_min + self.argument, self.axis_y_graf_max + self.argument)
                        self.y.append(yn)
                    except:
                        self.y.append(0)
                else:
                    try:
                        yn = random.uniform(self.axis_y_graph_min, self.axis_y_graf_max)
                        self.y.append(yn)
                    except:
                        self.y.append(0)

            """
            for i in range(self.N):
                yn = self.k * i + self.b
                self.y.append(yn)
            """
                


        if (self.option == 2):

            for i in range(self.N):
                try:
                    temp_string_time = str(time.time())
                    reverse_temp_string_time = temp_string_time[::-1]
                    new_value = int(reverse_temp_string_time[0])

                    temp_string_time_for_even = str(time.time())
                    reverse_temp_string_time_for_even = temp_string_time_for_even[::-1]
                    new_value_for_even = int(reverse_temp_string_time_for_even[0])
                    new_value_for_even = new_value_for_even % 2

                    new_value_choice = new_value

                    if new_value_choice == 5:
                        temp_string_time_spikes = str(time.time())
                        reverse_temp_string_time_spikes = temp_string_time_spikes[::-1]
                        new_value = int(reverse_temp_string_time_spikes[0])
                    else:
                        new_value = 0

                    if new_value_for_even == 1:
                        new_value = - new_value

                    print(new_value)
                    self.y.append(new_value)

                except:
                    self.y.append(0)

            """
            Здесь был график kx+b
            
            for i in range(self.n):
                yn = -self.k * i + self.b
                self.y.append(yn)
                
            """

        if (self.option == 3):

            for i in range(self.N):
                try:
                    temp_string_time = str(time.time())
                    reverse_temp_string_time = temp_string_time[::-1]
                    new_value = float(reverse_temp_string_time[0])
                    new_value = new_value / 10
                    #print(new_value)

                    temp_string_time_for_even = str(time.time())
                    reverse_temp_string_time_for_even = temp_string_time_for_even[::-1]
                    new_value_for_even = int(reverse_temp_string_time_for_even[0])
                    new_value_for_even = new_value_for_even % 2

                    if new_value_for_even == 1:
                        new_value = - new_value

                    print(new_value)
                    self.y.append(new_value)

                except:
                    self.y.append(0)

            """
            
            Здесь рабочий встроенный рандом
            
            
            for i in range(self.n):
                try:
                    yn = random.uniform(self.axis_y_min,self.axis_y_max)
                    self.y.append(yn)
                except:
                    self.y.append(0)
                    
                    
            """

            '''
            
            Здесь рабочая экспонента
            
            for i in range(self.n):
                try:
                    yn = self.beta * math.exp((self.alpha * i))
                    #yn = 2 * math.exp(i)
                    self.y.append(yn)
                except:
                    self.y.append(0)
            '''

        if (self.option == 4):

            for i in range(self.N):
                try:
                    yn = random.uniform(self.axis_y_graph_min, self.axis_y_graf_max)
                    self.y.append(yn)
                except:
                    self.y.append(0)

            """
        
            for i in range(self.n):
                yn = self.beta * math.exp(self.alpha * -i)
                self.y.append(yn)
            """