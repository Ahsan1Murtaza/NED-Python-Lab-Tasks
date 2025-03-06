from tkinter import *
import math
import tkinter.messagebox as tmsg

root = Tk()
root.title("Scientific Calculator - Ahsan")
root.geometry("500x550")

def but(val):
    current = e1.get()
    e1.delete(0, END)
    e1.insert(0, current + str(val))

def equal():
    try:
        result = eval(e1.get())
        e1.delete(0, END)
        e1.insert(0, result)
    except Exception as e:
        tmsg.showerror("Error", "Invalid Input")

def clear():
    e1.delete(0, END)

# Function to perform scientific operations
def sci_func(func):
    try:
        current = float(e1.get())
        e1.delete(0, END)
        if func == "sqrt":
            result = math.sqrt(current)
        elif func == "log":
            result = math.log10(current)
        elif func == "ln":
            result = math.log(current)
        elif func == "sin":
            result = math.sin(math.radians(current))
        elif func == "cos":
            result = math.cos(math.radians(current))
        elif func == "tan":
            result = math.tan(math.radians(current))
        e1.insert(0, result)
    except Exception as e:
        tmsg.showerror("Error", "Invalid Input")

e1 = Entry(root, font="helvetica 30 bold")
e1.grid(row=0, column=0, columnspan=5, pady=10)

# Numeric buttons
b7 = Button(root, text="7",padx=40,pady=30,command=lambda : but(7))
b8 = Button(root, text="8",padx=40,pady=30,command=lambda : but(8))
b9 = Button(root, text="9",padx=40,pady=30,command=lambda : but(9))

b4 = Button(root, text="4",padx=40,pady=30,command=lambda : but(4))
b5 = Button(root, text="5",padx=40,pady=30,command=lambda : but(5))
b6 = Button(root, text="6",padx=40,pady=30,command=lambda : but(6))

b1 = Button(root, text="1",padx=40,pady=30,command=lambda : but(1))
b2 = Button(root, text="2",padx=40,pady=30,command=lambda : but(2))
b3 = Button(root, text="3",padx=40,pady=30,command=lambda : but(3))

b0 = Button(root, text="0",padx=40,pady=30,command=lambda : but(0))
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b0.grid(row=4,column=0)

# Basic operation buttons
Button(root, text="+", padx=30, pady=20, command=lambda: but("+")).grid(row=1, column=3)
Button(root, text="-", padx=31, pady=20, command=lambda: but("-")).grid(row=2, column=3)
Button(root, text="*", padx=30, pady=20, command=lambda: but("*")).grid(row=3, column=3)
Button(root, text="/", padx=30, pady=20, command=lambda: but("/")).grid(row=4, column=3)

# Additional operation buttons
Button(root, text="=", padx=30, pady=20, command=equal).grid(row=4, column=2)
Button(root, text="CLS", padx=24, pady=20, command=clear).grid(row=4, column=1)

# Scientific function buttons
Button(root, text="sqrt", padx=20, pady=20, command=lambda: sci_func("sqrt")).grid(row=1, column=4)
Button(root, text="log", padx=20, pady=20, command=lambda: sci_func("log")).grid(row=2, column=4)
Button(root, text="ln", padx=22, pady=20, command=lambda: sci_func("ln")).grid(row=3, column=4)
Button(root, text="sin", padx=20, pady=20, command=lambda: sci_func("sin")).grid(row=1, column=5)
Button(root, text="cos", padx=18, pady=20, command=lambda: sci_func("cos")).grid(row=2, column=5)
Button(root, text="tan", padx=18, pady=20, command=lambda: sci_func("tan")).grid(row=3, column=5)

def help_():
    tmsg.showinfo("HELP", "Ahsan will help you with this scientific calculator!")

mainmenu = Menu(root)
helps = Menu(mainmenu, tearoff=0)
helps.add_command(label="Help", command=help_)
mainmenu.add_cascade(label="Help", menu=helps)
root.config(menu=mainmenu)

root.mainloop()
