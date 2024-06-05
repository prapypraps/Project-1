import tkinter as tk
from tkinter import messagebox
from tkinter import *
import math

def new_file():
    new_window = tk.Toplevel(calci)
    new_window.title('storing data temporary')
    new_window.geometry(calci.geometry())  

    
    expression = ""
    equation = tk.StringVar()

    expression_field = tk.Entry(new_window, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
    expression_field.grid(row=0, column=0, columnspan=4)

def version():
    messagebox.showinfo('Version', 'Version is 2.12.3')

def ccare():
    messagebox.showinfo('Contact us', ' Email - basic_calci@froze.com')

def tutorial():
    messagebox.showinfo('Tutorials', 'Tutorials are presently not available')

def open():
    messagebox.showinfo('File error', 'No file found')


expression = ""

def press(key):
    global expression
    expression = expression + str(key)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def sqrt():
    try:
        global expression
        total = str(math.sqrt(float(expression)))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def power():
    global expression
    expression = expression + "**"
    equation.set(expression)

def square():
    try:
        global expression
        total = str(float(expression) ** 2)
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

calci = tk.Tk()
calci.configure(background="light grey")
calci.title("Basic Calculator")
calci.geometry("330x300")

menu_bar = tk.Menu(calci)
file_menu = tk.Menu(menu_bar, tearoff=0)

file_menu.add_command(label='Open', command=open)

file_menu.add_separator()
file_menu.add_command(label='Exit', command=calci.destroy)
menu_bar.add_cascade(label='File', menu=file_menu)

tools_menu = tk.Menu(menu_bar, tearoff=0)
tools_menu.add_command(label='Addition', command=lambda: press("+"))
tools_menu.add_command(label='Subtraction', command=lambda: press("-"))
tools_menu.add_command(label='Multiplication', command=lambda: press("*"))
tools_menu.add_command(label='Division', command=lambda: press("/"))
menu_bar.add_cascade(label='Tools', menu=tools_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label='Version', command=version)
help_menu.add_command(label='Tutorial', command=tutorial)
help_menu.add_command(label='Contact us', command=ccare)
menu_bar.add_cascade(label='Help', menu=help_menu)

calci.config(menu=menu_bar)

equation = tk.StringVar()
expression_field = tk.Entry(calci, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)

button1 = tk.Button(calci, text=' 1 ', fg='black', bg='light blue', command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = tk.Button(calci, text=' 2 ', fg='black', bg='light blue', command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = tk.Button(calci, text=' 3 ', fg='black', bg='light blue', command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = tk.Button(calci, text=' 4 ', fg='black', bg='light blue', command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)

button5 = tk.Button(calci, text=' 5 ', fg='black', bg='light blue', command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = tk.Button(calci, text=' 6 ', fg='black', bg='light blue', command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = tk.Button(calci, text=' 7 ', fg='black', bg='light blue', command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = tk.Button(calci, text=' 8 ', fg='black', bg='light blue', command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = tk.Button(calci, text=' 9 ', fg='black', bg='light blue', command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = tk.Button(calci, text=' 0 ', fg='black', bg='light blue', command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=1)

plus = tk.Button(calci, text=' + ', fg='black', bg='light blue', command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = tk.Button(calci, text=' - ', fg='black', bg='light blue', command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = tk.Button(calci, text=' * ', fg='black', bg='light blue', command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = tk.Button(calci, text=' / ', fg='black', bg='light blue', command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)

equal = tk.Button(calci, text=' = ', fg='black', bg='light blue', command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)

clear_button = tk.Button(calci, text='Clear', fg='black', bg='light blue', command=clear, height=1, width=7)
clear_button.grid(row=5, column=0)

Decimal = tk.Button(calci, text='.', fg='black', bg='light blue', command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=6, column=0)

sqrt_button = tk.Button(calci, text=' √ ', fg='black', bg='light blue', command=sqrt, height=1, width=7)
sqrt_button.grid(row=6, column=1)

power_button = tk.Button(calci, text=' ^ ', fg='black', bg='light blue', command=power, height=1, width=7)
power_button.grid(row=6, column=2)

square_button = tk.Button(calci, text=' x² ', fg='black', bg='light blue', command=square, height=1, width=7)
square_button.grid(row=6, column=3)

Advance_calci = tk.Button(calci, text='Advance Calculator', fg='black', bg='light blue', command=lambda: messagebox.showinfo('Advance Calculator', 'Please buy subscription to avail this feature'), height=1, width=30)
Advance_calci.grid(row=7, column=0, columnspan=4)

calci.mainloop()

