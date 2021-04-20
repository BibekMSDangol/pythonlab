from tkinter import *

root = Tk()

myLabel1 = Label(root, text = "Tkinter Program Beggining")
myLabel2 = Label(root, text = "I am Baljeet")
myLabel3 = Label(root, text = "Jinder  ")



myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=1, column=5)


root.mainloop()