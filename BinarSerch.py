import os
from tkinter import *
from tkinter import ttk
from tkinter.massagbox import askyesno
from tkinter.filedialog import askopenfilename

class main():
    def __init__(self):
        self.root = Tk()
        self.root.title('Бинарный поиск')
        self.frameSerchList = Frame(borderwidth = 2,    #Толщина граници фрейма
                                    relief = RAISED,    #Определяет тип граници (SUNKEN, REISED, GROOVE, RIDGE)
                                    cursor = 'clock'    #Вид курсора при навидении на фрейм
                                    height =            #Высата фрейма
                                    width =             #Ширина фрейма
                                    padding = [10]      #Отступы от границ фрейма (может быть от 1 до 4 значений [10, 20, 15, 20])
                                    )
        

if __name__==__main__:
    BinarSerch = main()