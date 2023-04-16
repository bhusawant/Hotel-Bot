# from tkinter import *
# from PIL import Image, ImageTk
# from FirstPage import Option
# from Customers import Customers
# from room import RoomBooking



# class HotelManagementSystem:
#     def __init__(self, root):
#         self.root=root
#         self.root.title("HotelBot")
#         self.root.geometry("1550x800+0+0")

#         # For Hotel1 image
#         img1=Image.open(r"img\Hotel1.jpg")
#         img1=img1.resize((1550, 140), Image.ANTIALIAS)
#         self.photoimg1=ImageTk.PhotoImage(img1)

#         labImg=Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
#         labImg.place(x=0, y=0, width=1550, height=140)

#         # For logo
#         img2=Image.open(r"img\logo_for_hotelBot.jpg")
#         img2=img2.resize((150, 140), Image.ANTIALIAS)
#         self.photoimg2=ImageTk.PhotoImage(img2)

#         labImg=Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
#         labImg.place(x=0, y=0, width=150, height=140)

#         #title for hotel management system
#         lbl_title=Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
#         lbl_title.place(x=0, y=140, width=1550, height=50)


#         #main frame
#         main_frame = Frame(self.root, bd=4, relief=RIDGE)
#         main_frame.place(x=0, y=190, width=1550, height=620)

#         #menu
#         lbl_menu=Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
#         lbl_menu.place(x=0, y=0, width=230)

#         #btn frame
#         btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
#         btn_frame.place(x=0, y=35, width=228, height=190)

#         cust_btn = Button(btn_frame, text="CUSTOMER",command=self.OpenCusomersWindow, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
#         cust_btn.grid(row=0, column=0, pady=1)

#         room_btn = Button(btn_frame, text="ROOM", width=22,command=self.OpenRoomWindow, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
#         room_btn.grid(row=1, column=0, pady=1)

#         details_btn = Button(btn_frame, text="DETAILS", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
#         details_btn.grid(row=2, column=0, pady=1)

        
        
#         logout_btn = Button(btn_frame, text="LOGOUT", width=22,command=self.logout, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
#         logout_btn.grid(row=3, column=0, pady=1)

#         # right side image
#         img3=Image.open(r"img\hotelArea1.jpg")
#         img3=img3.resize((1310, 590), Image.ANTIALIAS)
#         self.photoimg3=ImageTk.PhotoImage(img3)

#         labImg1=Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
#         labImg1.place(x=225, y=0, width=1310, height=590)

#         # down side images
#         img4=Image.open(r"img\hotelArea2.jpg")
#         img4=img4.resize((230, 210), Image.ANTIALIAS)
#         self.photoimg4=ImageTk.PhotoImage(img4)

#         labImg1=Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
#         labImg1.place(x=0, y=225, width=230, height=210)


#         img5=Image.open(r"img\Food.jpg")
#         img5=img5.resize((230, 190), Image.ANTIALIAS)
#         self.photoimg5=ImageTk.PhotoImage(img5)

#         labImg1=Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
#         labImg1.place(x=0, y=420, width=230, height=190)
#     def OpenCusomersWindow(self):
#         self.new_window =Toplevel(self.root)
#         self.app = Customers(self.new_window)
        
#     def OpenRoomWindow(self):
#         self.new_window =Toplevel(self.root)
#         self.app = RoomBooking(self.new_window)
#         # root = Tk()
#         # obj=Customers(root)
#         # root.mainloop
        
#     def logout(self):
        
#         # self.first_page = Toplevel(self.root)
#         # self.app = Option(self.first_page)
#         (self.root).destroy()
#         root1 = Tk()
#         obj = Option(root1)
        
        

# if __name__ == "__main__":
#     root=Tk()
#     obj=HotelManagementSystem(root)
#     root.mainloop()
    






from tkinter import *
from PIL import Image, ImageTk
from FirstPage import Option
from Customers import Customers
from room import RoomBooking
from Details import DetailsRoom



class HotelManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("HotelBot")
        self.root.geometry("1550x800+0+0")

        # For Hotel1 image
        img1=Image.open(r"img\Hotel1.jpg")
        img1=img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        labImg=Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        labImg.place(x=0, y=0, width=1550, height=140)

        # For logo
        img2=Image.open(r"img\logo_for_hotelBot.jpg")
        img2=img2.resize((150, 140), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        labImg=Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        labImg.place(x=0, y=0, width=150, height=140)

        #title for hotel management system
        lbl_title=Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)


        #main frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        #menu
        lbl_menu=Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        #btn frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER",command=self.OpenCusomersWindow, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=2)

        room_btn = Button(btn_frame, text="ROOM", width=22,command=self.OpenRoomWindow, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=2)

        details_btn = Button(btn_frame, text="DETAILS", width=22,command=self.OpenDetailsWindow, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=2)

        
        
        logout_btn = Button(btn_frame, text="LOGOUT", width=22,command=self.logout, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=3, column=0, pady=2)

        # right side image
        img3=Image.open(r"img\hotelArea1.jpg")
        img3=img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        labImg1=Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        labImg1.place(x=225, y=0, width=1310, height=590)

        # down side images
        img4=Image.open(r"img\hotelArea2.jpg")
        img4=img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        labImg1=Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        labImg1.place(x=0, y=190, width=230, height=220)


        img5=Image.open(r"img\Food.jpg")
        img5=img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        labImg1=Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        labImg1.place(x=0, y=400, width=230, height=190)
    def OpenCusomersWindow(self):
        self.new_window =Toplevel(self.root)
        self.app = Customers(self.new_window)
        
    def OpenRoomWindow(self):
        self.new_window =Toplevel(self.root)
        self.app = RoomBooking(self.new_window)

    def OpenDetailsWindow(self):
        self.new_window =Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)
        # root = Tk()
        # obj=Customers(root)
        # root.mainloop
        
    def logout(self):
        
        # self.first_page = Toplevel(self.root)
        # self.app = Option(self.first_page)
        (self.root).destroy()
        root1 = Tk()
        obj = Option(root1)
        
        

if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()