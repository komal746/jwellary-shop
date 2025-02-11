import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from homepage import *
from PIL import Image,ImageTk

# Bill class to handle bill logic
class Bill:
    def __init__(self, customer_name, customer_id):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.items = []
        self.total = 0

    def add_item(self, item_name, unit_price, quantity):
        total_price = unit_price * quantity
        self.items.append({
            "item_name": item_name,
            "unit_price": unit_price,
            "quantity": quantity,
            "total_price": total_price
        })
        self.total += total_price

    def get_bill_summary(self):
        summary = f"Bill for {self.customer_name} (ID: {self.customer_id})\n"
        summary += "-" * 40 + "\n"
        for item in self.items:
            summary += f"{item['item_name']:20} {item['quantity']:5} x {item['unit_price']:10} = {item['total_price']}\n"
        summary += "-" * 40 + "\n"
        summary += f"Total: {self.total}\n"
        return summary

# Function to generate PDF of the bill
def generate_pdf(bill):
    filename = f"bill_{bill.customer_id}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, f"ID: {bill.customer_id}")
    c.drawString(100,770,f"Customer Name:{bill.customer_name}")
    c.drawString(100, 730, "-" * 50)
    y = 710
    for item in bill.items:
        c.drawString(100, y, f"{item['item_name']:20} {item['quantity']:5} x {item['unit_price']:10} = {item['total_price']}")
        y -= 20
    c.drawString(100, y, "-" * 50)
    c.drawString(100, y - 20, f"Total: {bill.total}")
    c.save()
    messagebox.showinfo("Success", f"Bill saved as {filename}")

# Function to handle button click for adding item to bill
def add_item_to_bill():
    item_name = item_name_entry.get()
    try:
        unit_price = float(unit_price_entry.get())
        quantity = int(quantity_entry.get())
        if item_name and unit_price > 0 and quantity > 0:
            bill.add_item(item_name, unit_price, quantity)
            update_bill_summary()
            item_name_entry.delete(0, tk.END)
            unit_price_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter valid item details.")
    except ValueError:
        messagebox.showerror("Error", "Price and Quantity must be valid numbers.")

# Function to update the bill summary display
def update_bill_summary():
    bill_summary.delete(1.0, tk.END)
    bill_summary.insert(tk.END, bill.get_bill_summary())

# Function to handle bill generation and saving as PDF
def generate_bill():
    if bill.items:
        generate_pdf(bill)
    else:
        messagebox.showerror("Error", "No items to generate bill.")
        
# Function to handle user inputs and bill creation
def create_new_bill():
    customer_name = customer_name_entry.get()
    customer_id = customer_id_entry.get()
    if customer_name and customer_id:
        global bill
        bill = Bill(customer_name, customer_id)
        bill_summary.delete(1.0, tk.END)
        
        messagebox.showinfo("Success", "New Bill Created")
    else:
        messagebox.showerror("Error", "Please enter customer details.")


def back():
    root.withdraw()
    HomePage()
    
   

# Set up the main application window
root = tk.Tk()
root.title("Billing System")
root.config(bg="pink")
image=Image.open("2.jpg")
image=image.resize((500,400))

photo=ImageTk.PhotoImage(image)

label=Label(root,image=photo)
label.place(relheight=1,relwidth=1)


# Customer Information Section
customer_frame = tk.Frame(root)
customer_frame.pack(pady=10)


customer_name_label = tk.Label(customer_frame, text="Customer Name:")
customer_name_label.grid(row=0, column=0)
customer_name_entry = tk.Entry(customer_frame)
customer_name_entry.grid(row=0, column=1)

customer_id_label = tk.Label(customer_frame, text="Customer ID:")
customer_id_label.grid(row=1, column=0)
customer_id_entry = tk.Entry(customer_frame)
customer_id_entry.grid(row=1, column=1)

create_bill_button = tk.Button(customer_frame, text="Create New Bill", command=create_new_bill)
create_bill_button.grid(row=2, columnspan=2, pady=10)

# Item Entry Section
item_frame = tk.Frame(root)
item_frame.pack(pady=10)

item_name_label = tk.Label(item_frame, text="Item Name:")
item_name_label.grid(row=0, column=0)
item_name_entry = tk.Entry(item_frame)
item_name_entry.grid(row=0, column=1)

unit_price_label = tk.Label(item_frame, text="Unit Price:")
unit_price_label.grid(row=1, column=0)
unit_price_entry = tk.Entry(item_frame)
unit_price_entry.grid(row=1, column=1)

quantity_label = tk.Label(item_frame, text="Quantity:")
quantity_label.grid(row=2, column=0)
quantity_entry = tk.Entry(item_frame)
quantity_entry.grid(row=2, column=1)

add_item_button = tk.Button(item_frame, text="Add Item", command=add_item_to_bill)
add_item_button.grid(row=3, columnspan=2, pady=10)

# Bill Summary Section
bill_summary_label = tk.Label(root, text="Bill Summary:")
bill_summary_label.pack()

bill_summary = tk.Text(root, width=50, height=10)
bill_summary.pack(pady=10)

# Generate PDF Section
generate_pdf_button = tk.Button(root, text="Generate PDF Bill", command=generate_bill)
generate_pdf_button.pack(pady=10)

back=tk.Button(root,text="Back",command=back)
back.pack(pady=20)

root.mainloop()
