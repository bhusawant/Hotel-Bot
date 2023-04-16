# Importing required libraries
import tkinter as tk
from tkinter import *
import re
import tkinter.font as font
from dbconnect import insertDetails, fetchDetails, fetchEmails

root = Tk()
root.geometry("1500x750")
same=True
n=0.3
global uname, uemail

def frame2():
    global mainframe,frame
    mainframe.destroy()
    
    mainframe=Frame(root,bg="#36D5FC")
    mainframe.pack(fill='both',expand='true')

    detailframe=Frame(mainframe)
    detailframe.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

def insertValue():
    global uname, uemail
    insertDetails([0 ,uname, uemail,int(v.get()), int(v2.get())-4, int(v3.get())-8, int(v4.get())-12, int(v5.get())-16])
    fetchDetails()
    root.destroy()   


    v = StringVar(mainframe, "1")
    q1 = Label(detailframe, text=" Q1. Information covered was consistent with training objective?", fg='black',font = ("Italic",18,"bold"))
    q1.place(relx=0, rely=0.1, relwidth=0.6, relheight=0.05)

    Radiobutton(detailframe, text='Strongly agree', variable=v, value=1, font = ("Italic",14)).place(relx=0, rely=0.15, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Agree', variable=v, value=2,  font = ("Italic",14)).place(relx=0.2, rely=0.15, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Neutral', variable=v, value=3,  font = ("Italic",14)).place(relx=0.4, rely=0.15, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Disagree', variable=v, value=4,  font = ("Italic",14)).place(relx=0.6, rely=0.15, relwidth=0.2, relheight=0.1)

    v2 = StringVar(mainframe, "5")
    q2 = Label(detailframe, text="  Q2. Information presented was relevant and valuable?", fg='black',font = ("Italic",18,"bold"))
    q2.place(relx=-0.05, rely=0.25, relwidth=0.6, relheight=0.05)

    Radiobutton(detailframe, text='Strongly agree', variable=v2, value=5, font = ("Italic",14)).place(relx=0, rely=0.3, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Agree', variable=v2, value=6, font = ("Italic",14)).place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Neutral', variable=v2, value=7, font = ("Italic",14)).place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Disagree', variable=v2, value=8, font = ("Italic",14)).place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.1)

    v3 = StringVar(mainframe, "9")
    q3 = Label(detailframe, text="   Q3. Information presented was dearly explained? ", fg='black',font = ("Italic",18,"bold"))
    q3.place(relx=-0.075, rely=0.4, relwidth=0.6, relheight=0.05)

    Radiobutton(detailframe, text='Strongly agree', variable=v3, value=9, font = ("Italic",14)).place(relx=0, rely=0.45, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Agree', variable=v3, value=10, font = ("Italic",14)).place(relx=0.2, rely=0.45, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Neutral', variable=v3, value=11, font = ("Italic",14)).place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Disagree', variable=v3, value=12, font = ("Italic",14)).place(relx=0.6, rely=0.45, relwidth=0.2, relheight=0.1)

    v4 = StringVar(mainframe, "13")
    q4 = Label(detailframe, text="    Q4. Participant questions were clearly answered? ", fg='black',font = ("Italic",18,"bold"))
    q4.place(relx=-0.075, rely=0.55, relwidth=0.6, relheight=0.05)

    Radiobutton(detailframe, text='Strongly agree', variable=v4, value=13, font = ("Italic",14)).place(relx=0, rely=0.6, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Agree', variable=v4, value=14, font = ("Italic",14)).place(relx=0.2, rely=0.6, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Neutral', variable=v4, value=15, font = ("Italic",14)).place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Disagree', variable=v4, value=16, font = ("Italic",14)).place(relx=0.6, rely=0.6, relwidth=0.2, relheight=0.1)

    v5 = StringVar(mainframe, "17")
    q5 = Label(detailframe, text="      Q5. I would recomment this course to my co-workers. ", fg='black',font = ("Italic",17,"bold"))
    q5.place(relx=-0.06, rely=0.7, relwidth=0.6, relheight=0.05)

    Radiobutton(detailframe, text='Strongly agree', variable=v5, value=17, font = ("Italic",14)).place(relx=0, rely=0.75, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Agree', variable=v5, value=18, font = ("Italic",14)).place(relx=0.2, rely=0.75, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Neutral', variable=v5, value=19, font = ("Italic",14)).place(relx=0.4, rely=0.75, relwidth=0.2, relheight=0.1)
    Radiobutton(detailframe, text='Disagree', variable=v5, value=20, font = ("Italic",14)).place(relx=0.6, rely=0.75, relwidth=0.2, relheight=0.1)    

    entrbtn = Button(detailframe, text="Submit", bg='#4E4E4E', fg='white', font = ("Italic",20), command=insertValue)
    entrbtn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.1)


def checkCredentials():
	if E1.get().isalpha() and check(E2.get()):
		global uname, uemail
		uname = E1.get()
		uemail = E2.get()
		emails = fetchEmails()
		#print(emails)
		if uemail in emails:
			errorLabel = Label(detailframe, text="Email already exists.", fg='red',font = ("Italic",15,"bold"))
			errorLabel.place(relx=0.03, rely=0.75, relwidth=1, relheight=0.15)
		else:
			frame2()
	elif E1.get().isalpha():
		errorLabel = Label(detailframe, text="Invalid Email.", fg='red',font = ("Italic",15,"bold"))
		errorLabel.place(relx=0.03, rely=0.75, relwidth=1, relheight=0.15)
	else:
		errorLabel = Label(detailframe, text="Only characters allowed in name.", fg='red',font = ("Italic",15,"bold"))
		errorLabel.place(relx=0.03, rely=0.75, relwidth=1, relheight=0.15)

regex = '^\\w+([\\.-]?\\w+)*@\\w+([\\.-]?\\w+)*(\\.\\w{2,3})+$' 
def check(email):  
    if(re.search(regex,email)):  
        return True    
    else:  
        return False  
      
myid = 1
mainframe=Frame(root,bg="#36D5FC")
mainframe.pack(fill='both',expand='true')
headingLabel = Label(mainframe, text="Feedback form", fg='black',font = ("Italic",30,"bold"))
headingLabel.place(relx=0.25, rely=0.04, relwidth=0.5, relheight=0.15)

detailframe=Frame(mainframe)
detailframe.place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.6)

name = Label(detailframe, text="Name", fg='black',font = ("Italic",15,"bold"))
name.place(relx=0.01, rely=0.1, relwidth=0.4, relheight=0.1)

E1 = Entry(detailframe, bd =5, font = ("Italic",15,"bold"))
E1.place(relx=0.4, rely=0.1, relwidth=0.5, relheight=0.1)

email = Label(detailframe, text="Email", fg='black',font = ("Italic",15,"bold"))
email.place(relx=0.01, rely=0.3, relwidth=0.4, relheight=0.1)

E2 = Entry(detailframe, bd =5, font = ("Italic",15,"bold"))
E2.place(relx=0.4, rely=0.3, relwidth=0.5, relheight=0.1)

entrbtn=Button(detailframe,text="Enter", bg='#4E4E4E', fg='white',command = checkCredentials)
entrbtn.place(relx=0.35, rely=0.6, relwidth=0.35, relheight=0.15)

root.mainloop()

