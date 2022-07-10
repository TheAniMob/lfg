from curses import window
from fileinput import filename
from os import name
from time import sleep
from tkinter import *
from turtle import pos
import wget
import webbrowser
import subprocess
def confirmclick():
    subprocess.call("clear", shell=True)
    sleep(2)
    window.destroy()
    subprocess.call("./packageinstaller.sh")
def declineclick():
    window.destroy()


window = Tk()
window.geometry("500x300")
window.title("Are You Sure You Would Like To Run This Script?")
confirmbutton = Button(window,text='Yes')
confirmbutton.config(command=confirmclick,activebackground="#00b33c",font=('Helvetica bold', 30))
confirmbutton.pack()
declinebutton = Button(window,text='No')
declinebutton.config(command=declineclick,activebackground="#e60000",font=('Helvetica bold', 30))
declinebutton.pack()
window.mainloop()
