####Created by Lamer3011####
from tkinter import *
from tkinter import messagebox
import os, time
try:
    import pyperclip
except:
    os.system('pip install pyperclip')

def show_message():
    time_sleep = IntVar()
    if message.get() == "":
        messagebox.askretrycancel("Empty strings", "Please enter text and time.")
    else:
        messagebox.showwarning("Attention!", "Use this application for its intended purpose.And be responsible for your actions.\n" 
        + message.get() + " will be copied")
        time.sleep(time_sleep.get())
        pyperclip.copy(message.get())

root = Tk()
root.title("ClipboardPro")

message = StringVar()
time_sleep = StringVar()

L1 = Label(root, text="Text: ")
L1.pack()
E1 = Entry(root, bd =5, textvariable=message)
E1.pack()

L2 = Label(root, text="Time sleep: (Seconds)")
L2.pack()
E2 = Entry(root, bd =5, textvariable=time_sleep)
E2.pack()

button_ok = Button(text="OK", command=show_message)
button_ok.pack()

root.mainloop()