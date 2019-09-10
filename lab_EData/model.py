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

        self.axis_y_min = -10
        self.axis_y_max = 10

        self.n = 100

        for i in range(self.n):
            self.x.append(i)

    def calculation(self):

        self.y[:] = []


        if(self.option == 1):

            for i in range(self.n):
                yn = self.k * i + self.b
                self.y.append(yn)

        if (self.option == 2):

            for i in range(self.n):
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

            for i in range(self.n):
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

            for i in range(self.n):
                try:
                    yn = random.uniform(self.axis_y_min, self.axis_y_max)
                    self.y.append(yn)
                except:
                    self.y.append(0)

            """
        
            for i in range(self.n):
                yn = self.beta * math.exp(self.alpha * -i)
                self.y.append(yn)
            """