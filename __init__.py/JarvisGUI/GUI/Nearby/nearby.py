from tkinter import * 
from PIL import ImageTk,Image, ImageDraw, ImageFont

root = Tk()
root.title('Near By Suggestions')
# root.iconbitmap(default='C:/Users/SAHIL/hotelbot.ico')

room_image = Image.open(r"JarvisGUI\GUI\Nearby\colaba1.png")
resize_image = room_image.resize((900, 500))
my_img1 = ImageTk.PhotoImage(resize_image)

room_image = Image.open(r"JarvisGUI\GUI\Nearby\gate.png")
resize_image = room_image.resize((900, 500))
my_img2 = ImageTk.PhotoImage(resize_image)
room_image = Image.open(r"JarvisGUI\GUI\Nearby\marine.png")
resize_image = room_image.resize((900, 500))
my_img3 = ImageTk.PhotoImage(resize_image)
room_image = Image.open(r"JarvisGUI\GUI\Nearby\snw.png")
resize_image = room_image.resize((900, 500))
my_img4 = ImageTk.PhotoImage(resize_image)
room_image = Image.open(r"JarvisGUI\GUI\Nearby\kidzania.png")
resize_image = room_image.resize((900, 500))
my_img5 = ImageTk.PhotoImage(resize_image)

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text = "1 of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)

my_Label = Label(text = ".....", image = my_img1, compound=CENTER)
my_Label.grid(row= 0, column=0, columnspan=3)

def forward(image_number):
    global my_Label
    global button_for
    global button_back

    my_Label.grid_forget()  #forgets/vanishes the last image stored in my_Label i.e my_img1

    my_Label= Label(image = image_list[image_number - 1])
    button_for = Button(root, text=">>",command=lambda: forward(image_number+1) )
    button_back = Button(root , text= "<<", command=lambda: back(image_number-1))

    if image_number==5:
        button_for = Button(root, text =">>",state=DISABLED)

    my_Label.grid(row= 0, column=0, columnspan=3)
    button_for.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(root, text = str(image_number) +" of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)
    status.grid (row =2, column = 0 , columnspan = 3, sticky = W+E)

def back(image_number):
    global my_Label
    global button_for
    global button_back


    my_Label.grid_forget() 
    my_Label= Label(image = image_list[image_number - 1])
    button_for = Button(root, text=">>",command=lambda: forward(image_number+1) )
    button_back = Button(root , text= "<<", command=lambda: back(image_number-1))

    if image_number==1:
        button_back = Button(root, text ="<<",state=DISABLED)

    my_Label.grid(row= 0, column=0, columnspan=3)
    button_for.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(root, text =  str(image_number) +" of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)
    status.grid (row =2, column = 0 , columnspan = 3, sticky = W+E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit", command= root.quit)
button_for = Button(root, text =">>", command=lambda:forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_for.grid(row=1, column=2)
status.grid (row =2, column = 0 , columnspan = 3, sticky = W+E)

root.mainloop()