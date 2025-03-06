# 3. Design any creative application from the exercises that have been taught to you in this lab. Such as POS systems for any Pharmacy, or any grocery store, or BBQ restaurant, or Pizza Hut or any application which you like.

from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

# Connect to the MySQL database
db = mysql.connect(
    host="localhost",
    user="root",
    password="password",  
    database="pizza_pos"
)
cursor = db.cursor()

# Create a function to add the order to the database
def add_order():
    try:
        customer_name = customer_entry.get()
        if not customer_name:
            messagebox.showerror("Error", "Customer name is required!")
            return
        
        total = float(total_label.cget("text").split("$")[1])
        cursor.execute("INSERT INTO orders (customer_name, total_amount) VALUES (%s, %s)", (customer_name, total))
        db.commit()
        
        messagebox.showinfo("Order Added", f"Order for {customer_name} added successfully!")
        customer_entry.delete(0, END)
        clear_order()
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# Function to calculate the total
def calculate_total():
    total = 0
    for item in menu_items:
        qty = int(order_vars[item[0]].get())
        total += qty * item[1]
    total_label.config(text=f"Total: ${total:.2f}")

# Function to clear the order
def clear_order():
    for item in menu_items:
        order_vars[item[0]].set(0)
    calculate_total()

def show_orders():
    global listbox1
    cursor.execute("SELECT * FROM orders")
    orders=cursor.fetchall()
    listbox1.delete(0,END)
    for i in orders:
        listbox1.insert(END,i)

# GUI Setup
root = Tk()
root.title("Pizza POS System")
root.geometry("500x500")
root.configure(bg="#2c3e50")

# Heading
Label(root, text="Pizza Hut POS", font="Helvetica 20 bold", bg="#2c3e50", fg="white").pack(pady=10)

# Customer Name
frame1 = Frame(root, bg="#2c3e50")
frame1.pack(pady=10)
Label(frame1, text="Customer Name:", font="Helvetica 14", bg="#2c3e50", fg="white").grid(row=0, column=0, padx=10)
customer_entry = Entry(frame1, font="Helvetica 14", width=20)
customer_entry.grid(row=0, column=1, padx=10)

# Menu Items
frame2 = Frame(root, bg="#34495e")
frame2.pack(pady=10)
Label(frame2, text="Menu", font="Helvetica 16 bold", bg="#34495e", fg="white").grid(row=0, column=0, columnspan=3, pady=10)

menu_items = [("Margherita", 10), ("Pepperoni", 12), ("Veggie", 9), ("BBQ Chicken", 14), ("Hawaiian", 13)]
order_vars = {}

for i, item in enumerate(menu_items):
    Label(frame2, text=item[0], font="Helvetica 12", bg="#34495e", fg="white").grid(row=i+1, column=0, pady=5, padx=10, sticky=W)
    Label(frame2, text=f"${item[1]:.2f}", font="Helvetica 12", bg="#34495e", fg="white").grid(row=i+1, column=1, pady=5, padx=10, sticky=W)
    var = IntVar(value=0)
    order_vars[item[0]] = var
    Spinbox(frame2, from_=0, to=10, width=5, textvariable=var, font="Helvetica 12", command=calculate_total).grid(row=i+1, column=2, pady=5, padx=10)

# Total and Buttons
frame3 = Frame(root, bg="#2c3e50")
frame3.place(relx=0.1,rely=0.1)
total_label = Label(frame3, text="Total: $0.00", font="Helvetica 14 bold", bg="#2c3e50", fg="white")
total_label.pack(pady=5)

listbox1=Listbox(root)
listbox1.pack()

Button(frame3, text="Add Order", font="Helvetica 14", bg="#1abc9c", fg="white", command=add_order).pack()
Button(frame3, text="Clear Order", font="Helvetica 14", bg="#e74c3c", fg="white", command=clear_order).pack()
Button(frame3, text="Show Orders", font="Helvetica 14", bg="#e74c3c", fg="white", command=show_orders).pack()


root.mainloop()
