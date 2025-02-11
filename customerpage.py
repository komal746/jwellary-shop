import mysql.connector
from tkinter import *
from tkinter import messagebox
from homepage import *
from PIL import Image,ImageTk
#insert
def insert():
    cid=e1.get()
    cname=e2.get()
    pprice=e3.get()
    pbrand=e4.get()
    cmobile=e5.get()
        
    if not e1.get()or not e2.get()or not e3.get() or not e4.get() or not e5.get():
        messagebox.showinfo("","please enter value")
    
    else:
        if not cid.isdigit() or cname.isdigit()or not pprice.isdigit() or pbrand.isdigit() or not cmobile.isdigit():
            messagebox.showinfo("","please enter correct values in entry for add data")
            
        else:
            mydb=mysql.connector.connect(host='localhost',user='root',password='',database='project')
            mycursor=mydb.cursor()
            sql="insert into customer values (%s,%s,%s,%s,%s)"
            data = (cid,cname,pprice,pbrand,cmobile)
            mycursor.execute(sql,data)
            mydb.commit()
            messagebox.showinfo("","record inserted")

            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)

#update
def update():
    cid=e1.get()
    cname=e2.get()
    pprice=e3.get()
    pbrand=e4.get()
    cmobile=e5.get()
    
    if not e1.get()or not e2.get()or not e3.get() or not e4.get() or not e5.get():
        messagebox.showinfo("","please enter value")
    else:
        if not cid.isdigit() or cname.isdigit()or not pprice.isdigit() or pbrand.isdigit() or not cmobile.isdigit():
            messagebox.showinfo("","please enter correct values in entry for update")
        else:
            mydb=mysql.connector.connect(host='localhost',user='root',password='',database='project')
            mycursor=mydb.cursor()
            sql="update customer set cname=%s,pprice=%s,pbrand=%s,cmobile=%s where cid=%s"
            data = (cname,pprice,pbrand,cmobile,cid)
            mycursor.execute(sql,data)
            mydb.commit()
            messagebox.showinfo("","record updated")

            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)


#delete
def delete():
    cid=e1.get()
    if not e1.get():
        messagebox.showinfo("","please enter id for delete record")
    else:
        if not cid.isdigit():
            messagebox.showinfo("","please enter correct values in entry for delete")

        else:
            mydb=mysql.connector.connect(host='localhost',user='root',password='',database='project')
            mycursor=mydb.cursor()
            sql="delete from customer where cid='%s'"
            mycursor.execute(sql)
            mydb.commit()
            messagebox.showinfo("","record deleted")

            e1.delete(0,END)

def back():
    w.withdraw()
    HomePage()

def select():
    w.withdraw()
    import demo1

#design part
w=Tk()
w.title("CUSTOMER PAGE")
w.geometry("500x400+500+200")
w.config(bg="pink")
image=Image.open("2.jpg")
image=image.resize((500,400))

photo=ImageTk.PhotoImage(image)

label=Label(w,image=photo)
label.place(relheight=1,relwidth=1)


l1=Label(w,text="JWELLARY SHOP",font=("times",20,"bold"))
l1.place(x=130,y=0)

l2=Label(w,text="Customer ID:",font=10)
l2.place(x=40,y=50)

l3=Label(w,text="Customer Name:",font=10)
l3.place(x=40,y=100)

l4=Label(w,text="Product Price:",font=10)
l4.place(x=40,y=150)

l5=Label(w,text="Product Brand:",font=10)
l5.place(x=40,y=200)

l6=Label(w,text="Customer Mobile:",font=10)
l6.place(x=40,y=250)


e1=Entry(w,bd=2)
e1.place(x=250,y=50)

e2=Entry(w,bd=2)
e2.place(x=250,y=100)

e3=Entry(w,bd=2)
e3.place(x=250,y=150)

e4=Entry(w,bd=2)
e4.place(x=250,y=200)

e5=Entry(w,bd=2)
e5.place(x=250,y=250)


b1=Button(w,text="ADD",font=10,command=insert)
b1.place(x=50,y=300)

b2=Button(w,text="UPDATE",font=10,command=update)
b2.place(x=115,y=300)

b3=Button(w,text="DELETE",font=10,command=delete)
b3.place(x=215,y=300)

b4=Button(w,text="SELECT",font=10,command=select)
b4.place(x=315,y=300)

b5=Button(w,text="HOME",font=10,command=back)
b5.place(x=415,y=300)

w.mainloop()

    

