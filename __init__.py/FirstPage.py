from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# from main import HotelManagementSystem


class Option:
    def __init__(self, root):
        self.root=root
        self.root.title("HotelBot")
        self.root.geometry("1550x800+0+0")
        root.config(bg='#2fbdef')

        lbl_title=Label(self.root, text="Use as Admin or Cutomer", font=("times new roman", 40, "bold"), bg="#148de4", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=2, width=1550, height=50)

        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Admin", font=("times new roman", 20, "bold"), padx=2, bg='#148de4')
        labelframeleft.place(x=5, y=55, width=700, height=700)

        labelframeright=LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer", font=("times new roman", 20, "bold"), padx=2, bg='#148de4')
        labelframeright.place(x=810, y=55, width=700, height=700)

        def loginadmin():
            root.destroy()
            from PIL import ImageTk, Image
            from tkinter import messagebox
            import mysql.connector

            from main import HotelManagementSystem  # type "Pip install pillow" in your terminal to install ImageTk and Image module


            window = Tk()
            window.rowconfigure(0, weight=1)
            window.columnconfigure(0, weight=1)
            window.state('zoomed')
            window.resizable(0, 0)
            window.title('Login and Registration Page')

            # Window Icon Photo
            icon = PhotoImage(file='img\\pic-icon.png')
            window.iconphoto(True, icon)

            LoginPage = Frame(window)
            RegistrationPage = Frame(window)

            for frame in (LoginPage, RegistrationPage):
                frame.grid(row=0, column=0, sticky='nsew')


            def show_frame(frame):
                frame.tkraise()


            show_frame(LoginPage)

            # ==================== LOGIN PAGE =====================================================================================

            design_frame1 = Listbox(LoginPage, bg='#0c71b9', width=150, height=50, highlightthickness=0, borderwidth=0)
            design_frame1.place(x=0, y=0)

            design_frame2 = Listbox(LoginPage, bg='#1e85d0', width=150, height=50, highlightthickness=0, borderwidth=0)
            design_frame2.place(x=676, y=0)

            design_frame3 = Listbox(LoginPage, bg='#1e85d0', width=115, height=40, highlightthickness=0, borderwidth=0)
            design_frame3.place(x=75, y=106)

            design_frame4 = Listbox(LoginPage, bg='#f8f8f8', width=115, height=40, highlightthickness=0, borderwidth=0)
            design_frame4.place(x=676, y=106)

            # =========================Text Vairable=============================
            Email_id1 = StringVar()
            Password1 = StringVar()

            # ====== Email ====================
            email_entry = Entry(design_frame4, fg="#a7a7a7", textvariable=Email_id1, font=("yu gothic ui semibold", 12), highlightthickness=2)
            email_entry.place(x=134, y=170, width=256, height=34)
            email_entry.config(highlightbackground="black", highlightcolor="black")
            email_label = Label(design_frame4, text='• Email account', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
            email_label.place(x=130, y=140)

            # ==== Password ==================
            password_entry1 = Entry(design_frame4, fg="#a7a7a7", textvariable=Password1, font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
            password_entry1.place(x=134, y=250, width=256, height=34)
            password_entry1.config(highlightbackground="black", highlightcolor="black")
            password_label = Label(design_frame4, text='• Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
            password_label.place(x=130, y=220)


            # function for show and hide password
            def password_command():
                if password_entry1.cget('show') == '•':
                    password_entry1.config(show='')
                else:
                    password_entry1.config(show='•')


            # ====== checkbutton ==============
            checkButton = Checkbutton(design_frame4, bg='#f8f8f8', command=password_command, text='show password')
            checkButton.place(x=140, y=288)

            # ========= Buttons ===============
            SignUp_button = Button(LoginPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                                command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
            SignUp_button.place(x=1100, y=175)

            # ===== Welcome Label ==============
            welcome_label = Label(design_frame4, text='Admin', font=('Arial', 20, 'bold'), bg='#f8f8f8')
            welcome_label.place(x=130, y=15)

            # ======= top Login Button =========

            def thankyou():
                if Email_id1.get() =="" or Password1.get() =="":
                    messagebox.showerror("Error","Please fill all the details")
                else:
                    my_db = mysql.connector.connect(
                                                host = 'localhost',
                                                user = 'root',
                                                password = '1234',
                                                database = 'team'
                                                )
                    my_cursor = my_db.cursor()
                    my_cursor.execute("select Password from signup where `Email Id`= %s",(Email_id1.get(),))
                    row1 = my_cursor.fetchone()
                    # my_cursor.execute("insert into verify values(%s)",(str(row1[0])))
                    my_db.commit()
                    if str(Password1.get()) == str(row1[0]):
                        window.destroy()
                        root = Tk()
                        obj = HotelManagementSystem(root)
                        root.mainloop()
                    
                    else:
                        messagebox.showerror("Error","Please enter the correct Password")
                    my_db.close()


            login_button = Button(LoginPage, text='Login',command=thankyou, font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                                borderwidth=0, activebackground='#1b87d2', cursor='hand2')
            login_button.place(x=845, y=175)

            login_line = Canvas(LoginPage, width=60, height=5, bg='#1b87d2')
            login_line.place(x=840, y=203)

            # ==== LOGIN  down button ============
            loginBtn1 = Button(design_frame4, fg='#f8f8f8', text='Login',command=thankyou, bg='#1b87d2', font=("yu gothic ui bold", 15),
                            cursor='hand2', activebackground='#1b87d2')
            loginBtn1.place(x=133, y=340, width=256, height=50)


            # ======= ICONS =================

            # ===== Email icon =========
            email_icon = Image.open('img\\email-icon.png')
            photo = ImageTk.PhotoImage(email_icon)
            emailIcon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
            emailIcon_label.image = photo
            emailIcon_label.place(x=105, y=174)

            # ===== password icon =========
            password_icon = Image.open('img\\pass-icon.png')
            photo = ImageTk.PhotoImage(password_icon)
            password_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
            password_icon_label.image = photo
            password_icon_label.place(x=105, y=254)

            # ===== picture icon =========
            picture_icon = Image.open('img\\pic-icon.png')
            photo = ImageTk.PhotoImage(picture_icon)
            picture_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
            picture_icon_label.image = photo
            picture_icon_label.place(x=280, y=5)

            # ===== Left Side Picture ============
            side_image = Image.open('img\\lock2.jpg')
            resized = side_image.resize((625, 650), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(resized)
            side_image_label = Label(design_frame3, image=photo, bg='#1e85d0')
            side_image_label.image = photo
            side_image_label.place(x=0, y=0)


            # === FORGOT PASSWORD  PAGE =========================================================================================

            def forgot_password():
                win = Toplevel()
                window_width = 350
                window_height = 350
                screen_width = win.winfo_screenwidth()
                screen_height = win.winfo_screenheight()
                position_top = int(screen_height / 4 - window_height / 4)
                position_right = int(screen_width / 2 - window_width / 2)
                win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
                win.title('Forgot Password')
                win.iconbitmap('img\\aa.ico')
                win.configure(background='#f8f8f8')
                win.resizable(0, 0)

                # =================Text Variable2=================
                Email_id2 = StringVar()
                password2 = StringVar()
                confirm_password1 = StringVar()

                # ====== Email ====================
                email_entry2 = Entry(win, fg="#a7a7a7", textvariable=Email_id2, font=("yu gothic ui semibold", 12), highlightthickness=2)
                email_entry2.place(x=40, y=30, width=256, height=34)
                email_entry2.config(highlightbackground="black", highlightcolor="black")
                email_label2 = Label(win, text='• Email account', fg="#89898b", bg='#f8f8f8',
                                    font=("yu gothic ui", 11, 'bold'))
                email_label2.place(x=40, y=0)

                # ====  New Password ==================
                new_password_entry = Entry(win, fg="#a7a7a7", textvariable=password2, font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
                new_password_entry.place(x=40, y=110, width=256, height=34)
                new_password_entry.config(highlightbackground="black", highlightcolor="black")
                new_password_label = Label(win, text='• New Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
                new_password_label.place(x=40, y=80)

                # ====  Confirm Password ==================
                confirm_password_entry = Entry(win, fg="#a7a7a7", textvariable=confirm_password1, font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
                confirm_password_entry.place(x=40, y=190, width=256, height=34)
                confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
                confirm_password_label = Label(win, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                            font=("yu gothic ui", 11, 'bold'))
                confirm_password_label.place(x=40, y=160)

                def update():
                    if Email_id2.get() == "" or password2.get() == "" or confirm_password1.get() == "":
                        messagebox.showerror("Error", "Please all the details")
                    else:
                        my_db = mysql.connector.connect(
                                                    host = 'localhost',
                                                    user = 'root',
                                                    password = '1234',
                                                    database = 'team'
                                                        )
                        my_cursor = my_db.cursor()
                        my_cursor.execute("update signup set password = %s where `Email Id`=%s",(password2.get(), Email_id2.get()))
                        my_db.commit()
                        my_db.close()
                        messagebox.showinfo("Success","Succesfully updated the password")

                # ======= Update password Button ============
                update_pass = Button(win, fg='#f8f8f8', text='Update Password',command=update, bg='#1b87d2', font=("yu gothic ui bold", 14),
                                    cursor='hand2', activebackground='#1b87d2')
                update_pass.place(x=40, y=240, width=256, height=50)


            forgotPassword = Button(design_frame4, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
                                    borderwidth=0, activebackground='#f8f8f8', command=lambda: forgot_password(), cursor="hand2")
            forgotPassword.place(x=290, y=290)


            # ==================== REGISTRATION PAGE ==============================================================================

            design_frame5 = Listbox(RegistrationPage, bg='#0c71b9', width=150, height=50, highlightthickness=0, borderwidth=0)
            design_frame5.place(x=0, y=0)

            design_frame6 = Listbox(RegistrationPage, bg='#1e85d0', width=150, height=50, highlightthickness=0, borderwidth=0)
            design_frame6.place(x=676, y=0)

            design_frame7 = Listbox(RegistrationPage, bg='#1e85d0', width=115, height=40, highlightthickness=0, borderwidth=0)
            design_frame7.place(x=75, y=106)

            design_frame8 = Listbox(RegistrationPage, bg='#f8f8f8', width=115, height=40, highlightthickness=0, borderwidth=0)
            design_frame8.place(x=676, y=106)

            # ============================= Text variables ====================
            Username = StringVar()
            Email_id = StringVar()
            password = StringVar()
            confirm_password = StringVar()

            # ==== Full Name =======
            name_entry = Entry(design_frame8, fg="#a7a7a7",textvariable=Username, font=("yu gothic ui semibold", 12), highlightthickness=2)
            name_entry.place(x=284, y=150, width=286, height=34)
            name_entry.config(highlightbackground="black", highlightcolor="black")
            name_label = Label(design_frame8, text='•Full Name', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
            name_label.place(x=280, y=120)

            # ======= Email ===========
            email_entry = Entry(design_frame8, fg="#a7a7a7",textvariable=Email_id,  font=("yu gothic ui semibold", 12), highlightthickness=2)
            email_entry.place(x=284, y=220, width=286, height=34)
            email_entry.config(highlightbackground="black", highlightcolor="black")
            email_label = Label(design_frame8, text='•Email', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
            email_label.place(x=280, y=190)

            # ====== Password =========
            password_entry = Entry(design_frame8, fg="#a7a7a7",textvariable=password,  font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
            password_entry.place(x=284, y=295, width=286, height=34)
            password_entry.config(highlightbackground="black", highlightcolor="black")
            password_label = Label(design_frame8, text='• Password', fg="#89898b", bg='#f8f8f8',
                                font=("yu gothic ui", 11, 'bold'))
            password_label.place(x=280, y=265)


            def password_command2():
                if password_entry.cget('show') == '•':
                    password_entry.config(show='')
                else:
                    password_entry.config(show='•')


            checkButton = Checkbutton(design_frame8, bg='#f8f8f8', command=password_command2, text='show password')
            checkButton.place(x=290, y=330)


            # ====== Confirm Password =============
            confirmPassword_entry = Entry(design_frame8, fg="#a7a7a7",textvariable=confirm_password, font=("yu gothic ui semibold", 12), highlightthickness=2)
            confirmPassword_entry.place(x=284, y=385, width=286, height=34)
            confirmPassword_entry.config(highlightbackground="black", highlightcolor="black")
            confirmPassword_label = Label(design_frame8, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                        font=("yu gothic ui", 11, 'bold'))
            confirmPassword_label.place(x=280, y=355)

            # =======================SignUP Function===============================
            # Username = name_entry.get()
            # Email_id = email_entry.get()
            # password = password_entry.get()
            # confirm_password = confirmPassword_entry.get()
            def signup():
                if Username.get()=="" or Email_id.get() =="" or password.get() =="" or confirm_password.get() == "":
                    # print(Username)
                    # print(Email_id)
                    # print(password)
                    # print(confirm_password)
                    messagebox.showerror("Error", "Please fill all the details")
                elif password.get() == confirm_password.get():
                    my_db = mysql.connector.connect(
                                                host = 'localhost',
                                                user = 'root',
                                                password = '1234',
                                                database = 'team'
                                                )
                    my_cursor = my_db.cursor()
                    my_cursor.execute("insert into signup values(%s, %s, %s)",(
                                                                    Username.get(),
                                                                    Email_id.get(),
                                                                    password.get()
                                                                    ))
                    my_db.commit()
                    my_db.close()
                    messagebox.showinfo("Success","Thankyou for signup")
                else:
                    messagebox.showerror("Error", "Please enter the password properly")
            # ========= Buttons ====================

            SignUp_button = Button(RegistrationPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                                command=lambda: show_frame(LoginPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
            SignUp_button.place(x=1100, y=175)

            SignUp_line = Canvas(RegistrationPage, width=60, height=5, bg='#1b87d2')
            SignUp_line.place(x=1100, y=203)


            # ===== Welcome Label ==================
            welcome_label = Label(design_frame8, text='Admin', font=('Arial', 20, 'bold'), bg='#f8f8f8')
            welcome_label.place(x=130, y=15)

            # ========= Login Button =========
            login_button = Button(RegistrationPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                                borderwidth=0, activebackground='#1b87d2', command=lambda: show_frame(LoginPage), cursor='hand2')
            login_button.place(x=845, y=175)

            # ==== SIGN UP down button ============
            signUp2 = Button(design_frame8, fg='#f8f8f8', text='Sign Up', command=signup, bg='#1b87d2', font=("yu gothic ui bold", 15),
                            cursor='hand2', activebackground='#1b87d2')
            signUp2.place(x=285, y=435, width=286, height=50)

            # ===== password icon =========
            password_icon = Image.open('img\\pass-icon.png')
            photo = ImageTk.PhotoImage(password_icon)
            password_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
            password_icon_label.image = photo
            password_icon_label.place(x=255, y=300)

            # ===== confirm password icon =========
            confirmPassword_icon = Image.open('img\\pass-icon.png')
            photo = ImageTk.PhotoImage(confirmPassword_icon)
            confirmPassword_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
            confirmPassword_icon_label.image = photo
            confirmPassword_icon_label.place(x=255, y=390)

            # ===== Email icon =========
            email_icon = Image.open('img\\email-icon.png')
            photo = ImageTk.PhotoImage(email_icon)
            emailIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
            emailIcon_label.image = photo
            emailIcon_label.place(x=255, y=225)

            # ===== Full Name icon =========
            name_icon = Image.open('img\\name-icon.png')
            photo = ImageTk.PhotoImage(name_icon)
            nameIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
            nameIcon_label.image = photo
            nameIcon_label.place(x=252, y=153)

            # ===== picture icon =========
            picture_icon = Image.open('img\\pic-icon.png')
            photo = ImageTk.PhotoImage(picture_icon)
            picture_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
            picture_icon_label.image = photo
            picture_icon_label.place(x=280, y=5)

            # ===== Left Side Picture ============
            side_image = Image.open('img\\lock2.jpg')
            resized = side_image.resize((625, 650), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(resized)
            side_image_label = Label(design_frame7, image=photo, bg='#1e85d0')
            side_image_label.image = photo
            side_image_label.place(x=0, y=0)





            window.mainloop()
              
        side_image = Image.open('img\\admin_logo1.png')
        resized = side_image.resize((685, 650), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized)
        side_image_label = Label(labelframeleft, image=photo, bg='#1e85d0')
        side_image_label.image = photo
        my_btn = Button(labelframeleft,command=loginadmin, image=photo)
        my_btn.pack()
        side_image_label.place(x=0, y=0)
        
        def customerlogin():
            root.destroy()
            from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
            from main import HotelManagementSystem
            import os

            window = Tk()
            window.rowconfigure(0, weight=1)
            window.columnconfigure(0, weight=1)
            window.state('zoomed')
            window.resizable(0, 0)
            window.title('Login and Registration Page')

            # Window Icon Photo
            icon = PhotoImage(file='img\\pic-icon.png')
            window.iconphoto(True, icon)

            LoginPage = Frame(window)
            RegistrationPage = Frame(window)

            for frame in (LoginPage, RegistrationPage):
                frame.grid(row=0, column=0, sticky='nsew')


            def show_frame(frame):
                frame.tkraise()


            show_frame(LoginPage)

            # ==================== LOGIN PAGE =====================================================================================

            design_frame1 = Listbox(LoginPage, bg='#0c71b9', width=150, height=50, highlightthickness=0, borderwidth=0)
            design_frame1.place(x=0, y=0)

            design_frame2 = Listbox(LoginPage, bg='#1e85d0', width=150, height=50, highlightthickness=0, borderwidth=0)
            design_frame2.place(x=676, y=0)

            design_frame3 = Listbox(LoginPage, bg='#1e85d0', width=115, height=40, highlightthickness=0, borderwidth=0)
            design_frame3.place(x=75, y=106)

            design_frame4 = Listbox(LoginPage, bg='#f8f8f8', width=115, height=40, highlightthickness=0, borderwidth=0)
            design_frame4.place(x=676, y=106)

            # ================ Text Variable =====================
            Email_id1 = StringVar()
            Password1 = StringVar()
            
            # ====== Email ====================
            email_entry = Entry(design_frame4, fg="#a7a7a7", textvariable=Email_id1, font=("yu gothic ui semibold", 12), highlightthickness=2)
            email_entry.place(x=134, y=170, width=256, height=34)
            email_entry.config(highlightbackground="black", highlightcolor="black")
            email_label = Label(design_frame4, text='• Email account', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
            email_label.place(x=130, y=140)

            # ==== Password ==================
            password_entry1 = Entry(design_frame4, fg="#a7a7a7", textvariable= Password1, font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
            password_entry1.place(x=134, y=250, width=256, height=34)
            password_entry1.config(highlightbackground="black", highlightcolor="black")
            password_label = Label(design_frame4, text='• Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
            password_label.place(x=130, y=220)


            # function for show and hide password
            def password_command():
                if password_entry1.cget('show') == '•':
                    password_entry1.config(show='')
                else:
                    password_entry1.config(show='•')


            # ====== checkbutton ==============
            checkButton = Checkbutton(design_frame4, bg='#f8f8f8', command=password_command, text='show password')
            checkButton.place(x=140, y=288)

            # ========= Buttons ===============
            SignUp_button = Button(LoginPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                                command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
            SignUp_button.place(x=1100, y=175)

            # ===== Welcome Label ==============
            welcome_label = Label(design_frame4, text='Customer', font=('Arial', 20, 'bold'), bg='#f8f8f8')
            welcome_label.place(x=130, y=15)
            
            
            # ======= top Login Button =========

            def thankyou():
                if Email_id1.get() =="" or Password1.get() =="":
                    messagebox.showerror("Error","Please fill all the details")
                else:
                    my_db = mysql.connector.connect(
                                                host = 'localhost',
                                                user = 'root',
                                                password = '1234',
                                                database = 'team'
                                                )
                    my_cursor = my_db.cursor()
                    my_cursor.execute("select Password from csignup where `Email Id`= %s",(Email_id1.get(),))
                    row1 = my_cursor.fetchone()
                    # my_cursor.execute("insert into verify values(%s)",(str(row1[0])))
                    # my_db.commit()
                    if str(Password1.get()) == str(row1[0]):
                        window.destroy()
                        # root = Tk()
                        # obj = HotelManagementSystem(root)
                        # root.mainloop()
                        # os.system(f'python {"Y:/PythonProject-project/__init__.py/JarvisGUI/jarvis.py"}')
                        os.system(f'python {"JarvisGUI/jarvis.py"}')
                    
                    else:
                        messagebox.showerror("Error","Please enter the correct Password")
                    my_db.close()

            # ======= top Login Button =========
            login_button = Button(LoginPage, text='Login',  font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                                borderwidth=0, activebackground='#1b87d2', cursor='hand2')
            login_button.place(x=845, y=175)

            login_line = Canvas(LoginPage, width=60, height=5, bg='#1b87d2')
            login_line.place(x=840, y=203)

            # ==== LOGIN  down button ============
            loginBtn1 = Button(design_frame4, fg='#f8f8f8', command=thankyou,  text='Login', bg='#1b87d2', font=("yu gothic ui bold", 15),
                            cursor='hand2', activebackground='#1b87d2')
            loginBtn1.place(x=133, y=340, width=256, height=50)


            # ======= ICONS =================

            # ===== Email icon =========
            email_icon = Image.open('img\\email-icon.png')
            photo = ImageTk.PhotoImage(email_icon)
            emailIcon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
            emailIcon_label.image = photo
            emailIcon_label.place(x=105, y=174)

            # ===== password icon =========
            password_icon = Image.open('img\\pass-icon.png')
            photo = ImageTk.PhotoImage(password_icon)
            password_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
            password_icon_label.image = photo
            password_icon_label.place(x=105, y=254)

            # ===== picture icon =========
            picture_icon = Image.open('img\\pic-icon.png')
            photo = ImageTk.PhotoImage(picture_icon)
            picture_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
            picture_icon_label.image = photo
            picture_icon_label.place(x=280, y=5)

            # ===== Left Side Picture ============
            side_image = Image.open('img\\lock2.jpg')
            resized = side_image.resize((625, 650), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(resized)
            side_image_label = Label(design_frame3, image=photo, bg='#1e85d0')
            side_image_label.image = photo
            side_image_label.place(x=0, y=0)


            # === FORGOT PASSWORD  PAGE =========================================================================================

            def forgot_password():
                win = Toplevel()
                window_width = 350
                window_height = 350
                screen_width = win.winfo_screenwidth()
                screen_height = win.winfo_screenheight()
                position_top = int(screen_height / 4 - window_height / 4)
                position_right = int(screen_width / 2 - window_width / 2)
                win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
                win.title('Forgot Password')
                win.iconbitmap('img\\aa.ico')
                win.configure(background='#f8f8f8')
                win.resizable(0, 0)

                # ======================= Text Variable ==========================
                Email_id2 = StringVar()
                password2 = StringVar()
                confirm_password1 = StringVar()
                
                # ====== Email ====================
                email_entry2 = Entry(win, fg="#a7a7a7", textvariable=  Email_id2, font=("yu gothic ui semibold", 12), highlightthickness=2)
                email_entry2.place(x=40, y=30, width=256, height=34)
                email_entry2.config(highlightbackground="black", highlightcolor="black")
                email_label2 = Label(win, text='• Email account', fg="#89898b", bg='#f8f8f8',
                                    font=("yu gothic ui", 11, 'bold'))
                email_label2.place(x=40, y=0)

                # ====  New Password ==================
                new_password_entry = Entry(win, fg="#a7a7a7", textvariable= password2, font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
                new_password_entry.place(x=40, y=110, width=256, height=34)
                new_password_entry.config(highlightbackground="black", highlightcolor="black")
                new_password_label = Label(win, text='• New Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
                new_password_label.place(x=40, y=80)

                # ====  Confirm Password ==================
                confirm_password_entry = Entry(win, fg="#a7a7a7",textvariable=confirm_password1, font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
                confirm_password_entry.place(x=40, y=190, width=256, height=34)
                confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
                confirm_password_label = Label(win, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                            font=("yu gothic ui", 11, 'bold'))
                confirm_password_label.place(x=40, y=160)
                
                def update():
                    if Email_id2.get() == "" or password2.get() == "" or confirm_password1.get() == "":
                        messagebox.showerror("Error", "Please all the details")
                    else:
                        my_db = mysql.connector.connect(
                                                    host = 'localhost',
                                                    user = 'root',
                                                    password = '1234',
                                                    database = 'team'
                                                        )
                        my_cursor = my_db.cursor()
                        my_cursor.execute("update csignup set password = %s where `Email Id`=%s",(password2.get(), Email_id2.get()))
                        my_db.commit()
                        my_db.close()
                        messagebox.showinfo("Success","Succesfully updated the password")

                # ======= Update password Button ============
                update_pass = Button(win, fg='#f8f8f8', command=update, text='Update Password', bg='#1b87d2', font=("yu gothic ui bold", 14),
                                    cursor='hand2', activebackground='#1b87d2')
                update_pass.place(x=40, y=240, width=256, height=50)


            forgotPassword = Button(design_frame4, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
                                    borderwidth=0, activebackground='#f8f8f8', command=lambda: forgot_password(), cursor="hand2")
            forgotPassword.place(x=290, y=290)


            # ==================== REGISTRATION PAGE ==============================================================================

            design_frame5 = Listbox(RegistrationPage, bg='#0c71b9', width=150, height=50, highlightthickness=0, borderwidth=0)
            design_frame5.place(x=0, y=0)

            design_frame6 = Listbox(RegistrationPage, bg='#1e85d0', width=150, height=50, highlightthickness=0, borderwidth=0)
            design_frame6.place(x=676, y=0)

            design_frame7 = Listbox(RegistrationPage, bg='#1e85d0', width=115, height=40, highlightthickness=0, borderwidth=0)
            design_frame7.place(x=75, y=106)

            design_frame8 = Listbox(RegistrationPage, bg='#f8f8f8', width=115, height=40, highlightthickness=0, borderwidth=0)
            design_frame8.place(x=676, y=106)
            
            # ========================== Text Variable ===================
            Username = StringVar()
            Email_id = StringVar()
            password = StringVar()
            confirm_password = StringVar()

            # ==== Full Name =======
            name_entry = Entry(design_frame8, fg="#a7a7a7", textvariable=Username, font=("yu gothic ui semibold", 12), highlightthickness=2)
            name_entry.place(x=284, y=150, width=286, height=34)
            name_entry.config(highlightbackground="black", highlightcolor="black")
            name_label = Label(design_frame8, text='•Full Name', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
            name_label.place(x=280, y=120)

            # ======= Email ===========
            email_entry = Entry(design_frame8, fg="#a7a7a7", textvariable=Email_id, font=("yu gothic ui semibold", 12), highlightthickness=2)
            email_entry.place(x=284, y=220, width=286, height=34)
            email_entry.config(highlightbackground="black", highlightcolor="black")
            email_label = Label(design_frame8, text='•Email', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
            email_label.place(x=280, y=190)

            # ====== Password =========
            password_entry = Entry(design_frame8, fg="#a7a7a7", textvariable=password, font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
            password_entry.place(x=284, y=295, width=286, height=34)
            password_entry.config(highlightbackground="black", highlightcolor="black")
            password_label = Label(design_frame8, text='• Password', fg="#89898b", bg='#f8f8f8',
                                font=("yu gothic ui", 11, 'bold'))
            password_label.place(x=280, y=265)


            def password_command2():
                if password_entry.cget('show') == '•':
                    password_entry.config(show='')
                else:
                    password_entry.config(show='•')


            checkButton = Checkbutton(design_frame8, bg='#f8f8f8', command=password_command2, text='show password')
            checkButton.place(x=290, y=330)


            # ====== Confirm Password =============
            confirmPassword_entry = Entry(design_frame8, textvariable=confirm_password, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
            confirmPassword_entry.place(x=284, y=385, width=286, height=34)
            confirmPassword_entry.config(highlightbackground="black", highlightcolor="black")
            confirmPassword_label = Label(design_frame8, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                        font=("yu gothic ui", 11, 'bold'))
            confirmPassword_label.place(x=280, y=355)
            
            # =============================== Signup Function ===========================
            def signup():
                if Username.get()=="" or Email_id.get() =="" or password.get() =="" or confirm_password.get() == "":
                    # print(Username)
                    # print(Email_id)
                    # print(password)
                    # print(confirm_password)
                    messagebox.showerror("Error", "Please fill all the details")
                elif password.get() == confirm_password.get():
                    my_db = mysql.connector.connect(
                                                host = 'localhost',
                                                user = 'root',
                                                password = '1234',
                                                database = 'team'
                                                )
                    my_cursor = my_db.cursor()
                    my_cursor.execute("insert into csignup values(%s, %s, %s)",(
                                                                    Username.get(),
                                                                    Email_id.get(),
                                                                    password.get()
                                                                    ))
                    my_db.commit()
                    my_db.close()
                    messagebox.showinfo("Success","Thankyou for signup")
                else:
                    messagebox.showerror("Error", "Please enter the password properly")

            # ========= Buttons ====================
            SignUp_button = Button(RegistrationPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                                command=lambda: show_frame(LoginPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
            SignUp_button.place(x=1100, y=175)

            SignUp_line = Canvas(RegistrationPage, width=60, height=5, bg='#1b87d2')
            SignUp_line.place(x=1100, y=203)

            # ===== Welcome Label ==================
            welcome_label = Label(design_frame8, text='Customer', font=('Arial', 20, 'bold'), bg='#f8f8f8')
            welcome_label.place(x=130, y=15)

            # ========= Login Button =========
            login_button = Button(RegistrationPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                                borderwidth=0, activebackground='#1b87d2', command=lambda: show_frame(LoginPage), cursor='hand2')
            login_button.place(x=845, y=175)

            # ==== SIGN UP down button ============
            signUp2 = Button(design_frame8, command= signup, fg='#f8f8f8', text='Sign Up', bg='#1b87d2', font=("yu gothic ui bold", 15),
                            cursor='hand2', activebackground='#1b87d2')
            signUp2.place(x=285, y=435, width=286, height=50)

            # ===== password icon =========
            password_icon = Image.open('img\\pass-icon.png')
            photo = ImageTk.PhotoImage(password_icon)
            password_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
            password_icon_label.image = photo
            password_icon_label.place(x=255, y=300)

            # ===== confirm password icon =========
            confirmPassword_icon = Image.open('img\\pass-icon.png')
            photo = ImageTk.PhotoImage(confirmPassword_icon)
            confirmPassword_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
            confirmPassword_icon_label.image = photo
            confirmPassword_icon_label.place(x=255, y=390)

            # ===== Email icon =========
            email_icon = Image.open('img\\email-icon.png')
            photo = ImageTk.PhotoImage(email_icon)
            emailIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
            emailIcon_label.image = photo
            emailIcon_label.place(x=255, y=225)

            # ===== Full Name icon =========
            name_icon = Image.open('img\\name-icon.png')
            photo = ImageTk.PhotoImage(name_icon)
            nameIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
            nameIcon_label.image = photo
            nameIcon_label.place(x=252, y=153)

            # ===== picture icon =========
            picture_icon = Image.open('img\\pic-icon.png')
            photo = ImageTk.PhotoImage(picture_icon)
            picture_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
            picture_icon_label.image = photo
            picture_icon_label.place(x=280, y=5)

            # ===== Left Side Picture ============
            side_image = Image.open('img\\lock2.jpg')
            resized = side_image.resize((625, 650), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(resized)
            side_image_label = Label(design_frame7, image=photo, bg='#1e85d0')
            side_image_label.image = photo
            side_image_label.place(x=0, y=0)



            window.mainloop()

        side_image = Image.open('img\\admin_logo1.jpg')
        resized = side_image.resize((685, 650), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized)
        side_image_label = Label(labelframeright, image=photo, bg='#1e85d0')
        side_image_label.image = photo
        my_btn = Button(labelframeright, command=customerlogin, image=photo)
        my_btn.pack()
        side_image_label.place(x=0, y=0)


if __name__ == "__main__":
    root=Tk()
    obj=Option(root)
    root.mainloop()