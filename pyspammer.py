import pyautogui
import time
import tkinter
import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk, Image 
from tkinter import filedialog, Text

root = tk.Tk()

def spam():
    x=(E1.get())
    y=(E2.get())
    z=(E3.get())
    time.sleep(int(z))
    for i in range(0,int(y)):
        time.sleep(0.05)
        pyautogui.typewrite(x + '\n')


Image = tk.PhotoImage(file="logo.png")


canvas = tk.Canvas(root, height=100, width=490, bg="#FEEFDD")
Title = Label(canvas, text="PySpammer",bg="#FEEFDD", fg = "black", padx =100, font = "Helvetica 36 bold italic").pack(side = LEFT)
logo = Label(canvas, image=Image).pack(side =RIGHT)
canvas.pack()



frame = tk.Frame(root, bg="#FEEFDD",padx =18, pady = 9)
L1 = Label(frame,pady=2, padx=4, text="Enter your message : ", font = "Helvetica 12 bold italic", bg="#FEEFDD", fg="black" )
L1.pack(side = LEFT)
E1 = Entry(frame, bd =2, bg="#FEEFDD", font = "Helvetica 12 bold italic", fg="black")
E1.pack(side = LEFT)

L2 = Label(frame,pady=2, padx=4, text="How many times : ", font = "Helvetica 12 bold italic", bg="#FEEFDD", fg="black")
L2.pack(side = LEFT)
E2 = Entry(frame, bd =2, bg="#FEEFDD", font = "Helvetica 12 bold italic", fg="black")
E2.pack(side = LEFT)
frame.pack(side = TOP)

frame = tk.Frame(root, bg ="#FEEFDD", pady=9,padx=107)
L3 = Label(frame, text="Delay before spamming starts (in seconds) : ", font = "Helvetica 12 bold italic", bg="#FEEFDD", fg="black")
L3.pack(side = LEFT)
E3 = Entry(frame, bd =2, bg="#FEEFDD", font = "Helvetica 12 bold italic", fg="black")
E3.pack(side = LEFT)
frame.pack()

frame = Frame(root)
B = tk.Button(frame, padx=130, pady=2, text="Click to start Spam", font = "Helvetica 36 bold italic", bg="#FEEFDD", fg="black", command = spam)
B.pack()
frame.pack(side = BOTTOM)


root.mainloop()


