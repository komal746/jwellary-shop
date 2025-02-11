import mysql.connector
import tkinter as tk
from tkinter import messagebox
from homepage import *
from PIL import Image,ImageTk
# Function to execute the query and display the result
def execute_query():
    
    
     try:
        connection = mysql.connector.connect(
            host="localhost",  
            user="root",  
            password="",  
            database="project"
        )
        
        cursor = connection.cursor()
        query="select * from product"
        
        cursor.execute(query)
        
        results = cursor.fetchall()
        
        result_text.delete(1.0, tk.END)
        
        if results:
            for row in results:
                result_text.insert(tk.END, f"{row}\n")
        else:
            result_text.insert(tk.END, "No results found.")
        
     except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
     finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def customer_query():
     try:
        connection = mysql.connector.connect(
            host="localhost",  
            user="root",  
            password="",  
            database="project"
        )
        
        cursor = connection.cursor()
        
        query="select * from customer"
        cursor.execute(query)
        
        results = cursor.fetchall()
        
        result_text.delete(1.0, tk.END)
        
        if results:
            for row in results:
                result_text.insert(tk.END, f"{row}\n")
        else:
            result_text.insert(tk.END, "No results found.")
        
     except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
     finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def employee_query():
     try:
        connection = mysql.connector.connect(
            host="localhost",  
            user="root",  
            password="",  
            database="project"  
        )
        
        cursor = connection.cursor()
        
        query="select * from employee"
        cursor.execute(query)
        
        results = cursor.fetchall()
        
        result_text.delete(1.0, tk.END)
        
        if results:
            for row in results:
                result_text.insert(tk.END, f"{row}\n")
        else:
            result_text.insert(tk.END, "No results found.")
        
     except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
     finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def order_query():
     try:
        # Establish a connection to MySQL Database
        connection = mysql.connector.connect(
            host="localhost",  # e.g., 'localhost' or IP address
            user="root",  # e.g., 'root'
            password="",  # e.g., 'password'
            database="project"  # e.g., 'test_db'
        )
        
        cursor = connection.cursor()
        
        query="select * from demo"
        cursor.execute(query)
        
        # Fetch all results from the query
        results = cursor.fetchall()
        
        # Clear previous result in text box
        result_text.delete(1.0, tk.END)
        
        # If results exist, display them
        if results:
            for row in results:
                result_text.insert(tk.END, f"{row}\n")
        else:
            result_text.insert(tk.END, "No results found.")
        
     except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
     finally:
        if connection.is_connected():
            cursor.close()
            connection.close()






def back():
    root.destroy()
    HomePage()

# Create the main window
root = tk.Tk()
root.title("MySQL Query Executor")
root.config(bg="pink")
image=Image.open("2.jpg")
image=image.resize((600,400))

photo=ImageTk.PhotoImage(image)

label=Label(root,image=photo)
label.place(relheight=1,relwidth=1)


# Set window size
root.geometry("600x400")

# SQL Query input field
# Execute button
execute_button = tk.Button(root, text="Product", command=execute_query)
execute_button.place(x=150,y=10)

customer=tk.Button(root,text="customer",command=customer_query)
customer.place(x=210,y=10)

employee=tk.Button(root,text="employee",command=employee_query)
employee.place(x=280,y=10)

order=tk.Button(root,text="order",command=order_query)
order.place(x=350,y=10)

back=tk.Button(root,text="Back",command=back)
back.place(x=400,y=10)



# Output text area to display query results
result_label = tk.Label(root, text="Query Result:")
result_label.place(x=200,y=70)

result_text = tk.Text(root, width=50, height=10)
result_text.place(x=100,y=100)

# Start the Tkinter event loop
root.mainloop()
