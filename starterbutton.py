from fileinput import filename
from time import sleep
from tkinter import *
import wget
import webbrowser
import subprocess
def confirmclick():
    url = 'https://code.jquery.com/jquery-3.6.0.min.js'
    wget.download(url)
    webbrowser.open_new_tab('google.com')
    sleep(1)
    window.destroy()

window = Tk()
confirmbutton = Button(window,text='Click Me To Run the Script')
confirmbutton.config(command=confirmclick)
confirmbutton.pack()
window.mainloop()
subprocess.call("clear", shell=True)
sleep(5)
subprocess.call("./test.sh")