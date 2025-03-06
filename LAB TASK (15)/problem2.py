import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host='localhost', 
    user='root',      
    password='password', 
    database='SchoolDB' 
)
cursor = conn.cursor()

# Insert function for adding a new department
def insert_dept():
    try:
        # Get input data
        deptid = entry_deptid.get()
        dname = entry_dname.get()

        # SQL query to insert department into the database
        query = "INSERT INTO Dept (deptid, dname) VALUES (%s, %s)"
        cursor.execute(query, (deptid, dname))
        conn.commit()  # Commit the transaction
        messagebox.showinfo("Success", "Department record inserted successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Delete function for removing a department by ID
def delete_dept():
    try:
        # Get department ID to delete
        deptid = entry_deptid.get()

        # SQL query to delete department record by deptid
        query = "DELETE FROM Dept WHERE deptid = %s"
        cursor.execute(query, (deptid,))
        conn.commit()  # Commit the transaction
        messagebox.showinfo("Success", "Department record deleted successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Department Management System")

# Labels and Entry fields
tk.Label(root, text="Department ID:").grid(row=0, column=0)
entry_deptid = tk.Entry(root)
entry_deptid.grid(row=0, column=1)

tk.Label(root, text="Department Name:").grid(row=1, column=0)
entry_dname = tk.Entry(root)
entry_dname.grid(row=1, column=1)

# Buttons for Insert and Delete
btn_insert = tk.Button(root, text="Insert", command=insert_dept)
btn_insert.grid(row=2, column=0)

btn_delete = tk.Button(root, text="Delete", command=delete_dept)
btn_delete.grid(row=2, column=1)

# Start Tkinter event loop
root.mainloop()

# Close MySQL connection when done
cursor.close()
conn.close()
