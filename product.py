import mysql.connector
from tkinter import *
from tkinter import messagebox
from homepage import *
from PIL import Image,ImageTk

#coding for insert
def insert():
     pid=e1.get()
     pname=e2.get()
     pprice=e3.get()
     pbrand=e4.get()
     if not e1.get()or not e2.get()or not e3.get() or not e4.get():
        messagebox.showinfo("","please enter value")
     else:
        if not pid.isdigit() or pname.isdigit()or not pprice.isdigit()or pbrand.isdigit():
            messagebox.showinfo("massage box","please enter correct value")
            
        else:
            mydb=mysql.connector.connect(host='localhost',user='root',password='',database='project')
            mycursor=mydb.cursor()

            sql="insert into product values (%s,%s,%s,%s)"
            data=(pid,pname,pprice,pbrand)
            mycursor.execute(sql,data)
            mydb.commit()
            messagebox.showinfo("","record inserted")

            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
        
#update
def update():
    
    pid=e1.get()
    pname=e2.get()
    pprice=e3.get()
    pbrand=e4.get()
        
    if not e1.get()or not e2.get()or not e3.get() or not e4.get():
        messagebox.showinfo("","please enter value")
    else:
        if not pid.isdigit() or pname.isdigit()or not pprice.isdigit()or pbrand.isdigit():
            messagebox.showinfo("massage box","please enter correct value")    
       
        else:
            mydb=mysql.connector.connect(host='localhost',user='root',password='',database='project')
            mycursor=mydb.cursor()
            sql="update product set pname=%s,pprice=%s,pbrand=%s where pid=%s"
            data=(pname,pprice,pbrand,pid)
            mycursor.execute(sql,data)
            mydb.commit()
            messagebox.showinfo("","record updated")

            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            
#delete                    
def delete():
    pid=e1.get()
    if not e1.get():
        messagebox.showinfo("","please enter id for delete data")
    else:
        if not pid.isdigit():
            messagebox.showinfo("massage box","please enter id no for delete data")
        else:
            mydb=mysql.connector.connect(host='localhost',user='root',password='',database='project')
            mycursor=mydb.cursor()
            sql="delete from product where pid='%s'"
            mycursor.execute(sql)
            mydb.commit()
            messagebox.showinfo("","record deleted")

            e1.delete(0,END)       

#home page
def back():
     w.withdraw()
     HomePage()
     
     
     

#select
def select():
     w.withdraw()
     import demo1

#design part
w=Tk()
w.title("PRODUCT PAGE")
w.geometry("500x400+500+200")
#w.config(bg="pink")
image=Image.open("2.jpg")
image=image.resize((500,400))

photo=ImageTk.PhotoImage(image)

label=Label(w,image=photo)
label.place(relheight=1,relwidth=1)


l1=Label(w,text="JWELLARY SHOP",font=("times",20,"bold"))
l1.place(x=130,y=0)

l2=Label(w,text="PRODUCT ID:",font=10)
l2.place(x=70,y=50)

l3=Label(w,text="PRODUCT NAME:",font=10)
l3.place(x=40,y=100)

l4=Label(w,text="PRODUCT PRICE:",font=10)
l4.place(x=40,y=150)

l5=Label(w,text="PRODUCT BRAND:",font=10)
l5.place(x=40,y=200)

e1=Entry(w,bd=2)
e1.place(x=250,y=50)

e2=Entry(w,bd=2)
e2.place(x=250,y=100)

e3=Entry(w,bd=2)
e3.place(x=250,y=150)

e4=Entry(w,bd=2)
e4.place(x=250,y=200)

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

    
