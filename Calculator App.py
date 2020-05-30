from tkinter import *

root = Tk()
root.title("Homemade Calculator")
root.iconbitmap("Images/calculator .ico")

e = Entry(root, width=90, borderwidth=5, bg="black", fg="white")
e.grid(row=0, column=0, columnspan=9, padx=10, pady=10)

# Section A
# Button methods that are not math related, but involve the general input of the user

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

    # This allows user to input data from button icons


def button_C():
    e.delete(0, END)

    # This clears everything in the entry slot


def button_CE():
    first_number = e.get()
    global f_num
    global math
    math = "delete"
    f_num = float(first_number)
    e.delete(0, 1)

    # This clears an individual entity (CE is short for clear entity)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

# Section B
# These are 'if statements' which allow the math methods to operate

    if math == "addition":
        e.insert(0, f_num + float(second_number))

    # I created a variable called "math" and set it equal to "addition"
    # If the user selects "addition" then add the first number with the second number

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    # I created a variable called "math" and set it equal "subtraction"
    # If the user selects "subtraction" then make the difference between the first and second numbers

    if math == "multiplication":
        e.insert(0, f_num * float(second_number))

    # I created a variable called "math" and set it equal "multiplication"
    # If the user selects "multiplication" then multiply the first and second numbers

    if math == "division":
        e.insert(0, f_num / float(second_number))

    # I created a variable called "math" and set it equal "division"
    # If the user selects "division" then divide the first and second numbers

    if math == "cubed":
        e.insert(0, f_num * f_num * f_num)

    # I created a variable called "math" and set it equal "cubed"
    # If the user selects "cubed" then cube the number that the user inputs

    if math == "squared":
        e.insert(0, f_num * f_num)

    # I created a variable called "math" and set it equal "squared"
    # If the user selects "squared" then square the number that the user inputs

    if math == "modulus":
        e.insert(0, f_num % float(second_number))

    # I created a variable called "math" and set it equal "modulus"
    # If the user selects "modulus" then take the remainder of the divided first and second numbers

    if math == "1/x":
        e.insert(0, 1 / f_num)

    # I created a variable called "math" and set it equal "1/x"
    # If the user selects "1/x" then take 1 and divide it by the number the user inputs

    if math == "sqrt()":
        e.insert(0, f_num ** (1 / 2.0))

    # I created a variable called "math" and set it equal "sqrt()"
    # If the user selects "sqrt()" then the number the user inputs is raised to the 1/2 power

    if math == "crt()":
        e.insert(0, f_num ** (1 / 3.0))

    # I created a variable called "math" and set it equal "crt()"
    # If the user selects "crt()" then the number the user inputs is raised to the 1/3 power

    if math == "()":
        e.insert(0, (f_num))

    # I created a variable called "math" and set it equal "()"
    # If the user selects "()" then the number the user inputs is converted from an int to a float


# Section C
# These are mathematical related methods

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

    # This is the "button_add" method
    # "first_number = e.get()" is the number the user inputs the first time
    # f_num = first number
    # math is the math variable
    # "e.delete(0, END)" deletes f_num to either replace it with an operator before the second number or the resultant


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

    # This is the "button_subtract" method
    # "first_number = e.get()" is the number the user inputs the first time
    # f_num = first number
    # math is the math variable
    # "e.delete(0, END)" deletes f_num to either replace it with an operator before the second number or the resultant


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

    # This is the "button_multiply" method
    # "first_number = e.get()" is the number the user inputs the first time
    # f_num = first number
    # math is the math variable
    # "e.delete(0, END)" deletes f_num to either replace it with an operator before the second number or the resultant


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

    # This is the "button_divide" method
    # "first_number = e.get()" is the number the user inputs the first time
    # f_num = first number
    # math is the math variable
    # "e.delete(0, END)" deletes f_num to either replace it with an operator before the second number or the resultant


def button_cubed():
    first_number = e.get()
    global f_num
    global math
    math = "cubed"
    f_num = float(first_number)
    e.delete(0, END)

    # This is the "button_cubed" method
    # "first_number = e.get()" is the number the user inputs the first time
    # f_num = first number
    # math is the math variable
    # "e.delete(0, END)" deletes f_num to either replace it with an operator before the second number or the resultant


def button_square():
    first_number = e.get()
    global f_num
    global math
    math = "squared"
    f_num = float(first_number)
    e.delete(0, END)

    # This is the "button_square" method
    # "first_number = e.get()" is the number the user inputs the first time
    # f_num = first number
    # math is the math variable
    # "e.delete(0, END)" deletes f_num to either replace it with an operator before the second number or the resultant


def button_mod():
    first_numer = e.get()
    global f_num
    global math
    math = "modulus"
    f_num = float(first_numer)
    e.delete(0, END)

    # This is the "button_mod" method
    # "first_number = e.get()" is the number the user inputs the first time
    # f_num = first number
    # math is the math variable
    # "e.delete(0, END)" deletes f_num to either replace it with an operator before the second number or the resultant


def button_sd():
    first_number = e.get()
    global f_num
    global math
    math = "1/x"
    f_num = float(first_number)
    e.delete(0, END)

    # This is the "button_sd" method == set division because numerator remains constant
    # "first_number = e.get()" is the number the user inputs the first time
    # f_num = first number
    # math is the math variable
    # "e.delete(0, END)" deletes f_num to either replace it with an operator before the second number or the resultant


def button_sr():
    first_number = e.get()
    global f_num
    global math
    math = "sqrt()"
    f_num = float(first_number)
    e.delete(0, END)

    # This is the "button_sr" method == square root
    # "first_number = e.get()" is the number the user inputs the first time
    # f_num = first number
    # math is the math variable
    # "e.delete(0, END)" deletes f_num to either replace it with an operator before the second number or the resultant


def button_cr():
    first_number = e.get()
    global f_num
    global math
    math = "crt()"
    f_num = float(first_number)
    e.delete(0, END)

    # This is the "button_cr" method == cube root
    # "first_number = e.get()" is the number the user inputs the first time
    # f_num = first number
    # math is the math variable
    # "e.delete(0, END)" deletes f_num to either replace it with an operator before the second number or the resultant


def button_q():
    first_number = e.get()
    global f_num
    global math
    math = "()"
    f_num = float(first_number)
    e.delete(0, END)

    # This is the "button_q" method == quantity converting to float
    # "first_number = e.get()" is the number the user inputs the first time
    # f_num = first number
    # math is the math variable
    # "e.delete(0, END)" deletes f_num to either replace it with an operator before the second number or the resultant

# Section D
# How the buttons are defined
# Section D.1
# These are the integer buttons going from 0 to 9

button_1 = Button(root, text="1", padx=54, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=56, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=48, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=48, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=48, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=48, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=48, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=55, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=56, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=48, pady=20, command=lambda: button_click(0))

# Section D.2
# As I like to call them, these are the logistic integer buttons
# They control if it is a decimal or a negative integer

button_dot = Button(root, text=".", padx=47, pady=20, command=lambda: button_click("."))
button_n = Button(root, text="-/+", padx=32, pady=20, command=lambda: button_click("-"))

# Section D.3
# These are the real logistic buttons
# (the ones with associated icons
# (explaining why click is not here(click is not an icon, it is how the user inputs data intp the entry slot)))

button_equal = Button(root, text="=", padx=92, pady=20, command=button_equal)
button_CE = Button(root, text="CE", padx=44, pady=20, command=button_CE)
button_C = Button(root, text="C", padx=46, pady=20, command=button_C)

# Section D.4
# These are the operator icons

button_subtract = Button(root, text="-", padx=48, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=48, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=39, pady=20, command=button_divide)
button_add = Button(root, text="+", padx=48, pady=20, command=button_add)

button_cubed = Button(root, text="x^3", padx=40, pady=20, command=button_cubed)
button_square = Button(root, text="x^2", padx=40, pady=20, command=button_square)
button_mod = Button(root, text="%", padx=48, pady=20, command=button_mod)
button_sd = Button(root, text="1/x", padx=42, pady=20, command=button_sd)

button_sr = Button(root, text="sqrt( x )", padx=40, pady=20, command=button_sr)
button_cr = Button(root, text="crt( x )", padx=40, pady=20, command=button_cr)
button_q = Button(root, text="( x )", padx=40, pady=20, command=button_q)

# Section E
# This is where the and how the buttons are made into icons and placed on the GUI grid

button_1.grid(row=2, column=4)
button_2.grid(row=2, column=3)
button_3.grid(row=2, column=2)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=0)
button_6.grid(row=1, column=6)

button_7.grid(row=1, column=5)
button_8.grid(row=1, column=4)
button_9.grid(row=1, column=3)
button_0.grid(row=1, column=2)

button_dot.grid(row=1, column=7)
button_n.grid(row=1, column=8)
button_q.grid(row=3, column=6)

button_C.grid(row=1, column=1)
button_CE.grid(row=1, column=0)
button_equal.grid(row=3, column=7, columnspan=2)

button_subtract.grid(row=2, column=6)
button_multiply.grid(row=2, column=7)
button_divide.grid(row=2, column=8)
button_add.grid(row=2, column=5)

button_cubed.grid(row=3, column=2)
button_square.grid(row=3, column=1)
button_mod.grid(row=3, column=5)

button_sd.grid(row=3, column=0)
button_sr.grid(row=3, column=3)
button_cr.grid(row=3, column=4)

root.mainloop()
