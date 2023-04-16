from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector
import random

'''
CREATE DATABASE team
USE team
CREATE TABLE `team`.`customer` (
  `Ref` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Mother` VARCHAR(45) NULL,
  `Gender` VARCHAR(45) NULL,
  `PostCode` VARCHAR(45) NULL,
  `Mobile` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `Nationality` VARCHAR(45) NULL,
  `Id_Proof` VARCHAR(45) NULL,
  `Id_Number` VARCHAR(45) NULL,
  `Address` VARCHAR(100) NULL,
  PRIMARY KEY (`Ref`));
'''

class Customers:
    def __init__(self, root):
        self.root=root
        self.root.title("HOTEL")
        self.root.geometry("1295x560+230+220")
        
        
        # ============================Variables========================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        

        # =========================Title============================
        lbl_title=Label(self.root, text="Add New Costumer Details", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ==========================Logo=============================
        img2=Image.open(r"img\logo_for_hotelBot.jpg")
        img2=img2.resize((100, 50), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        labImg=Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        labImg.place(x=0, y=0, width=100, height=50)


        img3=Image.open(r"img\customer.jpg")
        img3=img3.resize((100, 50), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        labImg=Label(self.root, image=self.photoimg3, bd=2, relief=RIDGE)
        labImg.place(x=100, y=0, width=100, height=50)
        
        
        # ===================================labelFrame==========================
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ==================================label and entry========================
        # Customer Reference Id
        lbl_cust_ref=Label(labelframeleft, text="Customer Ref:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref=ttk.Entry(labelframeleft, width=29,textvariable=self.var_ref, font=("arial", 13, "bold"),state="readonly")
        entry_ref.grid(row=0, column=1)

        # Customer Name
        cname=Label(labelframeleft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname=ttk.Entry(labelframeleft, width=29,textvariable=self.var_cust_name, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)

        # Mother Name
        lbl_mname=Label(labelframeleft, text="Mother Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mname.grid(row=2, column=0, sticky=W)
        txtmname=ttk.Entry(labelframeleft, width=29,textvariable=self.var_mother, font=("arial", 13, "bold"))
        txtmname.grid(row=2, column=1)

        # Gender
        lbl_gender=Label(labelframeleft, text="Gender", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)
        combo_gender=ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=27, textvariable=self.var_gender , state="readonly")
        combo_gender["value"]=("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # postcode
        lbl_Postcode=Label(labelframeleft, text="Postcode:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_Postcode.grid(row=4, column=0, sticky=W)
        txtpostcode=ttk.Entry(labelframeleft, width=29,textvariable=self.var_post, font=("arial", 13, "bold"))
        txtpostcode.grid(row=4, column=1)

        # mobile
        lbl_mobile=Label(labelframeleft, text="Mobile:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mobile.grid(row=5, column=0, sticky=W)
        txtmobile=ttk.Entry(labelframeleft, width=29, textvariable=self.var_mobile , font=("arial", 13, "bold"))
        txtmobile.grid(row=5, column=1)

        # email
        lbl_email=Label(labelframeleft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=6, column=0, sticky=W)
        txtemail=ttk.Entry(labelframeleft, width=29, textvariable=self.var_email, font=("arial", 13, "bold"))
        txtemail.grid(row=6, column=1)

        # id_proof
        lbl_Idproof=Label(labelframeleft, text="Id Proof:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_Idproof.grid(row=7, column=0, sticky=W)
        combo_id=ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=27, textvariable=self.var_id_proof , state="readonly")
        combo_id["value"]=("Aadhar Card", "Pan Card", "Passport")
        combo_id.current(0)
        combo_id.grid(row=7, column=1)


        # nationality
        lbl_nationality=Label(labelframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_nationality.grid(row=8, column=0, sticky=W)
        combo_nationality=ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=27, textvariable=self.var_nationality , state="readonly")
        combo_nationality["value"]=("India", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia (formerly Macedonia)", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates (UAE)", "United Kingdom (UK)", "United States of America (USA)", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City (Holy See)", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe")
        combo_nationality.current(0)
        combo_nationality.grid(row=8, column=1)


        # idproof
        lbl_idnumber=Label(labelframeleft, text="Id Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_idnumber.grid(row=9, column=0, sticky=W)
        txtidnumber=ttk.Entry(labelframeleft, width=29, textvariable=self.var_id_number , font=("arial", 13, "bold"))
        txtidnumber.grid(row=9, column=1)

        # address
        lbl_Address=Label(labelframeleft, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_Address.grid(row=10, column=0, sticky=W)
        txtaddress=ttk.Entry(labelframeleft, width=29, textvariable=self.var_address , font=("arial", 13, "bold"))
        txtaddress.grid(row=10, column=1)

        # ==========================================btns=======================
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd=Button(btn_frame, text="Add",command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnupdate=Button(btn_frame, text="Update",command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnupdate.grid(row=0, column=1, padx=1)

        btnDelete=Button(btn_frame, text="Delete",command=self.mDelete, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset=Button(btn_frame, text="Reset",command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)


        # =============================================Table Frame search system============================================
        Table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View details and search system", font=("times new roman", 12, "bold"), padx=2)
        Table_frame.place(x=435, y=50, width=860, height=490)

        lbl_searchby=Label(Table_frame, text="Search By:", font=("arial", 12, "bold"), bg="red", fg="white")
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)
        
        self.search_variable=StringVar()

        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_variable, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"]=("Mobile", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(Table_frame,textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtsearch.grid(row=0, column=2, padx=2)



        btnsearch=Button(Table_frame, text="Search",command=self.search, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall=Button(Table_frame, text="Show All",command=self.fetch_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnshowall.grid(row=0, column=4, padx=1)


        # =============================================Show Data Table===================================

        details_table=Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)


        scroll_x=ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_detail_table=ttk.Treeview(details_table, columns=("ref", "Name", "Father", "Gender", "Pincode", "Mobile", "Email", "id Proof", "Nationality", "Id Number", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_detail_table.xview)
        scroll_y.config(command=self.Cust_detail_table.yview)

        self.Cust_detail_table.heading("ref", text="Refer No")
        self.Cust_detail_table.heading("Name", text="Name")
        self.Cust_detail_table.heading("Father", text="Father")
        self.Cust_detail_table.heading("Gender", text="Gender")
        self.Cust_detail_table.heading("Pincode", text="Pincode")
        self.Cust_detail_table.heading("Mobile", text="Mobile")
        self.Cust_detail_table.heading("Email", text="Email")
        self.Cust_detail_table.heading("id Proof", text="Id Proof")
        self.Cust_detail_table.heading("Nationality", text="Nationality") 
        self.Cust_detail_table.heading("Id Number", text="Id Number")
        self.Cust_detail_table.heading("Address", text="Address")

        self.Cust_detail_table["show"]="headings"

        self.Cust_detail_table.column("ref", width=100)
        self.Cust_detail_table.column("Name", width=100)
        self.Cust_detail_table.column("Father", width=100)
        self.Cust_detail_table.column("Gender", width=100)
        self.Cust_detail_table.column("Pincode", width=100)
        self.Cust_detail_table.column("Mobile", width=100)
        self.Cust_detail_table.column("Email", width=100)
        self.Cust_detail_table.column("id Proof", width=100)
        self.Cust_detail_table.column("Nationality", width=100)
        self.Cust_detail_table.column("Id Number", width=100)
        self.Cust_detail_table.column("Address", width=100)


        self.Cust_detail_table.pack(fill=BOTH, expand=1)
        self.Cust_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
        # if len(str(a)) != 10:
        #     messagebox.showerror("Error","Please enter proper Mobile",parent=self.root)
    def add_data(self):
        if self.var_mother.get()=="" or self.var_mother.get()=="":
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
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_ref.get(),
                                                                                    self.var_cust_name.get(),
                                                                                    self.var_mother.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_post.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_id_proof.get(),
                                                                                    self.var_id_number.get(),
                                                                                    self.var_address.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
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
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_detail_table.delete(*self.Cust_detail_table.get_children())
            for i in rows:
                self.Cust_detail_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.Cust_detail_table.focus()
        content=self.Cust_detail_table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])
    
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter Mobile",parent=self.root)
        else:
            conn=mysql.connector.connect(
                                host="localhost",
                                username='root',
                                password='1234',
                                database='team'    
                                    )
            my_cursor=conn.cursor()
            my_cursor.execute('''update customer set 
                              Name=%s,
                              Mother=%s,
                              Gender=%s,
                              PostCode=%s,
                              Mobile=%s,
                              Email=%s,
                              Nationality=%s,
                              Id_Proof=%s,
                              Id_Number=%s,
                              Address=%s 
                              where Ref = %s
                              ''',(
                                    self.var_cust_name.get(),
                                    self.var_mother.get(),
                                    self.var_gender.get(),
                                    self.var_post.get(),
                                    self.var_mobile.get(),
                                    self.var_email.get(),
                                    self.var_nationality.get(),
                                    self.var_id_proof.get(),
                                    self.var_id_number.get(),
                                    self.var_address.get(),
                                    self.var_ref.get()
                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully")

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
            query="Delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    
    def reset(self):
        self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(
                                host="localhost",
                                username='root',
                                password='1234',
                                database='team'    
                                    )
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_variable.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_detail_table.delete(*self.Cust_detail_table.get_children())
        for i in rows:
            self.Cust_detail_table.insert("",END,values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root=Tk()
    obj=Customers(root)
    root.mainloop()