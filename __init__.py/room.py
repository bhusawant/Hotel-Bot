# from tkinter import *
# from PIL import Image, ImageTk
# from tkinter import ttk
# import random
# from tkinter import messagebox
# from datetime import datetime
# import mysql.connector
# import random

# class RoomBooking:
#     def __init__(self, root):
#         self.root=root
#         self.root.title("HOTEL")
#         self.root.geometry("1295x560+230+220")
        
#         # =======================Variable==========================
#         self.var_contact=StringVar()
#         self.var_checkin=StringVar()
#         self.var_checkout=StringVar()
#         self.var_roomtype=StringVar()
#         self.var_roomavailable=StringVar()
#         self.var_meal=StringVar()
#         self.var_noofdays=StringVar()
#         self.var_paidtax=StringVar()
#         self.var_actualtotal=StringVar()
#         self.var_total=StringVar()
        
#         # =========================Title============================
#         lbl_title=Label(self.root, text="Room Booking", font=("times new roman", 27, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
#         lbl_title.place(x=0, y=0, width=1295, height=50)

#         # ==========================Logo=============================
#         img2=Image.open(r"img\logo_for_hotelBot.jpg")
#         img2=img2.resize((100, 50), Image.ANTIALIAS)
#         self.photoimg2=ImageTk.PhotoImage(img2)

#         labImg=Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
#         labImg.place(x=0, y=0, width=100, height=50)
        
#          # ===================================labelFrame==========================
#         labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="RoomBooking Details", font=("times new roman", 12, "bold"), padx=2)
#         labelframeleft.place(x=5, y=50, width=425, height=490)
        
#         # ==================================label and entry========================
#         # Customer contact
#         lbl_cust_contact=Label(labelframeleft, text="Customer Contact:", font=("arial", 12, "bold"), padx=2, pady=6)
#         lbl_cust_contact.grid(row=0, column=0, sticky=W)

#         entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact, width=20, font=("arial", 13, "bold"))
#         entry_contact.grid(row=0, column=1,sticky=W)
        
#         # Fetch Data Button
#         btnFetchData=Button(labelframeleft, command=self.Fetch_contact, text="Fetch Data", font=("arial", 8, "bold"), bg="black", fg="gold", width=10)
#         btnFetchData.grid(row=0, column=1, padx=1,sticky=E)
#         # btnFetchData.place(x=340,y=4)
        
#         # Check_in Date
#         check_in_date=Label(labelframeleft, text="Check_in Date:", font=("arial", 12, "bold"), padx=2, pady=6)
#         check_in_date.grid(row=1, column=0, sticky=W)
#         txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin, width=29, font=("arial", 13, "bold"))
#         txtcheck_in_date.grid(row=1, column=1)
        
#         # Check_out Date
#         check_out_date=Label(labelframeleft, text="Check_out Date:", font=("arial", 12, "bold"), padx=2, pady=6)
#         check_out_date.grid(row=2, column=0, sticky=W)
#         txtcheck_out_date=ttk.Entry(labelframeleft, textvariable=self.var_checkout, width=29, font=("arial", 13, "bold"))
#         txtcheck_out_date.grid(row=2, column=1)
        
#         # Room Type
#         label_RoomType = Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
#         label_RoomType.grid(row = 3, column = 0, sticky = W)
        
#         combo_RoomType = ttk.Combobox(labelframeleft,font=('arial',12,'bold'), textvariable=self.var_roomtype,width=27,state='readonly')
#         combo_RoomType['value']=("single","double","luxury")
#         combo_RoomType.current(0)
#         combo_RoomType.grid(row=3,column=1)
        
#         # Available Room
#         lblRoomAvailable=Label(labelframeleft,font=('arial',12,'bold'),text='Available Room:',padx=2,pady=6)
#         lblRoomAvailable.grid(row=4,column=0,sticky=W)
#         txtRoomAvailable=ttk.Entry(labelframeleft, textvariable=self.var_roomavailable,font=('arial',12,'bold'),width=29)
#         txtRoomAvailable.grid(row=4,column=1)
        
#         # Meal
#         lblMeal=Label(labelframeleft,font=('arial',12,'bold'),text='Meal:',padx=2,pady=6)
#         lblMeal.grid(row=5,column=0,sticky=W)
#         txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,font=('arial',12,'bold'),width=29)
#         txtMeal.grid(row=5,column=1)
        
#         # No. of Days
#         lblNoOfDays=Label(labelframeleft,font=('arial',12,'bold'),text='No Of Days:',padx=2,pady=6)
#         lblNoOfDays.grid(row=6,column=0,sticky=W)
#         txtNoOfDays=ttk.Entry(labelframeleft, textvariable=self.var_noofdays,font=('arial',12,'bold'),width=29)
#         txtNoOfDays.grid(row=6,column=1)
        
#         # Paid Tax
#         lblPaidTax=Label(labelframeleft,font=('arial',12,'bold'),text='Paid Tax:',padx=2,pady=6)
#         lblPaidTax.grid(row=7,column=0,sticky=W)
#         txtPaidTax=ttk.Entry(labelframeleft, textvariable=self.var_paidtax,font=('arial',12,'bold'),width=29)
#         txtPaidTax.grid(row=7,column=1)
        
#         # Sub Total
#         lblSubTotal=Label(labelframeleft,font=('arial',12,'bold'),text='Sub Total:',padx=2,pady=6)
#         lblSubTotal.grid(row=8,column=0,sticky=W)
#         txtSubTotal=ttk.Entry(labelframeleft, textvariable=self.var_actualtotal,font=('arial',12,'bold'),width=29)
#         txtSubTotal.grid(row=8,column=1)
        
#         # Total Cost
#         lblTotalCost=Label(labelframeleft,font=('arial',12,'bold'),text='Total Cost:',padx=2,pady=6)
#         lblTotalCost.grid(row=9,column=0,sticky=W)
#         txtTotalCost=ttk.Entry(labelframeleft, textvariable=self.var_total,font=('arial',12,'bold'),width=29)
#         txtTotalCost.grid(row=9,column=1)
        
#         # =========================Bill Button===================
#         btnBill=Button(labelframeleft, command=self.total, text="Bill", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
#         btnBill.grid(row=10, column=0, padx=1,sticky=W)
        
#         # ==========================================btns=======================
#         btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
#         btn_frame.place(x=0, y=400, width=412, height=40)

#         btnAdd=Button(btn_frame, command=self.add_data, text="Add", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
#         btnAdd.grid(row=0, column=0, padx=1)

#         btnupdate=Button(btn_frame,command=self.update, text="Update", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
#         btnupdate.grid(row=0, column=1, padx=1)

#         btnDelete=Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
#         btnDelete.grid(row=0, column=2, padx=1)

#         btnReset=Button(btn_frame, text="Reset", command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
#         btnReset.grid(row=0, column=3, padx=1)
        
#         # ===========================================Right Side Image======================================
#         img3=Image.open(r"img\bed.jpg")
#         img3=img3.resize((520,300), Image.ANTIALIAS)
#         self.photoimg3=ImageTk.PhotoImage(img3)

#         labImg=Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
#         labImg.place(x=760, y=55, width=520, height=300)
        
        
#         # =============================================Table Frame search system============================================
#         Table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View details and search system", font=("times new roman", 12, "bold"), padx=2)
#         Table_frame.place(x=435, y=280, width=860, height=260)

#         lbl_searchby=Label(Table_frame, text="Search By:", font=("arial", 12, "bold"), bg="red", fg="white")
#         lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)
        
#         self.search_variable=StringVar()

#         combo_search=ttk.Combobox(Table_frame,textvariable=self.search_variable, font=("arial", 12, "bold"), width=24, state="readonly")
#         combo_search["value"]=("Contact", "Rooms")
#         combo_search.current(0)
#         combo_search.grid(row=0, column=1, padx=2)

#         self.txt_search=StringVar()
#         txtsearch=ttk.Entry(Table_frame,textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
#         txtsearch.grid(row=0, column=2, padx=2)



#         btnsearch=Button(Table_frame, text="Search",  command=self.search, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
#         btnsearch.grid(row=0, column=3, padx=1)

#         btnshowall=Button(Table_frame, text="Show All", command=self.fetch_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
#         btnshowall.grid(row=0, column=4, padx=1)
        
#         # =============================================Show Data Table===================================

#         details_table=Frame(Table_frame, bd=2, relief=RIDGE)
#         details_table.place(x=0, y=50, width=860, height=180)


#         scroll_x=ttk.Scrollbar(details_table, orient=HORIZONTAL)
#         scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)

#         self.room_table=ttk.Treeview(details_table, columns=(
#                                                     "contact", 
#                                                     "checkin", 
#                                                     "checkout", 
#                                                     "roomtype", 
#                                                     "roomavailable",
#                                                     "meal",
#                                                     "noOfdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

#         scroll_x.pack(side=BOTTOM, fill=X)
#         scroll_y.pack(side=RIGHT, fill=Y)

#         scroll_x.config(command=self.room_table.xview)
#         scroll_y.config(command=self.room_table.yview)

#         self.room_table.heading("contact", text="Contact")
#         self.room_table.heading("checkin", text="Check-in")
#         self.room_table.heading("checkout", text="Check-ou")
#         self.room_table.heading("roomtype", text="Room Type")
#         self.room_table.heading("roomavailable", text="Room No")
#         self.room_table.heading("meal", text="Meal")
#         self.room_table.heading("noOfdays", text="NoOfDays")
        

#         self.room_table["show"]="headings"

#         self.room_table.column("contact", width=100)
#         self.room_table.column("checkin", width=100)
#         self.room_table.column("checkout", width=100)
#         self.room_table.column("roomtype", width=100)
#         self.room_table.column("roomavailable", width=100)
#         self.room_table.column("meal", width=100)
#         self.room_table.column("noOfdays", width=100)
#         self.room_table.pack(fill=BOTH, expand=1)
#         self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
#         self.fetch_data()
        
#     def add_data(self):
#         if self.var_contact.get()=="" or self.var_checkin.get()=="":
#             messagebox.showerror("Error","All fields are required",parent=self.root)
#         # a = self.var_mobile.get()
#         else:
#             try:
#                 conn=mysql.connector.connect(
#                     host='localhost',
#                     user='root',
#                     password='1234',
#                     database='team'
#                     )
#                 my_cursor=conn.cursor()
#                 my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
#                                                                                     self.var_contact.get(),
#                                                                                     self.var_checkin.get(),
#                                                                                     self.var_checkout.get(),
#                                                                                     self.var_roomtype.get(),
#                                                                                     self.var_roomavailable.get(),
#                                                                                     self.var_meal.get(),
#                                                                                     self.var_noofdays.get()
#                                                                                 ))
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()
#                 messagebox.showinfo("Success","Customer has been added",parent=self.root)
#             except Exception as es:
#                 messagebox.showerror("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
        
#     # ==============================Fetch Data====================================
#     def fetch_data(self):
#         conn=mysql.connector.connect(
#                                 host = 'localhost',
#                                 username = 'root',
#                                 password = '1234',
#                                 database = 'team'
#                                 )
#         my_cursor = conn.cursor()
#         my_cursor.execute("select * from room")
#         rows=my_cursor.fetchall()
#         if len(rows)!=0:
#             self.room_table.delete(*self.room_table.get_children())
#             for i in rows:
#                 self.room_table.insert("",END,values=i)
#             conn.commit()
#         conn.close()
    
#     # Cursor
#     def get_cursor(self,event=""):
#         cursor_row=self.room_table.focus()
#         content=self.room_table.item(cursor_row)
#         row=content["values"]
        
#         self.var_contact.set(row[0]),
#         self.var_checkin.set(row[1]),
#         self.var_checkout.set(row[2]),
#         self.var_roomtype.set(row[3]),
#         self.var_roomavailable.set(row[4]),
#         self.var_meal.set(row[5]),
#         self.var_noofdays.set(row[6])
    
#     # ========================Update=============================
#     def update(self):
#         if self.var_contact.get()=="":
#             messagebox.showerror("Error","Please enter Mobile",parent=self.root)
#         else:
#             conn=mysql.connector.connect(
#                                 host="localhost",
#                                 username='root',
#                                 password='1234',
#                                 database='team'    
#                                     )
#             my_cursor=conn.cursor()
#             my_cursor.execute('''update room set 
#                               check_in=%s,
#                               check_out=%s,
#                               roomtype=%s,
#                               roomavailable=%s,
#                               meal=%s,
#                               noOfdays=%s
#                               where Contact=%s
#                               ''',(
#                                     self.var_checkin.get(),
#                                     self.var_checkout.get(),
#                                     self.var_roomtype.get(),
#                                     self.var_roomavailable.get(),
#                                     self.var_meal.get(),
#                                     self.var_noofdays.get(),
#                                     self.var_contact.get()
#                               ))
#             conn.commit()
#             self.fetch_data()
#             conn.close()
#             messagebox.showinfo("Update","Room details has been updated successfully")
    
#     def mDelete(self):
#         mDelete=messagebox.askyesno("Hotel Management system","Do you want to delete this customer",parent=self.root)
#         if mDelete>0:
#             conn=mysql.connector.connect(
#                                 host='localhost',
#                                 username='root',
#                                 password='1234',
#                                 database='team'    
#                                     )
#             my_cursor=conn.cursor()
#             query="Delete from room where contact=%s"
#             value=(self.var_contact.get(),)
#             my_cursor.execute(query, value)
#         else:
#             if not mDelete:
#                 return
#         conn.commit()
#         self.fetch_data()
#         conn.close()
        
#     def reset(self):
#         self.var_contact.set(""),
#         self.var_checkin.set(""),
#         self.var_checkout.set(""),
#         self.var_roomtype.set(""),
#         self.var_roomavailable.set(""),
#         self.var_meal.set(""),
#         self.var_noofdays.set("")
        
#     # Search System
#     def search(self):
#         conn=mysql.connector.connect(
#                                 host="localhost",
#                                 username='root',
#                                 password='1234',
#                                 database='team'    
#                                     )
#         my_cursor=conn.cursor()
#         my_cursor.execute("select * from room where "+str(self.search_variable.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
#         rows=my_cursor.fetchall()
#         if len (rows)!=0:
#             self.room_table.delete(*self.room_table.get_children())
#         for i in rows:
#             self.room_table.insert("",END,values=i)
#             conn.commit()
#         conn.close()
        
#     def total(self):
#         inDate = self.var_checkin.get()
#         outDate = self.var_checkout.get()
#         inDate = datetime.strptime(inDate,"%d/%m/%Y")
#         outDate = datetime.strptime(outDate,"%d/%m/%Y")
#         self.var_noofdays.set(abs(outDate-inDate).days)
        
#         if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=='luxury'):
#             q1=float(300)
#             q2=float(700)
#             q3=float(self.var_noofdays.get())
#             q4=float(q1 + q2)
#             q5=float(q3 + q4)
#             Tax="Rs."+str("%.2f"%((q5)*0.1))
#             ST="Rs."+str("%.2f"%((q5)))
#             TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
#             self.var_paidtax.set(Tax)
#             self.var_actualtotal.set(ST)
#             self.var_total.set(TT)
            
#         elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=='double'):
#             q1=float(300)
#             q2=float(600)
#             q3=float(self.var_noofdays.get())
#             q4=float(q1 + q2)
#             q5=float(q3 + q4)
#             Tax="Rs."+str("%.2f"%((q5)*0.1))
#             ST="Rs."+str("%.2f"%((q5)))
#             TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
#             self.var_paidtax.set(Tax)
#             self.var_actualtotal.set(ST)
#             self.var_total.set(TT)
        
#         elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=='single'):
#             q1=float(300)
#             q2=float(250)
#             q3=float(self.var_noofdays.get())
#             q4=float(q1 + q2)
#             q5=float(q3 + q4)
#             Tax="Rs."+str("%.2f"%((q5)*0.1))
#             ST="Rs."+str("%.2f"%((q5)))
#             TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
#             self.var_paidtax.set(Tax)
#             self.var_actualtotal.set(ST)
#             self.var_total.set(TT)
            
#         elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=='luxury'):
#             q1=float(350)
#             q2=float(700)
#             q3=float(self.var_noofdays.get())
#             q4=float(q1 + q2)
#             q5=float(q3 + q4)
#             Tax="Rs."+str("%.2f"%((q5)*0.1))
#             ST="Rs."+str("%.2f"%((q5)))
#             TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
#             self.var_paidtax.set(Tax)
#             self.var_actualtotal.set(ST)
#             self.var_total.set(TT)
            
#         elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=='double'):
#             q1=float(350)
#             q2=float(600)
#             q3=float(self.var_noofdays.get())
#             q4=float(q1 + q2)
#             q5=float(q3 + q4)
#             Tax="Rs."+str("%.2f"%((q5)*0.1))
#             ST="Rs."+str("%.2f"%((q5)))
#             TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
#             self.var_paidtax.set(Tax)
#             self.var_actualtotal.set(ST)
#             self.var_total.set(TT)
            
#         elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=='single'):
#             q1=float(350)
#             q2=float(250)
#             q3=float(self.var_noofdays.get())
#             q4=float(q1 + q2)
#             q5=float(q3 + q4)
#             Tax="Rs."+str("%.2f"%((q5)*0.1))
#             ST="Rs."+str("%.2f"%((q5)))
#             TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
#             self.var_paidtax.set(Tax)
#             self.var_actualtotal.set(ST)
#             self.var_total.set(TT)
        
#         elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=='luxury'):
#             q1=float(400)
#             q2=float(700)
#             q3=float(self.var_noofdays.get())
#             q4=float(q1 + q2)
#             q5=float(q3 + q4)
#             Tax="Rs."+str("%.2f"%((q5)*0.1))
#             ST="Rs."+str("%.2f"%((q5)))
#             TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
#             self.var_paidtax.set(Tax)
#             self.var_actualtotal.set(ST)
#             self.var_total.set(TT)
            
#         elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=='Double'):
#             q1=float(400)
#             q2=float(600)
#             q3=float(self.var_noofdays.get())
#             q4=float(q1 + q2)
#             q5=float(q3 + q4)
#             Tax="Rs."+str("%.2f"%((q5)*0.1))
#             ST="Rs."+str("%.2f"%((q5)))
#             TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
#             self.var_paidtax.set(Tax)
#             self.var_actualtotal.set(ST)
#             self.var_total.set(TT)
            
#         elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=='single'):
#             q1=float(400)
#             q2=float(250)
#             q3=float(self.var_noofdays.get())
#             q4=float(q1 + q2)
#             q5=float(q3 + q4)
#             Tax="Rs."+str("%.2f"%((q5)*0.1))
#             ST="Rs."+str("%.2f"%((q5)))
#             TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
#             self.var_paidtax.set(Tax)
#             self.var_actualtotal.set(ST)
#             self.var_total.set(TT)
        
            
#     # ======================================All Data Frame===========================
#     def Fetch_contact(self):
#         if self.var_contact.get() == "":
#             messagebox.showerror("Error","Please enter the Contact Number",parent=self.root)
#         else:
#             conn = mysql.connector.connect(
#                                         host = 'localhost',
#                                         user = 'root',
#                                         password = '1234',
#                                         database = 'team'
#                                         )
#             my_cursor = conn.cursor()
#             query = ("Select Name from customer where Mobile = %s")
#             value = (self.var_contact.get(),)
#             my_cursor.execute(query,value)
#             row=my_cursor.fetchone()
            
#             if row == None:
#                 messagebox.showerror("Error",'This number not found',parent=self.root)
#             else:
#                 conn.commit()
#                 conn.close()
                
#                 showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
#                 showDataFrame.place(x=450,y=55,width=300,height=180)
                
#                 lblName = Label(showDataFrame,text="Name:",font=('arial',12,'bold'))
#                 lblName.place(x=0,y=0)

#                 lbl = Label(showDataFrame,text=row,font=('arial',12,'bold'))
#                 lbl.place(x=75,y=0)
                
#             # ================================Gender==================================
#             conn = mysql.connector.connect(
#                                         host = 'localhost',
#                                         user = 'root',
#                                         password = '1234',
#                                         database = 'team'
#                                         )
#             my_cursor = conn.cursor()
#             query = ("Select Gender from customer where Mobile = %s")
#             value = (self.var_contact.get(),)
#             my_cursor.execute(query,value)
#             row=my_cursor.fetchone()
            
#             lblGender = Label(showDataFrame,text="Gender:",font=('arial',12,'bold'))
#             lblGender.place(x=0,y=30)

#             lbl2 = Label(showDataFrame,text=row,font=('arial',12,'bold'))
#             lbl2.place(x=75,y=30)
            
#             # ================================Email==============================
#             conn = mysql.connector.connect(
#                                         host = 'localhost',
#                                         user = 'root',
#                                         password = '1234',
#                                         database = 'team'
#                                         )
#             my_cursor = conn.cursor()
#             query = ("Select Email from customer where Mobile = %s")
#             value = (self.var_contact.get(),)
#             my_cursor.execute(query,value)
#             row=my_cursor.fetchone()
            
#             lblEmail = Label(showDataFrame,text="Email:",font=('arial',12,'bold'))
#             lblEmail.place(x=0,y=60)

#             lbl3 = Label(showDataFrame,text=row,font=('arial',10,'bold'))
#             lbl3.place(x=75,y=60)
            
#             # ==========================Nationality============================
#             conn = mysql.connector.connect(
#                                         host = 'localhost',
#                                         user = 'root',
#                                         password = '1234',
#                                         database = 'team'
#                                         )
#             my_cursor = conn.cursor()
#             query = ("Select Nationality from customer where Mobile = %s")
#             value = (self.var_contact.get(),)
#             my_cursor.execute(query,value)
#             row=my_cursor.fetchone()
            
#             lblNationality = Label(showDataFrame,text="Nationality:",font=('arial',12,'bold'))
#             lblNationality.place(x=0,y=90)

#             lbl4 = Label(showDataFrame,text=row,font=('arial',10,'bold'))
#             lbl4.place(x=75,y=90)
            
#             # ==========================Address============================
#             conn = mysql.connector.connect(
#                                         host = 'localhost',
#                                         user = 'root',
#                                         password = '1234',
#                                         database = 'team'
#                                         )
#             my_cursor = conn.cursor()
#             query = ("Select Address from customer where Mobile = %s")
#             value = (self.var_contact.get(),)
#             my_cursor.execute(query,value)
#             row=my_cursor.fetchone()
            
#             lblAddress = Label(showDataFrame,text="Address:",font=('arial',12,'bold'))
#             lblAddress.place(x=0,y=120)

#             lbl5 = Label(showDataFrame,text=row,font=('arial',10,'bold'))
#             lbl5.place(x=75,y=120)
        
# if __name__ == "__main__":
#     root=Tk()
#     obj=RoomBooking(root)
#     root.mainloop()








from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
from datetime import datetime
import mysql.connector
import random

class RoomBooking:
    def __init__(self, root):
        self.root=root
        self.root.title("HOTEL")
        self.root.geometry("1295x560+230+220")
        
        # =======================Variable==========================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        # =========================Title============================
        lbl_title=Label(self.root, text="Room Booking", font=("times new roman", 27, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ==========================Logo=============================
        img2=Image.open(r"img\logo_for_hotelBot.jpg")
        img2=img2.resize((100, 50), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        labImg=Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        labImg.place(x=0, y=0, width=100, height=50)
        
         # ===================================labelFrame==========================
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="RoomBooking Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)
        
        # ==================================label and entry========================
        # Customer contact
        lbl_cust_contact=Label(labelframeleft, text="Customer Contact:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact, width=20, font=("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1,sticky=W)
        
        # Fetch Data Button
        btnFetchData=Button(labelframeleft, command=self.Fetch_contact, text="Fetch Data", font=("arial", 8, "bold"), bg="black", fg="gold", width=10)
        btnFetchData.grid(row=0, column=1, padx=1,sticky=E)
        # btnFetchData.place(x=340,y=4)
        
        # Check_in Date
        check_in_date=Label(labelframeleft, text="Check_in Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin, width=29, font=("arial", 13, "bold"))
        txtcheck_in_date.grid(row=1, column=1)
        
        # Check_out Date
        check_out_date=Label(labelframeleft, text="Check_out Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        txtcheck_out_date=ttk.Entry(labelframeleft, textvariable=self.var_checkout, width=29, font=("arial", 13, "bold"))
        txtcheck_out_date.grid(row=2, column=1)
        
        # Room Type
        label_RoomType = Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_RoomType.grid(row = 3, column = 0, sticky = W)
        
        conn=mysql.connector.connect(
                                host = 'localhost',
                                username = 'root',
                                password = '1234',
                                database = 'team'
                                )
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()
        
        combo_RoomType = ttk.Combobox(labelframeleft,font=('arial',12,'bold'), textvariable=self.var_roomtype,width=27,state='readonly')
        combo_RoomType['value']=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)
        
        # Available Room
        lblRoomAvailable=Label(labelframeleft,font=('arial',12,'bold'),text='Available Room:',padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
#         txtRoomAvailable=ttk.Entry(labelframeleft, textvariable=self.var_roomavailable,font=('arial',12,'bold'),width=29)
#         txtRoomAvailable.grid(row=4,column=1)
        conn=mysql.connector.connect(
                                host = 'localhost',
                                username = 'root',
                                password = '1234',
                                database = 'team'
                                )
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()
        
        combo_RoomNo = ttk.Combobox(labelframeleft,font=('arial',12,'bold'), textvariable=self.var_roomavailable,width=27,state='readonly')
        combo_RoomNo['value']=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)
        
        # Meal
        lblMeal=Label(labelframeleft,font=('arial',12,'bold'),text='Meal:',padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,font=('arial',12,'bold'),width=29)
        txtMeal.grid(row=5,column=1)
        
        # No. of Days
        lblNoOfDays=Label(labelframeleft,font=('arial',12,'bold'),text='No Of Days:',padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft, textvariable=self.var_noofdays,font=('arial',12,'bold'),width=29)
        txtNoOfDays.grid(row=6,column=1)
        
        # Paid Tax
        lblPaidTax=Label(labelframeleft,font=('arial',12,'bold'),text='Paid Tax:',padx=2,pady=6)
        lblPaidTax.grid(row=7,column=0,sticky=W)
        txtPaidTax=ttk.Entry(labelframeleft, textvariable=self.var_paidtax,font=('arial',12,'bold'),width=29)
        txtPaidTax.grid(row=7,column=1)
        
        # Sub Total
        lblSubTotal=Label(labelframeleft,font=('arial',12,'bold'),text='Sub Total:',padx=2,pady=6)
        lblSubTotal.grid(row=8,column=0,sticky=W)
        txtSubTotal=ttk.Entry(labelframeleft, textvariable=self.var_actualtotal,font=('arial',12,'bold'),width=29)
        txtSubTotal.grid(row=8,column=1)
        
        # Total Cost
        lblTotalCost=Label(labelframeleft,font=('arial',12,'bold'),text='Total Cost:',padx=2,pady=6)
        lblTotalCost.grid(row=9,column=0,sticky=W)
        txtTotalCost=ttk.Entry(labelframeleft, textvariable=self.var_total,font=('arial',12,'bold'),width=29)
        txtTotalCost.grid(row=9,column=1)
        
        # =========================Bill Button===================
        btnBill=Button(labelframeleft, command=self.total, text="Bill", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnBill.grid(row=10, column=0, padx=1,sticky=W)
        
        # ==========================================btns=======================
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd=Button(btn_frame, command=self.add_data, text="Add", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnupdate=Button(btn_frame,command=self.update, text="Update", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnupdate.grid(row=0, column=1, padx=1)

        btnDelete=Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset=Button(btn_frame, text="Reset", command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)
        
        # ===========================================Right Side Image======================================
        img3=Image.open(r"img\bed.jpg")
        img3=img3.resize((520,300), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        labImg=Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        labImg.place(x=760, y=55, width=520, height=300)
        
        
        # =============================================Table Frame search system============================================
        Table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View details and search system", font=("times new roman", 12, "bold"), padx=2)
        Table_frame.place(x=435, y=280, width=860, height=260)

        lbl_searchby=Label(Table_frame, text="Search By:", font=("arial", 12, "bold"), bg="red", fg="white")
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)
        
        self.search_variable=StringVar()

        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_variable, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"]=("Contact", "Rooms")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(Table_frame,textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtsearch.grid(row=0, column=2, padx=2)



        btnsearch=Button(Table_frame, text="Search",  command=self.search, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall=Button(Table_frame, text="Show All", command=self.fetch_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnshowall.grid(row=0, column=4, padx=1)
        
        # =============================================Show Data Table===================================

        details_table=Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)


        scroll_x=ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table, columns=(
                                                    "contact", 
                                                    "checkin", 
                                                    "checkout", 
                                                    "roomtype", 
                                                    "roomavailable",
                                                    "meal",
                                                    "noOfdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-ou")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="NoOfDays")
        

        self.room_table["show"]="headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfdays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
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
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_contact.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomavailable.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
        
    # ==============================Fetch Data====================================
    def fetch_data(self):
        conn=mysql.connector.connect(
                                host = 'localhost',
                                username = 'root',
                                password = '1234',
                                database = 'team'
                                )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
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
        
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
    
    # ========================Update=============================
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Mobile",parent=self.root)
        else:
            conn=mysql.connector.connect(
                                host="localhost",
                                username='root',
                                password='1234',
                                database='team'    
                                    )
            my_cursor=conn.cursor()
            my_cursor.execute('''update room set 
                              check_in=%s,
                              check_out=%s,
                              roomtype=%s,
                              roomavailable=%s,
                              meal=%s,
                              noOfdays=%s
                              where Contact=%s
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
        mDelete=messagebox.askyesno("Hotel Management system","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(
                                host='localhost',
                                username='root',
                                password='1234',
                                database='team'    
                                    )
            my_cursor=conn.cursor()
            query="Delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        
    # Search System
    def search(self):
        conn=mysql.connector.connect(
                                host="localhost",
                                username='root',
                                password='1234',
                                database='team'    
                                    )
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_variable.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
        for i in rows:
            self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        
        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=='luxury'):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=='double'):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=='single'):
            q1=float(300)
            q2=float(250)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=='luxury'):
            q1=float(350)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=='double'):
            q1=float(350)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=='single'):
            q1=float(350)
            q2=float(250)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=='luxury'):
            q1=float(400)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=='Double'):
            q1=float(400)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=='single'):
            q1=float(400)
            q2=float(250)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=='Duplex'):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1 + q2)
            q5=float(q3 + q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
            
    # ======================================All Data Frame===========================
    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error","Please enter the Contact Number",parent=self.root)
        else:
            conn = mysql.connector.connect(
                                        host = 'localhost',
                                        user = 'root',
                                        password = '1234',
                                        database = 'team'
                                        )
            my_cursor = conn.cursor()
            query = ("Select Name from customer where Mobile = %s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row == None:
                messagebox.showerror("Error",'This number not found',parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)
                
                lblName = Label(showDataFrame,text="Name:",font=('arial',12,'bold'))
                lblName.place(x=0,y=0)

                lbl = Label(showDataFrame,text=row,font=('arial',12,'bold'))
                lbl.place(x=75,y=0)
                
            # ================================Gender==================================
            conn = mysql.connector.connect(
                                        host = 'localhost',
                                        user = 'root',
                                        password = '1234',
                                        database = 'team'
                                        )
            my_cursor = conn.cursor()
            query = ("Select Gender from customer where Mobile = %s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lblGender = Label(showDataFrame,text="Gender:",font=('arial',12,'bold'))
            lblGender.place(x=0,y=30)

            lbl2 = Label(showDataFrame,text=row,font=('arial',12,'bold'))
            lbl2.place(x=75,y=30)
            
            # ================================Email==============================
            conn = mysql.connector.connect(
                                        host = 'localhost',
                                        user = 'root',
                                        password = '1234',
                                        database = 'team'
                                        )
            my_cursor = conn.cursor()
            query = ("Select Email from customer where Mobile = %s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lblEmail = Label(showDataFrame,text="Email:",font=('arial',12,'bold'))
            lblEmail.place(x=0,y=60)

            lbl3 = Label(showDataFrame,text=row,font=('arial',10,'bold'))
            lbl3.place(x=75,y=60)
            
            # ==========================Nationality============================
            conn = mysql.connector.connect(
                                        host = 'localhost',
                                        user = 'root',
                                        password = '1234',
                                        database = 'team'
                                        )
            my_cursor = conn.cursor()
            query = ("Select Nationality from customer where Mobile = %s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lblNationality = Label(showDataFrame,text="Nationality:",font=('arial',12,'bold'))
            lblNationality.place(x=0,y=90)

            lbl4 = Label(showDataFrame,text=row,font=('arial',10,'bold'))
            lbl4.place(x=75,y=90)
            
            # ==========================Address============================
            conn = mysql.connector.connect(
                                        host = 'localhost',
                                        user = 'root',
                                        password = '1234',
                                        database = 'team'
                                        )
            my_cursor = conn.cursor()
            query = ("Select Address from customer where Mobile = %s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lblAddress = Label(showDataFrame,text="Address:",font=('arial',12,'bold'))
            lblAddress.place(x=0,y=120)

            lbl5 = Label(showDataFrame,text=row,font=('arial',10,'bold'))
            lbl5.place(x=75,y=120)
        
if __name__ == "__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()