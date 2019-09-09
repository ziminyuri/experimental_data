import math

class Model():
    def __init__(self, option):
        self.k = 5
        self.b = 10
        self.beta = 15
        self.alpha = 20
        self.y = []
        self.option = option

        self.x = []
        for i in range(1000):
            self.x.append(i)

    def calculation(self):
        if(self.option == 1):
            x_max = 1000

            for i in range(x_max):
                yn = self.k * i + self.b
                self.y.append(yn)

        if (self.option == 2):
            x_max = 1000

            for i in range(x_max):
                yn = -self.k * i + self.b
                self.y.append(yn)

        if (self.option == 3):   ### Проблемы с экспонентой
            x_max = 1000

            for i in range(x_max):
                try:
                    #yn = self.beta * math.exp((self.alpha * i))
                    yn = math.exp(i)
                    self.y.append(yn)
                except:
                    self.y.append(0)

        if (self.option == 4):
            x_max = 1000

            for i in range(x_max):
                yn = self.beta * math.exp(self.alpha * -i)
                self.y.append(yn)


    def calculation1(self):
        if(self.option == 1):
            x_max = 1000

            for i in range(x_max):
                yn = self.k * i + self.b
                self.y.append(yn)

        if (self.option == 2):
            x_max = 1000

            for i in range(x_max):
                yn = -self.k * i + self.b
                self.y.append(yn)

        if (self.option == 3):   ### Проблемы с экспонентой
            x_max = 1000

            for i in range(x_max):
                try:
                    #yn = self.beta * math.exp((self.alpha * i))
                    yn = math.exp(i)
                    self.y.append(yn)
                except:
                    self.y.append(0)

        if (self.option == 4):
            x_max = 1000

            for i in range(x_max):
                yn = self.beta * math.exp(self.alpha * -i)
                self.y.append(yn)
