from tkinter import *
from tkinter import ttk
import math



#Calculator class
class Calculator:

    default_value = 0.0

    #Variables for the math operations of the calculator
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False





    def __init__(self, root):

        self.entry_value = StringVar(root, value ="")

        root.title("Calculat0r")

        root.geometry("650x650")

        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton",
                        font="Arial",
                        padding = 10)

        style.configure("TEntry",
                        font="Arial",
                        padding=10)

        style.number_entry = ttk.Entry(root,
                        textvariable=self.entry_value, width =50)

        style.number_entry.grid(row = 0, columnspan = 5)

        #~~~~~~~~~~~~~~~First Row~~~~~~~~~~~~~


        self.button7 = ttk.Button(root, text="7",
             command = lambda: self.button_press('7')).grid(row=1, column=0)

        self.button8 = ttk.Button(root, text="8",
             command=lambda: self.button_press('8')).grid(row=1, column=1)

        self.button9 = ttk.Button(root, text="9",
             command=lambda: self.button_press('9')).grid(row=1, column=2)

        #Need to incrase font of division sign here

        self.button_div = ttk.Button(root, text = "\u00F7",
             command = lambda: self.math_button_press('/')).grid(row =1, column =3)

        self.button_clear = ttk.Button(root, text ='\u2190',
             command = lambda: self.clear_button_press()).grid(row = 1, column =4)




#~~~~~~~~~~~~~~~Second Row~~~~~~~~~~~~~


        self.button7 = ttk.Button(root, text="4",
             command = lambda: self.button_press('4')).grid(row=2, column=0)

        self.button8 = ttk.Button(root, text="5",
             command=lambda: self.button_press('5')).grid(row=2, column=1)

        self.button9 = ttk.Button(root, text="6",
             command=lambda: self.button_press('6')).grid(row=2, column=2)

        #Need to incrase font of multiplication sign here

        self.button_mult = ttk.Button(root, text = "\u00D7",
             command = lambda: self.math_button_press('*')).grid(row =2, column =3)

        # Need to pass command of math.sqrt(input()) for math_button_press

        self.button_root = ttk.Button(root, text="\u221A",
             command=lambda: self.math_button_press('/')).grid(row=2, column=4)


#~~~~~~~~~~~~~~~Third Row~~~~~~~~~~~~~


        self.button7 = ttk.Button(root, text="1",
             command = lambda: self.button_press('1')).grid(row=3, column=0)

        self.button8 = ttk.Button(root, text="2",
             command=lambda: self.button_press('2')).grid(row=3, column=1)

        self.button9 = ttk.Button(root, text="3",
             command=lambda: self.button_press('3')).grid(row=3, column=2)

        #Need to incrase font of addition sign here

        self.button_add = ttk.Button(root, text = "\u002B",
             command = lambda: self.math_button_press('+')).grid(row =3, column =3)

        self.button_exp = ttk.Button(root, text="^",
              command=lambda: self.math_button_press('**')).grid(row=3, column=4)

        #~~~~~~~~~~~~~~~Fourth Row~~~~~~~~~~~~~

        #Using the ipadx command to circumvent resizing the grid geometry to properly size the box as intended
        self.button0 = ttk.Button(root, text="0",
             command=lambda: self.button_press('0')).grid(row=4, columnspan= 2,  ipadx = 65)

        self.button_divPeriod = ttk.Button(root, text=".",
             command=lambda: self.button_press('.')).grid(row=4, column=2)


        self.button_Sub = ttk.Button(root, text="-",
             command=lambda: self.math_button_press('-')).grid(row=4, column=3)

        self.button_eq = ttk.Button(root, text = "=",
             command = lambda: self.equal_button_press('=')).grid(row = 4, column = 4)





root = Tk()

calc = Calculator(root)

root.mainloop()

