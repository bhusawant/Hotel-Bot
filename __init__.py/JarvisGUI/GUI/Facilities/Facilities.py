from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Facilties")
root.geometry("1550x800+0+0")
root.config(bg='#2fbdef')

f1 = Frame(root, bg="grey", borderwidth=2, relief=SUNKEN)
f1.pack(side=TOP, fill = "x")

l = Label(f1, text="Facilities", font="Helvetica 30 bold", fg="black", pady=15, bg='#2fbdef')
l.pack(fill="x")
# ---------------------Images---------------------------------------
f2 = Frame(root , borderwidth=2, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

room_image = Image.open(r"JarvisGUI/GUI/Facilities/f4.jpg")
resize_image = room_image.resize((450, 300))
room_img = ImageTk.PhotoImage(resize_image)
 
label1 = Label(f2, image=room_img, pady=400)
label1.image = room_img
label1.grid(row=1, column=0 , ipadx=30)

lbl1 = Label(f2, text="Lavish bathrooms with upscale features such as heated floors and soaking tubs.\n Deluxe pillows and mattresses so your sleeping hours. Beautiful views in every direction.")
lbl1.grid(row=2, column=0)
# -------------------------------------------------------
gym_image = Image.open(r"JarvisGUI/GUI/Facilities/gym.jpg")
 
# Resize the image using resize() method
resize_gym_image = gym_image.resize((450, 300))
 
gym_img = ImageTk.PhotoImage(resize_gym_image)
 
# create label and add resize image
label2 = Label(f2, image=gym_img)
label2.image = gym_img
label2.grid(row=1, column=1, ipadx=30)

lbl2 = Label(f2, text="Keep up with your fitness routine whilst you’re away with our free hotel gym. \nPacked with cardio and resistance equipment and free weights, you can unwind after a busy day.")
lbl2.grid(row=2, column=1)
# ---------------------------------------------------------------------
# Read the Image
pool_image = Image.open(r"JarvisGUI/GUI/Facilities/pool.jpg")
 
# Resize the image using resize() method
resize_pool_image = pool_image.resize((450, 300))
 
pool_img = ImageTk.PhotoImage(resize_pool_image)
 
# create label and add resize image
label3 = Label(f2, image=pool_img)
label3.image = pool_img
label3.grid(row=1, column=2,ipadx=20)

lbl3 = Label(f2, text="After a long day of traveling or sightseeing, there’s nothing like a refreshing dip in the pool.\n If you’re looking to make a splash on your vacation, we’ve the most exquisite pools.")
lbl3.grid(row=2, column=2)
# --------------------------------------------------------------------------

f3 = Frame(root, borderwidth=2, relief=SUNKEN)
f3.pack(side=TOP, fill="x")

food_image = Image.open(r"JarvisGUI/GUI/Facilities/food.jpeg")
 
# Resize the image using resize() method
resize_food_image = food_image.resize((450, 300))
 
food_img = ImageTk.PhotoImage(resize_food_image)
 
# create label and add resize image
label4 = Label(f3, image=food_img)
label4.image = food_img
label4.grid(row=2, column=0, ipadx=30)

lbl3 = Label(f3, text="When it comes to food, we had the best cooks and services available.\n Food is the prestige of our hotel surrounding with flavours of world")
lbl3.grid(row=3, column=0)
# --------------------------------------------------------------------------
# Read the Image
spa_image = Image.open(r"JarvisGUI/GUI/Facilities/spa.jpg")
 
# Resize the image using resize() method
resize_spa_image =spa_image.resize((450, 300))
 
spa_img = ImageTk.PhotoImage(resize_spa_image)
 
# create label and add resize image
label5 = Label(f3, image=spa_img)
label5.image = spa_img
label5.grid(row=2, column=1, ipadx=30)

lbl3 = Label(f3, text="Stop dreaming about treating yourself to a spa break and just book this one!\n It’s got everything you could possibly want from a pamper break")
lbl3.grid(row=3, column=1)
# ------------------------------------------------------------------------------
# Read the Image
meet_image = Image.open(r"JarvisGUI/GUI/Facilities/meet.jpeg")
 
# Resize the image using resize() method
resize_meet_image = meet_image.resize((450, 300))
meet_img = ImageTk.PhotoImage(resize_meet_image)
 
# create label and add resize image
label6 = Label(f3, image=meet_img)
label6.image = meet_img
label6.grid(row=2, column=2, ipadx=20)

lbl3 = Label(f3, text="Elevate your next meeting with the glamour and sophistication of our \n Art Deco-inspired event spaces.")
lbl3.grid(row=3, column=2)

root.mainloop()