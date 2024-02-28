from tkinter import *
import tkinter.messagebox as mbox
root = Tk()

def open():
    top = Toplevel(root)
    top.title('Top')
    label = Label(top, text="I am top level")
    label.pack()
    top.mainloop()

    mbox.showinfo("showinfo", "Information")
    mbox.showwarning("showwaring", "Warning")
    mbox.showerror("showerror", "Error")
    mbox.askquestion("askquestion", "Are you sure?")
    mbox.askyesno("askyesno", "Do you want to continue?")
    mbox.askokcancel("askockcancel", "Do you want to continue?")
    mbox.askretrycancel("askretrycancel", "Try again?")

btn = Button(root, text="open", command=open)
btn.place(x=75, y=50)
root.mainloop()
