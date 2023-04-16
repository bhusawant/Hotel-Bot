from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
# from login1 import close

from main import HotelManagementSystem


def login():
    Username = entry1.get()
    password = entry2.get()

    if (Username=="" and password==""):
        messagebox.showinfo("", "Blank Not Allowed")
    
    else:
        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="team")
        my_cursor=conn.cursor()
        my_cursor.execute('SELECT password_provided FROM login_user WHERE user=%s',(entry1.get(),))
        row = my_cursor.fetchone()
        if password == row[0]:
            messagebox.showinfo("success","You are logged in")
            root.destroy()
            root1 =Tk()
            obj = HotelManagementSystem(root1)
            root1.mainloop()
        else:
            messagebox.showinfo("Failed","You are failed to login")
            
            conn.commit()
        conn.close()

def new_func():
    root.destroy()
        
    


root = Tk()
root.title("Login here")
root.geometry("400x200")

global entry1
global entry

Label(root, text="Username").place(x=20, y=20)
Label(root, text="Password").place(x=20, y=70)

entry1 = Entry(root, bd= 5)
entry1.place(x= 140, y= 20)

entry2 = Entry(root, bd = 5)
entry2.place(x = 140, y= 70)

Button(root, text= "Login", command = login, height= 3, width= 13, bd = 6).place(x= 100, y=120)
root.mainloop()

