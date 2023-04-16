from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
# from details import DetailsRoom

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        # self.root.title()
        self.root.geometry("1295x550+230+220")
        
        # ============Title=================================

        lbl_title=Label(self.root, text="Room Booking", font=("times new roman", 27, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ==========================Logo=============================
        img2=Image.open(r"C:\Users\Bhuvan\Downloads\PythonProject-project\PythonProject-project\__init__.py\img\logo_for_hotelBot.jpg")
        img2=img2.resize((100, 50), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        labImg=Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        labImg.place(x=0, y=0, width=100, height=50)
        
         # ===================================labelFrame==========================
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

        # Floor 
        lbl_floor=Label(labelframeleft, text="Floor", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W, padx=20)

        self.var_floor = StringVar()

        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor, width=20, font=("arial", 13, "bold"))
        entry_floor.grid(row=0, column=1,sticky=W)

        lbl_RoomNo=Label(labelframeleft, text="Room No", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W, padx=20)
        self.var_roomNo = StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo, width=20, font=("arial", 13, "bold"))
        entry_RoomNo.grid(row=1, column=1,sticky=W)

        lbl_RoomType=Label(labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W, padx=20)
        self.var_RoomType = StringVar()
        entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType, width=20, font=("arial", 13, "bold"))
        entry_RoomType.grid(row=2, column=1,sticky=W)
# ==========================btns======================================
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd=Button(btn_frame, text="Add",command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnupdate=Button(btn_frame, text="Update",command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnupdate.grid(row=0, column=1, padx=1)

        btnDelete=Button(btn_frame, text="Delete",command=self.mDelete,font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset=Button(btn_frame, text="Reset",command=self.reset_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)
        # =============================================Table Frame search system============================================
        Table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=("times new roman", 12, "bold"), padx=2)
        Table_frame.place(x=600, y=55, width=600, height=350)

        scroll_x=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_frame, columns=("floor", "roomno", "roomtype"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")

        self.room_table["show"]="headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        # a = self.var_mobile.get()
        else:
            try:
                conn=mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='1234',
                    database='team'
                    )
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                    self.var_floor.get(),
                                                                                    self.var_roomNo.get(),
                                                                                    self.var_RoomType.get(),
                                                                                    
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(
                                host = 'localhost',
                                username = 'root',
                                password = '1234',
                                database = 'team'
                                )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # Cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        
        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_RoomType.set(row[2])


    # ========================Update=============================
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Floor Number",parent=self.root)
        else:
            conn=mysql.connector.connect(
                                host="localhost",
                                username='root',
                                password='1234',
                                database='team'    
                                    )
            my_cursor=conn.cursor()
            my_cursor.execute('''update details set 
                            
                              Floor=%s,
                              RoomNo=%s,
                              RoomType=%s,
                             
                              ''',(
                                    self.var_checkin.get(),
                                    self.var_checkout.get(),
                                    self.var_roomtype.get(),
                                    self.var_roomavailable.get(),
                                    self.var_meal.get(),
                                    self.var_noofdays.get(),
                                    self.var_contact.get()
                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully")


    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management system","Do you want to delete this room",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(
                                host='localhost',
                                username='root',
                                password='1234',
                                database='team'    
                                    )
            my_cursor=conn.cursor()
            query="Delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        self.var_floor.set(""),
        self.var_RoomType.set(""),
        self.var_roomNo.set("")

if __name__== "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()