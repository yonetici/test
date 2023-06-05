from tkinter import *
from tkinter import messagebox
from tkinter import ttk

window = Tk()
window.title("Python TkInter")
window.minsize(width=250,height=250)

#Label
myLabel = Label(
    text="Enter Your Weight",
    font=('Arial', 12, "normal"),
    fg="black"
)

myLabel.place(x=50, y=20)
#Label
myLabel2 = Label(
    text="Enter Your Height",
    font=('Arial', 12, "normal"),
    fg="black"
)

myLabel2.place(x=50, y=80)
#Entry
myEntry = Entry(width=20)
myEntry.focus()
myEntry.place(x=50, y= 50)

myEntry2 = Entry(width=20)
myEntry2.place(x=50, y= 110)
def buttonClicked():
    userBMI = round(int(myEntry.get()) / pow(int(myEntry2.get())/100,2),1)
    messagebox.showinfo("Your BMI Index", userBMI)
#Button
myButton = Button(window, text="Calculate", command=buttonClicked)
myButton.config(padx=5, pady=5)
myButton.place(x = 80, y = 130)

window.mainloop()
