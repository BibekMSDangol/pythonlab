from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root, text = "Button is Clicked!")
    myLabel.pack()

myButton = Button(root, text = "Click Me!", command=myClick, fg= "red", bg="black")
myButton.pack()


root.mainloop()