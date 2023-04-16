from tkinter import *
import time
import os
root = Tk()

frameCnt = 34
frames = [PhotoImage(file='Y:\Gif, images, png,jpeg for jarvis\Jarvis.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

# for i in range(34):
#     format = 'gif-index %i' %(i)
#     frames = PhotoImage(file='Y:\Gif, images, png,jpeg for jarvis\Jarvis.gif',format = 'gif-index %i' %(i))
    
    
def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
    time.sleep(0.09)
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()