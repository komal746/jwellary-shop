from tkinter import *
from tkinter import messagebox
from homepage import *

w=Tk()
w.title("login page")
w.geometry("500x300+500+200")
w.config(bg="pink")

def login():
    if e1.get()=="komal" and e2.get()=="0000":
        messagebox.showinfo("","login sucsessfully....")
        w.destroy()
        HomePage()
        
               
        
    
    else:
        messagebox.showinfo("","please enter correct password and username")
    


def clear():
    e1.delete(0,END)
    e2.delete(0,END)



l=Label(w,text="JWELLARY SHOP",font=("times",20,"bold",))
l.place(x=150,y=0)

l1=Label(w,text="LOGIN FORM",font=("times",15,"bold"))
l1.place(x=190,y=40)

l2=Label(w,text="USERNAME :",font=("times",10,"bold"))
l2.place(x=150,y=100)

l3=Label(w,text="PASSWORD :",font=("times",10,"bold"))
l3.place(x=150,y=150)


e1=Entry(w,font=("times",10,"bold"))
e1.place(x=260,y=100)

e2=Entry(w,font=("times",10,"bold"),show="*")
e2.place(x=260,y=150)

b1=Button(w,text="LOGIN",activebackground="green",command=login)
b1.place(x=190,y=200)

b2=Button(w,text="CANCEL",activebackground="red",command=w.destroy)
b2.place(x=250,y=200)

w.mainloop()
