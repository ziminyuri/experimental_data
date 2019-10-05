from tkinter import *
import tkinter.ttk as tt2
from model import *
from tkinter import messagebox

class OddsCalculationWindow(Toplevel):
    def __init__(self, main_window, root, graph_array):
        super().__init__(root)
        self.root = root
        self.graph_array = graph_array

        self.main = main_window
        self.init_odds_calculation_window()

    def init_odds_calculation_window(self):
        self.title('Добавить новый график')
        self.geometry('600x400')
        self.resizable(False, False)  # Нельзя изменить размер окна

        label1 = Label(text="Номер графика", height=1, width=14, font='Arial 14')
        label1.place(x=10, y=10)
        self.c1 = tt2.Combobox(values=[u"1", u"2", u"3", u"4"], height=4, width="24")
        self.c1.place(x=10, y=180)

        self._b3 = Button(self, text="Стационарность: СЗ", command=self.check_stationarity_click_button, width="26",
                          height="2",
                          state=DISABLED)
        self._b3.place(x=10, y=220)

        self._b4 = Button(text="Среднее значение", command=self.average_value_click_button, width="26", height="2",
                          state=DISABLED)
        self._b4.place(x=10, y=270)

        self._b5 = Button(text="Дисперсия", command=self.dispersion_click_button, width="26", height="2",
                          state=DISABLED)
        self._b5.place(x=10, y=320)

        self._b6 = Button(text="Дисперсия x10", command=self.dispersion_x_10_click_button, width="26",
                          height="2", state=DISABLED)
        self._b6.place(x=10, y=370)

        self._b7 = Button(text="Стандартное отклоение", command=self.standard_deviation, width="26",
                          height="2", state=DISABLED)
        self._b7.place(x=10, y=420)

        self._button_asymmetry = Button(text="Асимметрия", command=self.asymmetry_click_button, width="26", height="2",
                                        state=DISABLED)
        self._button_asymmetry.place(x=10, y=470)

        self._button_asymmetry_coefficient = Button(text="Коэффициент асимметрии",
                                                    command=self.asymmetry_coefficient_click_button,
                                                    width="26", height="2", state=DISABLED)
        self._button_asymmetry_coefficient.place(x=10, y=520)

        self._button_excess = Button(text="Эксцесс", command=self.excess_click_button, width="26", height="2",
                                     state=DISABLED)
        self._button_excess.place(x=10, y=570)

        self._button_kurtosis = Button(text="Куртозис", command=self.kurtosis_click_button, width="26", height="2",
                                       state=DISABLED)
        self._button_kurtosis.place(x=10, y=620)

        self._standard_ratio = Button(text="Стандартный коэфифциент", command=self.kurtosis_click_button,
                                      width="26", height="2", state=DISABLED)
        self._standard_ratio.place(x=10, y=670)

        self._standard_error = Button(text="Среднеквадратичная ошибка", command=self.kurtosis_click_button, width="26",
                                      height="2", state=DISABLED)
        self._standard_error.place(x=10, y=720)

        self._mean_absolute_deviation = Button(text="Среднее абсолютное отклонение",
                                               command=self.kurtosis_click_button, width="26", height="2",
                                               state=DISABLED)
        self._mean_absolute_deviation.place(x=10, y=770)

        self._x_min = Button(text="Минимальный Х", command=self.kurtosis_click_button, width="26",
                             height="2", state=DISABLED)
        self._x_min.place(x=10, y=820)

        self.grab_set()  # Перехватывает все события происходящие в приложении
        self.focus_set()  # Захватывает и удерживает фокус

